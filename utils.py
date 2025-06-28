from textblob import TextBlob
import os

# ------------ Sentiment ------------ #
def analyze_sentiment(text: str) -> str:
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.05:
        return "Positive"
    elif polarity < -0.05:
        return "Negative"
    return "Neutral"

# ------------ Simple FAQ Demo ------------- #
FAQ_ANSWERS = {
    "pan download": (
        "You can download your e‑PAN by visiting the Income‑Tax portal "
        "https://www.incometax.gov.in/iec/foportal → ‘Instant e‑PAN’. "
        "Authenticate with Aadhaar OTP and download the PDF instantly."
    ),
    "aadhar update": (
        "Visit https://myaadhaar.uidai.gov.in → ‘Update Aadhaar Online’. "
        "Login with Aadhaar + OTP, upload supporting proof, pay ₹50 fee, "
        "and track status under ‘Update History’. For biometric changes, "
        "book an appointment at an Aadhaar Seva Kendra."
    ),
    "driving licence apply": (
        "Go to your state’s Sarathi portal (https://sarathi.parivahan.gov.in). "
        "Step‑1: Apply for Learner’s Licence, fill Form‑2, upload photo & signature, "
        "book LL test slot, and pay fee. Step‑2 (after 30 days): Apply for Driving Licence, "
        "upload Form‑4, book road‑test at RTO, and pay fee."
    ),
    "passport apply": (
        "Create an account on https://passportindia.gov.in, fill the online form, "
        "pay the fee, schedule an appointment at PSK/POPSK, and visit with originals. "
        "After police verification, the passport is dispatched by Speed Post."
    ),
}

def granite_generate(prompt: str) -> str:
    """Return FAQ answer if matched, else fallback message."""
    text = prompt.lower()
    for key, ans in FAQ_ANSWERS.items():
        if all(word in text for word in key.split()):
            return ans
    return (
        "I’m a demo assistant and don’t have that answer in my offline FAQ yet. "
        "Plug in an IBM Granite / Watson Assistant / OpenAI key in utils.py "
        "to get fully AI‑generated answers."
    )
