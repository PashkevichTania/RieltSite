# Generated by Django 3.1.4 on 2020-12-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_dealsbackup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dealsbackup',
            options={'verbose_name': 'Резервная копия сделки', 'verbose_name_plural': 'Резервные копии сделок'},
        ),
        migrations.AddField(
            model_name='dealsbackup',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
