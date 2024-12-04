from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap, CategorySitemap, ProductSitemap, OrderSitemap


sitemaps = {
    'static': StaticSitemap,
    'categories': CategorySitemap,
    'products': ProductSitemap,
    # Include 'orders' only if they're public-facing
    # 'orders': OrderSitemap,
}


urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path("", views.index, name="index"),
    path("mabati/", views.mabati, name="mabati"),
    path("place_order/<str:name>/", views.place_order, name="place_order"),
    path("oda zako/",views.my_orders,name="my_orders"),
    path("wasifu/",views.wasifu,name="wasifu"),
    path("cancel_order/<int:pk>/",views.cancel_order,name="cancel_order"),
    path("update_order_status/<int:order_id>/",views.update_order_status,name="update_order_status"),
]
