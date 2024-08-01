

def analyze_cv(job_description, cv_text, api_key):
    
    return {
        "cv_score": "85",
        "improvements": [
            "Add more relevant experience",
            "Include specific skills mentioned in the job description"
        ],
        "skills_suggestions": [
            "Improve communication skills",
            "Gain proficiency in Python"
        ]
    }

def process_response(response):
    cv_score = response.get('cv_score', 'N/A')
    improvements = response.get('improvements', [])
    suggestions = response.get('skills_suggestions', [])
    return cv_score, improvements, suggestions







