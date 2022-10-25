# Generated by Django 4.1.2 on 2022-10-23 14:15

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
                ("judul", models.CharField(max_length=255)),
                ("deskripsi", models.TextField(blank=True, null=True)),
                ("gambar", models.ImageField(upload_to="")),
                ("target_galang_dana", models.PositiveIntegerField()),
                ("tanggal_berakhir", models.DateField()),
                ("status_keaktifan", models.BooleanField(default=True)),
                (
                    "tujuan_keperluan",
                    models.CharField(
                        choices=[
                            ("PRIBADI", "Pribadi"),
                            ("KERABAT", "Kerabat/Keluarga"),
                            ("LEMBAGA", "Institusi/Lembaga"),
                            ("OTHER", "Lainnya"),
                        ],
                        default="PRIBADI",
                        max_length=100,
                    ),
                ),
                (
                    "penggalang",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="general_user.generaluser",
                    ),
                ),
                (
                    "rekening_bank",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="general_user.rekeningbank",
                    ),
                ),
            ],
        ),
    ]
