# Generated by Django 3.0.3 on 2020-02-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0002_auto_20200222_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
