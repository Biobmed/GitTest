# Generated by Django 2.2.2 on 2019-07-15 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
    ]
