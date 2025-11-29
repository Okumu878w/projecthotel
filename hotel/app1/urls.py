from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home ,name="home"),
    path('about', views.about ,name="about"),
    path('book', views.book ,name="book"),
    path('chef', views.chef ,name="chef"),
    path('event', views.event ,name="event"),
    path('gallery', views.gallery ,name="gallery"),
    path('menu', views.menu ,name="menu"),
    path('display', views.orderdisplay ,name="orders"),
    path('dispone/<str:pk>', views.orderdispone ,name="dispone"),
    path('update/<str:pk>', views.update ,name="update"),
    path('delete/<str:pk>', views.delete ,name="delete")

]
