# Generated by Django 4.1.2 on 2022-10-31 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimoni', '0005_alter_testimonilist_nama'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonilist',
            name='user',
        ),
    ]