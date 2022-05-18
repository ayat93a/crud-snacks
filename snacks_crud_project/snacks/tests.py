from urllib import response
from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from .views import SnackDetailView

class SnacksTest(TestCase):
    def test_list_view(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response , 'snack-list.html')
        self.assertTemplateUsed(response , 'base.html')

    # def test_detail_view(self):
    #     url = reverse('snack_detail' , kwargs= {"pk" : 5})
    #     response = self.client.get(url )
    #     self.assertEqual(response.status_code , 200)
    #     self.assertTemplateUsed(response , 'snack-detail.html')
    #     self.assertTemplateUsed(response , 'base.html')

    def test_create_view(self):
        url = reverse('snack_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response , 'snack-create.html')
        self.assertTemplateUsed(response , 'base.html')

    # def test_update_view(self):
    #     url = reverse('snack_update')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code , 200)
    #     self.assertTemplateUsed(response , 'snack-update.html')
    #     self.assertTemplateUsed(response , 'base.html')
    
    # def test_delete_view(self):
    #     url = reverse('snack-delete')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code , 200)
    #     self.assertTemplateUsed(response , 'snack-delete.html')
    #     self.assertTemplateUsed(response , 'base.html')