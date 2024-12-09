import os
from llama_extract import LlamaExtract
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("LLAMA_CLOUD_API_KEY")

# Initialize LlamaExtract
extractor = LlamaExtract()

# Invoice schema
invoice_data_config = {
    "type": "object",
    "title": "InvoiceData",
    "required": [
        "forwarding_agent", "date", "invoice_number", "tracking_number", "paid_by",
        "order_id", "sold_by", "bill_to", "products", "sub_total", "shipping_charges",
        "insurance", "sales_tax", "total", "importing_company", "incoterms",
        "goods_description", "reason_for_export"
    ],
    "properties": {
        "forwarding_agent": {"type": "string", "title": "Forwarding Agent"},
        "date": {"type": "string", "format": "date", "title": "Date"},
        "invoice_number": {"type": "string", "title": "Invoice Number"},
        "tracking_number": {"type": "string", "title": "Tracking Number"},
        "paid_by": {"type": "string", "title": "Paid By"},
        "order_id": {"type": "string", "title": "Order ID"},
        "sold_by": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "title": "Sold By Name"},
                "address": {"type": "string", "title": "Sold By Address"},
                "phone": {"type": "string", "title": "Sold By Phone"},
                "email": {"type": "string", "title": "Sold By Email"},
                "eori": {"type": "string", "title": "Sold By EORI"}
            }
        },
        "bill_to": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "title": "Bill To Name"},
                "address": {"type": "string", "title": "Bill To Address"},
                "phone": {"type": "string", "title": "Bill To Phone"},
                "email": {"type": "string", "title": "Bill To Email"},
                "eori": {"type": "string", "title": "Bill To EORI"}
            }
        },
        "products": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "title": "Product Name"},
                    "hs_code": {"type": "string", "title": "HS Code"},
                    "units": {"type": "integer", "title": "Units"},
                    "unit_price": {"type": "number", "title": "Unit Price"},
                    "total": {"type": "number", "title": "Total"},
                    "country_of_origin": {"type": "string", "title": "Country of Origin"}
                }
            }
        },
        "sub_total": {"type": "number", "title": "Sub Total"},
        "shipping_charges": {"type": "number", "title": "Shipping Charges"},
        "insurance": {"type": "number", "title": "Insurance"},
        "sales_tax": {"type": "number", "title": "Sales Tax"},
        "total": {"type": "number", "title": "Total"},
        "importing_company": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "title": "Importing Company Name"},
                "address": {"type": "string", "title": "Importing Company Address"},
                "phone": {"type": "string", "title": "Importing Company Phone"},
                "email": {"type": "string", "title": "Importing Company Email"},
                "eori": {"type": "string", "title": "Importing Company EORI"}
            }
        },
        "incoterms": {"type": "string", "title": "Incoterms"},
        "goods_description": {"type": "string", "title": "Description of Goods"},
        "reason_for_export": {"type": "string", "title": "Reason for Export"}
    }
}

# Create schema
schema = extractor.create_schema("Invoice Schema", invoice_data_config)
print("Invoice Schema Created:", schema)

# Extract data from invoice
results = extractor.extract(
    schema_id=schema.id,
    files=["path_to_invoice.pdf"]
)
print("Extracted Invoice Data as JSON:")
print(results)
