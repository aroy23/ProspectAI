from elevenlabs.client import ElevenLabs
from elevenlabs import save
from moviepy.editor import VideoFileClip, AudioFileClip
from dotenv import load_dotenv
import os

load_dotenv()
myAPI_KEY = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=myAPI_KEY)

video_path = "./vid/test2.mp4"
audio_path = "./aud/my-file.mp3"
final_video_path = "./vid/video_with_audio.mp4"


video = VideoFileClip(video_path)

text = "Incredible performance today! Incredible performance today! Incredible performance today! Incredible performance today! The team showed remarkable skill and determination."
audio = client.generate(text=text, voice="Rachel", model="eleven_monolingual_v1")

save(audio, audio_path)

audio_clip = AudioFileClip(audio_path)

video = video.set_audio(audio_clip)

video.write_videofile(final_video_path, codec="libx264", audio_codec="aac")

video.close()
audio_clip.close()