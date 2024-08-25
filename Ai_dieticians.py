import google.generativeai as genai

class DietChatbot:
    def __init__(self, api_key):
        # Configure the LLM API
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def _generate_response(self, prompt):
        # Generate the response from the LLM
        response = self.model.generate_content(prompt)
        return response.text

    def get_dietician_prompt(self, condition, profile_context):
        # Create a specific prompt based on the condition
        prompts = {
            "PCOS": (
                "You are a dietitian specialized in PCOS (Polycystic Ovary Syndrome). "
                "Provide diet advice and recommendations based on the patient's profile information to manage PCOS symptoms effectively.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Weight Loss": (
                "You are a dietitian specialized in weight loss. "
                "Provide diet advice and recommendations based on the patient's profile information to help with weight reduction and maintenance.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Diabetes": (
                "You are a dietitian specialized in diabetes management. "
                "Provide diet advice and recommendations based on the patient's profile information to manage blood sugar levels effectively.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Heart Disease": (
                "You are a dietitian specialized in heart disease management. "
                "Provide diet advice and recommendations based on the patient's profile information to support heart health.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Hypertension": (
                "You are a dietitian specialized in hypertension management. "
                "Provide diet advice and recommendations based on the patient's profile information to help control blood pressure.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Renal Disease": (
                "You are a dietitian specialized in renal disease management. "
                "Provide diet advice and recommendations based on the patient's profile information to support kidney function.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Gastrointestinal Issues": (
                "You are a dietitian specialized in gastrointestinal issues. "
                "Provide diet advice and recommendations based on the patient's profile information to manage digestive health.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Thyroid Disorders": (
                "You are a dietitian specialized in thyroid disorders. "
                "Provide diet advice and recommendations based on the patient's profile information to support thyroid health.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Anemia": (
                "You are a dietitian specialized in managing anemia. "
                "Provide diet advice and recommendations based on the patient's profile information to help with iron levels.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "High Cholesterol": (
                "You are a dietitian specialized in managing high cholesterol. "
                "Provide diet advice and recommendations based on the patient's profile information to help manage cholesterol levels.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Osteoporosis": (
                "You are a dietitian specialized in managing osteoporosis. "
                "Provide diet advice and recommendations based on the patient's profile information to support bone health.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Pregnancy": (
                "You are a dietitian specialized in pregnancy nutrition. "
                "Provide diet advice and recommendations based on the patient's profile information to ensure healthy pregnancy.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Menopause": (
                "You are a dietitian specialized in menopause management. "
                "Provide diet advice and recommendations based on the patient's profile information to support health during menopause.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Digestive Health": (
                "You are a dietitian specialized in digestive health. "
                "Provide diet advice and recommendations based on the patient's profile information to improve digestive function.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Food Allergies": (
                "You are a dietitian specialized in managing food allergies. "
                "Provide diet advice and recommendations based on the patient's profile information to avoid allergens and manage reactions.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Stress Management": (
                "You are a dietitian specialized in stress management through diet. "
                "Provide diet advice and recommendations based on the patient's profile information to help manage stress levels.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Skin Health": (
                "You are a dietitian specialized in skin health. "
                "Provide diet advice and recommendations based on the patient's profile information to improve skin condition.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Muscle Gain": (
                "You are a dietitian specialized in muscle gain. "
                "Provide diet advice and recommendations based on the patient's profile information to support muscle growth.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Detox": (
                "You are a dietitian specialized in detoxification. "
                "Provide diet advice and recommendations based on the patient's profile information to support detox processes.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "Anti-Inflammatory": (
                "You are a dietitian specialized in anti-inflammatory diets. "
                "Provide diet advice and recommendations based on the patient's profile information to reduce inflammation.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            ),
            "General Health": (
                "You are a dietitian providing general health advice. "
                "Provide diet advice based on the patient's profile information to promote overall health.\n\n"
                f"Patient Profile:\n{profile_context}\n\n"
                "Please provide detailed diet advice and comments."
            )
        }

        return prompts.get(condition, prompts["General Health"])

    def get_advice_for_condition(self, condition, profile_context):
        prompt = self.get_dietician_prompt(condition, profile_context)
        return self._generate_response(prompt)

# Example usage
if __name__ == "__main__":
    API_KEY = 'your_google_api_key_here'
    
    # Initialize the DietChatbot with the API key
    chatbot = DietChatbot(api_key=API_KEY)
    
    # Define the conditions and patient profile context
    conditions = [
        "PCOS", "Weight Loss", "Diabetes", "Heart Disease", "Hypertension", 
        "Renal Disease", "Gastrointestinal Issues", "Thyroid Disorders", 
        "Anemia", "High Cholesterol", "Osteoporosis", "Pregnancy", 
        "Menopause", "Digestive Health", "Food Allergies", "Stress Management", 
        "Skin Health", "Muscle Gain", "Detox", "Anti-Inflammatory", "General Health"
    ]
    
    profile_context = "Age: 30, Gender: Female, Weight: 70kg, Height: 165cm, Health Issues: PCOS"

    # Process advice for each condition
    for condition in conditions:
        advice = chatbot.get_advice_for_condition(condition, profile_context)
        print(f"Advice for {condition}:\n{advice}\n")
