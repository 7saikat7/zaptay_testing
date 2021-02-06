from django.db import models
import uuid
# Create your models here.
class Product_Authentication_Policy_db(models.Model):
    idProduct_Authentication_Policy_db = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Product_Authentication_Policy_data = models.TextField(blank=False, default="")

    class Meta:
        db_table = 'Product_Authentication_Policy_db'

    def __str__(self):
        return self.id


class CashOnDeliveryPolicy_db(models.Model):
    idCashOnDeliveryPolicy_db = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CashOnDeliveryPolicy_data = models.TextField(blank=False, default="")

    class Meta:
        db_table = 'CashOnDeliveryPolicy_db'

    def __str__(self):
        return str(self.CashOnDeliveryPolicy_data)




class OnlinePaymentPolicy_db(models.Model):
    idOnlinePaymentPolicy_db = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    OnlinePaymentPolicy_data = models.TextField(blank=False, default="")

    class Meta:
        db_table = 'OnlinePaymentPolicy_db'

    def __str__(self):
        return self.OnlinePaymentPolicy_data


class FreeShippingPolicy_db(models.Model):
    idFreeShippingPolicy_db = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    FreeShippingPolicy_data = models.TextField(blank=False, default="")

    class Meta:
        db_table = 'FreeShippingPolicy_db'

    def __str__(self):
        return self.FreeShippingPolicy_data


class Return_Policy_db(models.Model):
    idReturn_Policy_db = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Return_Policy_data = models.TextField(blank=False, default="")

    class Meta:
        db_table = 'Return_Policy_db'

    def __str__(self):
        return self.Return_Policy_data


class MembershipPolicy_db(models.Model):
    idMembershipPolicy_db = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    MembershipPolicy_data = models.TextField(blank=False, default="")

    class Meta:
        db_table = 'MembershipPolicy_db'

    def __str__(self):
        return self.MembershipPolicy_data


class BestSeller_db(models.Model):
    idBestSeller_db = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    BestSeller_data = models.TextField(blank=False, default="")

    class Meta:
        db_table = 'BestSeller_db'

    def __str__(self):
        return self.BestSeller_data


class SuperDeal_db(models.Model):
    idSuperDeal_db = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SuperDeal_data = models.TextField(blank=False, default="")

    class Meta:
        db_table = 'SuperDeal_db'

    def __str__(self):
        return self.SuperDeal_data


class MembershipZone_db(models.Model):
    idMembershipZone_db = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    MembershipZone_data = models.TextField(blank=False, default="")

    class Meta:
        db_table = 'MembershipZone_db'

    def __str__(self):
        return self.MembershipZone_data


class EventCoupon_db(models.Model):
    idEventCoupon_db = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    EventCoupon_data = models.TextField(blank=False, default="")

    class Meta:
        db_table = 'EventCoupon_db'

    def __str__(self):
        return self.EventCoupon_data


class SendGift_db(models.Model):
    idSendGift_db = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SendGift_data = models.TextField(blank=False, default="")

    class Meta:
        db_table = 'SendGift_db'

    def __str__(self):
        return self.SendGift_data


class TermsPolicy_db(models.Model):
    idTermsPolicy_db = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TermsPolicy_data = models.TextField(blank=False, default="")

    class Meta:
        db_table = 'TermsPolicy_db'

    def __str__(self):
        return self.TermsPolicy_data


class Privacy_db(models.Model):
    idPrivacy_db = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Privacy_data = models.TextField(blank=False, default="")

    class Meta:
        db_table = 'Privacy_db'

    def __str__(self):
        return self.Privacy_data


class ContactUs_db(models.Model):
    idContactUs_db = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ContactUs_data = models.TextField(blank=False, default="")

    class Meta:
        db_table = 'ContactUs_db'

    def __str__(self):
        return self.ContactUs_data