# Generated by Django 3.0.6 on 2020-06-02 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20200602_1646'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-date', 'title']},
        ),
    ]
