# Generated by Django 4.0.5 on 2022-08-04 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0003_offeredcourse_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]