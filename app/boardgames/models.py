from django.db import models
from django.forms import ModelForm

class BoardGame(models.Model):
    title = models.CharField(max_length=50)
    eidtion_year = models.IntegerField()
    designer = models.CharField(max_length=30)
    game_duration_min = models.IntegerField()
    player_number = models.IntegerField()
    RATINGS = [
        (1, 'Very bad'),
        (2, 'Bad'),
        (3, 'Regular'),
        (4, 'Good'),
        (5, 'Very good'),
    ]
    rating = models.IntegerField(choices=RATINGS)
    played = models.BooleanField()
    acquisition_date = models.DateField()

    #calculated field example
    @property
    def label(self):
        return ''.join(
            [self.title, ' ', str(self.player_number), ' players, ', str(self.game_duration_min), ' min (', self.get_rating_display(), ' *).' ]
        )

class BoardGameForm(ModelForm):
    class Meta:
        model = BoardGame
        fields = ['title', 'eidtion_year', 'designer', 'game_duration_min', 'player_number', 'rating', 'played', 'acquisition_date']
