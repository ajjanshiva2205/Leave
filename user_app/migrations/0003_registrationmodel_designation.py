# Generated by Django 2.0.2 on 2019-12-19 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_registrationmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationmodel',
            name='designation',
            field=models.CharField(default=False, max_length=30),
        ),
    ]
