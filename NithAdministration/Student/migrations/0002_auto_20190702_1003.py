# Generated by Django 2.2.1 on 2019-07-02 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestions',
            name='student',
            field=models.CharField(max_length=15, verbose_name='student'),
        ),
    ]
