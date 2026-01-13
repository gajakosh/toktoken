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
