# Generated by Django 3.2.5 on 2021-07-25 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0005_merge_0003_auto_20210720_2020_0004_auto_20210723_0926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ['-created_at'], 'verbose_name': 'Dish', 'verbose_name_plural': 'Dishes'},
        ),
        migrations.RemoveField(
            model_name='dishingredient',
            name='dish_id',
        ),
        migrations.AlterField(
            model_name='orderingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oi', to='dishes.ingredient'),
        ),
        migrations.AlterField(
            model_name='orderingredient',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oi', to='dishes.order'),
        ),
    ]