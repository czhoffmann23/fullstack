from django.urls import reverse,resolve
from django.db import models

class TestUrls:
    def test_category(self):
        path = reverse('category')
        assert resolve(path).view_name== 'category'