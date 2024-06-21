from langchain_core.prompts import PromptTemplate


READING_COMPREHENSION_PROMPT = PromptTemplate.from_template(
    """
    Your task is to generate questions and answers based on the following text.
    The questions should be answerable based on the information in the text. You need to generate at least 5 different 
    questions and answers. Be sure to include the question and answer in the same json format as the examples below.
    [
        {
            "question": "What is the capital of France?",
            "answer": "Paris"
        },
        {
            "question": "What is the capital of Spain?",
            "answer": "Madrid"
        }
    ]
    The text is as follows:
    {text}
    Your response:
    """
)
