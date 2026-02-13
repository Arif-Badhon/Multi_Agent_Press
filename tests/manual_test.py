"""
manual_test.py
Runs the Reporter and Writer together manually.
"""
from src.agents.reporter import ReporterAgent
from src.agents.writer import WriterAgent

def main():
    topic = "The Future of AI Agents in 2025"
    
    # 1. Reporter Step
    reporter = ReporterAgent()
    notes = reporter.research(topic)
    print("\n\n(Notes collected. Passing to Writer...)\n\n")
    
    # 2. Writer Step
    writer = WriterAgent()
    article = writer.write(topic, notes)
    
    # 3. Save to file
    filename = f"news/{topic.replace(' ', '_').lower()}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(article)
        
    print(f"\n✅ Article saved to: {filename}")

if __name__ == "__main__":
    main()