# Generated by Django 5.1.1 on 2024-10-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_alter_produtos_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
