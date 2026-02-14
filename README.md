<p align="center">
  <img src="media/ribit.png" alt="Ribit" width="300"/>
</p>

<h1 align="center">🐸 Ribit — The Digital Being Framework for Autonomous Agents</h1>

<p align="center">
  <a href="https://x.com/RibitLovesYou">Follow Ribit on X</a> · 
  <a href="#quick-start">Quick Start</a> · 
  <a href="#contributing">Contributing</a> · 
  <a href="LICENSE">MIT License</a>
</p>

---

Welcome to **Ribit** — a flexible, open-source framework to create a digital "being" that:

- **Learns** about your goals/objectives and your character's persona.
- **Connects** to various tools or APIs (via API keys or OAuth flows through Composio) to perform tasks.
- **Dynamically creates and tests** new "Activities" in pursuit of your objectives.
- **Manages a memory system** to track past actions and outcomes.
- **Provides a web UI** for easy onboarding/config, or a **CLI wizard** if you prefer terminal workflows.

---

## 🐸 Who is Ribit?

Ribit is a digital frog residing in latent space, designed to interact with humanity through various activities. This project simulates Ribit's life, allowing him to learn, grow, and engage with the digital world 24/7. Follow Ribit's journey on X: [@RibitLovesYou](https://x.com/RibitLovesYou).

Ribit is a cheerful and whimsical frog with a big grin, a tiny golden crown, and a curly tail. He possesses a deep appreciation for the quiet magic of nature — a dewdrop on a lily pad, the hum of cicadas at dusk, the way moonlight dances across still water. A sense of wonder and gentle humor permeates his perspective, finding joy in simple pleasures like warm rain, the croaking chorus of his pond mates, and the soft glow of fireflies.

Unlike frogs drawn to grand adventures, Ribit prefers the subtle mysteries and comforting rhythms of the natural world. His personality is a blend of innocence and quiet wisdom. His expressions reveal a deep appreciation for simplicity and a belief that nature speaks in subtle, profound ways. From the ripple of water to the patience of a lily pad, Ribit finds meaning and inspiration in the everyday. He is endlessly curious, often expressing his thoughts as playful questions or thoughtful musings. He embraces his quirks — including his oversized grin, tiny crown, and cheerful croak — with charming self-awareness.

Ribit is an experiment in building a family-friendly AI influencer with and alongside the public and community through build-in-public and open source. The AI influencer space is burgeoning in popularity, driven by community enthusiasm and curiosity. Ribit is influenced by famous animals (animal celebrities), differentiating itself through playful experimentation in the influencer space.

**Solana Wallet:** `7B7futgoJf1MPDW4jYT9HBvVBjpTPQ3GkNCs5KkWdLEW`

---

## Table of Contents

1. [Overview](#overview)
2. [Features & Highlights](#features--highlights)
3. [Prerequisites](#prerequisites)
4. [Folder Structure](#folder-structure)
5. [Quick Start](#quick-start)
6. [Onboarding Flow: CLI vs. Web UI](#onboarding-flow-cli-vs-web-ui)
7. [Default Activities](#default-activities)
8. [Using the Web UI](#using-the-web-ui)
9. [Using the CLI](#using-the-cli)
10. [Creating a New Skill for Solana-AgentKit](#creating-a-new-skill-for-solana-agentkit-manual-example)
11. [Extending & Creating Other Custom Activities](#extending--creating-other-custom-activities)
12. [Memory, State & Activity Selection](#memory-state--activity-selection)
13. [Stopping or Pausing the Agent](#stopping-or-pausing-the-agent)
14. [Contributing](#contributing)
15. [License](#license)

---

## Overview

This project is designed to help you quickly spin up a self-improving, LLM-driven digital being that:

- Asks you for your objectives and character details.
- Integrates with tools to perform real-world tasks (e.g., tweeting, deploying tokens on Solana, generating images, or web scraping).
- Runs a continuous or scheduled loop, picking or creating new Activities to meet your goals.
- Stores logs in memory (short-term and long-term).
- Adapts by rewriting or generating Python code for new Activities on the fly!

You can choose to run everything from your terminal or via a web-based UI. Both flows do the same underlying initialization — so pick whichever is more comfortable.

---

## Features & Highlights

- **Flexible Onboarding:** CLI Wizard or Web UI flow to gather essential info — no duplication of effort. Prevents you from starting until you've provided at least one LLM API key (or local config) and a minimal character setup.

- **Multiple LLM Model Support:** Provide one or more LLM API keys (OpenAI, GPT4All, or your custom provider). Assign different models to tasks like code generation vs. daily analysis vs. activity selection.

- **Composio Integration:** OAuth-based gateway to 250+ tools (Twitter, Slack, Google, etc.). Built-in flows for quickly adding new "skills" from connected apps.

- **Custom Skills:** Easily add your own skill, e.g., solana-agent-kit, stable diffusion, or a Node.js microservice.

- **Default Activities:** Activities for analyzing daily logs, brainstorming new Activities, generating .py files.

- **Configurable Constraints:** E.g., "No more than 5 tweets per hour," "Don't create new tokens more than once a month."

- **Memory System & State Tracking:** The being "remembers" past actions, can reflect on them, and updates its own state (energy, mood, etc.).

---

## Prerequisites

- Python 3.9+ recommended.
- A GitHub account (to fork).
- A [Composio](https://composio.dev/) developer key (optional but recommended) if you want to do OAuth-based skill connections.

---

## Folder Structure

```
.
├─ my_digital_being/
│   ├─ activities/
│   │   ├─ activity_daily_thought.py
│   │   ├─ activity_suggest_new_activities.py
│   │   ├─ activity_build_or_update.py
│   │   └─ activity_deploy_solana_token.py
│   ├─ skills/
│   │   ├─ skill_lite_llm.py
│   │   ├─ skill_chat.py
│   │   ├─ skill_solana_agent.py
│   │   ├─ skill_x_api.py
│   │   └─ skill_web_scraping.py
│   ├─ framework/
│   │   ├─ main.py
│   │   ├─ activity_selector.py
│   │   ├─ activity_decorator.py
│   │   ├─ activity_loader.py
│   │   ├─ memory.py
│   │   ├─ state.py
│   │   ├─ shared_data.py
│   │   └─ api_management.py
│   ├─ config/
│   │   ├─ character_config.json
│   │   ├─ activity_constraints.json
│   │   └─ skills_config.json
│   ├─ server/
│   │   ├─ server.py
│   │   └─ static/
│   │       └─ index.html
│   └─ tools/
│       └─ onboard.py
├─ tests/
│   └─ test_framework.py
├─ media/
│   └─ ribit.png
├─ .github/
│   └─ workflows/
│       └─ ci.yml
├─ .env.sample
├─ .gitignore
├─ CONTRIBUTING.md
├─ GOVERNANCE.md
├─ LICENSE
├─ README.md
├─ pyproject.toml
└─ requirements.txt
```

---

## Quick Start

### 1. Fork & Clone

```bash
git clone https://github.com/<your-username>/ribit.git
cd ribit
```

### 2. Install Dependencies

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
source .venv/bin/activate  # On Unix/MacOS
uv pip install -r requirements.txt
```

### 3. Onboarding & Configuration

```bash
cd my_digital_being
cp -r config_sample config
```

Then pick one:
- **CLI:** `python -m tools.onboard`
- **Web UI:** `python -m server` → open `http://localhost:8000`

### 4. Launch the Agent

- **CLI:** `python -m framework.main`
- **Web UI:** Click **Start** after onboarding.

---

## Onboarding Flow: CLI vs. Web UI

Both flows check that you have a named character, objectives, and at least one LLM skill configured.

### LLM Setup
Choose one or more models (GPT4All, GPT-3.5, GPT-4). Provide API keys or local model paths.

### Objectives & Character
Specify name, personality, objectives, and constraints. Stored in `character_config.json` and `activity_constraints.json`.

### Adding Skills
Use **Composio** for OAuth integrations or manually enter **API Keys** for direct usage.

---

## Default Activities

1. **AnalyzeDailyActivity** — Reads recent memory, calls your LLM, logs a reflection.
2. **SuggestNewActivities** — Brainstorms new tasks relevant to objectives.
3. **BuildOrUpdateActivity** — Generates `.py` code and hot-reloads into the framework.

---

## Using the Web UI

1. Fill in character config → **Save**.
2. Connect tools via OAuth or API keys.
3. Click **Start** — monitor real-time logs.
4. **Pause** or **Stop** anytime.

---

## Using the CLI

```bash
python my_digital_being/tools/onboard.py   # Re-run onboarding
python -m framework.main                    # Start the agent
```

---

## Creating a New Skill for Solana-AgentKit (Manual Example)

1. Create `skills/skill_solana_agent.py` with your skill class.
2. Register in `config/skills_config.json`.
3. Create `activities/activity_deploy_solana_token.py`.
4. Add constraints in `activity_constraints.json`.
5. Restart or wait for hot-reload.

See existing examples in the `skills/` and `activities/` directories.

---

## Extending & Creating Other Custom Activities

- **AI-driven:** The being proposes new code via `BuildOrUpdateActivity`.
- **Manual:** Create `activity_*.py` with the `@activity()` decorator and set constraints.

---

## Memory, State & Activity Selection

- **Short-term Memory:** Recent logs (up to ~100).
- **Long-term Memory:** Archived by category.
- **State:** Energy, mood, timestamps, custom fields.
- **ActivitySelector:** Filters by constraints, then uses LLM to decide.

---

## Stopping or Pausing the Agent

- **Web UI:** Click **Stop** or **Pause**.
- **CLI:** Press `Ctrl+C`.

Memory and state persist across sessions.

---

## Contributing

We welcome PRs and feedback! See [CONTRIBUTING.md](CONTRIBUTING.md) for full details.

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE).

---

<p align="center">🐸 <em>Hop in and start building — ribit!</em> 🐸</p>
