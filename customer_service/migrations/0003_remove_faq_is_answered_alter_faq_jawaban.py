# Generated by Django 4.1.2 on 2022-10-26 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0002_remove_pertanyaan_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='is_answered',
        ),
        migrations.AlterField(
            model_name='faq',
            name='jawaban',
            field=models.CharField(max_length=500),
        ),
    ]
