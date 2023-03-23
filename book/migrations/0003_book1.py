# Generated by Django 3.2.15 on 2022-10-26 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20221019_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('pub_data', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('publish', models.CharField(max_length=32)),
            ],
        ),
    ]