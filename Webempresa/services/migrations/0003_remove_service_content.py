# Generated by Django 2.2.4 on 2019-10-02 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_remove_service_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='content',
        ),
    ]