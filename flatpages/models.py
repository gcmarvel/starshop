from django.contrib.sites.models import Site
from django.db import models
from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri
from django.utils.translation import gettext_lazy as _


class FlatPage(models.Model):
    url = models.CharField('URL', max_length=100, db_index=True)
    content = models.CharField('URL', max_length=100, blank=True)
    title = models.CharField('title', max_length=300)
    name = models.CharField('name', max_length=200, null=True)
    owner = models.CharField('owner', max_length=100, null=True)
    constellation = models.CharField('constellation', max_length=100, null=True)
    constellation_img = models.CharField('constellation image', max_length=200, null=True)
    draper = models.CharField('draper', max_length=20, null=True)
    starclass = models.CharField('starclass', max_length=100, null=True)
    starclass_img = models.CharField('starclass image', max_length=200, null=True)
    magnitude = models.CharField('visual magnitude', max_length=20, null=True)
    abs_magnitude = models.CharField('absolute magnitude', max_length=20, null=True)
    distance = models.CharField('distance', max_length=20, null=True)
    spectrum = models.CharField('spectrum', max_length=20, null=True)
    diameter = models.CharField('diameter', max_length=20, null=True)
    luminosity = models.CharField('luminocity', max_length=20, null=True)
    temperature = models.CharField('temperature', max_length=20, null=True)
    telescope1 = models.ImageField('telescope 1', null=True)
    telescope1_label = models.CharField('telescope 1 label', max_length=20, null=True)
    telescope2 = models.ImageField('telescope 2', null=True)
    telescope2_label = models.CharField('telescope 2 label', max_length=20, null=True)
    right_ascension = models.CharField('right ascension', max_length=40, null=True)
    declination = models.CharField('declination', max_length=40, null=True)
    coordinates_fullscreen = models.ImageField('coordinates fullscreen', null=True)
    coordinates_1to1 = models.ImageField('coordinates 1 to 1', null=True)
    coordinates_1to4 = models.ImageField('coordinates 1 to 4', null=True)
    coordinates_1to8 = models.ImageField('coordinates 1 to 8', null=True)
    video = models.URLField('video', blank=True)
    dossier_1_img = models.ImageField('dossier 1 image', null=True)
    dossier_1_cn = models.TextField('dossier 1 content', null=True, blank=True)
    dossier_2_img = models.ImageField('dossier 2 image', null=True)
    dossier_2_cn = models.TextField('dossier 2 content', null=True, blank=True)
    dossier_3_img = models.ImageField('dossier 3 image', null=True)
    dossier_3_cn = models.TextField('dossier 3 content', null=True, blank=True)
    dossier_4_img = models.ImageField('dossier 4 image', null=True)
    dossier_4_cn = models.TextField('dossier 4 content', null=True, blank=True)
    dossier_5_img = models.ImageField('dossier 5 image', null=True)
    dossier_5_cn = models.TextField('dossier 5 content', null=True, blank=True)
    dossier_6_img = models.ImageField('dossier 6 image', null=True)
    dossier_6_cn = models.TextField('dossier 6 content', null=True, blank=True)
    dossier_7_img = models.ImageField('dossier 7 image', null=True)
    dossier_7_cn = models.TextField('dossier 7 content', null=True, blank=True)
    dossier_8_img = models.ImageField('dossier 8 image', null=True)
    dossier_8_cn = models.TextField('dossier 8 content', null=True, blank=True)
    enable_comments = models.BooleanField('enable comments', default=False, null=True)
    template_name = models.CharField(
        _('template name'),
        max_length=70,
        blank=True,
        help_text=_(
            "Example: 'flatpages/contact_page.html'. If this isn't provided, "
            "the system will use 'flatpages/default.html'."
        ),
    )
    registration_required = models.BooleanField(
        _('registration required'),
        help_text=_("If this is checked, only logged-in users will be able to view the page."),
        default=False,
    )
    sites = models.ManyToManyField(Site, verbose_name=_('sites'))

    class Meta:
        db_table = 'django_flatpage'
        verbose_name = _('flat page')
        verbose_name_plural = _('flat pages')
        ordering = ('url',)

    def __str__(self):
        return "%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        # Handle script prefix manually because we bypass reverse()
        return iri_to_uri(get_script_prefix().rstrip('/') + self.url)
