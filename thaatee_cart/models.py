from django.db import models
from thaatee_lms.models import Courses
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Promocode(models.Model):
    promocode_type_choice = (
        ('value', 'VALUE OFF'),
        ('percentage', 'PERCENTAGE OFF')
    )

    promocode_payment_choice = (
        ('online_wallet', 'ONLINE WALLET'),
        ('card', 'CARD')

    )

    promocode_name = models.CharField(max_length=100, blank=True)
    promocode_quantity = models.IntegerField(default=0)
    promocode_type = models.CharField(
        max_length=20, blank=True, null=True, choices=promocode_type_choice, default="value")
    promocode_payment = models.CharField(
        max_length=20, blank=True, null=True, choices=promocode_payment_choice, default="online")
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'promocode'

    def __str__(self):
        return str(self.promocode_name)


class Cart(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT)
    courses = models.ForeignKey(Courses,
                                on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return str(self.product_variant)


class Order(models.Model):
    payment_choice = (
        ('online_wallet', 'ONLINE WALLET'),
        ('card', 'CARD')


    )
    order_status_choice = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),


    )
    order_id = models.CharField(
        max_length=100, default='', blank=True, null=True)
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT, limit_choices_to={'roles': 3})
    amount = models.IntegerField()
    payment = models.TextField(

        default='', blank=True, null=True)
    promocode = models.ForeignKey(
        Promocode, on_delete=models.PROTECT, limit_choices_to={'status': True}, blank=True, null=True)
    promocode_details = models.TextField(default='', blank=True, null=True)
    order_details = models.TextField(default='', blank=True, null=True)
    order_status = models.TextField(
        choices=order_status_choice, default="Pending")
    payment_status = models.TextField(default='', blank=True, null=True)
    payment_choice = models.CharField(
        max_length=20, blank=True, null=True, choices=payment_choice)
    paytment_details = models.TextField(
        default='', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        db_table = 'order'

    def save(self, *args, **kwargs):
        if not self.id:
            order_id = self.order_id
            order_id_exists = True
            counter = 1
            # self.order_id = order_id
            while order_id_exists:
                try:
                    order_id_exits = Order.objects.get(order_id=order_id)
                    if order_id_exits:
                        order_id = self.order_id + '_' + str(counter)
                        counter += 1
                except Order.DoesNotExist:
                    self.order_id = order_id
                    break
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.order_id)
