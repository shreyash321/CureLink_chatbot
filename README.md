# Curelink AI Assignment

## Overview

Curelink is dedicated to enhancing patient care for conditions such as PCOS, Preconception, and Pregnancy through a multidisciplinary approach. We aim to integrate AI to make chronic care more affordable and accessible. This assignment focuses on automating responses to patient queries received via WhatsApp, specifically meal pictures. 

The objective is to develop a Python program that uses Large Language Models (LLMs) to generate accurate and actionable responses based on meal images, patient context, and ideal responses.

## How the Code Works

### 1. **Data Extraction**

The code begins by fetching a JSON file from a specified URL, which contains sample patient queries along with the required context and ideal responses. 

- **Fetching Data**: Retrieves the JSON data from the provided URL.
- **Extracting Data**: Parses and extracts relevant key data points including `profile_context`, `latest_query`, `ideal_response`, and `chat_context`.
- **Saving to CSV**: Writes the extracted data into a CSV file, organizing it into columns for easy reference.

### 2. **Generating Responses with LLMs**

The AI agents use Google's Gemini LLM to generate diet-specific recommendations. The process involves:

- **LLM Configuration**: Setting up access to the LLM API.
- **Creating Prompts**: Tailoring prompts based on specific health conditions like PCOS, Weight Loss, Diabetes, etc. These prompts guide the LLM in generating relevant dietary advice.
- **Generating Advice**: Using the LLM to provide personalized dietary recommendations based on the input profile context and condition-specific prompts.

### 3. **AI Agents**

The code defines multiple AI agents, each specializing in providing dietary recommendations for specific conditions. These agents:

- **Adjust Prompts**: Customize prompts to fit the dietary needs associated with various health conditions.
- **Generate Responses**: Feed patient profile data and prompts into the LLM to obtain and display diet recommendations.

## Features Achieved

- **Automated Response Generation**: The system automatically generates dietary advice based on patient profiles and meal images, streamlining the care delivery process.
- **Customizable AI Agents**: Multiple AI agents handle different health conditions, providing tailored recommendations for conditions such as PCOS, Weight Loss, and Diabetes.
- **Data Handling**: Efficiently extracts, processes, and stores data in CSV format for further analysis.
- **Integration with LLMs**: Leverages Google's Gemini LLM to produce accurate and contextually relevant dietary recommendations.

## Conclusion

The implemented solution automates dietary recommendations using LLMs, enhancing the efficiency and effectiveness of patient care. The system provides personalized advice based on meal images and patient profiles, ensuring that dietary recommendations are both relevant and actionable.

Feel free to explore and adapt the provided code to suit specific needs or to integrate additional features.

---

**Note**: Ensure you replace placeholder API keys with actual credentials and update prompts based on the latest requirements.
