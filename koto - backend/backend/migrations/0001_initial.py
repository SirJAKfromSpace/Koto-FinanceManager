# Generated by Django 2.0.7 on 2018-07-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='googleCredentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('dob', models.DateTimeField(verbose_name='birth date')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='kotoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthlyExpencess', models.IntegerField(default=0)),
                ('profession', models.CharField(max_length=250)),
            ],
        ),
    ]
