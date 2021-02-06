# Generated by Django 3.0.2 on 2020-04-16 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hosinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=100)),
                ('hregistration', models.CharField(max_length=100)),
                ('htreatment', models.CharField(max_length=100)),
                ('hbed', models.IntegerField()),
                ('hpassword', models.CharField(max_length=100)),
                ('hstate', models.CharField(max_length=100)),
                ('hcity', models.CharField(max_length=100)),
                ('hcontact', models.CharField(max_length=12)),
                ('haddress', models.CharField(max_length=300)),
                ('hapos', models.IntegerField(default=0)),
                ('hbpos', models.IntegerField(default=0)),
                ('hopos', models.IntegerField(default=0)),
                ('habpos', models.IntegerField(default=0)),
                ('haneg', models.IntegerField(default=0)),
                ('hbneg', models.IntegerField(default=0)),
                ('honeg', models.IntegerField(default=0)),
                ('habneg', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'hosinfo',
            },
        ),
    ]
