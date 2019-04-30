from django.db import models

# Create your models here.


class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    parea_id = models.BigIntegerField(default=0)