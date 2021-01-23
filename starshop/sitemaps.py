from django.contrib.sitemaps import Sitemap
from oscar.core.loading import get_model

Product = get_model('catalogue', 'Product')
Category = get_model('catalogue', 'Category')


class StaticSitemap(Sitemap):

    def items(self):
        return ['/', '/terms/', '/reviews/', ]

    def location(self, obj):
        return obj


class ProductSitemap(Sitemap):

    def items(self):
        return Product.objects.browsable()


class CategorySitemap(Sitemap):

    def items(self):
        return Category.objects.all()


sitemaps = {
    'static': StaticSitemap,
    'product': ProductSitemap,
    'categories': CategorySitemap,
}
