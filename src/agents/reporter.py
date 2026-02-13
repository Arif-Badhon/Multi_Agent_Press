"""
src/agents/reporter.py
The Reporter agent searches for facts and produces raw notes.
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from src.tools.search import search_web

load_dotenv()

class ReporterAgent:
    # UPDATED: Changed model_id to a stable version
    def __init__(self, model_id: str = "gemini-2.0-flash"):
        """
        Initializes the Reporter agent with the Gemini client and search tools.
        """
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set.")

        self.client = genai.Client(api_key=api_key)
        self.model_id = model_id
        
        # We bind the python function directly to the tool configuration
        self.tools = [search_web]

        self.system_instruction = """
        You are a Senior Investigative Reporter.
        Your goal is to gather factual, up-to-date information on a given topic.
        
        PROTOCOL:
        1. When given a topic, you MUST use the 'search_web' tool to find information.
        2. Verify facts by cross-referencing search results.
        3. Do not write a blog post. Your output should be a set of detailed "Field Notes".
        4. Include the source URLs for every fact you list.
        """

    def research(self, topic: str) -> str:
        """
        Conducts research on a topic and returns field notes.
        """
        print(f"\n[Reporter] 🕵️ Starting research on: {topic}")

        # Create the chat session
        chat = self.client.chats.create(
            model=self.model_id,
            config=types.GenerateContentConfig(
                tools=self.tools,
                system_instruction=self.system_instruction,
                # Correct parameter name for google-genai SDK
                tool_config=types.ToolConfig(
                    function_calling_config=types.FunctionCallingConfig(
                        mode="AUTO"
                    )
                )
            )
        )

        response = chat.send_message(f"Research the following topic: {topic}")
        return response.text

if __name__ == "__main__":
    # If 2.0-flash gives a 404, try initializing with "gemini-1.5-flash"
    try:
        reporter = ReporterAgent(model_id="gemini-2.0-flash")
        notes = reporter.research("DeepSeek vs Gemini")
        print("\n--- FINAL NOTES ---\n")
        print(notes)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("💡 Tip: Try changing the model_id to 'gemini-1.5-flash'")