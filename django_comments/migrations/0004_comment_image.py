# Generated by Django 2.2.2 on 2020-02-06 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0003_add_submit_date_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='comments/%Y/%m/', verbose_name='Image'),
        ),
    ]
