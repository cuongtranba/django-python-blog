from django.db import models

# Create your models here.


class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True


class User(BaseModel):
    name = models.CharField(max_length=20)

    picture_url = models.CharField(max_length=200)


class Tag(BaseModel):
    tag_name = models.CharField(max_length=20)


class Category(BaseModel):
    category_name = models.CharField(max_length=200)


class Post(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

    pub_date = models.DateTimeField()
    user = models.ForeignKey(User,null=True)

    tag = models.ForeignKey(Tag,null=True)

    category = models.ForeignKey(Category,null=True)
