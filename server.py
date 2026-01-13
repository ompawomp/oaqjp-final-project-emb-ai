'''import needed components from the flask library'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)
@app.route("/emotionDetector")
def emotion_analysis():
    '''Retrieve text, pass to emotion_detector() and return output'''
    text_to_analyze = request.args.get('textToAnalyze', '')
    emotion_result = emotion_detector(text_to_analyze)
    anger = emotion_result['anger']
    disgust = emotion_result['disgust']
    fear = emotion_result['fear']
    joy = emotion_result['joy']
    sadness = emotion_result['sadness']
    dominant_emotion = emotion_result['dominant_emotion']
    if dominant_emotion is None:
        return(
            "Invalid text! Please try again!"
        )
    return (
        f"For the given statement, the system response is 'anger': {anger}, \
        'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. \
        The dominant emotion is {dominant_emotion}.")
@app.route("/")
def render_index_page():
    '''generates HTML based on dynamic input and index.html'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
