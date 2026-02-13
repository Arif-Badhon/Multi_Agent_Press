"""
src/agents/editor.py
The Editor-in-Chief orchestrates the workflow using Google ADK Runners.
"""

import os
import time  # <--- Added this import
import asyncio
from dotenv import load_dotenv
from google.adk.agents import LlmAgent 
from google.adk.runners import InMemoryRunner
from src.agents.reporter import ReporterAgent
from src.agents.writer import WriterAgent
from src.agents.presenter import PresenterAgent

load_dotenv()

class EditorAgent:
    def __init__(self):
        self.reporter = ReporterAgent()
        self.writer = WriterAgent()
        self.presenter = PresenterAgent()

        self.root_agent = LlmAgent(
            name="EditorInChief",
            model="gemini-2.0-flash",
            instruction="""
            You are the Editor-in-Chief.
            1. Call 'run_reporter' for research.
            2. Call 'run_writer' for the article.
            3. Call 'run_presenter' for the audio.
            """,
            tools=[self.run_reporter, self.run_writer, self.run_presenter]
        )
        
        self.runner = InMemoryRunner(agent=self.root_agent)

    def run_reporter(self, topic: str) -> str:
        return self.reporter.research(topic)

    def run_writer(self, topic: str, notes: str) -> str:
        # --- THE FIX IS HERE ---
        print("\n[System] ⏳  Pausing for 10s to respect API rate limits...")
        time.sleep(10)
        return self.writer.write(topic, notes)

    def run_presenter(self, topic: str, article_text: str) -> str:
        safe_name = topic.replace(" ", "_").lower()
        path = f"news/{safe_name}.mp3"
        self.presenter.speak(article_text, path)
        return f"Audio broadcast saved to {path}"

    async def produce_news(self, topic: str):
        print(f"\n[Editor] 👔 Workflow initialized for: {topic}")
        response = await self.runner.run_debug(
            f"Produce a complete news report on: {topic}",
            verbose=True
        )
        return response