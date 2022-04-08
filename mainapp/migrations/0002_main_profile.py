# Generated by Django 4.0.3 on 2022-04-07 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main', to='profileapp.profile'),
        ),
    ]