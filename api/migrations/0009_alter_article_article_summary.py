# Generated by Django 4.2.6 on 2023-12-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_profile_date_of_birth_profile_favorite_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Article_summary',
            field=models.TextField(),
        ),
    ]