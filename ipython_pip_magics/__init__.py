# Small ipython extensions

import sys
import subprocess

def pip(line):
    """Execute a pip command. 
    Do:
      %pip --help
    to get an overview.

    Note: when doing '%pip uninstall ...', use the -y option
    to avoid being prompted (which does not work using %pip).
    """
    do_pip(line.split())

def do_pip(args):
    args = (sys.executable, "-m", "pip") + tuple(args)
    with subprocess.Popen(args, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as pipe:
        while True:
            line = pipe.stdout.readline()
            if not line:
                break
            sys.stdout.write(line.decode())

def pip_upgrade_all_user(line):
    """Attempt to upgrade all packages installed with --user"""
    import pip
    for dist in pip.get_installed_distributions(user_only=True):
        do_pip(["install", "--upgrade", "--user", dist.project_name])

def pip_upgrade_all(line):
    """Attempt to upgrade all packages"""
    from pip import get_installed_distributions
    user = set(d.project_name for d in get_installed_distributions(user_only=True))
    all = set(d.project_name for d in get_installed_distributions())
    for dist in all - user:
        do_pip(["install", "--upgrade", dist])
    for dist in  user:
        do_pip(["install", "--upgrade", "--user", dist])


def load_ipython_extension(ipython):
    # The `ipython` argument is the currently active `InteractiveShell`
    # instance, which can be used in any way. This allows you to register
    # new magics or aliases, for example.
    ipython.register_magic_function(pip)
    ipython.register_magic_function(pip_upgrade_all_user)
    ipython.register_magic_function(pip_upgrade_all)


def unload_ipython_extension(ipython):
    # If you want your extension to be unloadable, put that logic here.
    pass
