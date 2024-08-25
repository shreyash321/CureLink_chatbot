import csv
import json
import google.generativeai as genai
import os

class DietChatbot:
    def __init__(self, api_key, csv_file, output_csv_file, output_json_file):
        # Configure the LLM API
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.csv_file = csv_file
        self.output_csv_file = output_csv_file
        self.output_json_file = output_json_file
    
    def _generate_response(self, profile_context, latest_query, chat_context):
        # Create the input prompt for the LLM
        prompt = (
            f"You are a friendly chatbot dietician that recommends people diet advice from the given data and profile information "
            f"of their diet and health issues. You can also appreciate if the person is following his/her diet on time.\n\n"
            f"Profile Context:\n{profile_context}\n\n"
            f"Latest Query:\n{latest_query}\n\n"
            f"Chat Context:\n{chat_context}\n\n"
            f"Please provide diet advice and comments."
        )
        
        # Generate the response from the LLM
        response = self.model.generate_content(prompt)
        return response.text

    def process_data(self, limit=10):
        # Read the input CSV file and process each row
        extracted_data = []
        with open(self.csv_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                if i >= limit:
                    break

                profile_context = row.get('profile_context', '')
                latest_query = row.get('latest_query', '')
                chat_context = row.get('chat_context', '')
                ideal_response = row.get('ideal_response', '')

                # Generate response from LLM
                generated_response = self._generate_response(profile_context, latest_query, chat_context)

                # Update the row with generated response
                row['generated_response'] = generated_response
                extracted_data.append(row)
        
        # Write updated data to output CSV file
        with open(self.output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['profile_context', 'latest_query', 'ideal_response', 'ticket_id', 'chat_context', 'generated_response']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in extracted_data:
                writer.writerow(row)

        # Create and save the output JSON file
        json_output = [
            {
                "ticket_id": row.get('ticket_id', ''),
                "latest_query": row.get('latest_query', ''),
                "generated_response": row.get('generated_response', ''),
                "ideal_response": row.get('ideal_response', '')
            }
            for row in extracted_data
        ]

        with open(self.output_json_file, 'w', encoding='utf-8') as jsonfile:
            json.dump(json_output, jsonfile, indent=4)

        print(f"Data for first {limit} entries processed and saved to '{self.output_csv_file}' and '{self.output_json_file}'.")

# Example usage
if __name__ == "__main__":
    API_KEY = API_KEY
    csv_file = 'extracted_data.csv'
    output_csv_file = 'updated_extracted_data.csv'
    output_json_file = 'output.json'
    
    chatbot = DietChatbot(api_key=API_KEY, csv_file=csv_file, output_csv_file=output_csv_file, output_json_file=output_json_file)
    chatbot.process_data(limit=10)  # Process only the first 10 entries
