# Generated by Django 5.1.1 on 2024-09-11 03:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('opportunities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('event_date', models.DateTimeField()),
                ('volunteer_limit', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('opportunity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opportunities.opportunity')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunities.organization')),
                ('registered_volunteers', models.ManyToManyField(blank=True, to='accounts.userprofile')),
            ],
        ),
    ]
