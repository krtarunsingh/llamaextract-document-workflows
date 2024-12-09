import os
from llama_extract import LlamaExtract
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("LLAMA_CLOUD_API_KEY")

# Initialize LlamaExtract
extractor = LlamaExtract()

# Book schema
book_data_config = {
    "type": "object",
    "title": "BookData",
    "required": ["page_number", "heading", "content"],
    "properties": {
        "page_number": {"type": "integer", "title": "Page Number"},
        "heading": {"type": "string", "title": "Heading"},
        "content": {"type": "string", "title": "Content"},
        "source": {"type": "string", "title": "Source"}
    },
}

# Create schema
schema = extractor.create_schema("Book Schema", book_data_config)
print("Book Schema Created:", schema)

# Extract data from tilted book image
results = extractor.extract(
    schema_id=schema.id,
    files=["path_to_tilted_book_image.jpg"]
)
print("Extracted Book Data as JSON:")
print(results)
