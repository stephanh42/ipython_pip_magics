ipython_pip_magics: %pip magics for IPython
===========================================

This project provides IPython "magics" for working with pip.

To load the IPython magics, do (in IPython):

   %load_ext ipython_pip


The primary magic is %pip. This works (almost) exactly
like pip from the operating system command line.

Do:
    %pip --help

to get an overview.

Note: when doing '%pip uninstall ...', use the -y option
to avoid being prompted (which does not work using %pip).
 
Other magics:

   %pip_upgrade_all

Attempt to upgrade all packages

   %pip_upgrade_all_user
