# Generated by Django 4.1.2 on 2022-10-29 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimoni', '0004_alter_testimonilist_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonilist',
            name='nama',
            field=models.CharField(default='Anonymous', max_length=50),
        ),
    ]
