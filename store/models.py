from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=700, blank=True)
    top_product = models.ForeignKey(to='Product', on_delete=models.SET_NULL, null=True)


class Discount(models.Model):
    discount = models.FloatField()
    description = models.CharField(max_length=250)


class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6 ,decimal_places=2)
    inventory = models.PositiveIntegerField()
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name='products')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    discounts = models.ManyToManyField(to=Discount, blank=True)


class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)


class Address(models.Model):
    customer = models.OneToOneField(to=Customer, on_delete=models.CASCADE, primary_key=True)
    province = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=250)


class Order(models.Model):
    ORDER_STATUS_PAID = 'p'
    ORDER_STATUS_UNPAID = 'u'
    ORDER_STATUS_CANCELED = 'c'

    ORDER_STATUS = [
        (ORDER_STATUS_PAID, 'Paid'),
        (ORDER_STATUS_UNPAID, 'Unpaid'),
        (ORDER_STATUS_CANCELED, 'Canceled'),
        ]
    
    customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT, related_name='orders')
    status = models.CharField(max_length=1, choices=2)
    datetime_created = models.DateTimeField(auto_now_add=True, choices=ORDER_STATUS, default=ORDER_STATUS_UNPAID)


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT, related_name='order_items')
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = [['order', 'product']]


class Cart(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [['cart', 'product']]
 

class Comment(models.Model):
    COMMENT_STATUS_WAITING = 'w'
    COMMENT_STATUS_APPROVED = 'a'
    COMMENT_STATUS_NOT_APPROVED = 'na'

    COMMENT_STATUS = [
        (COMMENT_STATUS_WAITING, 'Waiting'),
        (COMMENT_STATUS_APPROVED, 'Approved'),
        (COMMENT_STATUS_NOT_APPROVED, 'Not Approved'),
    ]

    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=250)
    body = models.TextField()
    status = models.CharField(max_length=2, choices=COMMENT_STATUS, default=COMMENT_STATUS_WAITING)

    datetime_created = models.DateTimeField(auto_now_add=True)
