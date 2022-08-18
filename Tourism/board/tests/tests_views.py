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

  def test_should_create_newboard(self):
    url = reverse('boardInsert')
    response = self.client.post(url,data={"title":"board3","writer":"writer3","date":"2022-08-01T02:00:00Z"})
    board = response.data
    # print(board)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(board["title"],"board3")
    url = reverse('boardList')
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 3)

  def test_should_delete_board2(self):
    url = reverse('boardDelete',kwargs={"pk":"2"})
    response = self.client.delete(url)
    print("---- delete ----")
    print(response.status_code)
    url = reverse('boardList')
    response = self.client.get(url, format='json')
    print(len(response.data))
    self.assertEqual(len(response.data), 1)

  def test_should_update_board1(self):
    print("---- update ----")
    url = reverse('boardList')
    response = self.client.get(url, format='json')
    print(len(response.data))
    url = reverse('boardView',kwargs={"pk":"1"})
    response = self.client.put(url,data={"title":"board1change","writer":"writer100","date":"2022-08-01T02:00:00Z"})
    url = reverse('boardList')
    response = self.client.get(url, format='json')
    print(response.data)