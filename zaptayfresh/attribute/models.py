from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime
from admin_login.models import zaptayadmin
import uuid
# Create your models here.
class MainCategory(models.Model):

    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    main_category_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "main_category"

    def save(self, *args, **kwargs):
        if not self.pk:
            get_main_category = self.main_category_name.lower()
            get_main_category = get_main_category.replace(" ", "-")
            self.main_category_seo_url = get_main_category
        super(MainCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.main_category_name

class SubCategory(models.Model):

    sub_category_id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sub_category_name = models.CharField(max_length=255)
    sub_category_seo_url = models.CharField(max_length=255, default="")
    sub_category_image = models.ImageField(upload_to="sub_category/images", default="")
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    category_id = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "sub_category"

    def save(self, *args, **kwargs):
        if not self.pk:
            get_sub_category = self.sub_category_name.lower()
            get_sub_category = get_sub_category.replace(" ", "-")
            self.sub_category_seo_url = get_sub_category
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.sub_category_name

class TertiaryCategory(models.Model):

    ter_category_id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ter_category_name = models.CharField(max_length=255)
    ter_category_seo_url = models.CharField(max_length=255, default="")
    tertiary_category_image = models.ImageField(upload_to="tertiary_category/images", default="")
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "tertiary_category"

    def save(self, *args, **kwargs):
        if not self.pk:
            get_ter_category = self.ter_category_name.lower()
            get_ter_category = get_ter_category.replace(" ", "-")
            self.ter_category_seo_url = get_ter_category
        super(TertiaryCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.ter_category_name

class UnderTertiaryCategory(models.Model):

    under_ter_category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    under_ter_category_name = models.CharField(max_length=255)
    under_ter_category_seo_url = models.CharField(max_length=255, default="")
    under_tertiary_category_image = models.ImageField(upload_to="under_tertiary_category/images", default="")
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    ter_category_id = models.ForeignKey(TertiaryCategory, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "under_tertiary_category"

    def save(self, *args, **kwargs):
        if not self.pk:
            get_under_ter_category = self.under_ter_category_name.lower()
            get_under_ter_category = get_under_ter_category.replace(" ", "-")
            self.under_ter_category_seo_url = get_under_ter_category
        super(UnderTertiaryCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.under_ter_category_name

class Brand(models.Model):

    brand_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    brand_name = models.CharField(max_length=100)
    BrandImage = models.ImageField(upload_to="BrandImage", default="")
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "brands"



    def __str__(self):
        return self.brand_name


class Colour(models.Model):

    color_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    color_name = models.CharField(max_length=100)
    ColorImage = models.ImageField(upload_to="colorImage", default="")
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "colours"

    def __str__(self):
        return self.color_name

class Size(models.Model):

    size_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    size_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "size"

    def __str__(self):
        return self.size_name

class MadeIn(models.Model):

    source_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "MadeIn"

    def __str__(self):
        return self.source_name

class SameDayDelivary(models.Model):

    same_day_pin_id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pincode = models.IntegerField()
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "same_day_delivary_pincode"

    def __str__(self):
        return str(self.pincode)

class NextDayDelivary(models.Model):

    next_day_pin_id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pincode = models.IntegerField()
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "next_day_delivary_pincode"

    def __str__(self):
        return str(self.pincode)