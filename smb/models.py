from django.db import models


class Element(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Temperature(models.Model):
    measured_at = models.DateTimeField(auto_now=True)
    temperature = models.IntegerField(null=True, default=None)
    element = models.ForeignKey(Element, null=True, default=None,
                                related_name='temperatures',
                                on_delete=models.SET_NULL)

    def __str__(self):
        return "{}: {} - T: {}C".format(
            self.element.name if self.element else '-',
            self.measured_at,
            self.temperature
        )
