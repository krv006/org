# Generated by Django 5.0.6 on 2024-05-31 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_social_media_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='social_media',
            old_name='image',
            new_name='icon',
        ),
    ]
