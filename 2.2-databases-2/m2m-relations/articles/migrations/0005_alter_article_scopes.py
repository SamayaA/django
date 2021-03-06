# Generated by Django 3.2.9 on 2022-02-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20220208_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='scope', through='articles.Relationship', to='articles.Scope', verbose_name='Тематика статьи'),
        ),
    ]
