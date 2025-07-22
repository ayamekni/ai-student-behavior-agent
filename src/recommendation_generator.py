def generate_recommendation(user_id, profile_data):
    """
    Generates a recommendation message for a student.

    Args:
        user_id (str): Student's ID
        profile_data (dict): Output from profile_classifier.py

    Returns:
        str: Formatted recommendation
    """
    profile = profile_data['profile']
    justification = profile_data['justification']
    
    # Intervention suggestions
    suggestions = {
        "Reflective but struggling": "review concepts slowly and provide worked examples to solidify understanding.",
        "Impulsive": "slow down when answering and use reflection prompts before submitting answers.",
        "Mastery learner": "explore more advanced material or challenging activities.",
        "Topic-specific struggler": "focus on targeted practice for the difficult topic areas.",
        "Unclassified": "keep practicing consistently and monitor for emerging patterns."
    }

    recommendation = f"{user_id} is a **{profile}** learner. Based on your activity, we recommend that you {suggestions.get(profile, 'continue learning with guidance')}."
    
    return recommendation
