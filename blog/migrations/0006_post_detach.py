# Generated by Django 3.0 on 2020-11-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='detach',
            field=models.BooleanField(default=False),
        ),
    ]
