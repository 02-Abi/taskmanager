from django.contrib import admin
from django.urls import path
from core.views import (
    signup_view,
    login_view,
    logout_view,
    dashboard_view,
    create_task_view,
    delete_task_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),

    path("dashboard/", dashboard_view, name="dashboard"),
    path("create/", create_task_view, name="create_task"),
    path("delete/<int:task_id>/", delete_task_view, name="delete_task"),
]
