---
layout: post
title: Binary image skeletonisation with Python
categories: Python, sci-kit
tags: python image 
---

I've been looking to do some [skeletonisation](https://en.wikipedia.org/wiki/Topological_skeleton) using python libraries and found something that did precisely that using the third party python package [scikit-image](http://scikit-image.org/). It was so quick to implement (after having spent a while trying to roll my own version) I thought I'd share it with everyone.

Let's first make some toy data to play with called _arr_.

{% highlight python %}
import numpy as np

arr = np.ones([100,100])
arr[:, 50:100]=0
arr[50:70, 50:90]=1
{% endhighlight %}

![Toy data]({{ site.baseurl }}/images/skeletonise/toy_data.png "Toy data")

Now, import the medial_axis function from skimage.morphology which comes as part of the [scikit-image package](http://scikit-image.org/). If you are using a canopy distribution with an academic license, this is available in the [package manager](http://docs.enthought.com/canopy/quick-start/package_manager.html).

{% highlight python %}
from skimage.morphology import medial_axis
{% endhighlight %}

Using our toy data, we are now going to create two arrays - one a boolean array called _skeleton_ and the other the distance transform called _distance_.

{% highlight python %}
skeleton, distance = medial_axis(arr, return_distance=True)
{% endhighlight %}

We can mask out the _distance_ array by multiplying it by the boolean array _skeleton_:

{% highlight python %}
dist_masked = distance * skeleton
{% endhighlight %}

We now have a boolean _skeleton_ array, _distance_ array and clipped distance array showing distances where the skelton pixels lie. Althogther, these look like:

![Final output arrays]({{ site.baseurl }}/images/skeletonise/data_skel_dist.png "Final output arrays")

Essentialy what we have done is calculate the distance transform (_distance_) of the initial input array (_arr_) which has then been used to create a boolean array (_skeleton_) based on local maximum distance values. For the red cells extending out of the block to the left of the original image, this local maximum falls expectedly along the centre of this stretch of pixels. The skeleton can then be seen to continue up the left hand side of the red region to the left - the area furthest from the blue cells on the right of _arr_.

More info [here](http://scikit-image.org/docs/dev/auto_examples/edges/plot_medial_transform.html)