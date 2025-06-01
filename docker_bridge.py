import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# 컨테이너 설정
TEXT_CONTAINER = os.getenv("TEXT_CONTAINER", "text-emotion")
TEXT_PORT = os.getenv("TEXT_PORT", "8001")

AUDIO_CONTAINER = os.getenv("AUDIO_CONTAINER", "audio-emotion")
AUDIO_PORT = os.getenv("AUDIO_PORT", "8002")

IMAGE_CONTAINER = os.getenv("IMAGE_CONTAINER", "image-emotion")
IMAGE_PORT = os.getenv("IMAGE_PORT", "8003")

VIDEO_CONTAINER = os.getenv("VIDEO_CONTAINER", "video-emotion")
VIDEO_PORT = os.getenv("VIDEO_PORT", "8004")

# OpenAI API 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODE = os.getenv("OPENAI_MODE", "text") 

openai_client = OpenAI(api_key=OPENAI_API_KEY)


def request_text_analysis(payload: dict) -> dict:
    url = f"http://{TEXT_CONTAINER}:{TEXT_PORT}/analyze"
    response = requests.post(url, json=payload)
    return response.json()


def request_audio_analysis(file: bytes, filename: str) -> dict:
    url = f"http://{AUDIO_CONTAINER}:{AUDIO_PORT}/analyze"
    files = {"file": (filename, file)}
    response = requests.post(url, files=files)
    return response.json()


def request_image_analysis(file: bytes, filename: str) -> dict:
    url = f"http://{IMAGE_CONTAINER}:{IMAGE_PORT}/analyze"
    files = {"file": (filename, file)}
    response = requests.post(url, files=files)
    return response.json()


def request_video_analysis(file: bytes, filename: str) -> dict:
    url = f"http://{VIDEO_CONTAINER}:{VIDEO_PORT}/analyze"
    files = {"file": (filename, file)}
    response = requests.post(url, files=files)
    return response.json()


def convert_emotion_to_openai_output(emotion_result: dict) -> dict:
    emotion = emotion_result.get("emotion")
    if not emotion:
        return {"output": "Invalid emotion result"}

    if OPENAI_MODE == "text":
        prompt = f"Generate a short emotional sentence that reflects the feeling of '{emotion}'."
    else:
        prompt = f"Return an 8-bit RGB color code (like 'R:255, G:0, B:0') that matches the emotion '{emotion}'."

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an assistant that maps emotions to expressive output."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content.strip()
    return {"output": content}
