import requests

# Replace with your Twelve Labs API key
API_KEY = ""
video_file = "test.mp4"

# Define the headers for authentication
headers = {
"Authorization": f"Bearer {API_KEY}",
"Content-Type": "application/json",
}

# Upload the video to Twelve Labs
with open(video_file, 'rb') as f:
	response = requests.post(
		"https://api.twelvelabs.io/videos", 
		headers=headers,
		files={"file": f}
	)

if response.status_code == 200:
	video_id = response.json().get("id")
	print(f"Video uploaded successfully. Video ID: {video_id}")
else:
	print("Failed to upload video", response.text)
	
transcription_endpoint = f"https://api.twelvelabs.io/videos/{video_id}/transcribe"

transcription_response = requests.post(
	transcription_endpoint,
	headers=headers
)

if transcription_response.status_code == 200:
	transcription = transcription_response.json()
	print("Transcription:", transcription)
else:
	print("Failed to transcribe video", transcription_response.text)
# Check transcription status
status_response = requests.get(
	transcription_endpoint,
	headers=headers
)

if status_response.status_code == 200:
	transcript_text = status_response.json().get("transcript")
	print("Transcription completed:", transcript_text)
else:
	print("Transcription not ready yet.")