from django.urls import path,include
from authentication import views

urlpatterns = [
   
    path('', views.home,name="home"),
    path('signin', views.signin,name="signin"),
    path('signout', views.signout,name="signout"),
    path('signup', views.signup,name="signup"),
]