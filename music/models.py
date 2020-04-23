from django.db import models

class Register_form(models.Model):
      Application_no = models.CharField( max_length=100)
      password = models.CharField(max_length=100)
      security = models.CharField(max_length=100)




