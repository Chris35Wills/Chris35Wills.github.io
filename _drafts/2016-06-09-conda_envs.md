##################
# New anaconda enviornment

READ: http://conda.pydata.org/docs/using/envs.html#list-all-environments

Do this in windows cmd (not git bash or cygwin as activate doesn;t work!):

1. Temporarily remove the python path (where your other functions are stored):
set PYTHONPATH=.
2. see what environments you have: conda env list
3. create new environment (must pass it a package to do this):
conda create --name test_env numpy
4. activate it: activate test_env
5. check which python you are using (ipython won;t be installed in your new env): where python 
5. go to diectory of thing to test: cd LFMapper
6. install nosetests: conda install nose
7. run it: nosetests
8: shoudl fail as no osgeo available so try:
conda install -c osgeo gdal=1.11.2 numpy matplotlib scipy
9. rerun nosetests
10. should work now
11. go back to normal environment: deactivate 
NB/ If you get a DLL error, do a full update of conda on your machine (see this post here:http://stackoverflow.com/questions/36724202/dll-load-failed-for-all-packages-after-conda-update-command)
Updating conda: http://conda.pydata.org/docs/commands/conda-update.html