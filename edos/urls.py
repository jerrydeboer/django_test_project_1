from django.urls import path

from . import views


urlpatterns = [
    path('', views.new_template, name="new_template"),
]
