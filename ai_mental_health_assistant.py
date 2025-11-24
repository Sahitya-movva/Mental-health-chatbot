# mental_health_chatbot.py
# Mini & cute AI Mental Health Support Assistant
# NOTE: This is a simple educational prototype, not medical advice.

import re

# -----------------------------
# 1. EMOTION CLASSIFIER (RULE-BASED)
# -----------------------------
def classify_emotion(text: str) -> str:
    """
    Very simple keyword-based emotion classifier.
    In a bigger project, this can be replaced with a trained ML model.
    """
    text_l = text.lower()

    sad_words = ["sad", "lonely", "tired", "empty", "cry", "worthless", "hopeless"]
    stress_words = ["stressed", "stress", "overwhelmed", "pressure", "tension",
                    "exam", "deadlines", "workload", "too much work"]
    anxious_words = ["anxious", "anxiety", "worried", "worry", "scared",
                     "nervous", "panic", "overthinking", "afraid"]

    sad_score = sum(1 for w in sad_words if w in text_l)
    stress_score = sum(1 for w in stress_words if w in text_l)
    anxious_score = sum(1 for w in anxious_words if w in text_l)

    if sad_score == 0 and stress_score == 0 and anxious_score == 0:
        return "neutral"

    if sad_score >= stress_score and sad_score >= anxious_score:
        return "sad"
    elif stress_score >= sad_score and stress_score >= anxious_score:
        return "stressed"
    else:
        return "anxious"


# -----------------------------
# 2. RISK DETECTION
# -----------------------------
def detect_risk_level(text: str) -> str:
    """
    Simple keyword-based high-risk detection.
    If we detect dangerous phrases, we return 'high'.
    """
    text_l = text.lower()

    high_risk_patterns = [
        r"\bi want to die\b",
        r"\bkill myself\b",
        r"\bend my life\b",
        r"\bno reason to live\b",
        r"\bsuicide\b",
        r"\bi can’t do this anymore\b",
    ]

    for pattern in high_risk_patterns:
        if re.search(pattern, text_l):
            return "high"

    return "normal"


# -----------------------------
# 3. KNOWLEDGE BASE (SIMPLE RAG)
# -----------------------------
KB = {
    "sad": [
        "It’s okay to feel sad sometimes. Allow yourself to feel it without judging.",
        "Try talking to someone you trust or writing down your thoughts in a journal.",
        "Do one small thing you usually enjoy – music, a walk, drawing, anything gentle.",
    ],
    "stressed": [
        "Break your work into smaller tasks and focus on one thing at a time.",
        "Take short breaks, drink some water, and stretch your body a little.",
        "Make a simple to-do list and start with the easiest task first.",
    ],
    "anxious": [
        "Try a breathing exercise: inhale slowly for 4 seconds, hold for 4, exhale for 4.",
        "Focus on what you can do in the next 10 minutes instead of the whole future.",
        "Ground yourself: name 5 things you can see, 4 you can touch, 3 you can hear.",
    ],
    "neutral": [
        "Thanks for sharing. You can tell me more about how you feel if you want.",
        "Taking care of your mind is just as important as taking care of your body.",
    ],
}


def retrieve_tips(emotion: str) -> list:
    """
    Retrieve suggestions based on detected emotion.
    This is like a tiny RAG knowledge base by emotion category.
    """
    return KB.get(emotion, KB["neutral"])


# -----------------------------
# 4. RESPONSE GENERATOR
# -----------------------------
def generate_response(user_text: str, emotion: str, tips: list) -> str:
    """
    Build a friendly, empathetic reply using emotion + tips.
    This simulates an LLM-style natural response with templates.
    """
    intro_map = {
        "sad": "I’m really sorry that you’re feeling sad right now. 💙",
        "stressed": "It sounds like you’re feeling quite stressed. 😥",
        "anxious": "It seems like you’re feeling anxious or worried. 💭",
        "neutral": "Thank you for sharing that with me. 🌼",
    }

    intro = intro_map.get(emotion, intro_map["neutral"])

    tips_text = ""
    if tips:
        tips_text = "\nHere are a few gentle suggestions that might help:\n"
        for t in tips:
            tips_text += f"• {t}\n"

    closing = (
        "\nRemember, I’m just an AI assistant, not a professional. "
        "If these feelings stay for a long time or become very strong, "
        "please consider talking to a trusted person or a mental health professional."
    )

    return f"{intro}\n\n{tips_text}{closing}"


# -----------------------------
# 5. MAIN CHAT LOOP
# -----------------------------
def run_chatbot():
    print("╔════════════════════════════════════════════╗")
    print("║  AI Mental Health Support Assistant 💬     ║")
    print("╚════════════════════════════════════════════╝")
    print("Hi, I’m here to listen. You can type how you feel.")
    print("Type 'exit' anytime to stop.\n")

    while True:
        user_text = input("You: ").strip()
        if user_text.lower() in ("exit", "quit", "bye"):
            print("\nAI: Thank you for sharing with me. Take care of yourself 💙")
            break

        if not user_text:
            print("AI: You can type anything, even a small sentence. I’m listening. 🙂")
            continue

        # 1) Risk detection
        risk = detect_risk_level(user_text)
        if risk == "high":
            print(
                "\nAI: I’m really sorry that you’re feeling this way. 💔\n"
                "I’m not a professional, so I can’t handle emergencies.\n"
                "Please reach out to someone you trust or contact a local helpline\n"
                "or mental health professional as soon as possible. You deserve support.\n"
            )
            continue

        # 2) Emotion classification
        emotion = classify_emotion(user_text)

        # 3) Retrieve tips (knowledge base)
        tips = retrieve_tips(emotion)

        # 4) Generate final response
        reply = generate_response(user_text, emotion, tips)
        print("\nAI:")
        print(reply)
        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    run_chatbot()
