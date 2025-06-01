from pydantic import BaseModel
from typing import Optional

class TextAnalysisRequest(BaseModel):
    text: str

class AudioAnalysisRequest(BaseModel):
    audio_url: str

class ImageAnalysisRequest(BaseModel):
    image_url: str

class VideoAnalysisRequest(BaseModel):
    video_url: str

class AnalysisResult(BaseModel):
    result: str
    rgb_color: Optional[tuple[int, int, int]] = None
