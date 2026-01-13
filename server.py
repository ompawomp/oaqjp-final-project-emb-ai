from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)
@app.route("/emotionDetector")
def emotion_analysis():
    text_to_analyze = request.args.get('textToAnalyze', '')
    emotion_result = emotion_detector(text_to_analyze)
    anger = emotion_result['anger']
    disgust = emotion_result['disgust']
    fear = emotion_result['fear']
    joy = emotion_result['joy']
    sadness = emotion_result['sadness']
    dominant_emotion = emotion_result['dominant_emotion']
    return (
        f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}.")

         
@app.route("/")
    render_index_page():
    return render_template('index.html')

    _name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)