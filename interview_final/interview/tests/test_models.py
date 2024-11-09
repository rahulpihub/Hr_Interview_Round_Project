from django.test import TestCase
from interview.models import InterviewRound

class InterviewRoundTests(TestCase):
    def setUp(self):
        self.round = InterviewRound.objects.create(
            round_number=1,
            round_type='HR'
        )

    def test_round_creation(self):
        self.assertEqual(self.round.round_number, 1)
        self.assertEqual(self.round.round_type, 'HR')
        self.assertEqual(str(self.round), 'Round 1 - HR Round')
