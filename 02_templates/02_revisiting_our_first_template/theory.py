"""
Templates
Revisiting Our First Template

The first template usually made is the homepage of the application.
Templates can be plain HTML files and are stored inside of appname/templates/appname/.
While the template can usually be left as a normal HTML file, most of the time Django Template Language or DTL will be added to the template to assist with the creation of the application.
If you want to go into more detail regarding how to build the application using plain HTML, check out our course here.
Please note that this lesson will be using DTL and HTML throughout the exercises.

When any template is referenced later, it will be done by calling appname/template_name.html.
This is to help the Django engine find the template because DTL will not look in any sub folders in the template folder for files.

Once the template is made, some of the code in views.py will have to be modified in order to render the template.
Rendering the template is the Django application taking the template and displaying it as a normal HTML page in a web browser.

Inside of views.py, we need functions, or classes, that tell the template what information to include.
For example, one function (homepage()) will be created that takes in one parameter called request.
The homepage() function will return another function called render() that takes two arguments.
The first being the request that gets passed into homepage(), and the name of the template.
Just as a refresher, the final method in views.py should look like the one below:
"""

def homepage(request):
  return render(request, "app_name/sample_template.html")

"""
These modifications to views.py will be covered in more detail in a later lesson.
In this lesson, the code for views.py will be provided so that we can focus primarily on templates and not the views.
Instructions
1.

Note: To save you some work and time, we’ve reorganized the structure of our Django project to have you automatically working in the root folder.
We’ve also made it so your development server is automatically running!

home.html is opened in the code editor, notice that it’s now empty. That’s because we will be building this from scratch with DTL in mind.

For now, add a heading (<h1>) that says Welcome to Vet Office! and a paragraph (<p>) that says Welcome!.
Don’t worry, everything else will be added back later.

home.html should look very similar to the following code.

<h1>This is the title</h1>
<p>This is a paragraph following the title</p>

If you aren’t too comfortable with HTML at the moment, try taking our course introducing HTML.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
"""
