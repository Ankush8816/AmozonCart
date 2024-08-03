
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="BlogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome")

]
