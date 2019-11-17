# Generated by Django 2.2.7 on 2019-11-17 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_website', '0005_delete_sponsor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['site', '-pk']},
        ),
        migrations.AlterModelOptions(
            name='carouselitem',
            options={'ordering': ['site', '-pk']},
        ),
        migrations.AlterModelOptions(
            name='contestlanguage',
            options={'ordering': ['site', 'name', '-pk']},
        ),
        migrations.AlterModelOptions(
            name='contestrule',
            options={'ordering': ['site', '-pk']},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['site', '-pk']},
        ),
        migrations.AlterModelOptions(
            name='faqitem',
            options={'ordering': ['site', '-pk']},
        ),
        migrations.AlterModelOptions(
            name='flatpage',
            options={'ordering': ['site', 'name', '-pk']},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['-pk']},
        ),
    ]
