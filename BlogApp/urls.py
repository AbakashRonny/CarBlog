from django.urls import path
from . import views
urlpatterns=[
    path('blog/',views.car_blog,name='blog'),
    path('add_blog/',views.add_blog),
    path('<int:id>/',views.description,name='description'),
]