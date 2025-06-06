# Generated by Django 5.1.3 on 2025-03-29 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='stones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='products/')),
                ('description', models.TextField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.CharField(choices=[('ruby', 'Ruby'), ('sapphire', 'Sapphire'), ('aquamarine', 'Aquamarine'), ('diamond', 'Diamond'), ('emerald', 'Emerald'), ('white topaz', 'White Topaz'), ('moon stone', 'Moon Stone'), ('citrine', 'Citrine')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock', models.IntegerField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], max_length=20)),
                ('rating', models.FloatField(default=0.0)),
                ('review_count', models.IntegerField(default=0)),
                ('brand', models.CharField(default='Unknown', max_length=100)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('is_discounted', models.BooleanField(default=False)),
                ('discount_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('packaging', models.CharField(max_length=100)),
                ('warranty', models.CharField(blank=True, max_length=100)),
                ('additional_info', models.TextField(blank=True)),
                ('tags', models.ManyToManyField(blank=True, to='gold.tag')),
            ],
        ),
        migrations.CreateModel(
            name='silver_ring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='products/')),
                ('description', models.TextField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.CharField(choices=[('gold', 'Gold'), ('silver', 'Silver')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock', models.IntegerField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], max_length=20)),
                ('rating', models.FloatField(default=0.0)),
                ('review_count', models.IntegerField(default=0)),
                ('brand', models.CharField(default='Unknown', max_length=100)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('is_discounted', models.BooleanField(default=False)),
                ('discount_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('packaging', models.CharField(max_length=100)),
                ('warranty', models.CharField(blank=True, max_length=100)),
                ('additional_info', models.TextField(blank=True)),
                ('tags', models.ManyToManyField(blank=True, to='gold.tag')),
            ],
        ),
        migrations.CreateModel(
            name='silver_hand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='products/')),
                ('description', models.TextField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.CharField(choices=[('gold', 'Gold'), ('silver', 'Silver')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock', models.IntegerField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], max_length=20)),
                ('rating', models.FloatField(default=0.0)),
                ('review_count', models.IntegerField(default=0)),
                ('brand', models.CharField(default='Unknown', max_length=100)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('is_discounted', models.BooleanField(default=False)),
                ('discount_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('packaging', models.CharField(max_length=100)),
                ('warranty', models.CharField(blank=True, max_length=100)),
                ('additional_info', models.TextField(blank=True)),
                ('tags', models.ManyToManyField(blank=True, to='gold.tag')),
            ],
        ),
        migrations.CreateModel(
            name='silver_goshvareh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='products/')),
                ('description', models.TextField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.CharField(choices=[('gold', 'Gold'), ('silver', 'Silver')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock', models.IntegerField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], max_length=20)),
                ('rating', models.FloatField(default=0.0)),
                ('review_count', models.IntegerField(default=0)),
                ('brand', models.CharField(default='Unknown', max_length=100)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('is_discounted', models.BooleanField(default=False)),
                ('discount_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('packaging', models.CharField(max_length=100)),
                ('warranty', models.CharField(blank=True, max_length=100)),
                ('additional_info', models.TextField(blank=True)),
                ('tags', models.ManyToManyField(blank=True, to='gold.tag')),
            ],
        ),
        migrations.CreateModel(
            name='gold_ring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='products/')),
                ('description', models.TextField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.CharField(choices=[('gold', 'Gold'), ('silver', 'Silver')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock', models.IntegerField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], max_length=20)),
                ('rating', models.FloatField(default=0.0)),
                ('review_count', models.IntegerField(default=0)),
                ('brand', models.CharField(default='Unknown', max_length=100)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('is_discounted', models.BooleanField(default=False)),
                ('discount_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('packaging', models.CharField(max_length=100)),
                ('warranty', models.CharField(blank=True, max_length=100)),
                ('additional_info', models.TextField(blank=True)),
                ('tags', models.ManyToManyField(blank=True, to='gold.tag')),
            ],
        ),
        migrations.CreateModel(
            name='gold_hand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='products/')),
                ('description', models.TextField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.CharField(choices=[('gold', 'Gold'), ('silver', 'Silver')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock', models.IntegerField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], max_length=20)),
                ('rating', models.FloatField(default=0.0)),
                ('review_count', models.IntegerField(default=0)),
                ('brand', models.CharField(default='Unknown', max_length=100)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('is_discounted', models.BooleanField(default=False)),
                ('discount_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('packaging', models.CharField(max_length=100)),
                ('warranty', models.CharField(blank=True, max_length=100)),
                ('additional_info', models.TextField(blank=True)),
                ('tags', models.ManyToManyField(blank=True, to='gold.tag')),
            ],
        ),
        migrations.CreateModel(
            name='gold_goshvareh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='products/')),
                ('description', models.TextField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.CharField(choices=[('gold', 'Gold'), ('silver', 'Silver')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock', models.IntegerField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], max_length=20)),
                ('rating', models.FloatField(default=0.0)),
                ('review_count', models.IntegerField(default=0)),
                ('brand', models.CharField(default='Unknown', max_length=100)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('is_discounted', models.BooleanField(default=False)),
                ('discount_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('packaging', models.CharField(max_length=100)),
                ('warranty', models.CharField(blank=True, max_length=100)),
                ('additional_info', models.TextField(blank=True)),
                ('tags', models.ManyToManyField(blank=True, to='gold.tag')),
            ],
        ),
    ]
