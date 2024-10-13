# Prospect AI

Prospect AI is a cutting-edge platform designed to bridge the gap between high school athletes and college recruiters, streamlining the recruitment process through AI-driven highlights and commentary. Athletes can upload their sports footage, and recruiters can quickly evaluate talent thanks to object detection, play-by-play commentary, and player tracking.

## Inspiration

Each year, high school student-athletes face a daunting recruitment process as they compete for attention from college recruiters. Coaches, on the other hand, spend countless hours sifting through footage to find the right players. ProspectAI was developed to simplify this process, offering a platform where athletes can easily showcase their talents and recruiters can efficiently evaluate potential recruits.

## What it does

- **Upload and Highlight**: Athletes can upload their highlight videos. Our AI highlights the featured player, tracking them throughout the footage, making it easier for recruiters to focus on the athlete's performance.
- **AI Commentary**: Using computer vision, the platform generates live, AI-driven commentary that syncs with the video, offering a real-time, play-by-play analysis of key moments.
- **College Aspirations**: Athletes can add their desired colleges and recruiters' contact information, facilitating the connection between talent and opportunity.

**Tech Stack:**
- **Backend**: Flask (video uploads, object detection, processing)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (athlete profiles, video data)
- **Object Detection**: YOLO (real-time sports footage)
- **AI Commentary**: OpenAI (scripts), ElevenLabs AI (text-to-speech)
- **Video Processing**: MoviePy (sync video/audio)

**Team Members:**
- **Arnav Roy** (CS @ UCLA) - Computer Vision, AI Commentary
- **Choidorj Bayarkhuu** (CS @ UCLA) - Text-to-Speech, Backend
- **Stanley Sha** (CS @ UCI) - Full Stack
- **Emma Wu** (Data Science @ UCLA) - Frontend, Web Scraping
- **Leah Shin** (Data Science @ UCLA) - Frontend

## Installation

To set up ProspectAI locally, ensure you have Python installed and clone this repository. Then, install the required dependencies:

```bash
pip install ultralytics
pip install supervision
pip install opencv-python
pip install scikit-learn
pip install numpy
pip install pandas
pip install matplotlib
pip install flask
pip install elevenlabs
pip install openai
pip install moviepy
