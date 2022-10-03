from django.db import models


MEDIUM = (
    (0, 'Oil'),
    (1, 'Acrylic'),
    (2, 'Watercolour'),
    (3, 'Pencil')
)


class Artist(models.Model):
    """
    Database model for Artist
    """
    full_name = models.CharField(max_length=254, unique=True)
    nationality = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=254, null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    """
    Database model for Category
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Database model for Product
    """
    artist = models.ForeignKey('Artist', null=True, blank=True,
                               on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    medium = models.IntegerField(choices=MEDIUM, default=0)
    height = models.IntegerField()
    width = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
