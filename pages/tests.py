from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.
#SimpleTestCase is efficient in testing views and forms that do not require data
#base access
class HomePageTests(SimpleTestCase):
    
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_templates(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html') 
#we're using Testcase cause we need to interact with a database
class SignUpPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@gmail.com'
    def test_siguppages_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
    
    
    def uses_correct_templates(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        
    def test_signup_form(self):
        model_object = get_user_model().objects
        new_user = model_object.create_user(self.username, self.email)
        self.assertEqual(model_object.all().count(), 1)
        self.assertEqual(model_object.all()[0].username, self.username)
        self.assertEqual(model_object.all()[0].email, self.email)