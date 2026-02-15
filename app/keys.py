import os

# Define paths
SECRET_PATHS = {
    "GEMINI_KEY": r"/home/kailasha/Development/llm_assist/.secret/gemini.txt",
    "GROQ_KEY": r"/home/kailasha/Development/llm_assist/.secret/groq.txt",
    "MISTRAL_KEY": r"/home/kailasha/Development/llm_assist/.secret/mistral.txt"
}

def load_keys():
    for env_var, path in SECRET_PATHS.items():
        try:
            with open(path, "r") as f:
                os.environ[env_var] = f.read().strip()
        except FileNotFoundError:
            print(f"Warning: Secret file not found at {path}")
        except Exception as e:
            print(f"Error loading {env_var}: {e}")

# Execute loading
load_keys()