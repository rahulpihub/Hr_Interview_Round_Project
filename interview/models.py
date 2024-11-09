from django.db import models

class InterviewRound(models.Model):
    ROUND_TYPES = [
        ('HR', 'HR Round'),
        ('COMM', 'Communication Round'),
        ('TECH', 'Technical Round'),
        ('APT', 'Aptitude Round'),
    ]
    
    round_number = models.IntegerField()
    round_type = models.CharField(max_length=4, choices=ROUND_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['round_number']

    def __str__(self):
        return f"Round {self.round_number} - {self.get_round_type_display()}"
