# Generated by Django 2.1.5 on 2020-09-02 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_articlepost_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='article/%Y%m%d/'),
        ),
    ]
