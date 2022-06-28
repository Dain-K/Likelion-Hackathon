# Generated by Django 3.2 on 2021-08-04 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0011_auto_20210804_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='list/', verbose_name='사진')),
                ('post_time', models.DateField(auto_now_add=True)),
                ('body', models.CharField(max_length=500)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
