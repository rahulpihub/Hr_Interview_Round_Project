from django.test import TestCase, Client
from django.urls import reverse
from interview.models import InterviewRound

class InterviewViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.round = InterviewRound.objects.create(
            round_number=1,
            round_type='HR'
        )

    def test_round_list_view(self):
        response = self.client.get(reverse('interview:round-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interview/round_list.html')
        self.assertContains(response, 'HR Round')
