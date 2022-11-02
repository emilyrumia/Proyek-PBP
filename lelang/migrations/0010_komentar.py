# Generated by Django 4.1.2 on 2022-10-26 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("general_user", "0001_initial"),
        ("lelang", "0009_alter_baranglelang_tanggal_berakhir_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Komentar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("waktu_ditambahkan", models.DateTimeField(auto_now_add=True)),
                ("teks", models.TextField()),
                (
                    "barang_lelang",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lelang.baranglelang",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="general_user.generaluser",
                    ),
                ),
            ],
        ),
    ]
