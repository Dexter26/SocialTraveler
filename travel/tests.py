from django.test import TestCase
from travel.user import UserModel

# Create your tests here.
from .user import UserModel



class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        UserModel.Todo.objects.create(title='first todo')
        UserModel.Todo.objects.create(description='a description here')

    def test_title_content(self):
        todo = UserModel.Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'first todo')

    def test_description_content(self):
        todo = UserModel.Todo.objects.get(id=2)
        expected_object_name = f'{todo.description}'
        self.assertEquals(expected_object_name, 'a description here')
