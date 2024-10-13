import sys
sys.path.append('../')
from utils import get_center_of_bbox, measure_distance

class PlayerBallAssigner():
    def __init__(self):
        # Maximum allowable distance between player and ball for assignment
        self.max_player_ball_distance = 70
        self.last_assigned_player = -500
        self.teams = {213: 'Green',
                        3: 'Green',
                        14: 'Green',
                        1: 'Green',
                        8: 'Green',
                        7: 'Green',
                        34: 'Green',
                        26: 'Green',
                        10: 'Green',
                        4: 'Green',
                        13: 'Green',
                        22: 'White',
                        120: 'Green',
                        134: 'Green',
                        156: 'Green',
                        236: 'Green',
                        91: 'White',
                        28: 'White',
                        19: 'White',
                        9: 'White',
                        6: 'White',
                        15: 'White',
                        5: 'White',
                        11: 'White',
                        12: 'White',
                        16: 'White',
                        132: 'White',
                        142: 'White',
                        227: 'White'}
        self.currentpossession = 'White'
        self.set_possession = {6, 11, 91, 13, 7, 213, 3, 5}
        with open('commentary.txt', 'w') as f:
            f.write('')
    def assign_ball_to_player(self, players, ball_bbox):
        # Get the center position of the ball's bounding box
        ball_position = get_center_of_bbox(ball_bbox)

        # Initialize variables to track the minimum distance and assigned player
        minimum_distance = 99999
        assigned_player = -1

        # Iterate through each player to find the closest one to the ball
        for player_id, player in players.items():
            player_bbox = player['bbox']

            # Calculate distances from the ball to the left and right edges of the player's bounding box
            distance_left = measure_distance((player_bbox[0], player_bbox[-1]), ball_position)
            distance_right = measure_distance((player_bbox[2], player_bbox[-1]), ball_position)
            distance = min(distance_left, distance_right)

            # Check if the current player is within the maximum allowable distance
            if distance < self.max_player_ball_distance:
                # Update the assigned player if the current player is closer to the ball
                if distance < minimum_distance:
                    minimum_distance = distance
                    assigned_player = player_id
        if self.last_assigned_player != assigned_player and assigned_player != -1:
            self.last_assigned_player = assigned_player
            with open('commentary.txt', 'a') as f:
                if assigned_player in self.set_possession:
                    f.write("Player " + str(assigned_player) + " of " + self.teams[assigned_player] + " possesses the ball\n")
                    if self.teams[assigned_player] != self.currentpossession:
                        self.currentpossession = self.teams[assigned_player]
                        f.write("Possession changed to " + self.currentpossession + " player " + str(assigned_player) + "\n")
        return assigned_player