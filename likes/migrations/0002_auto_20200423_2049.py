# Generated by Django 3.0.5 on 2020-04-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='likes',
            constraint=models.UniqueConstraint(fields=('user_id', 'post_id'), name='like_constraint'),
        ),
    ]