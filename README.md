# 📰 Agent Press

An Automated AI Newsroom powered by Google GenAI & Python.

Agent Press is a multi-agent system designed to automate the entire news production cycle. It employs a team of specialized AI agents to research topics, write engaging blog posts, and produce audio broadcasts without human intervention.

## 🏗 Architecture

The system orchestrates four distinct roles:

- 🕵️ **Reporter**: Scours the web for real-time facts using DuckDuckGo.
- ✍️ **Writer**: Synthesizes research notes into polished blog posts using Gemini.
- 🎙️ **Presenter**: Converts written content into broadcast-ready audio using gTTS.
- 👔 **Editor**: The orchestrator that manages the workflow and quality control.

## 🛠 Tech Stack

- **Core Model**: Google Gemini 2.0 Flash (via `google-genai` SDK)
- **Language**: Python 3.12+ (managed by `uv`)
- **Dependencies**:
  - `google-adk`: Google AI Development Kit
  - `google-genai`: Interaction with Gemini models
  - `pydantic`: Data validation and settings management
  - `python-dotenv`: Environment variable management
  - `pyyaml`: Configuration parsing

## 📂 Project Structure

The project is currently in a skeleton state, with the following structure:

```plaintext
agent-press/
├── src/
│   ├── agents/      # Agent implementations (base classes logic)
│   ├── core/        # Core logic (planning, memory, reasoning)
│   ├── environment/ # Environment simulation
│   └── utils/       # Utility functions (logging, metrics)
├── pyproject.toml   # Dependency configuration
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- `uv` installed
- A Google Cloud/AI Studio API Key

### Installation

1. Clone the repository:

   ```bash
   git clone <https://github.com/your-username/agent-press.git>
   cd agent-press
   ```

2. Install dependencies:

   ```bash
   uv sync
   ```

3. Set up environment variables:
   Create a `.env` file with your API key:

   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```

## 🚦 Usage

**Current Status: Skeleton / Initial Development**

The project infrastructure is set up, but the specific agent implementations (Reporter, Writer, etc.) are currently placeholders or in early development stages.

You can verify the installation by running the tests (once added) or checking the module imports:

```bash
uv run python -c "import src.agents; print('Agents module imported successfully')"
```

## 🗺 Roadmap

- [x] Phase 0: Project Skeleton & Dependency Setup
- [ ] Phase 1: Implement Reporter Agent (Web Search Integration)
- [ ] Phase 2: Implement Writer Agent (Drafting Logic)
- [ ] Phase 3: Implement Presenter Agent (Audio Generation)
- [ ] Phase 4: Implement Editor Agent (Workflow Orchestration)
