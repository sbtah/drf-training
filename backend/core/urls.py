from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls", namespace="api")),
    path("api/search/", include("search.urls", namespace="search")),
    path("api/products/", include("products.urls", namespace="products")),
    path("api/v2/", include("core.routers", namespace="products-v2")),
]
