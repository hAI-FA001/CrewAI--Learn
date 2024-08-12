from crewai import Task

from tools import yt_tool
from agents import blog_researcher, blog_writer


research_task = Task(
    description=(
        "Identify the video {topic}."
        " Get detailed information about the video from the channel."
    ),
    expected_output="A comprehensive 3 paragraphs long report based on the {topic} of video content.",
    tools=[yt_tool],
    agent=blog_researcher
)

writing_task = Task(
    description=(
        "Get information from the YT channel on the topic {topic}."
    ),
    expected_output="Summarize the info from the YT channel's video on the topic {topic} and create content for the blog.",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,  # cuz sequential process
    output_file="new-blog-post.md"
)