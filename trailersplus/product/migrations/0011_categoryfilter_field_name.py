# Generated by Django 3.0.9 on 2020-08-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20200826_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryfilter',
            name='field_name',
            field=models.CharField(choices=[('', '')], default='category__web_category', max_length=150),
        ),
    ]