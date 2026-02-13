"""
src/agents/presenter.py
The Presenter agent converts written articles into audio broadcasts.
"""

import os
from gtts import gTTS
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

class PresenterAgent:
    def __init__(self, model_id: str = "gemini-2.0-flash"):
        self.client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
        self.model_id = model_id
        
        # This instruction tells Gemini to rewrite the text for "the ear"
        self.system_instruction = """
        You are a Professional News Anchor.
        Your task is to convert a Markdown blog post into a natural-sounding broadcast script.
        
        RULES:
        1. Remove all Markdown syntax (##, **, etc.).
        2. Remove URLs (instead of reading a link, say "source details are in the show notes").
        3. Make the sentences flow naturally for speaking.
        4. Do NOT add your own commentary; stay true to the article provided.
        """

    def speak(self, article_text: str, output_path: str):
        """
        Processes text to a script and then saves it as an MP3.
        """
        print(f"\n[Presenter] 🎙️  Preparing broadcast script...")

        # 1. Transform Markdown to "Spoken Script"
        response = self.client.models.generate_content(
            model=self.model_id,
            contents=f"Convert this article into a broadcast script:\n\n{article_text}",
            config=types.GenerateContentConfig(system_instruction=self.system_instruction)
        )
        spoken_script = response.text

        # 2. Convert Script to Audio
        print(f"[Presenter] 🔊 Generating audio file...")
        tts = gTTS(text=spoken_script, lang='en', slow=False)
        tts.save(output_path)
        
        return output_path

if __name__ == "__main__":
    # Quick standalone test
    presenter = PresenterAgent()
    presenter.speak("## Hello World\nThis is a **test**.", "news/test_audio.mp3")