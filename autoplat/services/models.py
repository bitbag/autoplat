from django.db import models

class services(models.Model):
    service_id = models.IntegerField()
    service_name = models.CharField(max_length=120)
    service_version = models.CharField(max_length=30,default='')
    service_port = models.IntegerField()
    service_status = models.CharField(max_length=10)
    remark = models.TextField()


