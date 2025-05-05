from llama_cpp import Llama

llm = Llama(model_path="models/tinyllama-1.1b-chat.gguf", n_ctx=2048)

def tinyllama_chat(prompt: str) -> str:
    try:
        response = llm.create_chat_completion(
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"TinyLlama failed: {str(e)}"
