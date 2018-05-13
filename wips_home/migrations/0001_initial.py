# Generated by Django 2.0.5 on 2018-05-13 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockLog',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('mac', models.CharField(max_length=6)),
                ('block_pkt', models.FileField(upload_to='')),
                ('atk_type', models.TextField()),
                ('pkt_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]