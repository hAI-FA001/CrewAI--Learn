from crewai_tools import YoutubeChannelSearchTool

from dotenv import load_dotenv
import os

load_dotenv()

yt_tool = YoutubeChannelSearchTool(youtube_channel_handle=os.environ['CHANNEL_HANDLE'])

