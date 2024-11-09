from django.test import TestCase
from django.core import mail
from interview.utils import send_round_assignment_email

class UtilsTests(TestCase):
    def test_send_round_assignment_email(self):
        success = send_round_assignment_email(
            'test@example.com',
            'HR Round',
            1
        )
        self.assertTrue(success)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            mail.outbox[0].subject,
            'Assignment for HR Round - Round 1'
        )