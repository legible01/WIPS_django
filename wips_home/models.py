from django.db import models
from django.utils import timezone
#import sys
#sys.path.append('/home/wipsDjango/wips/mod_def')
#import fieldType


class BlockLog(models.Model):
    number = models.AutoField(primary_key=True)
    #number = BigIntegerField()
    #mac = fieldType.PositiveBigIntegerField()
    mac = models.CharField(max_length=12)
    #block_pkt = models.FileField()
    atk_type = models.TextField()
    #pkt_time = models.DateTimeField(
     #       blank=True, null=True)
    block_stat = models.BooleanField(blank=True,default='False')

    def __str__(self):
        return self.atk_type
# Create your models here.
