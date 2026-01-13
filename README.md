# toktoken# TokToon 🪄

**TokToon** is a lightweight Python library for **reducing LLM prompt token size** using **JSON squashing**, **schema-aware compression**, and **lossless/lossy modes**.  
It is designed to make large JSON or prompt data **token-efficient**, **LLM-friendly**, and easy to integrate into your AI pipelines.

---

## 🔥 Features

- **JSON Squasher** – Converts nested JSON into a compact, schema-first format.
- **Lossless and Lossy Modes** – Preserve full data or aggressively compress for maximum token savings.
- **LLM-Friendly Output** – Clean, bracket-free, semi-tabular format for faster model reasoning.
- **Lightweight & Dependency-Free** – Pure Python, works in any environment.
- **Planned Features** – Semantic compression, auto-learned aliases, token analytics.

---

## 🎚️ Lossless vs Lossy Modes

| Mode | Description |
|------|------------|
| **Lossless** | Preserves all fields and values, fully reversible. |
| **Lossy** | Aggressive compression for token savings (drops low-value fields, shortens values). |

---

## 💾 Installation

Install via **PyPI**:

```bash
pip install toktoon==0.1.2

## JSON Example (Nested JSON → Squashed Output)
from toktoon.json_squash import JsonSquasher

data = {
    "context": {
        "task": "Our favorite hikes together",
        "location": "Boulder",
        "season": "spring_2025"
    },
    "friends": ["ana", "luis", "sam"],
    "hikes": [
        {"id": 1, "name": "Blue Lake Trail", "distanceKm": 7.5, "elevationGain": 320, "companion": "ana", "wasSunny": True},
        {"id": 2, "name": "Ridge Overlook", "distanceKm": 9.2, "elevationGain": 540, "companion": "luis", "wasSunny": False},
        {"id": 3, "name": "Wildflower Loop", "distanceKm": 5.1, "elevationGain": 180, "companion": "sam", "wasSunny": True}
    ]
}

squasher = JsonSquasher(lossy=False)
print(squasher.squash(data))

## Output
context:
  task: Our favorite hikes together
  location: Boulder
  season: spring_2025
friends[3]: ana,luis,sam
hikes[3]{id,name,distanceKm,elevationGain,companion,wasSunny}:
  1,Blue Lake Trail,7.5,320,ana,True
  2,Ridge Overlook,9.2,540,luis,False
  3,Wildflower Loop,5.1,180,sam,True


## Text Example (Prompt Compression)
from toktoon.text_squash import TextSquasher  # assuming you implement text squasher
from toktoon.json_squash import JsonSquasher

long_prompt = """
As an AI language model, please summarize the following report.
This report contains detailed metrics on user engagement, including daily active users,
session times, click-through rates, and retention metrics. Kindly generate a concise
summary that focuses only on key insights.
"""

# Compress text (lossless)
text_squasher = TextSquasher(lossy=False)
compressed_text = text_squasher.squash(long_prompt)
print(compressed_text)
