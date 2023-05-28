# Generated by Django 4.1.7 on 2023-02-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0013_alter_categorie_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(choices=[('Al', 'Alimentaire'), ('Mb', 'Meuble'), ('Sn', 'Sanitaire'), ('Vs', 'Vaisselle'), ('Vt', 'Vêtement'), ('Jx', 'Jouets'), ('Lg', 'Linge de Maison'), ('Bj', 'Bijoux'), ('Dc', 'Décor'), ('Im', 'Immobilier'), ('Me', 'Meuble'), ('Pp', 'ParaPharmacie'), ('El', 'Electroménager'), ('Fr', 'Frais'), ('Ta', 'Tapis')], default='Al', max_length=50),
        ),
    ]
