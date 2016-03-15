---
---

# Array fucntions: Solutions

## Create a *1-dimensional* array of ones and print out its shape

	arr_1d=np.ones(10)
	arr_1d.shape

---

## Create a *2-dimensional* array of random numbers and print out its shape

	rand_2d=numpy.random.random((5,5))
	rand_2d.shape

---

## Create a *2-dimensional* array of values between 10 and 30 and print out its shape

	arr=np.arange(10,30)
	arr_2d=arr.reshape(2,10)
	arr_2d.shape

---

## Create a 10 x 10 *2-dimensional* numpy array of random numbers - what are the max, min and mean values of this array?

	rand_2d=numpy.random.random((5,5))
	print(rand_2d.max())
	print(rand_2d.min())
	print(rand_2d.mean())

# [Previous](../numpy_array_funcs)



