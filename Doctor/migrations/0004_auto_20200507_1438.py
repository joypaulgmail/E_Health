# Generated by Django 3.0.2 on 2020-05-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0003_auto_20200420_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctorappoient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='0', max_length=100)),
                ('registration', models.CharField(default='0', max_length=100)),
                ('pattient', models.CharField(default='0', max_length=100)),
            ],
            options={
                'db_table': 'doctorappoient',
            },
        ),
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
