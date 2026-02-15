import os
from typing import List, Union
from abc import ABC, abstractmethod
from google import genai
from groq import Groq
from mistralai import Mistral

_initialized = False
class LLM(ABC):
    def __init__(self):
        global _initialized
        if not _initialized:
            print("Initializing LLM base class")
            import keys  # Ensure keys are loaded into environment variables
            _initialized = True

    @abstractmethod
    def call_llm(self, prompt: str) -> Union[str, List, None]:
        """Implement in concrete LLM subclasses"""
        raise NotImplementedError

class GeminiLLM(LLM):
    def __init__(self):
        super().__init__()

    def call_llm(self, prompt:str):
        return self._call_gemini_api(prompt)
    def _call_gemini_api(self, prompt:str):
        try:

            client = genai.Client(api_key=os.environ["GEMINI_KEY"])

            response = client.models.generate_content(
                model="gemini-3-flash-preview", contents=prompt
            )
            print(response.text)
            return response.text
        except Exception as e:
            print(f"Error calling Gemini API: {e}")
            return None

class GroqLLM(LLM):
    def __init__(self):
        super().__init__()

    def call_llm(self, prompt:str):
        return self._call_groq_api(prompt)

    def _call_groq_api(self, prompt:str):
        try:
            client = Groq(api_key=os.environ["GROQ_KEY"])
            completion = client.chat.completions.create(
                model="groq/compound",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            print(f"Error calling Groq API: {e}")
            return None

class MistralLLM(LLM):
    def __init__(self):
        super().__init__()

    def call_llm(self, prompt:str):
        return self._call_mistral_api(prompt)

    def _call_mistral_api(self, prompt:str):
        try:
            with Mistral(
                api_key=os.environ["MISTRAL_KEY"],
            ) as mistral:

                res = mistral.chat.complete(model="mistral-small-latest", messages=[
                    {
                        "content": "Who is the best French painter? Answer in one short sentence.",
                        "role": "user",
                    },
                ], stream=False)

                # Handle response
                if res.choices[0].message.content:
                    return res.choices[0].message.content
                else:
                    return None
        except Exception as e:
            print(f"Error calling Mistral API: {e}")
            return None
