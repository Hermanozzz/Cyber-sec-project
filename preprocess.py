import re

def clean_text(text):
    """
    Clean each email text for mails:
    - lowercase
    -replace URL's with token 'url'
    -replace email addresses with token 'email'
    -remove non-alphabetic characters (except for basic punctuation)
    """
    # Remove leading and trailing whitespace
    text = text.lower()
    
    text = re.sub(r"http\S+|www\.\S+", "url", text)
    text = re.sub(r'\S+@\S+', 'email', text)
    text =re.sub(r"\s+", " ", text).strip()  # Replace multiple spaces with a single space
    text = re.sub(r"[^a-zA-Z\s]","",text)
    
    return text