# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import RedirectView
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
# from base.admin_site import admin_site 

# urlpatterns = [
#     path("admin/", admin_site.urls),

#     # Include your users app routes
#     path("/api/", include("users.urls")),
#     path("api/", include("task.urls")),
#     path("api/", include("notification.urls")),
#     path("api/", include("file.urls")),
#     path("api/", include("department.urls")),
#     # JWT endpoints
#     path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
#     path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

#     # Root → redirect to admin
#     path("", RedirectView.as_view(url="/admin/", permanent=False)),
# ]
# # task_manager/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version="v1",
        description="API documentation for Task Manager",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Your app routes
    path("api/task/", include("task.urls")),
    path("api/department/", include("department.urls")),
    path("api/notification/", include("notification.urls")),
    path("api/users/", include("users.urls")),
    path("api/file/", include("file.urls")),
    # Swagger / Redoc UIs
    path("api/swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    # Raw schema download endpoints
    path("api/openapi.json", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("api/openapi.yaml", schema_view.without_ui(cache_timeout=0), name="schema-yaml"),
]
