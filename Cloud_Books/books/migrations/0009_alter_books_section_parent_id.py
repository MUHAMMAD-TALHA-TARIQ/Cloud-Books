# Generated by Django 4.0.2 on 2022-02-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_books_section_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books_section',
            name='parent_id',
            field=models.CharField(blank=True, default='-', max_length=1000, null=True),
        ),
    ]
