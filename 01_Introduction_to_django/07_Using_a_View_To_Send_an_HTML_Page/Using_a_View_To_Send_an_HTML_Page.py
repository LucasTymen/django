"""
Creating Your First Django App
Using a View To Send an HTML Page

We just made a view that sends raw text to the browser.
But, websites aren’t just plain text! In order to create stylish web pages, we mainly use HTML, CSS, and JavaScript.

We can use Django to render an HTML page when a view function is called.
Django will look in each app folder inside INSTALLED_APPS for directories named templates.
The best practice for structuring this folder is to namespace them.
That is to place our HTML pages inside a directory that has the same name as your app within the templates/ directory.

The resulting templates folder structure will look like this:

myapp/
└── templates/
    └── myapp/
      └── mytemplate.html

The reason for this nested structure is if there was a template file with the same name in a different application, Django would be unable to distinguish between them.
We need to be able to point Django at the right one and namespacing them ensures against future conflicts, so that apps lower down in the INSTALLED_APPS setting do not override previous templates.

With our file structure set up, we can build out the logic in our view function in views.py like so:
"""

from django.template import loader
def home():
  template = loader.get_template("app/home.html")
  return HttpResponse(template.render())

"""
In the above code, we import loader from django.template.
Inside the view function (home()) we load the template with .get_template().
Then, we use the .render() method on the template object inside the HttpResponse object to send HTML pages to clients.
Instructions
1.

Create the template directory structure inside the vetoffice app folder.
Click on the folder icon on the top-left corner and hover the vetoffice/ folder.
Select the three dots to the right of the menu item to bring up the options menu.
Click on the “New Folder” option and provide templates as the name.
Again, select the “New Folder” option on the templates/ folder create another folder within it named, vetoffice/.

The final folder structure should look like this.

djangovet/
└──vetoffice/
  └── templates/
    └── vetoffice/

Using the file explorer, inside vetoffice create a folder named templates.
Inside the templates folder, create another folder called vetoffice.

Screenshot of add Folder
2.

Create a file named home.html inside the vetoffice/ template folder by selecting the vetoffice/ folder options in the file explorer and select “New File”.
Inside it copy in the following HTML:

<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Vet Office</title>
</head>
<body>
  <h1>Welcome to the Vet Office Page</h1>
</body>
</html>

Copy the provided HTML into a file named home.html inside djangovet/vetoffice/templates/vetoffice/
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
"""
