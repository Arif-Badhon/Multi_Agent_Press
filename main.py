"""
main.py
The entry point for the Agent Press Automated Newsroom.
"""
import asyncio
import os
from src.agents.editor import EditorAgent

async def main():
    os.makedirs("news", exist_ok=True)

    print("\n" + "═"*40)
    print(" 🎙️  WELCOME TO THE AGENT PRESS NEWSROOM")
    print("═"*40)
    
    topic = input("\nWhat is today's headline? ").strip()
    if not topic:
        topic = "Developments in AI Agents 2026"

    editor = EditorAgent()
    
    print("\n[System] ⚙️  Orchestrator active...")
    
    # Await the async produce_news method
    final_report = await editor.produce_news(topic)
    
    print("\n" + "═"*40)
    print("📢 EDITOR'S FINAL SUMMARY:")
    print(final_report)
    print("═"*40 + "\n")

if __name__ == "__main__":
    # Use asyncio to run the main function
    asyncio.run(main())