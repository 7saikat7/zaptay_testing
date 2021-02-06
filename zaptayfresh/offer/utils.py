import random
import string
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))




def unique_Offer_ID(instance ):
    
    Offer_ID = random_string_generator().upper()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(offer_custom_id=Offer_ID).exists()
    if qs_exists:
        return unique_Offer_ID(instance )
    return Offer_ID



def unique_Offer_Prod_ID(instance ):
    
    Offer_Prod_ID = random_string_generator().upper()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(offer_product_id=Offer_Prod_ID).exists()
    if qs_exists:
        return unique_Offer_Prod_ID(instance )
    return Offer_Prod_ID