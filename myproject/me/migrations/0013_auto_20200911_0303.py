# Generated by Django 3.0.8 on 2020-09-10 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0012_auto_20200911_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
