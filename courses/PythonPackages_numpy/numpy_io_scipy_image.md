---
---

# Read in data using scipy (image)

*IMPORTANT: This walk through makes use of a few additional packages that work with numpy arrays, namely scipy and matplotlib*

As seen [here](../numpy_io_text), numpy can be used with tabulated data sets but where it really excels is when it is applied to workflows involving matrices of data - think of photographs, satellite images, digital elevation models (DEMs) etc. 

Right click [this link](../puppy.png) and save this 
file to a location on your machine.

## Open an image as a numpy array

To read the image in as a numpy array, we are going to need a little help from a function from the [scipy](http://www.scipy.org/scipylib/index.html) library:

```python
from scipy import misc
```

You now have access to the routines available within scipy's [misc module](http://docs.scipy.org/doc/scipy-0.16.0/reference/misc.html). To read in the image, type the following:

```python
dog=misc.imread('/path/to/file/puppy.png')
type(dog)
```

You have now created a numpy array object holding the image information. You can see the image in its array form using:

```python
print(dog)
```

## Plot your image 

You can visualise the array using [pyplot](http://matplotlib.org/api/pyplot_api.html) from the [matplotlib module](http://matplotlib.org/):

```python
import matplotlib.pyplot
matplotlib.pyplot.imshow(dog)
matplotlib.pyplot.show()
```

which will result in:

!["RGB puppy"]({{ site.baseurl }}../dog_matplotlib.png)

By using ```shape``` you will see that the array has 3 dimensions - as the file we are using is an RGB image, in this case, each dimension applies to its red, green and blue colour bands:

	>>> dog.shape
	>>> (400L, 600L, 3L)

To slice the array and access the red component use:

```python
red=dog[:,:,0]
```

for the green component use:

```python
green=dog[:,:,1]
```

and for the blue component use:

```python
blue=dog[:,:,2]
```

Now that we have accessed slices of the image, let's manipulate them and create something new. Lets [turn our RGB image into a greyscale image](https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale). This can be achieved using the equation:

**grey = (0.2126 * red) + (0.7152 * green) + (0.0722 * blue)**

To make a greyscale array, we'll aply the above equation and use the sliced parts of the original image as held by the arrays we called ```red```, ```green``` and ```blue```. We'll call our new array ```grey```:

```python
grey = (0.2126 * red) + (0.7152 * green) + (0.0722 * blue)
```

No looping or anything required - this efficiency is what makes numpy fast. If we had used a vanilla python approach, we would have to have looped through each element of the array which would have taken *much* longer.

Now we have our grey image, we can plot it using matplotlib again, but this time we must tell it that the image is greyscale - this is done by using the ```cmap``` option within the ```imshow``` command:

```python
import matplotlib.cm as cm 
matplotlib.pyplot.imshow(grey, cmap = matplotlib.cm.Greys_r)
matplotlib.pyplot.show()
```

To write the array out as an image, we'll use scipy again:

```python
misc.imsave('puppy_grey.png', grey)
```

Open this image and check out your funky new colour scheme, all thanks to a bit of python and numpy.

# [Previous](../numpy_io_text) [Home](../README_numpy) [Next](../numpy_what_next)
