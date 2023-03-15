# Generated by Django 4.1.7 on 2023-02-20 08:21

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('category', models.CharField(choices=[('Tanks', 'Tanks'), ('Healers', 'Healers'), ('Damage Dealers', 'Damage Dealers'), ('Traders', 'Traders'), ('Guild Masters', 'Guild Masters'), ('Quest Givers', 'Quest Givers'), ('Blacksmith', 'Blacksmith'), ('Tanner', 'Tanner'), ('Potion Master', 'Potion Master'), ('Spell Master', 'Spell Master')], default='Tanks', max_length=20)),
                ('time_add', models.DateTimeField(auto_now_add=True)),
                ('short_resp', models.CharField(max_length=255)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_resp', models.DateTimeField(auto_now_add=True)),
                ('text_resp', models.TextField(verbose_name='Message in response')),
                ('status_delete', models.BooleanField(default=False, verbose_name='Response removed')),
                ('status_accept', models.BooleanField(default=False, verbose_name='Response accepted')),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.advert', verbose_name='Advert')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Response author')),
            ],
        ),
    ]
