# Generated by Django 3.2.9 on 2022-02-08 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_article_scopes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='relation', through='articles.Relationship', to='articles.Scope', verbose_name='Тематика статьи'),
        ),
    ]