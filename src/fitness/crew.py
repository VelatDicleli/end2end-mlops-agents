from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai import LLM
from typing import List
import os


url = os.getenv("OLLAMA_API_URL", "http://localhost:11434")



@CrewBase
class Fitness():
    """Fitness crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    ollama_llm1 = LLM(
  	model="ollama/hf.co/VelatDicleli/diet_expert:Q4_K_M",
  	api_base=f'{url}'
  )
    ollama_llm2 = LLM(
  	model="ollama/hf.co/VelatDicleli/exercise_expert:Q4_K_M",
  	api_base=f'{url}'
  )
    



    @agent
    def nutritionist(self) -> Agent:
        return Agent(
            config=self.agents_config['nutritionist'], 
            verbose=False,
            llm=self.ollama_llm1
        )

    @agent
    def exercise_recommender(self) -> Agent:
        return Agent(
            config=self.agents_config['exercise_recommender'],
            verbose=False,
            llm=self.ollama_llm2
        )


    @task
    def nutrition_task(self) -> Task:
        return Task(
            config=self.tasks_config['nutrition_task'], 
        )
  

    @task
    def exercise_task(self) -> Task:
        return Task(
            config=self.tasks_config['exercise_task'], 
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Fitness crew"""


        return Crew(
            agents=self.agents,
            tasks=self.tasks, 
            verbose=False,
            process=Process.sequential, 
           
        )
