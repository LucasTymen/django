"""
Models and Databases
Native Model Methods

We haven’t implemented methods yet to emulate any model behaviors.
The properties we’ve created for our flowers describe what our flower is or has.
They are like the nouns and adjectives that describe each flower.
What we are missing though, and why modeling database data is so useful to begin with, are the verbs, the actions associated with our flowers.
These are called methods. Methods are functions defined in our model that describe the behaviors and actions of our model.
If properties are what our models are, then methods are what our models do. For example, our flower might bloom() and grow().

In Python classes, which Django uses to create models, there are built-in methods we can override like the __str__ method (https://docs.djangoproject.com/en/4.1/ref/models/instances/#str).
All this means is we are creating a method using the same name as the built-in one.
This is how we, the programmer, take control, or “override”, the default behavior of the built-in version:
"""

class Gardener(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

"""
Methods always require the first parameter to be self, then we can provide other optional parameters and add logic within the method body.
In the next lesson, we’ll learn how useful overriding __str__ is when we need to retrieve instances of models from our database
— by default, if we didn’t override __str__ printing our instances would generate output that’s hard to read like:

<QuerySet [<Gardener:>,<Gardener:>,<Gardener:>....]

But with our overridden __str__ method, we’ll get more helpful information, in this case, we’re returning the Gardener instance’s name:

<QuerySet [<Gardener: Linnaeus>,<Gardener: Mendel>, <Gardener: Carver >....]

Instructions
1.

In the Owner model create a __str__ method that returns the instance’s .first_name and .last_name concatenated with a space in between like:

first_string + " " + second_string

That should print out one concatenated string like:

John Doe

Or

Danny Glover

Checkpoint 2 Passed
2.

Let’s also implement a __str__ method for Patient as well.
This time return a string that contains the .pet_name and the .animal_type separated by a comma and space (", ").

For example, the outputs should look like:

Captain Whiskers, Cat

Or

Mustached Dragon, Reptile

Checkpoint 3 Passed
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
"""
