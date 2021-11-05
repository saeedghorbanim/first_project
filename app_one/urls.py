from django.urls import path
from . import views

urlpatterns = [
    #localhost8000/first-app/first-route
    #localhost8000/first-route
    path('first-route/', views.index),

    #localhost8000/first-app/second-sample
    #localhost8000/second-sample
    path('second-sample/', views.people),

    path('', views.root_method),
    path('another_route', views.another_method),
    path('redirected_route', views.redirected_method)
]
