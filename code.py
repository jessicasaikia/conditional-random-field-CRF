!pip install pandas sklearn-crfsuite

import pandas as pd
from sklearn_crfsuite import CRF

def extract_features(sentence):
    features = []
    tokens = sentence.split()
    for i, word in enumerate(tokens):
        features.append({
            'word': word,
            'prev_word': tokens[i - 1] if i > 0 else '',
            'next_word': tokens[i + 1] if i < len(tokens) - 1 else '',
            'word_length': len(word),
            'is_capitalized': word[0].isupper(),
        })
    return features

data = pd.read_csv('/content/CRF.csv')

X, y = [], []
for _, row in data.iterrows():
    tokens = row['Sentence']
    tags = row['POS_Tags'].split()
    X.append(extract_features(tokens))
    y.append(tags)

crf = CRF(algorithm='lbfgs', max_iterations=100, all_possible_transitions=True)
crf.fit(X, y)

def predict_pos(input_data):
    if isinstance(input_data, str):
        features = extract_features(input_data)
        tags = crf.predict([features])[0]
        return list(zip(input_data.split(), tags))
    elif isinstance(input_data, pd.DataFrame):
        predictions = []
        for _, row in input_data.iterrows():
            sentence = row['Sentence']
            features = extract_features(sentence)
            tags = crf.predict([features])[0]
            predictions.append((sentence, tags))
        return predictions
    else:
        raise ValueError("Input should be a sentence (str) or a DataFrame (pd.DataFrame).")

user_input_type = input("Enter 'sentence' for a sentence or 'csv' for CSV input: ").strip().lower()

if user_input_type == "sentence":
    user_sentence = input("Enter your sentence: ")
    predicted_tags = predict_pos(user_sentence)
    print("Predicted POS tags:", predicted_tags)

elif user_input_type == "csv":
    csv_path = input("Enter path to CSV file: ")

    try:
        input_data = pd.read_csv(csv_path)
        if 'Sentence' not in input_data.columns:
            print("CSV file must contain 'Sentence' column")
        else:
            predictions = predict_pos(input_data)
            output_data = []

            for sentence, tags in predictions:
                output_data.append({'Sentence': sentence, 'Predicted_POS_Tags': ' '.join(tags)})
            output_df = pd.DataFrame(output_data)

            output_csv_path = '/content/CRFoutput.csv'
            output_df.to_csv(output_csv_path, index=False)
            print(f"Output is saved to {output_csv_path}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")

else:
    print("Invalid input. Please enter 'sentence' or 'csv'.")
