# Generated by Django 3.0.8 on 2020-09-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_no', models.IntegerField()),
                ('e_name', models.CharField(max_length=64)),
                ('e_sal', models.FloatField()),
                ('e_addr', models.CharField(max_length=64)),
            ],
        ),
    ]
