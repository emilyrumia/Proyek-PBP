# Generated by Django 4.1.2 on 2022-10-29 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimoni', '0003_testimonilist_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonilist',
            name='target',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
