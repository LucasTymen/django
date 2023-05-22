"""
Creating Your First Django App
Wiring Up a View

On the internet, every page needs its own URL because each URL displays unique information.
In Django, we can use something called a URLconf, for URL configuration.
This module is a set of patterns that Django will try to match the requested URL to find the correct view.

An app’s URLconf is located in a file named urls.py inside the app’s directory.
At the top of the urls.py we import the path object from django.urls and we import the view functions from views.py and add routes that direct to each of our view functions.

The urls.py will look like this:
"""

from django.urls import path
from . import views

urlpatterns = [
  path('', views.home),
  path('profile/', views.profile, name="profile")
]

"""
After the import statements is a list of patterns called urlpatterns, which contain the routes to each view function.
Each route is provided as a path() object that has three arguments:
the URL route as a string, the name of the function of the view, and an optional name used to refer to the view.

With the above example, when we navigate to the URL without any additional route, '', the home() view function will be called.
Going to the URL ending with /profile will call the profile() view function.

To make Django aware of the app’s URLconf, it must be included in the project’s URLconf, also called urls.py.

The default urls.py folder for a project looks like this:
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
  path("admin/", admin.site.urls),
]

"""
We can see that Django already includes some URLs for us in urlpatterns.
The admin page we visited earlier is already there: path('admin/', admin.site.urls).

To include the app’s URLconf we import the include path from django.urls and add a path()to the urlpatterns.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  path("admin/", admin.site.urls),
  path("", include("myapp.urls")),
]

"""
With both URLconfs set up, we can properly view our routes for the application: myapp in a web browser.
Instructions
1.

Create a file called urls.py in the djangovet/vetoffice directory and import path from django.urls and the view functions (from . import views).

Create a file called urls.py in djangovet/vetoffice. Import the path and views by including the following at the top of urls.py:
"""

from django.urls import path
from . import views

"""
2.

Include a urlpatterns list with a path() function in the list. Provide "" and views.home as arguments.

Include the URL patterns by adding to the urlpatterns list:
"""

urlpatterns = [
  path('', views.index)
]

"""
3.

You’ve set up the path inside your app, now time to set up the path in your overall project!

Inside the main URLconf (djangovet/djangovet/urls.py), import the include module from django.urls.

Import the include module inside djangovet/djangovet/urls.py.
4.

Use the path module to include the vetoffice URLconf to the main URLconf.

After you’ve included the path module, you can launch the server and check out your newly created page!

Include the vetoffice URLconf by adding path('', include('vetoffice.urls')) to the urlpatterns in djangovet/djangovet/urls.py.

To launch the server, in the terminal:

cd djangovet/

Then

python3 manage.py runserver 0.0.0.0:4001

You should see the text of the <h1> displayed in your mini-browser!
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
"""
