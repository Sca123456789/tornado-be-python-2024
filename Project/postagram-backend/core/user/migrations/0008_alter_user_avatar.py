# Generated by Django 5.0 on 2024-03-22 06:55

import core.user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core_user", "0007_rename_comment_liked_user_comments_liked_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to=core.user.models.user_directory_path
            ),
        ),
    ]
