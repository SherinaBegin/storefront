from django.db import models
#no id field because django creates it automatically
# sku = models.CharField(max_length=10, primary_key=True) 
# django does not set a primary key, at this makes it the primary key
# Create your models here.
# Promotion Many to Many Product

class Promotion (models.Model):
   description = models.CharField(max_length=255)
   discount = models.FloatField()
   #product_set: returns all the products that the promotion is linked to.

class Collection(models.Model):
   title = models.CharField(max_length=255)
   feautured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')


class Product(models.Model):
   title = models.CharField(max_length=255) #varchar(255)
   #search engine optimization technique
   slug = models.SlugField()
   description = models.TextField()
   unit_price = models.DecimalField(max_digits=6, decimal_places=2) 
   #monetary values should always be decimal field
   inventory = models.IntegerField()
   last_update = models.DateTimeField(auto_now=True) 
   #auto_now_add only stores at time of creation
   collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
   promotions = models.ManyToManyField(Promotion)
   #plural because a product can have many promotions.

class Customer(models.Model):
   #specifying value here so prevents having to change it in multiple places in the future.
   MEMBERSHIP_BRONZE = 'B'
   MEMBERSHIP_SILVER = 'S'
   MEMBERSHIP_GOLD = 'G'

   MEMBERSHIP_CHOICES = [ 
      #Uppercase to indicate that this is a fixed list of values
      (MEMBERSHIP_BRONZE, 'Bronze'),
      (MEMBERSHIP_SILVER, 'Silver'),
      (MEMBERSHIP_GOLD, 'Gold'),
   ]
   first_name = models.CharField(max_length=255)
   last_name = models.CharField(max_length=255)
   email = models.EmailField(unique=True)# unique/ no dupes
   phone = models.CharField(max_length=255)
   birth_date = models.DateField(null=True) #nullable
   membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

class Order(models.Model):
   PAYMENT_STATUS_PENDING = 'P'
   PAYMENT_STATUS_COMPLETE = 'C'
   PAYMENT_STATUS_FAILED = 'F'

   PAYMENT_STATUS_CHOICES = [
      (PAYMENT_STATUS_PENDING, 'Pending'),
      (PAYMENT_STATUS_COMPLETE, 'Complete'),
      (PAYMENT_STATUS_FAILED, 'Failed'),
   ]

   placed_at = models.DateTimeField(auto_now_add=True)
   payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
   customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
   order = models.ForeignKey(Order, on_delete=models.PROTECT)
   product = models.ForeignKey(Product, on_delete=models.PROTECT)
   quantity = models.PositiveIntegerField()
   unit_price = models.DecimalField(max_digits=6, decimal_places=2)
   
class Address(models.Model):
   street = models.CharField(max_length=255)
   city = models.CharField(max_length=255)
   #one to one : models.OneToOneField django primarykey = True automatically created reverse relationship in parent class
   #one to many: models.ForeignKey no need for primary key
   customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 

class Cart(models.Model):
   created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
   cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.PositiveSmallIntegerField()