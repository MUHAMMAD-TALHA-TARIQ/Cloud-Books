# Generated by Django 4.0.2 on 2022-02-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books_Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('self_id', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('section_name', models.CharField(blank=True, default='', max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Book Sections',
            },
        ),
    ]
