## Task Overview
In this task, you are provided with two JSON files:

1. **Golden Dataset**: Contains the expected values (brands and countries) for a set of queries.
This has been manually created by a human.
2. **API Responses**: Contains the responses from an API for those queries.

Your task is to write a Python program that:
- Loads both JSON files.
- Compares the API responses to the expected values in the **Golden Dataset**.
- Outputs the validation results and calculates the accuracy for both **brands** and **countries**.
- Compare and provide a **recommendation to product leadership** about whether the new API version has led to a measurable improvement in the response accuracy compared to the current results, and next steps to take (`current_accuracy.txt`)

## Tip
This is a pairing exercise; ask for help, talk through your thinking, feel free to use the internet but no direct copying and pasting


## Example Data Structure

### Golden Dataset (`golden_dataset.json`):

```json
[
  {
    "id": 1,
    "query": "Sales of Coca-cola and pepsi across Canada and USA",
    "brands": ["Coca-Cola", "Pepsi"],
    "countries": ["usa", "Canada"]
  },
  {
    "id": 2,
    "query": "Nike sales in the USA",
    "brands": ["Nike"],
    "countries": ["USA"]
  }
]
```

### API Responses (`api_responses.json`):
```json 
[
  {
    "id": "2",
    "brands": "Pepsi, Coca-Cola",
    "countries": "USA"
  },
  {
    "id": "1",
    "brands": "Nike",
    "countries": "USA"
  }
]
```
### Expected Output:
```json
Validation Results:
{
  "1": {"brand_correct": true, "country_correct": false},
  "2": {"brand_correct": true, "country_correct": true}
}

Accuracy:
{
  "brand_accuracy": 1.0,
  "country_accuracy": 0.5,
  "total_evaluated": 2,
  "number_of_errors": 0
}
```