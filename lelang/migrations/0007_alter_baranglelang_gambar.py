# Generated by Django 4.1.2 on 2022-10-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lelang", "0006_alter_baranglelang_gambar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="baranglelang",
            name="gambar",
            field=models.ImageField(blank=True, null=True, upload_to="lelang/upload"),
        ),
    ]
