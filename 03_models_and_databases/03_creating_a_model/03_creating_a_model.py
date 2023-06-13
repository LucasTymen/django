"""
Models and Databases
Creating a Model

We’ve thought through the schema and our database was set up by default when we first created our project. Time to create our models!

Every time we create a new app, Django provides us with a folder structure for our work which includes a file called models.py with the following starter code:
"""

from django.db import models

# Create your models here.

"""
To create a model, we write a class, like so:
"""

class Flower(models.Model):
  ## Define attributes here
  pass

"""
Notice that our model actually inherits from the Model parent class django.db.models.Model module. These models will later inform the database to use this schema to build its tables. In the example above, our database will know that incoming data records will contain attributes of our flowers, like perhaps, petal color, number of petals, average height, etc. For now, we’ve added the pass keyword to avoid any errors since Python doesn’t allow for empty classes.

Let’s now create our first models!
Instructions
1.

The file vetoffice/models.py is opened in the code editor.

    Under the provided comment, create a model called Owner.
    In the body of the class, add in the pass keyword to avoid getting an error about missing fields.

Remember to provide the models.Model argument for your class:
"""

class SampleModel(models.Model):
  pass

"""
2.

Add another model called Patient along with the pass keyword.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
"""
