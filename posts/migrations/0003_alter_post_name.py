# Generated by Django 4.2.dev20221007110535 on 2022-11-07 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_post_likecount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=50, verbose_name='Name'),
        ),
    ]