# Generated by Django 4.2.6 on 2023-10-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cssapp', '0002_remove_acta_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='acta',
            name='firmacontrata',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='acta',
            name='firmacss',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
