"""litreview_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from authentication import views as auth_views
from ticket import views as ticket_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', auth_views.sign_in_form),
    path('sign_up/', auth_views.sign_up_form),
    path('logout/', include("django.contrib.auth.urls")),
    path('create_ticket/', ticket_views.create_ticket),
    path('posts/', ticket_views.posts_page),
    path('posts/delete_ticket/<int:id>', ticket_views.delete_ticket),
    path('posts/edit_ticket/<int:id>', ticket_views.edit_ticket),

]
