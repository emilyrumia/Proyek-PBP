# Generated by Django 4.1.2 on 2022-10-27 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0004_pertanyaan_is_answered_alter_faq_pertanyaan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='pertanyaan',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer_service.pertanyaan'),
        ),
    ]
