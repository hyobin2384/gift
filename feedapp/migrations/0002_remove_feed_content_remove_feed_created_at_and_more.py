# Generated by Django 4.0.3 on 2022-04-06 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
        ('feedapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='content',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='title',
        ),
        migrations.AddField(
            model_name='feed',
            name='main',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feed', to='mainapp.main'),
        ),
    ]
