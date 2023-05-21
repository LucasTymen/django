"""
Creating Your First Django App
Creating a Django Template

To place content generated from Django inside the HTML file, we need to turn our static HTML file into a template.

In the context of a web framework, templates are pages created with special markup that allows for backend data and commands to modify the contents of a page.
Django employs a special syntax called Django Templating Language to distinguish itself from HTML, CSS, and JavaScript.
That syntax in many template languages uses curly braces, sometimes referred to as handlebars, as a placeholder for data that is passed by Django.

In HTML, we use curly braces like this:

<h1>Hello, {{name}}</h1>

When we call the view to render the template, we can use something called a context to tell Django what to replace in the template.
The relationships in the context are referred to as a name/value pair. By default, a context is an empty dictionary.
Our context for name will look like this inside the view function:
"""

context = {"name": "Junior"}

"""
We then pass the context as an argument in the render function. The full view.py will look like this:
"""

from django.http import HttpResponse
from django.template import loader
def home(request):
  context = {"name": "Junior"}
  template = loader.get_template("app/home.html")
  return HttpResponse(template.render(context))

"""
This would return a webpage that says “Hello, Junior” inside an <h1> tag.

It’s quite common in Django to load templates, fill their context, and return an HttpResponse object with their rendered template.
Django provides a shortcut for this pattern called the render() function! The render() function will do the work of loading the template and provide the contexts when they are passed as arguments.

Our example above can be rewritten with the shortcut function like this:
"""

from django.shortcuts import render

def home(request):
  context = {"name": "Junior"}
  return render(request, "app/home.html", context)

"""
Note that we no longer need to import loader and HttpResponse when we use the render() function.
The render() function takes the request object as its first argument, a template name as its second argument, and a dictionary as an optional third argument that passes the context variables to the template.
Instructions
1.

Refactor the home() function in views.py to use the render() function and pass the request, template path as a string, "vetoffice/home.html" and context.

The render() function takes three arguments: The request, path to the template, and context.

"""
