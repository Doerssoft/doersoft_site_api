# Generated by Django 3.1.5 on 2021-01-31 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doerscareer', '0003_career_careerform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careercategory',
            name='skill_type',
            field=models.CharField(choices=[('Web Developer', 'Web Developer'), ('Wordpress Developer', 'Wordpress Developer'), ('Designer', 'Designer'), ('Content Writing', 'Content Writing')], max_length=50),
        ),
    ]
