from elevenlabs.client import ElevenLabs
from elevenlabs import play, stream, save
from moviepy.editor import VideoFileClip, AudioFileClip
from dotenv import load_dotenv
load_dotenv()
import os

myAPI_KEY = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(
  api_key=myAPI_KEY,
)
video_path = "path/to/your/video.mp4"
video = VideoFileClip(video_path)
video_duration = video.duration  # in seconds

# Generate the audio with a duration that matches the video
text = "Arnav you're goated for forgetting your government-issued ID."

# Adjust the speed of the voice to match the video duration
audio = client.generate(
    text=text,
    voice="Rachel",
    model="eleven_monolingual_v1",
    speed=1.0  # Set speed to make sure audio matches video duration
)

# Save the generated audio
audio_path = "my-file.mp3"
save(audio, audio_path)

# Load the generated audio, and trim or adjust if needed using moviepy
audio = AudioFileClip(audio_path).set_duration(video_duration)
audio.write_audiofile("trimmed-audio.mp3")