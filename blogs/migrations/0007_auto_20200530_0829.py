# Generated by Django 3.0.6 on 2020-05-30 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20200529_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.AddField(
            model_name='blog',
            name='author_name',
            field=models.CharField(default='Unknown', max_length=50),
        ),
    ]