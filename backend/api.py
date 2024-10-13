from elevenlabs.client import ElevenLabs
from elevenlabs import save
from moviepy.editor import VideoFileClip, AudioFileClip
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
myAPI_KEY = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=myAPI_KEY)

# Paths
video_path = "./vid/test2.mp4"
audio_path = "./aud/my-file.mp3"  # Save path for the audio
final_video_path = "./vid/video_with_audio.mp4"

# Load the video
video = VideoFileClip(video_path)
# Generate audio commentary
text = "Incredible performance today! Incredible performance today! Incredible performance today! Incredible performance today! The team showed remarkable skill and determination."
audio = client.generate(text=text, voice="Rachel", model="eleven_monolingual_v1")

# Save the generated audio to a file
save(audio, audio_path)

# Load the saved audio as an AudioFileClip without changing duration
audio_clip = AudioFileClip(audio_path)

# Set the audio to the video
video = video.set_audio(audio_clip)

# Export the final video with the audio appended
video.write_videofile(final_video_path, codec="libx264", audio_codec="aac")

# Close the video and audio clips to free resources
video.close()
audio_clip.close()