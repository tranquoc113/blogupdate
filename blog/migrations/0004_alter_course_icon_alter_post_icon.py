# Generated by Django 4.0 on 2021-12-29 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='icon',
            field=models.ImageField(upload_to='image/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='icon',
            field=models.ImageField(upload_to='image/%Y/%m/%d'),
        ),
    ]