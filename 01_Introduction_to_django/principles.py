"""


urlpatterns
"""
path("", views.home, name="home")
"""
URLs are created using the path() function which takes three arguments— the route, the view function, and an optional name.

Viewing the Project
When the development server is started on the default port, the project can be viewed in the browser at the URL: http://localhost:8000.

Starting a Development Server:
"""
python3 manage.py runserver
"""

HTTP Responses
"""
def myView(request):
  return HttpResponse("Here is my response")
"""
A response to a web request is given in a HttpResponse object, which can be anything from HTML to an image.


Projects and Apps

└── myproject/
  └── myproject/
  └── myapp/



A project is a collection of configurations and individual apps for a particular website. Each app should have a clearly defined purpose.
"""

"""
Template Namespace

└── myapp/
  └── templates/
    └── myapp/
      └── mytemplate.html

mysite/
├── manage.py
└── mysite
    ├── __init__.py
    ├── settings.py
    └── urls.py

Templates should be namespaced by creating a nested folder structure to avoid name conflicts between apps.

__
manage.py
manage.py is a file that includes commands to administer a Django app.
__
settings.py
The settings.py file contains the project settings for a Django project.
__
Migrations
python3 manage.py migrate
The migrate command will update database models for projects installed in INSTALLED_APPS.

"""
