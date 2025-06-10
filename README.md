# MindEase - Your AI Mental Health Companion 🧠

A simple, offline-capable mental health support application that analyzes emotions and provides empathetic responses.

## Features
- 🎯 Real-time emotion detection
- 💡 Contextual supportive responses
- 🔒 Privacy-focused (works completely offline)
- 🎨 Clean, user-friendly interface

## Installation

1. Clone the repository:
```bash

cd mindease
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
streamlit run src/app.py
```

2. Open your browser at `http://localhost:8501`
3. Share your thoughts in the text area
4. Click "Analyze Emotion" to get insights and support

## Project Structure
```
mindease/
├── src/
│   ├── app.py               # Main Streamlit application
│   └── utils/
│       ├── emotion_detection.py  # Emotion analysis logic
│       └── responder.py          # Response generation
├── assets/
│   └── logo.png            # Application logo
└── requirements.txt        # Project dependencies
```

## Dependencies
- streamlit
- textblob
- pillow

## Development
- Python 3.8+
- Uses TextBlob for sentiment analysis
- Streamlit for the web interface

## Contributing
Feel free to open issues or submit pull requests for improvements.

## License
MIT License - Feel free to use this project as you wish.