from django.contrib.sitemaps import Sitemap
from .models import Category, Product, Order
from django.urls import reverse

class StaticSitemap(Sitemap):
    changefreq = "daily"  # How frequently the page content changes
    priority = 0.8  # Relative importance of the page

    def items(self):
        # Return the names of static views to include in the sitemap
        return ['index', 'wasifu']

    def location(self, item):
        # Return the URL for each item
        return reverse(item)




# Category Sitemap
class CategorySitemap(Sitemap):
    changefreq = "weekly"  # Adjust based on update frequency of categories
    priority = 0.9

    def items(self):
        return Category.objects.all()





# Product Sitemap
class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Product.objects.all()

  




# Order Sitemap (Optional - Only include if orders are public-facing)
class OrderSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6

    def items(self):
        return Order.objects.filter(status=Order.OrderStatus.APPROVED)
