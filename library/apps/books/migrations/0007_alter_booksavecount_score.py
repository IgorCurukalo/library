# Generated by Django 4.1 on 2022-09-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_booksavecount_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksavecount',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]