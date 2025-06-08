from flask import Flask, render_template, request, jsonify
import random

# Initialize the Flask application
app = Flask(__name__)

# --- Prediction Logic ---
def generate_prediction(details):
    """Generates a future prediction based on user details."""
    name = details.get('name', 'friend')
    hobby = details.get('hobby', 'something you enjoy')
    occupation = details.get('occupation', 'your current path')
    future_goal = details.get('future_goal', 'a noble ambition')
    positive_moment = details.get('positive_moment', 'a time of strength')
    negative_moment = details.get('negative_moment', 'a challenge you faced')

    # Templates for building the prediction
    openers = [
        f"Ah, {name}, the threads of fate are swirling around you.",
        f"{name}, your journey is a unique tapestry. Let's look at the patterns.",
        f"The cosmos has taken note of your story, {name}.",
    ]

    connections = [
        f"Your passion for {hobby} is not just a pastime; it's a source of creative energy that will fuel your future.",
        f"The skills you've gained as a {occupation} have built a solid foundation for what's to come.",
        f"The memory of {positive_moment} is a beacon, reminding you of your inner strength and potential for joy.",
        f"The lesson learned from {negative_moment} has forged resilience in you, a quality essential for your destiny.",
    ]

    predictions = [
        f"I see a significant opportunity arising in the next 2-3 years directly related to your ambition of becoming a {future_goal}. Your experience with {hobby} will be the key to unlocking it.",
        f"Your path towards becoming a {future_goal} will be accelerated by an unexpected mentor you'll meet through a circle related to your current work as a {occupation}.",
        f"A challenge reminiscent of your {negative_moment} will appear, but this time, drawing strength from your {positive_moment}, you will turn it into a stepping stone for your dream of being a {future_goal}.",
    ]
    
    # Shuffle to make it feel more random and unique
    random.shuffle(connections)

    # Combine the parts into a full prediction
    prediction = f"{random.choice(openers)} {connections[0]} {connections[1]} {random.choice(predictions)}"
    
    return prediction

def handle_question(question, details):
    """Handles follow-up questions."""
    question = question.lower()
    hobby = details.get('hobby', 'your passion')
    future_goal = details.get('future_goal', 'your goal')

    if "how" in question or "what should i do" in question:
        return f"To get there, focus on consistency. Dedicate small, regular amounts of time to both your {hobby} and skills related to becoming a {future_goal}. The path reveals itself to those who walk it."
    elif "when" in question:
        return "The exact timing is fluid and depends on your actions. The key events are not tied to a calendar but to your readiness. Stay prepared."
    elif "doubt" in question or "sure" in question or "really" in question:
        return "It's natural to have doubts. But the energies surrounding your past experiences and future hopes are strong. Trust in the journey and your own resilience."
    elif "thank you" in question or "thanks" in question:
        return "You are most welcome. May your path be bright. The future is in your hands."
    else:
        return "That is a deep question. The answer lies within your own heart. Reflect on what your positive moments have taught you."

# --- API Routes ---

@app.route("/")
def index():
    """Render the main chat page."""
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    """Receives user details and returns a prediction."""
    data = request.get_json()
    prediction_text = generate_prediction(data)
    return jsonify({"answer": prediction_text})

@app.route("/ask", methods=["POST"])
def ask():
    """Receives a follow-up question and returns a contextual answer."""
    data = request.get_json()
    question = data.get("question")
    details = data.get("details")
    answer_text = handle_question(question, details)
    return jsonify({"answer": answer_text})

# --- Run the App ---
if __name__ == "__main__":
    app.run(debug=True)