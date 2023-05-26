from django.urls import include, path

from . import views

urlpatterns = [
    path('sign-up/',views.signUp ,name="sign-up"),
]