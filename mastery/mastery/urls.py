"""mastery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from tracker import views

urlpatterns = [
    path('', views.show_user),
    path('admin/', admin.site.urls),
    path('new_user', views.new_user),
    path('show_user', views.show_user),
    path('edit_user/<str:username>', views.edit_user),
    path('update_user/<str:username>', views.update_user),
    path('destroy_user/<str:username>', views.destroy_user),
    path('show_skills/<str:username>', views.show_skills),
    path('new_skill/<str:username>', views.new_skill),
    path('edit_skill/<str:username>/<str:skill_name>', views.edit_skill),
    path('update_skill/<str:username>/<str:skill_name>', views.update_skill),
    path('destroy_skill/<str:username>/<str:skill_name>', views.destroy_skill),
    path('oops', views.oops)
]
