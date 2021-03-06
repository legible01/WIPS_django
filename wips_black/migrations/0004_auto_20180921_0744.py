# Generated by Django 2.1.1 on 2018-09-20 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wips_black', '0003_auto_20180921_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='blacklist',
            name='ap_auth',
            field=models.IntegerField(choices=[(17, 'A_RESERVATION'), (18, 'A_8021X'), (19, 'PSK')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blacklist',
            name='ap_cipher',
            field=models.IntegerField(choices=[(0, 'OPEN'), (11, 'GROUP_CIPHER_SUITE'), (12, 'WEP40'), (13, 'TKIP'), (14, 'C_RESERVATON'), (15, 'CCMP'), (16, 'WEP104')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blacklist',
            name='ap_enc',
            field=models.IntegerField(choices=[(1, 'WEP'), (10, 'WPA1'), (20, 'WPA2')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blacklist',
            name='mac_type',
            field=models.IntegerField(choices=[(0, 'AP_TYPE'), (1, 'ST_TYPE')], default=1),
            preserve_default=False,
        ),
    ]
