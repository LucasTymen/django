"""
Models and Databases
Field Type Optional Arguments

We can continue to customize our models by supplying fields with options, that specify how data can be inserted into the database.
Django provides field option documentation (https://docs.djangoproject.com/en/4.1/topics/db/models/#field-options), which shows a huge list of these options. Let’s go over some common ones together!

One common option is null that can take on a value of True or False.
This null option tells the database if a field can be left intentionally void of information.
By default, Django sets null=False. However, we can override the default and set null=True. Here’s an example:
"""

class Flower(model.Model):
  petal_number = models.IntegerField(max_length=20, null=True)
  # Other fields

"""
With the code above, when we create a Flower instance, we can set petal_number to null.

Another common option is blank, which is similar to null, but setting blank to True means a field doesn’t have to take anything, not even a null value.
By default blank is False.
"""

class Flower(model.Model):
  nickname = models.CharField(max_length=20, blank=True)
  # Other fields

"""
Now, when we create a Flower instance, we can leave the nickname field blank.

The last one we’ll touch upon is choices which limits the input a field can accept.
We can set choices by creating a list of tuples that contain 2 items: a key and a value. Take for example:
"""

class Flower(models.Model):
  COLOR_CHOICES = [
     ("R", "Red"),
     ("Y", "Yellow"),
     ("P", "Purple"),
     ("O", "Other"),
  ]

  color = models.CharField(max_length=1, choices=COLOR_CHOICES)
  # Other fields

"""
For our Flower instance, we can specify its color with the limited choices provided
—> meaning our color field can only be assigned "R" (for "Red"), "Y" (for "Yellow"), or "P" (for "Purple"), or "O" (for "Other" from the COLOR_CHOICES list.
With choices we know exactly what data we can accept from users.

We covered 3 options in this exercise, but remember, there are many more field options to explore!
https://docs.djangoproject.com/en/4.1/topics/db/models/#field-options


Instructions


1.

Let’s implement choices for our Patient model, starting with creating the variables for our tuple’s key values.
This implementation will look slightly different from the provided examples, but it’s the same underlying concept.

In the Patient class, create the variables with the associated values:

    DOG with a value of "DO"
    CAT with a value of "CA"
    BIRD with a value of "BI"
    REPTILE with a value of "RE"
    OTHER with a value of "OT"

You’ll be using these values later in the list of tuples later.

As mentioned, this implementation will look different, different apps have different approaches — but both ways work for choices.

If we were to change our Flower example it would look like:
"""

class Flower(models.Model):
  ORIGINAL = "O"
  HYBRID = "H"
  LAB_GROWN = "L"

"""
2.

Below your newly created variables, you can create your list of tuples now.

The list should have a name of ANIMAL_TYPE_CHOICES and contain the values:

    (DOG, "Dog")
    (CAT, "Cat")
    (BIRD, "Bird")
    (REPTILE, "Reptile")
    (OTHER, "Other")

Using the Flowers example, the syntax would look like:
"""

class Flower(models.Model):
  ORIGINAL = "O"
  HYBRID = "H"
  LAB_GROWN=  "L"

  DNA = [
     (ORIGINAL, "Original"),
     (HYBRID, "Hybrid"),
     (LAB_GROWN, "Lab grown"),
  ]

"""
3.

Your tuple’s good to go, so you can create the actual field named animal_type. This field should:

    be a character field
    have a max length of 2 characters
    choices of ANIMAL_TYPE_CHOICES
    a default of OTHER

Using the Flowers example, the syntax would look like:
"""

class Flower(models.Model):
  ORIGINAL = "O"
  HYBRID = "H"
  LAB_GROWN=  "L"

  DNA = [
     (ORIGINAL, "Original"),
     (HYBRID, "Hybrid"),
     (LAB_GROWN,  "Lab grown"),
  ]

  dna = models.CharField(max_length=1, choices=DNA, default="O")

"""
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
"""
