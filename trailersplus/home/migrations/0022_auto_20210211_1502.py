# Generated by Django 3.0.11 on 2021-02-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20201016_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='close_menu_button_text',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='header',
            name='close_menu_button_text_en',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='header',
            name='close_menu_button_text_es',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]