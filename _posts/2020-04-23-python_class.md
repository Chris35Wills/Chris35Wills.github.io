---
layout: post
title: Creating classes in python - the Dog class example
categories: python
---

The dog class example. I always come back to this when thinking about setting up classes in Python. This is modified from [Real Python](https://realpython.com/python3-object-oriented-programming/#classes-in-python).

```python
class Dog:
    """Creates a class representating a dog

    This method requires a name and an age 
    e.g. rex=Dog('Rex',7)
    """

    # Class Attributes << these are common to all new objects made of this class
    species = 'mammal'
    Kingdom="Animalia"
    Phylum="Chordata"
    Class="Mammalia"
    Order="Carnivora"
    Family="Canidae"
    Subfamily="Caninae"
    Tribe="Canini"
    Genus="Canis"
    Species="C. lupus"
    Subspecies="C. l. familiaris"

    # Initializer / Instance Attributes << this inititalizer is required to create a new object of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method << a method that can be run by an object of the class
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method << a method that can be run by an object of the class - this one needs an input when called
    def speak(self, sound):
        """Make your dog speak 

        This method requires a sound to be passed as a string
        e.g. your_dog.speak('bark')
        """
        return "{} says {}".format(self.name, sound)
```

Then to create a dog object:

```python
rex=Dog('Rex',7)
```

You can access attributes like:

```python
rex.Kingdom
rex.Species
```

and you can call the Dog class's methods:

```python
print(rufus.description())
print(rufus.speak('woof'))
```

Given it's the 23rd April here in the UK, why not have a go at making your own `dragon` class?

Here's some code to start you off:

```python
class dragon():
    """Creates a class representating a dragon

    This method requires a name and an age 
    e.g. drogon=dragon('Drogon',7)
    """

    # Class Attributes
    Kingdom="Animalia"
    Phylum="Chordata"
    Class="Reptilia
    Order="Squamata"
    Suborder="Iguania"
    Family="Agamidae"
    Subfamily="Draconinae"

    # Initializer / Instance Attributes << this inititalizer is required to create a new object of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method << make it do something
    def description(self):
        ...

    # instance method << make it do something
    def breathe_fire(self):
        ...
```
