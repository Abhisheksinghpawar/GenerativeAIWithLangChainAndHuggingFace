# GenerativeAIWithLangChainAndHuggingFace

url - https://www.udemy.com/course/complete-generative-ai-course-with-langchain-and-huggingface/

Minimal notes and example scripts for learning NLP and generative models.

Contents
- `S9_StreamlitWithPython/` — Streamlit examples and widgets
- `S10_MachineLearningForNLP/` — NLP notes, examples, and scripts

Quick start (Windows)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt  # create if needed
```
Run examples:
```powershell
python S10_MachineLearningForNLP/nltkNotes.py
python S9_StreamlitWithPython/app.py
```
Notes
- Do not name files after packages (e.g., `nltk.py`) — it will shadow the real package.
- Download NLTK data before first run: `import nltk; nltk.download('punkt','stopwords','wordnet','averaged_perceptron_tagger')`.

License
- Personal notes (no license).
