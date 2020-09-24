# Generated by Django 3.0.8 on 2020-09-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0005_experience_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_type', models.CharField(blank=True, default=None, max_length=20)),
                ('technology', models.CharField(blank=True, default=None, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='color',
            field=models.CharField(default='primary', max_length=20),
        ),
    ]
