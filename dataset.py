import requests
import csv

# Fetch the JSON data from the provided link
url = "https://clchatagentassessment.s3.ap-south-1.amazonaws.com/queries.json"
response = requests.get(url)
data = response.json()

# Define the specific keys to extract based on the provided names
keys_to_extract = {
    "profile_context": [
        "patient_profile",
        "program_name",
        "diet_chart.notes",
        "diet_chart.hindi_notes",
        "diet_chart.meals_by_days.meals.name",
        "diet_chart.meals_by_days.meals.timings",
        "diet_chart.meals_by_days.meals.meal_options.notes",
        "diet_chart.meals_by_days.meals.meal_options.hindi_notes",
        "diet_chart.meals_by_days.meals.meal_options.meal_option_food_items.Food.name",
        "diet_chart.meals_by_days.meals.meal_options.meal_option_food_items.Food.name_hi",
        "diet_chart.meals_by_days.meals.meal_options.meal_option_food_items.Food.food_measures.name",
        "diet_chart.meals_by_days.meals.meal_options.meal_option_food_items.Food.food_measures.weight",
        "diet_chart.meals_by_days.meals.meal_options.meal_option_food_items.Food.food_measure_quantity"
    ],
    "ideal_response": [],
    "chat_context": [
        "chat_history.role",
        "chat_history.message",
        "chat_history.timestamp"
    ]
}

# Function to get nested value from JSON data based on a dot-separated key
def get_nested_value(data, key):
    keys = key.split('.')
    for k in keys:
        if isinstance(data, dict):
            data = data.get(k, None)
        elif isinstance(data, list):
            try:
                index = int(k)
                data = data[index]
            except (ValueError, IndexError):
                return None
        else:
            return None
    return data

# Extract data for each category
extracted_data = []

for record in data:
    row = {}
    
    # Extract profile_context data
    profile_context_data = []
    for key in keys_to_extract["profile_context"]:
        value = get_nested_value(record, f"profile_context.{key}")
        profile_context_data.append(value)
    
    # Extract latest_query data
    latest_query_data = get_nested_value(record, "latest_query")
    
    if isinstance(latest_query_data, dict):
        latest_query_combined = " | ".join(f"{k}: {v}" for k, v in latest_query_data.items())
    elif isinstance(latest_query_data, list):
        latest_query_combined = " | ".join(
            f"{item.get('role', 'No role available')}: {item.get('content', 'No content available')}" 
            for item in latest_query_data if isinstance(item, dict)
        )
    else:
        latest_query_combined = "No latest_query data available"
    
    # Extract ideal_response data
    ideal_response = get_nested_value(record, "ideal_response")
    
    # Extract ticket_id
    ticket_id = get_nested_value(record, "chat_context.ticket_id")
    
    # Extract chat_context data
    chat_context_data = []
    chat_history_data = get_nested_value(record, "chat_context.chat_history")
    if isinstance(chat_history_data, list):
        for chat in chat_history_data:
            role = get_nested_value(chat, "role")
            message = get_nested_value(chat, "message")
            timestamp = get_nested_value(chat, "timestamp")
            chat_context_data.append(f"role: {role} | message: {message} | timestamp: {timestamp}")
    else:
        chat_context_data.append("No chat history available")

    # Construct the row
    row['profile_context'] = " | ".join(map(str, profile_context_data))
    row['latest_query'] = latest_query_combined
    row['ideal_response'] = ideal_response
    row['ticket_id'] = ticket_id
    row['chat_context'] = " | ".join(map(str, chat_context_data))
    
    extracted_data.append(row)

# Write the extracted data into a CSV file with five columns
with open('extracted_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['profile_context', 'latest_query', 'ideal_response', 'ticket_id', 'chat_context']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in extracted_data:
        writer.writerow(row)

print("Data extracted and saved to 'extracted_data.csv'.")
