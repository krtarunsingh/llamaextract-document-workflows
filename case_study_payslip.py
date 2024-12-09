import os
from llama_extract import LlamaExtract
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("LLAMA_CLOUD_API_KEY")

# Initialize LlamaExtract
extractor = LlamaExtract()

# Payslip schema
payslip_data_config = {
    "type": "object",
    "title": "PayslipData",
    "required": [
        "employee_name", "employee_id", "department", "pay_period_start",
        "pay_period_end", "payment_date", "basic_salary", "gross_pay", "net_pay", "deductions"
    ],
    "properties": {
        "employee_name": {"type": "string", "title": "Employee Name"},
        "employee_id": {"type": "string", "title": "Employee ID"},
        "department": {"type": "string", "title": "Department"},
        "pay_period_start": {"type": "string", "format": "date", "title": "Pay Period Start"},
        "pay_period_end": {"type": "string", "format": "date", "title": "Pay Period End"},
        "payment_date": {"type": "string", "format": "date", "title": "Payment Date"},
        "basic_salary": {"type": "number", "title": "Basic Salary"},
        "gross_pay": {"type": "number", "title": "Gross Pay"},
        "net_pay": {"type": "number", "title": "Net Pay"},
        "deductions": {
            "type": "array",
            "title": "Deductions",
            "items": {
                "type": "object",
                "properties": {
                    "deduction_type": {"type": "string", "title": "Deduction Type"},
                    "deduction_amount": {"type": "number", "title": "Deduction Amount"}
                }
            }
        }
    },
}

# Create schema
schema = extractor.create_schema("Payslip Schema", payslip_data_config)
print("Schema Created:", schema)

# Extract data from image
results = extractor.extract(
    schema_id=schema.id,
    files=["path_to_payslip_image.jpg"]
)
print("Extracted Payslip Data as JSON:")
print(results)
