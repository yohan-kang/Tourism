from django.test import TestCase
from django.urls import  include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase


class TestBoardViewMethods(APITestCase, URLPatternsTestCase):
  fixtures = ['boards.json']
  urlpatterns = [
      path('board/', include('board.urls')),
  ]
  
  def test_should_return_404(self):
    response = self.client.get('url_that_doesnt_exist', format='json')
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_should_get_two_boards(self):
    url = reverse('boardList')
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 2)

  def test_should_get_board_number_2(self):
    url = reverse('boardView',kwargs={"pk":"2"})
    response = self.client.get(url,format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    board = response.data
    self.assertEqual(board["id"], 2)
    self.assertEqual(board["title"], "board2")

  