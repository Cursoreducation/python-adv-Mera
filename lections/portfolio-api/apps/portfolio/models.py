from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


def image_upload_to(instance, filename):
    return "user_{0}/{1}/{2}".format(
        instance.created_by.username, instance.created_at, filename
    )


class BaseModel(models.Model):
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="+"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Portfolio(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Image(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to=image_upload_to)
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="images"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return "%s: %s" % (self.name, self.description)


class Comment(BaseModel):
    text = models.TextField(max_length=5000)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.text
