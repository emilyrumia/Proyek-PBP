# Generated by Django 4.1.2 on 2022-10-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimoni', '0002_alter_testimonilist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonilist',
            name='target',
            field=models.CharField(default='', max_length=50),
        ),
    ]