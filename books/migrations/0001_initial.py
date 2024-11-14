# Generated by Django 5.1.3 on 2024-11-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("book_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("genre", models.CharField(max_length=50)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]