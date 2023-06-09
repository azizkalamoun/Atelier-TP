# Generated by Django 4.1.7 on 2023-02-28 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0003_rename_type_produit_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Alimentaire', max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='Type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='produit',
            name='catégorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.categorie'),
        ),
    ]
