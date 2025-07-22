import pandas as pd

def detect_behavior_patterns(df):
    """
    Detects behavior patterns from gameplay data.
    
    Args:
        df (pd.DataFrame): Loaded gameplay data.
        
    Returns:
        dict: Dictionary with detected patterns.
    """
    patterns = {}

    # Prolonged Thinking
    prolonged = df[df['response_time'] > 10]
    patterns['prolonged_thinking_questions'] = prolonged['question_id'].tolist()

    # Impulsive Answering
    impulsive = df[df['response_time'] < 3]
    patterns['impulsive_questions'] = impulsive['question_id'].tolist()

    # Frequent Mistakes
    total = len(df)
    incorrect = len(df[df['is_correct'] == False])
    patterns['frequent_mistakes'] = (incorrect / total) > 0.5

    # Repetitive Mistakes in Topics
    topic_errors = df[df['is_correct'] == False].groupby('topic').size()
    repetitive = topic_errors[topic_errors >= 3]
    patterns['repetitive_topic_errors'] = repetitive.to_dict()

    return patterns
