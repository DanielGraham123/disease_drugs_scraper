from django.db import models

class Disease(models.Model):
    """
    Disease model
    """
    name = models.CharField(max_length=500, editable=False)
    description = models.TextField(default='', blank=True, max_length=500000)
    symptoms =  models.TextField(max_length=5000, default='', blank=True)
    causes = models.TextField(default='', blank=True, max_length=5000)
    complications = models.TextField(default='', blank=True, max_length=5000)
    risks = models.TextField(blank=True, default='', max_length=5000)
    preventions = models.TextField(blank=True, default='', max_length=5000)
    link = models.URLField(null=True, default='')

    def __str__(self):
        return '{}'.format(str(self.name))
