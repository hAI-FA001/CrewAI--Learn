from crewai_tools import YoutubeChannelSearchTool

from dotenv import load_dotenv
import os

load_dotenv()

hf_ep = os.environ['HUGGINGFACE_ENDPOINT']

yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle=os.environ['CHANNEL_HANDLE'],
    config={
        "llm": {
            "provider": "huggingface",
            "config": {
                "model": hf_ep
            }
        },
        "embedder": {
            "provider": "huggingface",
            "config": {
                "model": hf_ep
            }
        }
    }
)

