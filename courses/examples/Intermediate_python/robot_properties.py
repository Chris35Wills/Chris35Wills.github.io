"""
The following example shows a class, which has internal attributes, which can't be accessed from outside. These are the private attributes self.__potential_physical and self.__potential_psychic. Furthermore we show that a property can be deduced from the values of more than one attribute. The property "condition" of our example returns the condition of the robot in a descriptive string. The condition depends on the sum of the values of the psychic and the physical conditions of the robot. 

Links:

  Properties: http://www.python-course.eu/python3_properties.php
  Properties: https://eev.ee/blog/2012/05/23/python-faq-descriptors/

  Private variables: https://docs.python.org/2/tutorial/classes.html#tut-private

  Variabes: http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#other-languages-have-variables
"""

__credits__ = http://www.python-course.eu/python3_properties.php

class Robot:

    def __init__(self, name, build_year, lk = 0.5, lp = 0.5 ):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
           return "I feel miserable!"
        elif s <= 0:
           return "I feel bad!"
        elif s <= 0.5:
           return "Could be worse!"
        elif s <= 1:
           return "Seems to be okay!"
        else:
           return "Great!" 
  
if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4 )
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)