"""
src/agents/writer.py
The Writer agent takes raw notes and drafts a polished blog post.
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

class WriterAgent:
    def __init__(self, model_id: str = "gemini-2.0-flash"):
        """
        Initializes the Writer agent.
        """
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set.")

        self.client = genai.Client(api_key=api_key)
        self.model_id = model_id

        # The Writer doesn't need search tools, just a strong persona.
        self.system_instruction = """
        You are a Senior Tech Journalist for a top-tier tech blog (like The Verge or TechCrunch).
        
        YOUR TASK:
        Take the provided "Field Notes" and write an engaging, structured blog post.
        
        GUIDELINES:
        1. Write in a clear, professional, yet accessible tone.
        2. Use Markdown formatting (## Headings, **Bold**, etc.).
        3. Start with a catchy headline (H1).
        4. Include a "Key Takeaways" section at the top.
        5. weaving the sources/links naturally into the text or adding a "References" section at the bottom.
        6. Do NOT invent information. Only use facts found in the notes.
        """

    def write(self, topic: str, notes: str) -> str:
        """
        Drafts a blog post based on the provided notes.
        """
        print(f"\n[Writer] ✍️ Drafting post on: {topic}...")

        prompt = f"""
        TOPIC: {topic}
        
        FIELD NOTES:
        {notes}
        
        Please write the full blog post now.
        """

        response = self.client.models.generate_content(
            model=self.model_id,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=self.system_instruction,
                temperature=0.7 # Slightly creative
            )
        )
        
        return response.text

# Test block
if __name__ == "__main__":
    # We simulate passing notes from the Reporter
    dummy_notes = """
    * Gemini is Google's multimodal model, strong in coding.
    * DeepSeek is an open-weight model from China, very efficient.
    * Benchmarks show Gemini 1.5 Pro leads in long context.
    * DeepSeek-V3 is cheaper to run.
    """
    
    writer = WriterAgent()
    post = writer.write("DeepSeek vs Gemini", dummy_notes)
    print("\n--- FINAL POST ---\n")
    print(post)