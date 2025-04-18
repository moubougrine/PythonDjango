# Generated by Django 5.1.6 on 2025-03-22 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_try"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="loging",
            name="password",
        ),
        migrations.RemoveField(
            model_name="loging",
            name="username",
        ),
        migrations.AddField(
            model_name="loging",
            name="email",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="loging",
            name="name",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="loging",
            name="subject",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="loging",
            name="text",
            field=models.TextField(null=True),
        ),
    ]
