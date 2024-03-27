from django.test import TestCase

from django.urls import reverse
from django.contrib.auth.models import User
from .models import Business, Item, Service

class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.business = Business.objects.create(owner=self.user, name='Test Business', description='Test Description')
        self.item = Item.objects.create(business=self.business, item_name='Test Item', price=10)
        self.service = Service.objects.create(business=self.business, service_name='Test Service', price=20)

    def test_business_management(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('business_management', args=(self.business.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/business-admin.html')

    def test_add_item(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('add_item'), {'item_name': 'New Test Item', 'price': 15})
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Item.objects.filter(item_name='New Test Item').exists())

    def test_create_business(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('create_business'), {'name': 'New Test Business', 'description': 'New Test Description'})
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(Business.objects.filter(name='New Test Business').exists())

    def test_shop(self):
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/home.html')

    def test_product_detail(self):
        response = self.client.get(reverse('product_detail', args=(self.item.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/product_detail.html')

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/index.html')

    def test_about(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/about_us.html')

    def test_service_management(self):
        response = self.client.get(reverse('service_management'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services.html')

    def test_menu_management(self):
        response = self.client.get(reverse('menu_management'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/menu.html')

    def test_business_register(self):
        response = self.client.get(reverse('business_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_business_profile(self):
        response = self.client.get(reverse('business_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/business-profile-page.html')
