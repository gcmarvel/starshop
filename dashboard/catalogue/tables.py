from oscar.apps.dashboard.catalogue.tables import ProductTable as CoreProductTable
from django.utils.translation import ugettext_lazy as _

from django_tables2 import A, Column,  TemplateColumn

from oscar.core.loading import get_class, get_model

Product = get_model('catalogue', 'Product')
Category = get_model('catalogue', 'Category')
ProductCategory = get_model('catalogue', 'Productcategory')
DashboardTable = get_class('dashboard.tables', 'DashboardTable')


class ProductTable(CoreProductTable):

    title = TemplateColumn(
        verbose_name=_('Title'),
        template_name='dashboard/catalogue/product_row_title.html',
        order_by='title', accessor=A('title'))
    image = TemplateColumn(
        verbose_name=_('Image'),
        template_name='dashboard/catalogue/product_row_image.html',
        orderable=False)
    product_class = Column(
        verbose_name=_('Product type'),
        accessor=A('product_class'),
        order_by='product_class__name')
    category = Column(
        verbose_name=_("Category"),
        accessor=A('linktocategory'),
        order_by='categories')
    actions = TemplateColumn(
        verbose_name=_('Actions'),
        template_name='dashboard/catalogue/product_row_actions.html',
        orderable=False)

    icon = "sitemap"

    class Meta(DashboardTable.Meta):
        model = Product
        fields = ('title', 'image', 'product_class', 'category', 'date_updated', 'actions')
        sequence = ('title', 'image', 'product_class', 'category', 'date_updated','...', 'actions' )
        order_by = '-date_updated'
        exclude = ('upc', 'variants', 'stock_records')
