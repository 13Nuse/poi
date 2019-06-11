from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Sum

# User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first = models.CharField(max_length=110, blank=True)
    last = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    employee_number = models.CharField(max_length=50, default='')
    phone = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
        return user_profile


post_save.connect(create_profile, sender=User)


# Inventory


class InventoryCountProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Inventory Count'

    name = models.CharField(max_length=100, blank=False)
    # proteins
    steak = models.FloatField(default=0)
    sirloin = models.FloatField(default=0)
    beef_patty = models.FloatField(default=0)
    chicken_wing = models.FloatField(default=0)
    chicken_breast = models.FloatField(default=0)
    hotdog = models.FloatField(default=0)
    bacon = models.FloatField(default=0)
    # spices
    salt = models.FloatField(default=0)
    pepper_black = models.FloatField(default=0)
    pepper_red_flakes = models.FloatField(default=0)
    sugar = models.FloatField(default=0)
    sugar_brown = models.FloatField(default=0)
    garlic_granulated = models.FloatField(default=0)
    garlic_powder = models.FloatField(default=0)
    onion_powder = models.FloatField(default=0)
    parsley_dry = models.FloatField(default=0)
    cinnamon_ground = models.FloatField(default=0)
    bay_leaves = models.FloatField(default=0)
    italian_seasoning = models.FloatField(default=0)
    # condiments
    sriracha = models.FloatField(default=0)
    ketchup_20oz = models.FloatField(default=0)
    ketchup_10c = models.FloatField(default=0)
    mustard = models.FloatField(default=0)
    oil_truffle = models.FloatField(default=0)
    oil_90_10 = models.FloatField(default=0)
    oil_shortening = models.FloatField(default=0)
    honey = models.FloatField(default=0)
    tahini = models.FloatField(default=0)
    lemon_juice = models.FloatField(default=0)
    mango_nectar = models.FloatField(default=0)
    lemonade_mix = models.FloatField(default=0)
    chili_sauce = models.FloatField(default=0)
    a1_sauce = models.FloatField(default=0)
    vinegar_malt = models.FloatField(default=0)
    cocao_hershey = models.FloatField(default=0)
    cherries_marashino = models.FloatField(default=0)
    banana_pepper_hot = models.FloatField(default=0)
    bbq_sw_sp = models.FloatField(default=0)
    gojujang_sc = models.FloatField(default=0)
    pineapple_juice = models.FloatField(default=0)
    beans_garbanzo = models.FloatField(default=0)
    beans_red_kidney = models.FloatField(default=0)
    tomato_can_peeled = models.FloatField(default=0)
    tomato_can_whole = models.FloatField(default=0)
    sauce_cheddar = models.FloatField(default=0)
    broth_beef = models.FloatField(default=0)
    broth_chicken = models.FloatField(default=0)
    jalapeno_slice = models.FloatField(default=0)
    pepperoncini = models.FloatField(default=0)
    mayonnaise = models.FloatField(default=0)
    russian_dressing = models.FloatField(default=0)
    marinara_salsa = models.FloatField(default=0)
    chipotle_in_adobo = models.FloatField(default=0)
    giardiniara = models.FloatField(default=0)
    potato_chips = models.FloatField(default=0)
    molasses_fancy = models.FloatField(default=0)
    hot_sauce_franks = models.FloatField(default=0)
    el_yucateco = models.FloatField(default=0)
    vinegar_apple_cider = models.FloatField(default=0)
    # walk-in
    whip_cream = models.FloatField(default=0)
    creamer = models.FloatField(default=0)
    pita_bread = models.FloatField(default=0)
    olives = models.FloatField(default=0)
    eggs = models.FloatField(default=0)
    # buns
    sub_panini_roll = models.FloatField(default=0)
    hamberger_bun = models.FloatField(default=0)
    brioche_bun_4 = models.FloatField(default=0)
    brioche_bun_2 = models.FloatField(default=0)
    # fresh
    oranges = models.FloatField(default=0)
    limes = models.FloatField(default=0)
    potato = models.FloatField(default=0)
    brussels_sprouts = models.FloatField(default=0)
    tomato = models.FloatField(default=0)
    romaine_lettuce = models.FloatField(default=0)
    red_onion = models.FloatField(default=0)
    white_onion = models.FloatField(default=0)
    pickles = models.FloatField(default=0)
    avocado = models.FloatField(default=0)
    cucumber = models.FloatField(default=0)
    red_pepper = models.FloatField(default=0)
    yellow_pepper = models.FloatField(default=0)
    garlic = models.FloatField(default=0)
    leeks = models.FloatField(default=0)
    scallions = models.FloatField(default=0)
    basil = models.FloatField(default=0)
    jalapeno_fresh = models.FloatField(default=0)
    cilantro = models.FloatField(default=0)
    # cheese
    cheese_romano = models.FloatField(default=0)
    cheese_swiss = models.FloatField(default=0)
    cheese_provalone = models.FloatField(default=0)
    cheese_cheddar = models.FloatField(default=0)
    cheese_pepperjack = models.FloatField(default=0)
    cheese_parmesan = models.FloatField(default=0)
    # dairy
    butter = models.FloatField(default=0)
    buttermilk = models.FloatField(default=0)
    heavy_cream = models.FloatField(default=0)
    sour_cream = models.FloatField(default=0)
    # freezer
    fries = models.FloatField(default=0)
    fries_sweet_potato = models.FloatField(default=0)
    broccoli_bites = models.FloatField(default=0)
    jalapeno_poppers = models.FloatField(default=0)
    mozzerella_sticks = models.FloatField(default=0)
    hash_brown_patty = models.FloatField(default=0)

    def __str__(self):
        return self.name


