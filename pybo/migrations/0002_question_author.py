# Generated by Django 4.0 on 2021-12-16 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]