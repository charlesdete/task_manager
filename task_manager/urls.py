# task_manager/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import JsonResponse, HttpResponseRedirect
from users.views import CookieTokenRefreshView, CookieTokenObtainPairView, LogoutView

schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version="v1",
        description="API documentation for Task Manager",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Simple health check / landing view
def home(request):
    return JsonResponse({"message": "Task Manager API is running"})

urlpatterns = [
    # Root landing page
    path("", home, name="home"),

    # Admin
    path("admin/", admin.site.urls),

    # App routes
    path("api/task/", include("task.urls")),
    path("api/department/", include("department.urls")),
    path("api/notification/", include("notification.urls")),
    path("api/users/", include("users.urls")),
    path("api/file/", include("file.urls")),

    # Auth routes
    path("api/logout/", LogoutView.as_view(), name="logout"),
    path("api/token/", CookieTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", CookieTokenRefreshView.as_view(), name="token_refresh"),

    # API docs
    path("api/swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    # Raw schema
    path("api/openapi.json", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("api/openapi.yaml", schema_view.without_ui(cache_timeout=0), name="schema-yaml"),
]