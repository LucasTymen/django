"""
Models and Databases
Custom Model Methods

In addition to overriding native methods, we can define our own custom methods!

We can do something simple like returning a boolean:
"""

class Flower(models.Model):
  has_sunlight = models.BooleanField(default=True)
  has_water = models.BooleanField(default=True)

  def can_grow(self):
    return self.has_sunlight and self.has_water

"""
Above, we defined our custom .can_grow() method that checks if the instance’s .has_sunlight and .has_water fields are True.
Notice that even for custom methods, we need to provide the first parameter as self.
We can also provide additional parameters as needed.

Here’s another example that returns a string:
"""

class Gardener(models.Model):
  years_experience = models.IntegerField()

  def identify_flower(self, flower):
    return f"I've studied flowers for {self.years_experience}. I believe this flower is {flower.name} and is found in {flower.native_env}."

"""
In this case, we’ve added a second parameter to our method, a flower instance, and returned a string.
Both methods do different things but both help emulate real-life behaviors. Check out Django documentation for more insight!
https://docs.djangoproject.com/en/3.1/topics/db/models/#model-methods


Instructions
1.

Let’s define a method for Owner that checks if they have multiple pets or not.

Inside the Owner class, define a method called .has_multiple_pets() that returns a boolean if the owner does have more than 1 pet.
Use the logic provided below:


return self.patient_set.count() > 1


This code checks the related Patient model and how many instances belong to the Owner.
We’ll cover more of this logic in the next lesson.

Your syntax should look like:
"""

Class SampleMod(models.Models):
    # ... Fields
    def custom_method(self):
    # Logic for method
    return self.method
