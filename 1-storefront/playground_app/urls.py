from django.urls import path
import views
urlpatterns=[
    path('/hello',views.say_hello)
]