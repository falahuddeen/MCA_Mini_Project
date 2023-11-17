from django.db import models
from django.utils import timezone
from django.utils.html import format_html
# Create your models here.

# Category Model

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(max_length=50)
    add_date=timezone.now()

    def image_tag(self):
        return format_html('<img src="{}" style="width:40px;height:40px;border-radius:50%"/>'.format(self.image.url))

    class Meta:
        managed = False
        db_table='category'



# Post Model

class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    url=models.CharField(max_length=100)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(max_length=50)



    class Meta:
        managed=False
        db_table='post'