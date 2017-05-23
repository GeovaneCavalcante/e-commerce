from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail
from model_mommy import mommy
from django.contrib.auth import get_user_model


User = get_user_model()


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')


class ContactViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_form_ok(self):

        data = {'name': 'geovane', 'message': 'cuzão', 'email': 'geovane@gmail.com'}
        response = self.client.post(self.url, data)
        self.assertTrue(response.context['success'], True)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'Contato do django ecommerce')


class LoginViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user = mommy.prepare(User)
        self.user.set_password('123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_login_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_login_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_error(self):
        data = {'username': self.user.username, 'password': '1234'}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        error_msg = ('Erro na bagaça')
        self.assertFormError(response, 'form', None, error_msg)


class LogoutViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('logout')

    def tearDown(self):
        pass

    def test_logout_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)

