import llm
from llm import LLM
from llm import GeminiLLM
from llm import GroqLLM
from llm import MistralLLM

def llm_factory(llm_name: str) -> LLM:
    if llm_name == "gemini":
        
        return GeminiLLM()
    elif llm_name == "groq":
        
        return GroqLLM()
    elif llm_name == "mistral":
        
        return MistralLLM()
    else:
        raise ValueError(f"Unsupported LLM: {llm_name}")


if __name__ == "__main__":
    print("This is a module, not a script. Please import it to use its functionality.")

    for llm_name in [ "groq", "mistral", "gemini"]:
        print(f"\nTesting {llm_name.capitalize()} LLM:")
        llm = llm_factory(llm_name)
        response = llm.call_llm("Hello, world!")
        print(f"Response from {llm_name.capitalize()}: {response}")
    