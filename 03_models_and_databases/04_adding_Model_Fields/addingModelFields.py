"""
Models and Databases
Adding Model Fields

As we mentioned, models are used to represent real-life objects.
We can mimic and create object attributes in our models using fields.
Fields have names and are assigned a type. For example, a Flower model can have a petal_color field that expects a string:

class Flower(models.Model):
  petal_color = models.CharField()

Django uses specific field types to match the expected data with what will go into the database.
Above, we used the .CharField() type to store a short string.
We can continue to add to our model and include other attributes, like petal_number.
"""

class Flower(models.Model):
  petal_color = models.CharField()
  petal_number = models.IntegerField()
  # More attributes…

"""
Since we want petal_number to be a number, we used the .IntegerField() field type.
Django provides a huge variety of field types for us to specify the data types of our model attributes, check out theField Types Documentation to explore the entire list of possibilities!

We might also want to add constraints to our fields.
For example, we might want our petal_color field to have a max length of 20 characters. We can supply an argument like so:
"""

class Flower(models.Model):
  petal_color = models.CharField(max_length=20)
  petal_number = models.IntegerField(default=0)

"""
These arguments give us finer control over what data we want to include in our database.
For .CharField() we used max_length to limit the number of acceptable characters to 20.
We can even set default values, like for petal_number, we set default=0 meaning if we didn’t provide a value for petal_number the value is automatically 0.

Each field accepts different arguments, so make sure to check the documentation.
Instructions
1.

Let’s continue to build out our Owner and Patient models, starting with Owner.

In the Owner model:

    delete the pass keyword
    add a first_name field that is a field type of .CharField()
    add an argument so first_name can take up to 30 characters

You no longer need the pass keyword since you’re adding in fields!

Here’s a refresher on syntax:
"""

class Flower(models.Model):
  petal_color = models.CharField(max_length=20)

"""
2.

The Owner model still needs two more fields:

    last_name that expects a string with a max of 30 characters.
    phone that expects a string with a max of 30 characters.

Both field types are .CharField()s.

phone is a .CharField() instead of an .
IntegerField() because we don’t want the database to interpret character like - as a minus sign and evaluate it as an expression, e.g.
"""

example_str = "555-123-1455"
# Evaluates to: "555-123-1455"

example_int = 555-123-1455
# Evaluates to: -1023

"""
3.

Great, you can turn your attention to the Patient model now. Add in:

    breed as a character field with a max length of 200 characters.
    pet_name as a character field with a max length of 200 characters.
    age as an integer field that defaults to 0.

We’ll continue to add to the Patient model later on to match the provided schema earlier.

For now, add in the fields provided.

Here’s a refresher on syntax:
"""

class Flower(models.Model):
  petal_color = models.CharField(max_length=20)
  petal_number = models.IntegerField(default=0)

"""
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
"""
