# Generated by Django 4.1.2 on 2022-10-06 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
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
                ("name", models.CharField(max_length=100)),
                ("is_actived", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
                ("is_actived", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100)),
                (
                    "state",
                    models.CharField(
                        choices=[("Open Box", "Open Box"), ("New", "New")], max_length=8
                    ),
                ),
                ("description", models.TextField()),
                ("value", models.DecimalField(decimal_places=2, max_digits=7)),
                ("qty_parcel", models.IntegerField(blank=True, null=True)),
                (
                    "value_parcel",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True
                    ),
                ),
                (
                    "cover",
                    models.ImageField(
                        blank=True, null=True, upload_to="app/covers/%Y/%m/"
                    ),
                ),
                ("is_published", models.BooleanField(default=False)),
                ("slug", models.SlugField(unique=True)),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.brand"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.category"
                    ),
                ),
            ],
        ),
    ]
