def classify_learner(patterns):
    """
    Classify learner based on detected patterns.

    Args:
        patterns (dict): Output from pattern_detection.py

    Returns:
        dict: {
            'profile': str,
            'justification': list of triggered rules
        }
    """
    profile = "Unclassified"
    justification = []

    # Rule: Reflective but struggling
    if patterns['prolonged_thinking_questions'] and patterns['frequent_mistakes']:
        profile = "Reflective but struggling"
        justification.append("Prolonged thinking and frequent mistakes")

    # Rule: Impulsive learner
    elif patterns['impulsive_questions'] and patterns['frequent_mistakes']:
        profile = "Impulsive"
        justification.append("Impulsive answers and frequent mistakes")

    # Rule: Mastery learner
    elif not patterns['frequent_mistakes'] and not patterns['impulsive_questions'] and not patterns['prolonged_thinking_questions']:
        profile = "Mastery learner"
        justification.append("Few or no mistakes, stable response times")

    # Rule: Topic-specific struggler
    elif patterns['repetitive_topic_errors']:
        profile = "Topic-specific struggler"
        justification.append("Multiple repeated mistakes in a topic")

    return {
        'profile': profile,
        'justification': justification
    }
