# Generated by Django 3.2 on 2021-04-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_qualification_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='experience',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='employee',
            name='target',
            field=models.FloatField(),
        ),
    ]
