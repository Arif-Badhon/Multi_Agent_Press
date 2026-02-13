"""
manual_test.py
Runs the Reporter and Writer together based on user input.
"""
import os
from src.agents.reporter import ReporterAgent
from src.agents.writer import WriterAgent

def main():
    # --- GET USER INPUT ---
    print("\n" + "="*30)
    print(" 📰 AGENT PRESS: NEWS DESK")
    print("="*30)
    
    # Prompt user for a topic
    user_prompt = input("\nEnter a topic for the news report (or press Enter for default): ").strip()
    
    # Set a default if input is empty
    topic = user_prompt if user_prompt else "The Future of AI Agents in 2026"
    
    print(f"\n🚀 Processing: '{topic}'...")

    # 1. Reporter Step: Gather notes
    reporter = ReporterAgent()
    notes = reporter.research(topic)
    
    # 2. Writer Step: Turn notes into an article
    writer = WriterAgent()
    article = writer.write(topic, notes)
    
    # --- SAVE LOGIC ---
    output_folder = "news"
    os.makedirs(output_folder, exist_ok=True)
    
    # Create a safe filename (removes spaces, adds .md)
    safe_filename = topic.replace(' ', '_').lower() + ".md"
    file_path = os.path.join(output_folder, safe_filename)
    
    # Write the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(article)
        
    print(f"\n✅ Success! Article saved to: {file_path}")
    print("="*30 + "\n")

if __name__ == "__main__":
    main()