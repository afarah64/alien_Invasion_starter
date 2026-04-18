"""Track statistics for the Alien Invasion game.

This class stores and manages game-related state information,
such as the number of remaining ships (lives).
"""
class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ship_limit: int):
        """Initialize game statistics

    Args:
        ship_limit (int): The number of ships (lives) the player starts with.
    """
        self.ships_left = ship_limit
        
    
