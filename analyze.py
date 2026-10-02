import argparse
import joblib
from preprocess import clean_text
from db import init_db, save_analysis, save_phishing_attempt, get_stats
from train import MODEL_PATH, VECTORIZER_PATH

def load_model():
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    return model, vectorizer

def analyze_email(email_text, model, vectorizer):
    clean_email = clean_text(email_text)
    email_vector = vectorizer.transform([clean_email])
    prediction = model.predict(email_vector)[0]
    confidence = model.predict_proba(email_vector)[0].max()

    label = "Phishing" if prediction == 1 else "Not Phishing"
    print(f"Analysis Results:")
    print(f"Prediction: {label}, Confidence: {confidence:.2f}")

#storing the result in the database
    save_analysis(email_text, prediction, confidence)
    
    if prediction == 1:
        save_phishing_attempt(email_text, confidence)
        print("Phishing attempt detected and saved to the database.")
    
    return prediction, confidence

def main():
    parser = argparse.ArgumentParser(description="Analyze an email for phishing indicators.")
    parser.add_argument("email_text", type=str, help="The email text to analyze.")
    parser.add_argument("--stats", action="store_true", help="Display phishing statistics from the database.")
    args = parser.parse_args()

    init_db()

    if args.stats:
        stats = get_stats()
        print(f"Total analyses: {stats['total_analyses']}")
        print(f"Phishing attempts: {stats['phishing_attempts']}")
    else:
        model, vectorizer = load_model()
        analyze_email(args.email_text, model, vectorizer)

if __name__ == "__main__":
    main()