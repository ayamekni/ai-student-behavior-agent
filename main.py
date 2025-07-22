import pandas as pd
import os

from src.profile_classifier import classify_learner

from src.data_ingestion import load_gameplay_data
from src.pattern_detection import detect_behavior_patterns


from src.recommendation_generator import generate_recommendation

# Create the folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Sample data
data = {
    'user_id': ['u001'] * 6,
    'question_id': ['q101', 'q102', 'q103', 'q104', 'q105', 'q106'],
    'timestamp': [
        '2025-07-21 10:01:00',
        '2025-07-21 10:03:00',
        '2025-07-21 10:05:00',
        '2025-07-21 10:07:00',
        '2025-07-21 10:09:00',
        '2025-07-21 10:11:00'
    ],
    'response_time': [12.4, 7.1, 15.2, 2.5, 3.0, 1.8],
    'is_correct': [False, True, False, False, True, False],
    'topic': ['fractions', 'fractions', 'geometry', 'geometry', 'geometry', 'geometry']
}

# Convert to DataFrame and save
df = pd.DataFrame(data)
df.to_csv("data/dummy_gameplay_data.csv", index=False)

print("Dummy gameplay data created and saved to data/dummy_gameplay_data.csv")



df = load_gameplay_data("data/dummy_gameplay_data.csv")
patterns = detect_behavior_patterns(df)

print("Detected Patterns:")
for key, value in patterns.items():
    print(f"- {key}: {value}")


from src.profile_classifier import classify_learner

learner_profile = classify_learner(patterns)
print(f"\n📌 Learner Profile: {learner_profile['profile']}")
print(f"🔍 Justification: {learner_profile['justification']}")



recommendation = generate_recommendation("u001", learner_profile)
print("\n📝 Final Recommendation:")
print(recommendation)
