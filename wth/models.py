from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Location(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Measure(models.Model):
    measured_at = models.DateTimeField(auto_now=True)
    temperature = models.IntegerField(null=True, default=None)
    humidity = models.IntegerField(null=True, default=None)
    location = models.ForeignKey(Location, null=True, default=None,
                                 related_name='measures',
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return "{}: {} - T: {}C / H: {}%".format(
            self.location.name if self.location else '-',
            self.measured_at,
            self.temperature,
            self.humidity
        )
