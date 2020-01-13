from oscar.core.loading import get_model
from oscar.apps.dashboard.pages.forms import PageUpdateForm as CorePageUpdateForm

FlatPage = get_model('flatpages', 'FlatPage')


class PageUpdateForm(CorePageUpdateForm):

    class Meta:
        model = FlatPage

        fields = ('title', 'url', 'name', 'owner', 'constellation', 'constellation_img', 'draper', 'starclass',
                  'starclass_img', 'magnitude', 'abs_magnitude', 'distance', 'spectrum', 'diameter', 'luminosity',
                  'temperature', 'telescope1', 'telescope1_label', 'telescope2', 'telescope2_label', 'right_ascension',
                  'declination', 'coordinates_fullscreen', 'coordinates_1to1', 'coordinates_1to4', 'coordinates_1to8',
                  'video', 'dossier_1_img', 'dossier_1_cn', 'dossier_2_img', 'dossier_2_cn', 'dossier_3_img', 'dossier_3_cn',
                  'dossier_3_img', 'dossier_3_cn', 'dossier_4_img', 'dossier_4_cn', 'dossier_5_img', 'dossier_5_cn',
                  'dossier_6_img', 'dossier_6_cn', 'dossier_7_img', 'dossier_7_cn', 'dossier_8_img', 'dossier_8_cn',)
