# Generated by Django 5.1 on 2024-08-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_rename_name_genre_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='short_biography',
            field=models.TextField(help_text='Enter a short biography about this author', null=True, max_length=1000),
        ),
    ]
