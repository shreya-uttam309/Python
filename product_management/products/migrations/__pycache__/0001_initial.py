import datetime
from django.db import migrations,models
class Migration(migrations.Migration):
    initial=True
    
    dependencies=[
        
    ]
    operations=[
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id',models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID') ),
                ('image',models.ImageField(upload_to='')),
                ('name',models.CharField(max_length=200)),
                ('price',models.DecimalField(decimal_places=2,max_digits=5)),
                ('description',models.TextField()),
                ('is_published',models.BooleanField(default=True)),
                ('created_at',models.DateTimeField(blank=True,default=datetime.datetime.now)),
            ],
            
        ),
    ]