---
layout: post
title: Removing a component of a signal using FFT
categories: Python
tags: FFT signal
---

A component of a signal can easily be removed by using the Fast Fourier Transform (and its inverse) - in Python, this is easily implemented using numpy. The code below zeros out parts of the FFT - this should be done with caution and is discussed in the various threads you can find [here](https://dsp.stackexchange.com/questions/6220/why-is-it-a-bad-idea-to-filter-by-zeroing-out-fft-bins). Martin put together a function to smooth the FFT (based on [Moisan, 2011](https://link.springer.com/article/10.1007/s10851-010-0227-1)) which can help with this [here](https://github.com/mewo2/smoothfft).

A simple example (take from [here](https://dsp.stackexchange.com/questions/6220/why-is-it-a-bad-idea-to-filter-by-zeroing-out-fft-bins)):

```python
import numpy as np
import matplotlib.pyplot as plt

# Make some data
t=np.linspace(0,1,256, endpoint=False)
x = np.sin(2 *np.pi * 3 * t) + np.cos(2 * np.pi * 100 * t)

# Run FFT
X=np.fft.fft(x)

# Zero some channels
X[64:192] = 0

# Run inverse FFT
y = np.fft.ifft(X)

# Plot it
plt.plot(x)
plt.plot(y)
plt.legend(['raw signal', 'filtered signal'])
plt.show(block=False)
```

![Filter signal with FFT]({{ site.baseurl }}/images/simple_fft_filter.png "Filter signal with FFT")

What we've done is

* run FFT on a signal
* zero out some of the bins (real and complex)
* run an inverse FFT on the remaining
* returned the signal, without the components you zeroed
	


   



