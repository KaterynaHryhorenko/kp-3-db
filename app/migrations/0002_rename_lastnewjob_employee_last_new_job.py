# Generated by Django 3.2 on 2021-04-16 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='lastnewjob',
            new_name='last_new_job',
        ),
    ]