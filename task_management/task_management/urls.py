"""task_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from project.views import ProjectListView, ProjectView, MainView, CreateProjectView
from django.contrib.auth.views import LogoutView
from accounts.views import RegisterView, LoginView
from task.views import CreateTaskView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name="home"),
    path('register/', RegisterView.as_view(), name="register"),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/create/', CreateProjectView.as_view(), name="create_project"),
    path('project/<str:project_id>/', ProjectView.as_view(), name="project_task"),
    path('project/<str:project_id>/task.create', CreateTaskView.as_view(), name="create_task"),
    path('login/', LoginView.as_view(), name="app_login"),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
