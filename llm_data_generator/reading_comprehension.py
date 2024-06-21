import os
from loguru import logger
from unstructured.partition.auto import partition
from langchain_core.prompts import PromptTemplate

from llm_data_generator.base import LLMDataGenerator
from llm_data_generator.prompt import READING_COMPREHENSION_PROMPT


class ReadingComprehension(LLMDataGenerator):
    def __init__(self, document_dir: str, prompt: PromptTemplate = READING_COMPREHENSION_PROMPT, language: str = "English"):
        super().__init__()
        self.document_dir = document_dir
        self.prompt = prompt

    def generate(self, num_samples: int):
        files = os.listdir(self.document_dir)
        for file in files:
            elements = partition(os.path.join(self.document_dir, file))
            logger.debug(f"Elements: {elements}")


if __name__ == "__main__":
    rc = ReadingComprehension(document_dir="data")
    rc.generate(1)
