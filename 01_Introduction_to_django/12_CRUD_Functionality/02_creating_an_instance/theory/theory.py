"""
CRUD Functionality
Creating an Instance

In this exercise, we will use the Python shell to create instances of models.
The Python shell is a command-line tool that starts up a Python interpreter which we will use to execute CRUD functionality.

We can run the Python shell by using the following command in the command-line tool.

python3 manage.py shell

In order to work with our models in the Python shell we need to import them the same way we would in a Python file:

>>> from app_name.models import ModelName

With our model imported, we can start creating instances (specific examples) of the model.
Let’s say that we’re creating a website like Twitter that has a Post model with the fields title and description.
To create an instance of our model we need to call our model and fill out the fields like so:

>>> post_instance=Post(title="New", description="My Post")

Here, we start with a variable called post_instance that will store our instance.
Then we used the Post model and provided the necessary arguments and values for the title and description fields.
Note that while variables are not necessary to create instances, it gives us a nice way to refer to our created instances later on.

We’ve created our instance but we still need to save it to our database by calling .save() on the post_instance variable:

>>> post_instance.save()

With our instance made, we should exit out of the shell.
We can exit out of the Python shell by typing out the command exit(). In Windows we can press ctrl + Z.
On Mac or Linux ctrl + D.
Instructions
1.

Launch the Python shell in the terminal using:
"""
python3 manage.py shell
"""
    Note: If your screen size doesn’t allow for the commands to fit on a single line, the tests in this lesson’s exercises may fail.
    To ensure that tests are working properly, please stretch out the length of the Terminal to fit any commands into a single line.

Since we’re already in the root folder in the terminal, we can launch the Python shell by running

python3 manage.py shell

2.

Import the Owner model from the vetoffice app with the following code:

from vetoffice.models import Owner

Importing a model into a Python shell is the same as importing a model in a Python file.

from app_name.models import modelName

3.

Create an instance of the Owner model using a variable called owner_instance with the fields:
"""

    first_name as "Vint"

    last_name as "Kahn"

    phone as "951-262-3062"

"""
Once we create our owner_instance variable we can call our Owner model inside the variable.
Then in our Owner model, we can fill out each of its fields.
"""

var_name=Post(field_1="blank", field_2="blank again")

"""
4.

Save the instance of the model by calling .save() on owner_instance.
"""

Call.save() on the owner_instance variable like so:

owner_instance.save()

"""
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
