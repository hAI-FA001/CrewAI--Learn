from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, llm, tool
from crewai_tools import YoutubeChannelSearchTool

from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os


load_dotenv()
hf_ep = os.environ['HUGGINGFACE_ENDPOINT']


@CrewBase
class BlogWritingCrew():
	"""BlogWriting crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@tool
	def yt_tool(self):
		return YoutubeChannelSearchTool(
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

	@agent
	def blog_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			memory=True,
			allow_delegation=True,
			verbose=True,
		)

	@agent
	def blog_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['blog_writer'],
			memory=True,
			allow_delegation=True,
			verbose=True,
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def writing_task(self) -> Task:
		return Task(
			config=self.tasks_config['writing_task'],
			output_file='new-blog-post.md'
		)
	
	@llm
	def llm(self):
		return HuggingFaceEndpoint(
			repo_id=hf_ep,
			task="text-generation",
			max_new_tokens=512,
			do_sample=False,
			repetition_penalty=1.03
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the BlogWriting crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			memory=True,
			cache=True,
			max_rpm=100,
			share_crew=False,
		)