import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
from preprocess import clean_text
from db import init_db

DATASET_PATH = "phishing_email.csv"
MODEL_PATH = "phishing_model.pkl"
VECTORIZER_PATH = "tfidf_vectorizer.pkl"

#processing the data and training the model
def train():
    df =pd.read_csv(DATASET_PATH)
    print("Columns in dataset:", df.columns.tolist())

    df = df.dropna(subset=["text_combined", "label"])
    df["clean_text"] = df["text_combined"].apply(clean_text)

    X = df["clean_text"]
    y = df["label"]

    # Splitting the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    vectorizer = TfidfVectorizer(max_features=5000, stop_words="english")
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    #Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    
    # Training the model
    model.fit(X_train_vec, y_train)

    y_pred = model.predict(X_test_vec)
    print("model accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred, target_names =["Not Phishing", "Phishing"]))

    # Save model and vectorizer
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)
    print(f"\nModel saved to {MODEL_PATH}")
    print(f"Vectorizer saved to {VECTORIZER_PATH}")

# Initalise database
if __name__ == "__main__":
    init_db()
    print("Database initialised.")
    train()
