
from transformers import pipeline

MODEL_PATH = "content/model_directory"

# Load summarization 
summarizer = pipeline(
    "summarization",
    model=MODEL_PATH,
    tokenizer=MODEL_PATH
)

def summarize(blog_post: str) -> str:
    """
    Generate summary for input text without explicit torch usage.
    """

    if not blog_post or not blog_post.strip():
        return "Please enter valid text to summarize."

    result = summarizer(
        blog_post,
        max_length=150,
        min_length=40,
        length_penalty=2.0,
        num_beams=4,
        do_sample=False
    )

    return result[0]["summary_text"]
