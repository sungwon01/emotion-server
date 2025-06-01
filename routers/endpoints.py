from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from docker_bridge import (
    request_text_analysis,
    request_audio_analysis,
    request_image_analysis,
    request_video_analysis,
    convert_emotion_to_openai_output
)

router = APIRouter()

@router.post("/analyze/text")
async def analyze_text(payload: dict):
    try:
        result = request_text_analysis(payload)
        openai_output = convert_emotion_to_openai_output(result)
        return {"emotion_result": result, "openai_output": openai_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze/audio")
async def analyze_audio(file: UploadFile = File(...)):
    try:
        data = await file.read()
        result = request_audio_analysis(data, file.filename)
        openai_output = convert_emotion_to_openai_output(result)
        return {"emotion_result": result, "openai_output": openai_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze/image")
async def analyze_image(file: UploadFile = File(...)):
    try:
        data = await file.read()
        result = request_image_analysis(data, file.filename)
        openai_output = convert_emotion_to_openai_output(result)
        return {"emotion_result": result, "openai_output": openai_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze/video")
async def analyze_video(file: UploadFile = File(...)):
    try:
        data = await file.read()
        result = request_video_analysis(data, file.filename)
        openai_output = convert_emotion_to_openai_output(result)
        return {"emotion_result": result, "openai_output": openai_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
