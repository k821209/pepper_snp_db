from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class snpdb(models.Model):
     cardname   = models.CharField(max_length=20)
     chromosome = models.CharField(max_length=20)
     position   = models.IntegerField(default=0)
     reference  = models.CharField(max_length=5)
     var_a      = models.CharField(max_length=20)
     var_t      = models.CharField(max_length=20)
     var_g      = models.CharField(max_length=20)
     var_c      = models.CharField(max_length=20)
     gwas_sig_report = models.CharField(max_length=50) # PubMed ID 
     created_date = models.DateTimeField(default=timezone.now)
     published_date = models.DateTimeField(blank=True, null=True)
     def publish(self):
          self.published_date = timezone.now()
          self.save()
     def __unicode__(self):  
          return self.cardname


