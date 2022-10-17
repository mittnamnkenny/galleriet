from django.db import models


SUBJECT = (
    (0, 'Customer service'),
    (1, 'Technical assistance')
)


class Contact(models.Model):
    """
    Database model for Contact
    """
    subject = models.IntegerField(choices=SUBJECT, default=0)
    full_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.full_name
