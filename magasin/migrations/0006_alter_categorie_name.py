# Generated by Django 4.1.7 on 2023-02-28 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0005_alter_categorie_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(default='Al', max_length=50),
        ),
    ]
