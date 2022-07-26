from django.db import models

class employee(models.Model):
    eid= models.CharField(max_length=25)
    ename= models.CharField(max_length=25)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=30)