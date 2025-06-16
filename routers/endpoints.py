from fastapi import APIRouter, UploadFile, File, HTTPException, Request
from docker_bridge import (
    request_text_analysis,
    request_audio_analysis,
    request_image_analysis,
    request_video_analysis,
    convert_emotion_to_openai_output
)
import traceback
import logging

logger = logging.getLogger("uvicorn.error")

router = APIRouter()

@router.post("/analyze/text")
async def analyze_text(payload: dict, request: Request):
    try:
        result = request_text_analysis(payload)

        if "emotion" not in result:
            raise ValueError("Missing 'emotion' key in result: " + str(result))

        openai_output = convert_emotion_to_openai_output(result)

        log_entry = {
            "type": "text",
            "input": payload.get("text", ""),
            "emotion_result": result,
            "openai_output": openai_output
        }

        await request.app.state.collection.insert_one(log_entry)

        return {"emotion_result": result, "openai_output": openai_output}
    except Exception as e:
        logger.error("Exception in /analyze/text endpoint: ")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze/audio")
async def analyze_audio(request: Request, file: UploadFile = File(...)):
    try:
        data = await file.read()
        result = request_audio_analysis(data, file.filename)

        if "emotion" not in result:
            raise ValueError("Missing 'emotion' key in result: " + str(result))

        openai_output = convert_emotion_to_openai_output(result)

        await request.app.state.collection.insert_one({
            "type": "audio",
            "filename": file.filename,
            "emotion_result": result,
            "openai_output": openai_output
        })

        return {"emotion_result": result, "openai_output": openai_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze/image")
async def analyze_image(request: Request, file: UploadFile = File(...)):
    try:
        data = await file.read()
        result = request_image_analysis(data, file.filename)

        if "emotion" not in result:
            raise ValueError("Missing 'emotion' key in result: " + str(result))

        openai_output = convert_emotion_to_openai_output(result)

        await request.app.state.collection.insert_one({
            "type": "image",
            "filename": file.filename,
            "emotion_result": result,
            "openai_output": openai_output
        })

        return {"emotion_result": result, "openai_output": openai_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze/video")
async def analyze_video(request: Request, file: UploadFile = File(...)):
    try:
        data = await file.read()
        result = request_video_analysis(data, file.filename)
        
        if "emotion" not in result:
            raise ValueError("Missing 'emotion' key in result: " + str(result))
        
        openai_output = convert_emotion_to_openai_output(result)

        await request.app.state.collection.insert_one({
            "type": "video",
            "filename": file.filename,
            "emotion_result": result,
            "openai_output": openai_output
        })

        return {"emotion_result": result, "openai_output": openai_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
