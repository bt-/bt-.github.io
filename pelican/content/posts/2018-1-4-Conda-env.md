Title: Creating a Conda environment.yml file
Date: 2018-01-04 12:00

I've been learning the Python data science tools as a hobby off and on for years and have re-focused my efforts over the last six months.  As a learning exercise and hopefully to create something useful for the solar industry, I've been working on a Python module ([pvcaptest](https://github.com/bt-/pvcaptest)) that facilitates capacity testing following ASTM E2848 standard.

The project is ongoing, but I am going to start documenting my experience in a series of posts.

I'll start with my most recent exercise: moving my work to a different computer by creating environment.yml file and a using it to create a new conda environment.

I was traveling over the holidays and I've been testing pvcaptest on a bulky windows laptop, which requires the skills of a contortionist to use on an airplane.  I happened to have a nice compact MacBook Pro with me and I thought, "I'll move my work over to the other computer to work on the plane.  I just need to replicate my conda environment and clone my repository from github."

And it was almost that simple.  I couldn't make an explicit replica of my conda environment using


```
conda list --explicit
``` 

because I was moving from windows to OSX, so I created a .yml file including the packages I knew I would need, commited it, and pushed it to my remote repository on github.

```
name: pvc_env
dependencies:
- python=3.5
- pandas=0.20.3
- numpy=1.13.1
- dateutil=2.5.3
- matplotlib=1.5.3
- statsmodels=0.8.0
- scikit-learn=0.19.0
- seaborn=0.7.1
- bokeh=0.12.4
```

I moved over to my MacBook, cloned the repository, ran 

```
conda env -f pvc_env.yml
```

and, somewhat expectedly, received an error.

```
NoPackagesFoundError: Package missing in current osx-64 channels: 
  - dateutil 2.5.3*
```

I fixed that by looking at the packages in my working environment again and prepended "python-" to "dateutil 2.5.3".  I try again and ...

```
UnsatisfiableError: The following specifications were found to be in conflict:
  - matplotlib 1.5.3* -> numpy 1.11* -> mkl 11.3.3
  - numpy 1.13.1*
Use "conda info <package>" to see the dependencies for each package.
```

So, I follow the directions and start looking at the dependencies, but that route starts to look like a bit of a black hole.  I thought I likely had over constrained the versions, so I try throwing some * on the end and see if the wonderful folks at Anaconda have made conda Ben (idiot) proof.  And, success!

The next step was to activate my new env and run the jupyter notebook file.

```
source activate pvc_env
```

I run the notebook and ...

```
AttributeError: 'DataFrame' object has no attribute 'agg'
```

Well I know that the version of Pandas I specified for new environment does include the DataFrame aggregate method, so I must not be running that version in the notebook.  I run a quick check of the version 

```
pd.show_versions(as_json=False)
```

and confirm that I'm still using pandas 0.17.1.

I try checking the version in ipython and have the same issue.  At this point I'm a bit stumped.  I realize that my new env is not listed when running conda list env even thought it is shown in anaconda/envs/.  At the moment, this issue is still a mystery to me.

After a bit of thinking and scrolling through the packages installed in my working environment on the original computer, I realize maybe if I'm trying to run a notebook file that I need ipython and the notebook packages in my environment!

I conda install those and viola!  After making the adjustments to get to this point my environment file looks like this:

```
name: pvc_env
dependencies:
- python=3.5*
- pandas=0.20.3
- numpy=1.13*
- python-dateutil=2.5*
- matplotlib=2*
- statsmodels=0.8*
- scikit-learn=0.19*
- seaborn=0.7*
- bokeh=0.12*
- ipython-notebook*
- ipython*
```

That wraps up this post, but there will be more to come.  Here is a preview of possible future topics:

- Setting up the project directory structure for a python project
- Using Sphinx to build project documentation from docstrings
- Finding docstring conventions, picking and following one
- Using git for version control and github to work across multiple computers
- Understanding decorators and writing one for the module
- Organizing classes and methods and refactoring to improve
- Learning how to generate linked plots in Bokeh
