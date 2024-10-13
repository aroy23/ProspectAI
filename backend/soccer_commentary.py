import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

# Load environment variables from .env file
env_path = Path('../.env')
load_dotenv(dotenv_path=env_path)

class SoccerCommentaryGenerator:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=self.api_key)
        self.teams = {
            213: 'Green',
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
            227: 'White'
        }
    
    def load_play_by_play(self, file_path):
        """Loads the play-by-play data from a text file"""
        with open(file_path, 'r') as file:
            play_by_play_data = file.read()
        return play_by_play_data.replace("\n", " ")

    def generate_commentary(self, play_by_play_string):
        """Generates soccer commentary based on play-by-play data"""
        prompt = f"""This is a play-by-play for a soccer match. You are a soccer commentator. Generate commentary for a short 17-second clip.

        Player 91 is the goalie of the white team, player 213 is the goalie of the green team. 
        No goals were scored, only passes in this sequence.

        Here is the list of players and their teams:
        {self.teams}

        Here is the play by play:
        {play_by_play_string}

        After player 91 gets the ball, pause for 4 seconds but do not physically write this before continuing the commentary. you can fill in the pause with general commentary about the game but 
        
        DO NOT talk about the physical pause in the script so a commentator can read it naturally

        Make sure to include all plays in the play by play in the commentary. Also, at the end there is no need to summarize just finish talking when the last play ends
        """

        # Call the OpenAI API using the chat completion method
        response = self.client.chat.completions.create(
            model='gpt-4o',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=300,
            temperature=0.7
        )

        # Return the generated commentary
        return response.choices[0].message.content.strip()

# Example usage:
if __name__ == "__main__":
    generator = SoccerCommentaryGenerator()
    play_by_play_string = generator.load_play_by_play('commentary.txt')
    commentary = generator.generate_commentary(play_by_play_string)
    print(commentary)
