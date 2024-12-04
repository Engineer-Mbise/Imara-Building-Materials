from django.contrib.sitemaps import Sitemap
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
