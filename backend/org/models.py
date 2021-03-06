from django.db import models
from django.utils.translation import ugettext_lazy as _


class Organization(models.Model):

    name = models.CharField(_('Name'), max_length=200)
    logo = models.ImageField(null=True, blank=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    rules = models.TextField(_('Rules'), null=True, blank=True)

    class Meta:
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')

    def __str__(self):
        return self.name
