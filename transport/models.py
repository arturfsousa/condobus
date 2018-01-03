from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.utils.translation import ugettext_lazy as _
from org.models import Organization


class Bus(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='buses',
        verbose_name=_('Organization')
    )

    class Meta:
        verbose_name = _('Bus')
        verbose_name_plural = _('Buses')

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='routes',
        verbose_name=_('Organization')
    )

    class Meta:
        verbose_name = _('Route')
        verbose_name_plural = _('Routes')

    def __str__(self):
        return self.name


class StopPoint(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    location = models.PointField(_('Location'), default=Point(-22.99977, -43.36063))
    obs = models.TextField(_('Observation'), null=True, blank=True)
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name='stop_points',
        verbose_name=_('Route')
    )

    class Meta:
        verbose_name = _('StopPoint')
        verbose_name_plural = _('StopPoints')

    def __str__(self):
        return self.name


class Direction(models.Model):
    name = models.CharField(_('Name'), max_length=200)

    class Meta:
        verbose_name = _('Direction')
        verbose_name_plural = _('Directions')

    def __str__(self):
        return self.name


class TimeSheet(models.Model):
    version = models.PositiveSmallIntegerField(_('Version'))
    validity = models.DateField(_('Validity'))
    direction = models.ForeignKey(
        Direction,
        on_delete=models.CASCADE,
        related_name='time_sheets',
        verbose_name=_('Direction')
    )
    name = models.CharField(_('Name'), max_length=200)

    class Meta:
        verbose_name = _('TimeSheet')
        verbose_name_plural = _('TimeSheets')

    def __str__(self):
        return self.name
