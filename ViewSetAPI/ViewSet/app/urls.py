from django.urls import path,include
from . import views

urlpatterns = [
    path('api/',views.CarAPI.as_view()),
    path('api/<pk>',views.CarAPI.as_view()),

]


# tumrukaji