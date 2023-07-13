"""

CRUD Functionality
Updating an Instance

In the previous exercise, we learned how to view all instances of a model and individual instances.
Now let’s learn how to update an instance’s field value.

Imagine we stored our first instance of a model in a variable called first_instance.
To view one of its field’s values we can use dot notation:

first_instance.name

Above, we’re accessing first_instance‘s .name field’s value. This would give us an output of the value like so:

>>> first_instance.name
'Asiqur'

If we want to change the field’s value, we can reassign it to something else.

>>> first_instance.name = "Ruqisa"

When we hit Enter the instance’s name field value will be changed to "Ruqisa".
If we type out first_instance.name again and hit Enter it will return an output value of "Ruqisa".

>>> first_instance.name
'Ruqisa'

Great! We were able to update the field value of our instance, but it’s still not saved into our database until we call the .save() method like so:

>>> first_instance.save()

Instructions
1.

As mentioned, here are the commands to get started:

python3 manage.py shell

Followed by:

from vetoffice.models import Owner

    We can launch the Python shell by running:

    python3 manage.py shell

    We can import the Owner model by using the following command:

    from vetoffice.models import Owner

2.

Now that we’re in the shell and have imported our Owner model:

    Store the first instance of the Owner model in a variable called first_owner by using the .first() query method.

    Access the .first_name field of the instance saved in the first_owner variable.

We can access the first instance of a model using .first() query method by following the below syntax:

var_name = ModelName.objects.first()

We can access the instance field by using dot notation like so:

var_name.field_name

3.

Change the value of the field first_name of the instance saved in the first_owner variable to "Khadaza".

We can use the following syntax to change the value of an instance field.

variable_name.field_name = "change_value_here"

4.

Use the .save() method on the first_owner variable to send the change into the database.

Call the .save() method on the first_owner variable.

var_name.save()

5.

Type out first_owner.first_name and hit Enter again to see the changes.

Use the following syntax as reference:

var_name.field_name

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
