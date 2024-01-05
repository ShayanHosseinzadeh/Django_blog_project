from django.test import TestCase
from .models import Game
from django.shortcuts import reverse


# Create your tests here.
class Game_PostTests(TestCase):
    def setUp(self):
        self.game1 = Game.objects.create(
            name="game1",
            description="Test game",
            year_released=1990,
            company='testbox',
            status=Game.STATUS_CHOICES[0][0]
        )


    def test_game_model_str(self):
        self.assertEqual(str(self.game1),'game1')


    def test_game_url(self):
        response = self.client.get('/game/')
        self.assertEqual(response.status_code, 200)

    def test_game_url_by_name(self):
        response = self.client.get(reverse('Game_list_view'))
        self.assertEqual(response.status_code, 200)

    def test_game_list_show_on_home_page(self):
        response = self.client.get(reverse('Game_list_view'))
        self.assertContains(response, self.game1.name)
        self.assertContains(response, self.game1.description)
        self.assertContains(response, self.game1.company)

    def test_game_detail_by_id(self):
        response = self.client.get(reverse('Game_detail_view', args=[self.game1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.game1.name)
        self.assertContains(response, self.game1.description)
        self.assertContains(response, self.game1.company)

    def test_game_404_detail_view(self):
        response = self.client.get(reverse('Game_detail_view', args=[999]))
        self.assertEqual(response.status_code, 404)


    def test_add_game_view(self):
        response = self.client.post(reverse('Create_game'),{
            'name': 'Game2',
            'description': 'This is Game2 description',
            'company': 'testbox',
            'year_released':1990,
            'status': 'Released',

        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(Game.objects.last().name,'Game2')
        self.assertEqual(Game.objects.last().description,'This is Game2 description')

    def test_update_game_view(self):
        response = self.client.post(reverse('edit_game',args=[self.game1.id]),{
            'name': 'updated game',
            'description': 'updated text',
            'company': 'testbox1',
            'year_released':2002,
            'status': 'Released',

        })
        self.assertEqual(response.status_code,302)

    def test_delete_game_view(self):
        response = self.client.post(reverse('Delete_game',args=[self.game1.id]))
        self.assertEqual(response.status_code,302)