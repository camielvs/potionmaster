# Generated by Django 4.0.2 on 2022-04-05 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_potion_ingredients_alter_ingredient_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potion',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.recipe'),
        ),
    ]
