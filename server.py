"""Flask server for the Emotion Detection application."""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """Detect emotions from user input."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


@app.route("/")
def home():
    """Display the application home page."""
    return """
    <h1>Emotion Detection Application</h1>
    <form action="/emotionDetector">
        <input name="textToAnalyze" placeholder="Enter text">
        <button type="submit">Analyze Emotion</button>
    </form>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
