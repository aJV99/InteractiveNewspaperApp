# Generated by Django 4.2.6 on 2023-12-14 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_profile_bio_alter_profile_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Article_category',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='favorite_categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_categories',
            field=models.TextField(default='[]'),
        ),
    ]