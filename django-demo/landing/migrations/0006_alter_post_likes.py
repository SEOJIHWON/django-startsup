# Generated by Django 4.0.4 on 2022-04-26 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_remove_post_likes_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='user_likses', to='landing.tempuser'),
        ),
    ]
