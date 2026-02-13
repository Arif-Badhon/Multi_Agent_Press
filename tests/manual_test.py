"""
manual_test.py
Runs the Reporter and Writer together and saves the output to the /news folder.
"""
import os
from src.agents.reporter import ReporterAgent
from src.agents.writer import WriterAgent

def main():
    topic = "The Future of AI Agents in 2025"
    
    # 1. Reporter Step: Gather notes
    reporter = ReporterAgent()
    notes = reporter.research(topic)
    
    # 2. Writer Step: Turn notes into an article
    writer = WriterAgent()
    article = writer.write(topic, notes)
    
    # --- SAVE LOGIC ---
    # Create the 'news' directory if it doesn't already exist
    output_folder = "news"
    os.makedirs(output_folder, exist_ok=True)
    
    # Create a safe filename
    safe_filename = topic.replace(' ', '_').lower() + ".md"
    
    # Construct the full path (e.g., news/the_future_of_ai_agents_in_2025.md)
    file_path = os.path.join(output_folder, safe_filename)
    
    # Write the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(article)
        
    print(f"\n✅ Success! Article saved to: {file_path}")

if __name__ == "__main__":
    main()