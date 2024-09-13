import json
from groq import Groq

groq = Groq(api_key="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")


class PromptDao:
    def __init__(self):
        self.model = "llama3-8b-8192"  # Replace with appropriate model if necessary

    def refine_prompt(self, prompt: str):
        """
        Refines a given prompt using the Groq LLM model and returns the result as a JSON dictionary.
        """
        chat_completion = groq.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Help me refine the prompt for image generation, and return in format of JSON like so: {'pos':'<String>', 'neg':'<String>'}",
                },
                {
                    "role": "user",
                    "content": f"{prompt}",
                },
            ],
            model=self.model,
            temperature=0.7,  # Adjust temperature for creativity or strictness
            stream=False,
            response_format={"type": "json_object"},
        )

        result = json.loads(chat_completion.choices[0].message.content)

        pos = result["pos"]
        neg = result["neg"]

        return pos, neg


# Example usage
if __name__ == "__main__":
    prompt_dao = PromptDao()
    prompt = "A man riding a horse in the wild west"
    pos, neg = prompt_dao.refine_prompt(prompt)

    print(prompt)

    print(pos, neg)
