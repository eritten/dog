# Generated by Django 3.2 on 2023-02-22 04:50

from django.db import migrations
import markdownfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='text_rendered',
            field=markdownfield.models.RenderedMarkdownField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dog',
            name='description',
            field=markdownfield.models.MarkdownField(rendered_field='text_rendered'),
        ),
    ]
