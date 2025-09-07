import logging
import subprocess

# Configure logging to file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("llm_requests.log"),
        logging.StreamHandler()
    ]
)

def call_local_llm_cli(prompt: str, model: str):
    logging.info(f"Sending prompt to LLM model '{model}': {prompt}")

    try:
        # Run the ollama CLI command to chat with the local model
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
            check=True
        )
        response = result.stdout.strip()
        logging.info(f"Received response from LLM: {response}")
        return response

    except subprocess.CalledProcessError as e:
        logging.error(f"LLM CLI command failed: {e.stderr}")
        return None

if __name__ == "__main__":
    model_name = "llama2"  # Replace with your actual local model name
    prompt_text = "Hello, LLM! How are you?"
    response = call_local_llm_cli(prompt_text, model_name)
    if response:
        print("LLM response:", response)
