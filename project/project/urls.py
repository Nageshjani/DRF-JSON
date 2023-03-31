"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import books,book_detail,book_create,book_delete,book_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',books,name='books_list'),
    path('create/', book_create, name='book_create'),
    path('detail/<int:pk>',book_detail, name='book_detail'),
    path('update/<int:pk>',book_update, name='book_update'),
    path('delete/<int:pk>',book_delete, name='book_delete'),

]