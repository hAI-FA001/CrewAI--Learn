from crewai import Agent

from tools import yt_tool



blog_researcher = Agent(
    role='Blog Researcher from YouTube Videos',
    goal='Get the relevant video content for topic {topic} from YT channel.',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in Data Science, Machine Learning and GenAI, and providing suggestions."
    ),
    tools=[yt_tool],
    allow_delegation=True,
)

blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT channel.',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        " engaging narratives that captivate and educate, bringing new"
        " discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False
)
