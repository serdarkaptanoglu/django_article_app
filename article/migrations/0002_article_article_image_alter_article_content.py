# Generated by Django 5.0.4 on 2024-04-15 23:19

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Fotoğraf Ekle'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
    ]
