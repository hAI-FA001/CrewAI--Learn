from langchain_huggingface import HuggingFaceEndpoint

from dotenv import load_dotenv
import os


load_dotenv()
hf_ep = os.environ['HUGGINGFACE_ENDPOINT']

llm = HuggingFaceEndpoint(
    repo_id=hf_ep,
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03
)