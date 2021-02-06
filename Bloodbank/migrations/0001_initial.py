# Generated by Django 3.0.2 on 2020-04-17 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bloodpatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=20)),
                ('blood', models.CharField(max_length=100)),
                ('medical', models.CharField(max_length=150)),
                ('number', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'bloodpatient',
            },
        ),
    ]