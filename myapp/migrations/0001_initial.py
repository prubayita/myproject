# Generated by Django 4.2.2 on 2023-08-09 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('description', models.TextField(blank=True)),
                ('priority', models.CharField(choices=[('High', 'Urgent'), ('Medium', 'Need Attention'), ('Low', 'Not Urgent')], max_length=20)),
                ('attach_file', models.FileField(upload_to='attachment')),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
    ]
