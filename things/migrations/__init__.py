from django.db import migrations, models
from django.core.validators import MaxValueValidator, MinValueValidator


class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=30, unique=True, blank=False)),
                ('description', models.CharField(unique=False, blank=True, max_length=120)),
                ('quantity',
                 models.IntegerField(unique=False, validators=[MinValueValidator(0), MaxValueValidator(100)])),
            ],
        ),
    ]
