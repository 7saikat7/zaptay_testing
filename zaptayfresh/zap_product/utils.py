import random
import string
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_Product_ID(instance):

    Product_ID = random_string_generator().upper()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(prod_custom_id=Product_ID).exists()
    if qs_exists:
        return unique_Product_ID(instance)
    return Product_ID


def unique_Prodimg_ID(instance):

    Prodimg_ID = random_string_generator().upper()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(prod_image_id=Prodimg_ID).exists()
    if qs_exists:
        return unique_Prodimg_ID(instance)
    return Prodimg_ID