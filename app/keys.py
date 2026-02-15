import os


gemini_key:str = r"/home/kailasha/Development/llm_assist/.secret/gemini.txt"
groq_key:str = r"/home/kailasha/Development/llm_assist/.secret/groq.txt"
mistral_key:str = r"/home/kailasha/Development/llm_assist/.secret/mistral.txt"

with open(gemini_key, "r") as f:
    gemini_key = f.read().strip()
    os.environ["GEMINI_KEY"] = gemini_key

with open(groq_key, "r") as f:
    groq_key = f.read().strip()
    os.environ["GROQ_KEY"] = groq_key

with open(mistral_key, "r") as f:
    mistral_key = f.read().strip()
    os.environ["MISTRAL_KEY"] = mistral_key