# Generated by Django 4.2.6 on 2023-12-13 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_category_profile_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favorite_categories',
            field=models.ManyToManyField(blank=True, to='api.category'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]