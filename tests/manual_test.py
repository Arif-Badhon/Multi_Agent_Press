import os
from src.agents.reporter import ReporterAgent
from src.agents.writer import WriterAgent
from src.agents.presenter import PresenterAgent

def main():
    print("\n" + "="*30)
    print(" 📰 AGENT PRESS: MULTI-AGENT NEWSROOM")
    print("="*30)
    
    user_prompt = input("\nEnter a topic: ").strip()
    topic = user_prompt if user_prompt else "The Future of AI Agents in 2026"
    
    # 1. Reporter
    reporter = ReporterAgent()
    notes = reporter.research(topic)
    
    # 2. Writer
    writer = WriterAgent()
    article = writer.write(topic, notes)
    
    # 3. Presenter (Phase 3)
    presenter = PresenterAgent()
    
    # --- SAVE AND CONVERT ---
    output_folder = "news"
    os.makedirs(output_folder, exist_ok=True)
    
    base_name = topic.replace(' ', '_').lower()
    md_path = os.path.join(output_folder, f"{base_name}.md")
    mp3_path = os.path.join(output_folder, f"{base_name}.mp3")
    
    # Save Markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(article)
    
    # Generate Audio
    presenter.speak(article, mp3_path)
        
    print(f"\n✅ DONE!")
    print(f"📄 Article: {md_path}")
    print(f"🎧 Audio:   {mp3_path}")
    print("="*30 + "\n")

if __name__ == "__main__":
    main()