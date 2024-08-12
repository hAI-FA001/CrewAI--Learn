#!/usr/bin/env python
import sys
from blog_writing.crew import BlogWritingCrew

import os
from dotenv import load_dotenv

load_dotenv()
TOPIC = os.environ['TOPIC']


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': TOPIC
    }
    BlogWritingCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": TOPIC
    }
    try:
        BlogWritingCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        BlogWritingCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": TOPIC
    }
    try:
        BlogWritingCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
