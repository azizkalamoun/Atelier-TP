# Generated by Django 4.1.7 on 2023-03-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0015_commande'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(choices=[('Alimentaire', 'Al'), ('Meuble', 'Mb'), ('Sanitaire', 'Sn'), ('Vaisselle', 'Vs'), ('Vêtement', 'Vt'), ('Jouets', 'Jx'), ('Linge de Maison', 'Lg'), ('Bijoux', 'Bj'), ('Décor', 'Dc'), ('Immobilier', 'Im'), ('Meuble', 'Me'), ('ParaPharmacie', 'Pp'), ('Electroménager', 'El'), ('Frais', 'Fr'), ('Tapis', 'Ta')], default='Alimentaire', max_length=50),
        ),
    ]
