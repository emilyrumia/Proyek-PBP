# Generated by Django 4.1.2 on 2022-10-26 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("general_user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GalangDana",
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
                ("tujuan", models.CharField(max_length=20)),
                ("judul", models.CharField(max_length=255)),
                ("deskripsi", models.TextField()),
                ("target", models.CharField(max_length=30)),
                ("gambar", models.ImageField(blank=True, upload_to="images/")),
                ("tanggal_pembuatan", models.DateField(auto_now_add=True)),
                ("tanggal_berakhir", models.DateField(default=None)),
                ("status_keaktifan", models.BooleanField(default=True)),
                (
                    "akun_bank",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="general_user.rekeningbank",
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
                ("komentar", models.TextField()),
                ("tanggal_komentar", models.DateField(auto_now_add=True)),
                (
                    "objek_galang",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resipien.galangdana",
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
