# Generated by Django 4.2.2 on 2023-08-09 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='attach_file',
            field=models.FileField(blank=True, null=True, upload_to='attachment'),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(max_length=20),
        ),
    ]
