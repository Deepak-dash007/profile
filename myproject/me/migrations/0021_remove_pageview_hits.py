# Generated by Django 3.0.8 on 2020-09-24 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0020_pageview_when'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageview',
            name='hits',
        ),
    ]
