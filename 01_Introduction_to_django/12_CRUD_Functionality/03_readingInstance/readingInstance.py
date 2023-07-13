"""CRUD Functionality
Reading Instances

Being able to read instances of a model can give us more information about what’s stored in the database and the shape of our data.
When we want to view all instances of a model, we can run the .all() method on the model like so:
https://docs.djangoproject.com/en/3.1/ref/models/querysets/#all

>>> every_instance = ModelName.objects.all()

Here we created a variable called every_instance.
In the variable, we called a model followed by .objects followed by the .all() query method.
This will return every instance of the model, which should look something like this:

>>> every_instance
<QuerySet [<ModelName: object (1)>, <ModelName: object (2)>]>

Our code returns us a QuerySet, a collection of objects from our database.
In this QuerySet two instances, each instance associated with a number which is the instance’s ID number.
We should also know that a QuerySet is indexable, meaning we can grab an instance by their index.

>>> every_instance[0]
<ModelName: object (1)>

In the above code snippet, we referenced the variable every_instance and searched for the instance in the index position 0.
In the next line, we get returned the first instance in the QuerySet (<ModelName: object (1)>).

There’s also another way that we can return the first instance of a model using a query method using the .first() query method:

>>> first_instance = ModelName.objects.first()
>>> first_instance
<ModelName: object (1)>

In our code snippet, we created a variable called first_instance where we called ModelName.objects.first().
Then, we referenced the variable first_instance and it returned us the very first instance created for that model.

The .first() and .all() method (or any other method) can be combined with other methods to make more complicated queries
but we will get deeper into this as we progress throughout the lesson.
Instructions
1.

Since we’ll be primarily working in the shell for this lesson, run these commands to get started:

    Launch Python shell using:

    python3 manage.py shell

    Import the Owner model using:

    from vetoffice.models import Owner

    Reminder Note:
    If your screen size doesn’t allow for the commands to fit on a single line, the tests in this lesson’s exercises may fail.
    To ensure that tests are working properly, please stretch out the length of the Terminal to fit any commands into a single line.

2.

In the terminal create a variable called all_instances.

In the variable use the Owner model and run the .all() query method on the model.

Then type out the variable all_instances and hit Enter to view all instances of the model.

Note: We’ve provided 3 Owner instances for you to see a lengthier queryset.

Here’s a syntax refresher.

variable_name = ModelName.objects.method_name()

3.

Access the first instance of the Owner model using .first() in a variable called first_owner.

First, we need to create a variable called first_owner.
Then in the variable, we need to call the Owner model followed by .objects followed by the .first() query method:

first_owner = Owner.objects.first()

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
"""
