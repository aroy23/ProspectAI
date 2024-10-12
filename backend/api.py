from elevenlabs.client import ElevenLabs
from elevenlabs import play, stream, save
from dotenv import load_dotenv
load_dotenv()
import os

myAPI_KEY = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(
  api_key=myAPI_KEY,
)
audio = client.generate(
  text="Lebron James is the best basketball player but Micheal Jordan was the actual genuine Greatest of All Time.",
  voice="Rachel",
  model="eleven_monolingual_v1"
)
save(audio, "my-file.mp3")