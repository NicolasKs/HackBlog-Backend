# Generated by Django 3.0.6 on 2020-05-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='topic',
            field=models.CharField(choices=[('politics', 'Politics'), ('sport', 'Sport'), ('opinion', 'Opinion'), ('business', 'Business'), ('science', 'Science'), ('health', 'Health'), ('style', 'Style'), ('food', 'Food'), ('tech', 'Tech'), ('science', 'Science'), ('psychology', 'Psychology'), ('other', 'Other')], default='Opinion', max_length=30),
        ),
    ]
