# Generated by Django 5.0.6 on 2024-07-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newsletter', '0002_alter_post_content_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='many',
        ),
        migrations.RemoveField(
            model_name='newsletteremail',
            name='state',
        ),
        migrations.AlterField(
            model_name='newsletteremail',
            name='email',
            field=models.EmailField(max_length=45, unique=True),
        ),
        migrations.DeleteModel(
            name='PostNewsLetterEmail',
        ),
    ]