class InventorySequence(models.Model):
    """
    adjusting items be reoredering the sequence of items ID/PK
    """
    pass


class InventoryProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Inventory'

    RAW = 'raw'
    FRESH = 'fresh'
    DAIRY = 'dairy'
    PREP = 'prep'
    SPICE = 'spice'
    SAUCE = 'sauce'
    APPS = 'apps'
    ENTREE = 'entree'

    category_choice = (
        ('RAW', 'raw'),
        ('FRESH', 'fresh'),
        ('DAIRY', 'dairy'),
        ('PREP', 'prep'),
        ('SPICE', 'spice'),
        ('APPS', 'apps'),
        ('ENTREE', 'entree')
    )

    GAL = 'gal'
    QT = 'quart'
    PT = 'pint'
    FLOZ = 'fl-oz'
    WTOZ = 'wt-oz'
    EA = 'each'
    unit_choice = (
        ('FLOZ', 'fl-oz'),
        ('WTOZ', 'wt-oz'),
        ('EA', 'each'),
        ('GAL', 'gal'),
        ('PT', 'pint'),
        ('QT', 'quart')
    )

    company = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    sku = models.IntegerField(default=0)
    category = models.CharField(max_length=15, choices=category_choice, default=PREP)
    case = models.FloatField(default=0)
    serving_yield = models.FloatField(default=0)
    serving_size = models.FloatField(default=0)
    unit = models.CharField(max_length=10, choices=unit_choice, default=FLOZ)
    quantity = models.FloatField(default=0)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class InventoryTotals(models.Model):
    pass


# Employee

class EmployeeProfile(models.Model):
    first = models.CharField(max_length=110, blank=True)
    last = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    employee_number = models.CharField(max_length=50, default='')
    pay = models.IntegerField(default=11, blank=False)
    phone = models.IntegerField(default=0, blank=True)
    active = models.CharField(max_length=15, choices=[('active', 'Active'), ('not active', 'Not Active')])

    def __str__(self):
        return self.first


# Sales

class ForcastedSalesProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Forcasted Sales'

    date_start = models.DateField()
    date_end = models.DateField()
    monday = models.FloatField(default=0)
    tuesday = models.FloatField(default=0)
    wednesday = models.FloatField(default=0)
    thursday = models.FloatField(default=0)
    friday = models.FloatField(default=0)
    saturday = models.FloatField(default=0)
    sunday = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def get_total(self, total):
        return sum([self.total])


class ActualSalesProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Actual Sales'

    date_start = models.DateField()
    date_end = models.DateField()
    monday = models.FloatField(default=0)
    tuesday = models.FloatField(default=0)
    wednesday = models.FloatField(default=0)
    thursday = models.FloatField(default=0)
    friday = models.FloatField(default=0)
    saturday = models.FloatField(default=0)
    sunday = models.FloatField(default=0)
    total = models.FloatField(default=0)


class salestotals(models.Model):
    forcast_total = models.ForeignKey(ForcastedSalesProfile, on_delete=models.CASCADE)
    actual_total = models.ForeignKey(ActualSalesProfile, on_delete=models.CASCADE)

# Purchasing


class DistributorProfile(models.Model):
    pass
