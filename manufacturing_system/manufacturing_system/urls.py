from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('api/', include('core.urls')),  # Include core app APIs
    re_path(r'^.*$', TemplateView.as_view(template_name="index.html")),  # Catch-all route for Vue frontend
]
