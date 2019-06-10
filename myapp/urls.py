from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('hello', views.hello),
    path('hello_tem', views.hello_tem), #여기서 hello_tem과 views.hello_tem의 hello_tem은 굳이 같을 필요가 없다.
]
