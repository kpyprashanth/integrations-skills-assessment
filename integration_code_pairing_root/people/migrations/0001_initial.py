# Generated by Django 3.1.5 on 2021-02-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('people_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('birth_year', models.CharField(max_length=10)),
                ('eye_color', models.CharField(max_length=16)),
                ('gender', models.CharField(max_length=10)),
                ('hair_color', models.CharField(max_length=16)),
                ('height', models.IntegerField()),
                ('mass', models.IntegerField()),
                ('skin_color', models.CharField(max_length=16)),
                ('homeworld', models.URLField()),
            ],
            options={
                'db_table': 'people',
            },
        ),
    ]
