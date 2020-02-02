"""
Game Status Check

"""

# -*- coding: utf-8 -*-

class GameStats():

    def __init__(self, ai_settings):
        super().__init__()

        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.high_score = 0

    # reset game to initial stage
    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
