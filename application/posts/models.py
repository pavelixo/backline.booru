from django.db import models
from users.models import User
from contrib.validators import TextValidator, FileUpload


class TagManager(models.Manager):
    def create(self, **kwargs):
        kwargs["name"] = kwargs["name"].lower()
        return super().create(**kwargs)


class Tag(models.Model):
    name_validator = TextValidator()  # validator
    name = models.CharField(max_length=64, unique=True, validators=[name_validator])

    objects = TagManager()

    class Meta:
        db_table = "tags"
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return f"<{self.name}:{self.pk}>"


class Image(models.Model):
    title_validator = TextValidator()  # validator
    title = models.CharField(max_length=128, validators=[title_validator])

    file_rename = FileUpload()  # validator
    file = models.ImageField(upload_to=file_rename)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="images")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "images"
        verbose_name = "Image"
        verbose_name_plural = "Images"

    @property
    def score(self):
        total_votes = self.ratings.aggregate(total_score=models.Sum("vote_value"))["total_score"]
        return total_votes if total_votes is not None else 0

    def __str__(self):
        return f"<{self.title}:{self.pk}>"


class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comments"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"<{self.author.pk}:{self.image.pk}>"


class Rating(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="ratings")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_value = models.IntegerField(choices=[(1, "up"), (-1, "down")])

    class Meta:
        db_table = "ratings"
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"
        unique_together = (("image", "author"),)

    def __str__(self):
        return f"<{self.author.pk}:(<{self.image.pk}:{self.get_vote_value_display()}>)>"
