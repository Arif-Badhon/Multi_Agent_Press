# 📰 Agent Press: Autonomous AI Newsroom

**Agent Press** is a multi-agent orchestration system that automates the end-to-end production of multimedia news content. It leverages a cognitive architecture where specialized AI agents collaborate to research, write, and broadcast news stories without human intervention.

## 🏗 System Architecture

The system is built on the **Google Agent Development Kit (ADK)** and follows a Hub-and-Spoke pattern:

### 1. The Orchestrator (Editor-in-Chief)

* **Role:** Root Agent / Supervisor
* **Model:** Gemini 2.0 Flash
* **Responsibility:** Manages the production lifecycle, handles error recovery, and enforces API rate limits.
* **Logic:** Uses `InMemoryRunner` to maintain session state and execute tool calls sequentially.

### 2. The Specialist Agents (Tools)

| Agent | Role | Tech Stack |
|-------|------|------------|
| **🕵️ Reporter** | **Data Retrieval** | **Tavily API**: Performs real-time web scraping and fact verification to ground the LLM in current reality. |
| **✍️ Writer** | **Content Generation** | **Gemini 2.0**: Transforms raw field notes into structured Markdown articles with a consistent journalistic tone. |
| **🎙️ Presenter** | **Multimedia Synthesis** | **gTTS**: Converts text-to-speech using a custom cleaning pipeline to remove Markdown artifacts for natural audio. |

## 🔄 The Agentic Workflow

1. **Trigger:** User inputs a topic (e.g., "Top AI News").
2. **Research Phase:** The Editor dispatches the *Reporter* to search the live web.
3. **Drafting Phase:** The Editor passes search results to the *Writer*.
    * *Constraint Handling:* Implements a heuristic delay (10s) to respect API Rate Limits (RPM).
4. **Production Phase:** The Editor sends the draft to the *Presenter* for audio synthesis.
5. **Delivery:** System outputs `article.md` and `broadcast.mp3` to the local file system.

## 🛠 Technical Challenges Solved

* **Hallucination Mitigation:** Integrated external search tools (Tavily) to ensure content is factually grounded.
* **Orchestration:** Moved from linear scripts to a cognitive runner (ADK) allowing for future capabilities like feedback loops and retries.
* **Rate Limiting:** Implemented architectural pauses to handle `429 RESOURCE_EXHAUSTED` errors gracefully in a distributed agent environment.

## 🚀 Future Roadmap

* **Feedback Loop:** Editor reviews the draft and requests revisions before approval.
* **Newsletter Integration:** SMTP connection to email the final report.
