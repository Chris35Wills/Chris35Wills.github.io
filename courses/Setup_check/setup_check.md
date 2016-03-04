---
---

# Checking everything works

Below are a couple of scripts for ensuring everything as detailed on the [SETUP page](../../SETUP/setup) works.

1. Go to [this page](https://raw.githubusercontent.com/Chris35Wills/Chris35Wills.github.io/master/courses/Setup_check/installation-test-1.py), right click anywhere in the window, select **save as** and call it installation-test-1.py - remember where you sav it!

2. Run it from the bash shell you set up as detailed on the [SETUP page](../../SETUP/setup)

  {% highlight bash %}
  $ cd path/to/where/you/downloaded/the/file
  $ python installation-test-1.py
  Passed
  {% endhighlight bash %}

3. Go to [this page](https://raw.githubusercontent.com/Chris35Wills/Chris35Wills.github.io/master/courses/Setup_check/installation-test-2.py), right click anywhere in the window, select **save as** and call it installation-test-2.py - remember where you sav it!

4. Run it from the bash shell as in step 2

  {% highlight bash %}
  $ cd path/to/where/you/downloaded/the/file
  $ python installation-test-1.py
  check virtual-shell...  pass
  ...
  Successes:
  
  virtual-shell Bourne Again Shell (bash) 4.2.37
  ...
  {% endhighlight bash %}

  If you see something like:

  {% highlight bash %}
  $ python swc-installation-test-2.py
  check virtual-shell...  fail
  ...
  check for command line shell (virtual-shell) failed:
   	command line shell (virtual-shell) requires at least one of the following 
   	dependencies
  	For instructions on installing an up-to-date version, see
   	http://software-carpentry.org/setup/
   	causes:
   	check for Bourne Again Shell (bash) failed:
    	could not find 'bash' executable for Bourne Again Shell (bash)
    	For instructions on installing an up-to-date version, see
    	http://software-carpentry.org/setup/
  ...
  {% endhighlight bash %}

  follow the suggestions to try and install any missing software. For additional troubleshooting information, you can use the --verbose option:

  {% highlight %}
  $ python swc-installation-test-2.py --verbose
  check virtual-shell...  fail
  ...
  ==================
  System information
  ==================
  os.name            : posix
  ...
  {% highlight %}