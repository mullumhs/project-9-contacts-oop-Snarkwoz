"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and manipulate Car objects in Python to understand 
  basic concepts of Object-Oriented Programming.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        self.is_engine_on = False
        self.odometer = 0

    def start_engine(self):
        self.is_engine_on = True
        print(f"The engine of the {self.color} {self.brand} is now on.")

    def stop_engine(self):
        self.is_engine_on = False
        print(f"The engine of the {self.color} {self.brand} is now off.")

    def zoomzoom(self, distance):
        if (self.is_engine_on):
            self.odometer = distance
            print(f"You do be zoomin")
        else:
            print("Engine not on dumbass")


# Add another property to the Car class called "odometer".
# This property should be initialised to 0.


# Create two Car objects. One should be a red Toyota and the other a blue Ford.

Toyota = Car("Red", "Toyota")
Ford = Car("Blue", "Ford")

# Start the engine of the red Toyota.

Toyota.start_engine()

# Create a method called "drive" that takes a distance as a parameter.
# The car can only be driven if the engine is on.



# Attempt to drive both cars 100Km.

Toyota.zoomzoom(100)
Ford.zoomzoom(100)

# Print the brand, odometer and colour of both cars.


