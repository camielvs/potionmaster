# Generated by Django 4.0.3 on 2022-04-06 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_recipe_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='potion',
            name='recipe',
        ),
        migrations.AddField(
            model_name='ingredientquantity',
            name='potion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.potion'),
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]