from django.urls import path
from . import views
urlpatterns = [
   path('hi',views.hi),
   path('create',views.create),
   path('',views.Home),
   path('delete/<aid>',views.delete),
   path('edit/<aid>',views.edit),
   path('details',views.view_details),
   path('register',views.register)
]