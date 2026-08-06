# ☕ Bloom Battles Trainer

> *Train your palate. Randomize your brew. Battle the bloom.*

Bloom Battles Trainer is a CLI tool for specialty coffee enthusiasts who want to level up their brewing game. It randomly assigns you a brew method, coffee process, dose, and ratio — then generates a pour-over recipe and optionally asks an AI to suggest the perfect grind size for your Comandante C40.

---

## ✨ Features

- 🎲 **Randomized training scenarios** — brew method, coffee process, dose (12–30g), and ratio (1:10–1:20)
- 📐 **Pour schedule generator** — calculates bloom and subsequent pours based on coffee process
- 🤖 **AI grind advisor** — powered by Groq (Gemma 7B) to suggest Comandante C40 click counts
- 🫧 Supports Natural, Honey, and Termico processed coffees with tailored pouring schedules

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A [Groq API key](https://console.groq.com/) (free tier available)

### Installation

```bash
git clone https://github.com/nosarabs/bloom-battles-trainer.git
cd bloom-battles-trainer
pip install openai python-dotenv
```

### Configuration

Create a `.env` file in the project root:

```env
GROQ_KEY=your_groq_api_key_here
```

### Run

```bash
python bb_trainer.py
```

---

## 🎮 How It Works

1. **Choose your brew method** (or let it randomize):
   - Aeropress, V60, Origami (Flat or Cone Filter), Kalita
2. **Choose your coffee process** (or let it randomize):
   - Red Catuai Natural, Marsellesa Termico, Geisha Red Honey, Pacamara Honey
3. **Get your randomized parameters** — dose in grams and brew ratio
4. **Receive your pour schedule** — a bloom + progressive pour plan calculated for your coffee
5. **Optionally ask the AI** for a grind size recommendation tailored to your setup

---

## 📋 Example Session

```
Bloom Battles Trainer!

Choose an option:
1. Aeropress
2. V60
3. Origami w/ Flat Filter
4. Origami w/ Cone Filter
5. Kalita
6. Random
Enter the number of your choice: 2

Choose an option:
1. Red Catuai Natural
2. Marsellesa Termico
3. Geisha Red Honey
4. Pacamara Honey
5. Random
Enter the number of your choice: 3

Your selection:
V60
Geisha Red Honey
18g
1:15

Recipe:
[54, 108.0, 144.0, 180.0, 216.0]

Suggest a recipe? (y/n): y
For a V60 with a Geisha Red Honey at 1:15, I'd suggest starting around 20–22 clicks on the Comandante C40...
Get Bloomin!
```

---

## 🍵 Supported Coffees & Pour Schedules

| Process | Pour Style | Pours After Bloom |
|---|---|---|
| Red Catuai Natural | 2-stage | 2 equal pours (60% of total) |
| Marsellesa Termico | 2-stage | 2 equal pours (60% of total) |
| Geisha Red Honey | 3-stage | 3 equal pours (60% of total) |
| Pacamara Honey | 3-stage | 3 equal pours (60% of total) |

Bloom is always **3× the coffee dose**.

---

## 🛠️ Tech Stack

- **Python** — core logic
- **OpenAI SDK** — API client (configured to use Groq)
- **Groq (Gemma 7B)** — AI grind size recommendations
- **python-dotenv** — environment variable management

---

## 📄 License

[MIT](LICENSE)

---

*Made with ☕ and a little chaos.*