"""
Flask server for emotion detection application that provides a web interface
for detecting emotions in text using the EmotionDetection library.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_analyzer():
    """
    Analyze the emotional content of provided text.
    Returns emotional analysis including anger, disgust, fear, joy, sadness scores
    and the dominant emotion.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    try:
        response = emotion_detector(text_to_analyse)
        if response is None or response['dominant_emotion'] is None:
            return "<strong>Invalid text! Please try again!</strong>"
        emotion_score = {
            'anger': response['anger'],
            'disgust': response['disgust'],
            'fear': response['fear'],
            'joy': response['joy'],
            'sadness': response['sadness'],
            'dominant_emotion': response['dominant_emotion']
        }
        # Split the long f-string into multiple parts for better readability
        emotion_response = (
            f"For the given statement, the system response is "
            f"'anger': {emotion_score['anger']}, "
            f"'disgust': {emotion_score['disgust']}, "
            f"'fear': {emotion_score['fear']}, "
            f"'joy': {emotion_score['joy']} and "
            f"'sadness': {emotion_score['sadness']}. "
            f"The dominant emotion is <strong>{emotion_score['dominant_emotion']}</strong>"
        )
        return emotion_response
    except KeyError as error:
        print(f"KeyError occurred: {error}")
        return "<strong>Invalid text! Please try again!</strong>"

@app.route("/")
def render_index_page():
    """Render the main page of the application."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
