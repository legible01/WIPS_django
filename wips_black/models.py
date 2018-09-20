from django.db import models
from django.utils import timezone


class blackList(models.Model):
    number = models.AutoField(primary_key=True)
    ap_mac = models.CharField(max_length=12)
    st_mac = models.CharField(max_length=12)

    channel= models.IntegerField()
    choice_mac_type = (
        (0,'AP_TYPE'),
        (1, 'ST_TYPE'),
    )
    choice_ap_enc =(
        (1,'WEP'),
        (10, 'WPA1'),
        (20, 'WPA2'),
    )
    choice_ap_cipher = (
    	(0,'OPEN'),
    	(11, 'GROUP_CIPHER_SUITE'),
    	(12, 'WEP40'),
    	(13, 'TKIP'),
    	(14, 'C_RESERVATON'),
    	(15, 'CCMP'),
    	(16, 'WEP104'),
    )
    choice_ap_auth = (
    	(17,'A_RESERVATION'),
    	(18, 'A_8021X'),
    	(19, 'PSK'),
    )
    mac_type = models.IntegerField(choices=choice_mac_type)
    ap_enc = models.IntegerField(choices=choice_ap_enc)
    ap_cipher = models.IntegerField(choices=choice_ap_cipher)
    ap_auth = models.IntegerField(choices=choice_ap_auth)
    block_stat = models.BooleanField(blank=True,default='False')   	    


    


    def __str__(self):
        return self.ap_mac
