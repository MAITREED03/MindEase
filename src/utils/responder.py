import random

RESPONSES = {
    "happy": [
        "I'm glad you're feeling positive! Keep embracing these good moments.",
        "Your happiness is contagious! Keep spreading that positive energy.",
        "It's wonderful to see you in such high spirits!"
    ],
    "neutral": [
        "You seem to be taking things in stride. That's a balanced approach.",
        "Sometimes a neutral perspective helps us see things clearly.",
        "Taking a measured approach can be very helpful."
    ],
    "sad": [
        "I hear you, and it's okay to feel this way. Things will get better.",
        "I'm here to listen. Remember that difficult times don't last forever.",
        "Take care of yourself during this time. Your feelings are valid."
    ],
    "angry": [
        "I understand your frustration. Let's take a deep breath together.",
        "Your feelings are valid. Would you like to talk more about what's bothering you?",
        "It's okay to feel angry. Take your time to process these emotions."
    ]
}

def generate_response(emotion):
    """Generate a supportive response based on detected emotion"""
    return random.choice(RESPONSES.get(emotion, [
        "I'm here to listen and support you.",
        "Thank you for sharing your feelings with me.",
        "Would you like to tell me more about how you're feeling?"
    ]))