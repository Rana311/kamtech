# Generated by Django 2.1.2 on 2018-11-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0003_auto_20181111_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='hours',
            field=models.CharField(default='10:00Am – 08:00PM (Mon-Sat)', max_length=100),
        ),
    ]
