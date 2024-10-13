from elevenlabs.client import ElevenLabs
from elevenlabs import save
from moviepy.editor import VideoFileClip, AudioFileClip, vfx
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path('../.env')
load_dotenv(dotenv_path=env_path)
class VideoAudioGenerator:
    def __init__(self, video_path, audio_dir, output_video_dir):
        self.api_key = os.getenv('ELEVENLABS_API_KEY')
        self.client = ElevenLabs(api_key=self.api_key)
        self.video_path = video_path
        self.audio_dir = audio_dir
        self.output_video_dir = output_video_dir

    def generate_video_with_audio(self, text, voice="Brian", model="eleven_monolingual_v1", video_speed_factor=0.70, audio_speed_factor=1.25):
        # Paths for audio and final video output
        audio_path = os.path.join(self.audio_dir, "my-file.mp3")
        final_video_path = os.path.join(self.output_video_dir, "video_with_audio.mp4")
        
        # Load video from path
        video = VideoFileClip(self.video_path)

        # Generate audio from ElevenLabs
        audio = self.client.generate(text=text, voice=voice, model=model)
        save(audio, audio_path)

        # Load the generated audio file
        audio_clip = AudioFileClip(audio_path)

        # Slow down the video
        slowed_video = video.fx(vfx.speedx, video_speed_factor)

        # Slow down the audio by the same factor
        slowed_audio_clip = audio_clip.fx(vfx.speedx, audio_speed_factor)

        # Set the slowed-down audio to the slowed video
        slowed_video = slowed_video.set_audio(slowed_audio_clip)

        # Save the final video with slower video and audio
        slowed_video.write_videofile(final_video_path, codec="libx264", audio_codec="aac")

        # Close clips
        slowed_video.close()
        audio_clip.close()
        
        print(f"Final video saved at: {final_video_path}")