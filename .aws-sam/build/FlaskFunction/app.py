from flask import Flask, render_template, request, jsonify, make_response
import random
from flask_cors import CORS

# Initialize the Flask application
app = Flask(
    __name__,
    template_folder="frontend_build",
    static_folder="frontend_build/static"
    )
CORS(app)

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
        f"Destiny whispers your name, {name}, carried on the wind of stars.",
        f"{name}, the energies align in curious ways around you today.",
        f"Let us peer into the mists of time and possibility, {name}.",
        f"{name}, your life is a symphony — let’s see what notes the future will play next.",
        f"The stars murmur secrets when your name is spoken, {name}. Let’s listen in.",
        f"Every heartbeat of yours echoes through the universe, {name}. Let’s trace where it leads.",
        f"{name}, I dusted off my crystal ball and it sneezed — something big is coming.",
        f"The stars were arguing about your destiny again, {name}. I had to step in.",
        f"{name}, the universe spilled tea about you today — want to hear it?",
        f"Hey {name}, ready to find out what life’s been plotting for you?",
        f"{name}, I’ve got some fascinating signals here with your name all over them.",        
        f"Shadows shift and symbols glow, {name} — something stirs beneath the surface.",
        f"{name}, your story is inked in invisible runes. Let’s decode what they say.",        
        f"{name}, every choice sends ripples across time. Let’s explore where yours are heading.",
        f"Fate may not be fixed, {name}, but it always leaves clues. Let’s examine a few.",        
        f"{name}, sometimes clarity starts with asking the right questions — let’s begin.",
    ]

    connections = [
        f"Your passion for {hobby} is not just a pastime; it's a source of creative energy that will fuel your future.",
        f"The skills you've gained as a {occupation} have built a solid foundation for what's to come.",
        f"The lesson learned from {negative_moment} has forged resilience in you, a quality essential for your destiny.",
        f"{positive_moment} wasn't just a happy time; it revealed your capacity to uplift others as well.",
        f"Every step you've taken as a {occupation} has been training for something greater — you're more prepared than you know.",
        f"The memory of {positive_moment} is a beacon, reminding you of your inner strength and potential for joy.",
        f"The shadow of {negative_moment} still lingers, but it's shaped your wisdom and sharpened your instincts.",
        f"In quiet moments spent with {hobby}, you connect with a deeper part of yourself that guides your decisions.",
        f"As {occupation}, you've developed insights that others often overlook — this will set you apart.",
        f"{negative_moment} was more than hardship — it was the universe's way of tempering your spirit for a greater role.",
        f"Your love for {hobby} adds color to your days and gives you a spark that others can feel around you.",
        f"Being a {occupation} has taught you more than tasks — it's taught you how to lead, listen, and grow.",
        f"{positive_moment} still makes your heart smile — don’t forget how capable of joy and presence you really are.",
        f"You've been through {negative_moment}, and yet you’ve come out more grounded, more you. That’s worth more than gold.",
        f"There’s a quiet wisdom in your journey through {negative_moment} — it whispers truth in every decision you make now.",
        f"Your time spent with {hobby} isn't random — it’s where your soul stretches, dreams, and finds its way home.",
    ]


    predictions = [
        f"I see a significant opportunity arising in the next 2-3 years directly related to your ambition of becoming a {future_goal}. Your experience with {hobby} will be the key to unlocking it.",
        f"Your path towards becoming a {future_goal} will be accelerated by an unexpected mentor you'll meet through a circle related to your current work as a {occupation}.",
        f"A challenge reminiscent of your {negative_moment} will appear, but this time, drawing strength from your {positive_moment}, you will turn it into a stepping stone for your dream of being a {future_goal}.",
        f"The passion you’ve shown in {hobby} will evolve into a unique skill set, catching the attention of someone influential in your journey toward becoming a {future_goal}.",
        f"As a {occupation}, your daily grind hides a spark—soon, that spark will ignite a bold step forward toward your {future_goal}.",
        f"An echo from your past, tied to {positive_moment}, will unexpectedly open a door leading you closer to your goal of becoming a {future_goal}.",
        f"There will be a moment — quiet, almost unnoticeable — when your {hobby} aligns with your purpose. That moment will be the seed of your future as a {future_goal}.",
        f"An inner restlessness you've felt lately is not discomfort — it's a sign of growth. You're being gently pushed toward your next chapter as a {future_goal}.",
        f"During a time when others doubt you, your belief in yourself — strengthened by your journey through {negative_moment} — will be what sets you apart as a future {future_goal}.",
        f"Your {positive_moment} wasn't just a memory; it was a glimpse of who you’re becoming. Let that light guide you forward to your role as a {future_goal}.",
        f"Through the lens of {hobby}, you’ll begin to see the world — and yourself — differently. That shift in vision will shape your rise toward becoming a {future_goal}.",
        f"The universe will soon place a choice before you. Choosing with courage — even if it's uncomfortable — will lead directly to your emergence as a {future_goal}.",
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

    if "how" in question or "what should i do" in question or "steps" in question or "plan" in question:
        return f"To get there, focus on consistency. Dedicate small, regular amounts of time to both your {hobby} and skills related to becoming a {future_goal}. The path reveals itself to those who walk it."
    
    elif "when" in question or "timeline" in question or "soon" in question or "time frame" in question:
        return "The exact timing is fluid and depends on your actions. The key events are not tied to a calendar but to your readiness. Stay prepared."

    elif "doubt" in question or "sure" in question or "really" in question or "possible" in question or "believe" in question:
        return "It's natural to have doubts. But the energies surrounding your past experiences and future hopes are strong. Trust in the journey and your own resilience."
    
    elif "thank you" in question or "thanks" in question or "grateful" in question:
        return "You are most welcome. May your path be bright. The future is in your hands."

    elif "why" in question or "reason" in question or "meaning" in question:
        return "Sometimes the universe doesn't offer clear reasons, only nudges. Trust that your experiences are shaping you for a purpose, even if it's not fully visible yet."

    elif "who" in question or "guide" in question or "mentor" in question or "help" in question:
        return "Guides appear when you're ready. Stay open to advice from unexpected places — sometimes the most profound wisdom comes from humble sources."

    elif "afraid" in question or "fear" in question or "scared" in question:
        return "Fear is a sign you're near something meaningful. Breathe through it. Each step forward weakens fear's grip and strengthens your courage."

    elif "fail" in question or "failure" in question or "what if i can't" in question:
        return "Failure is part of the path, not the end of it. What matters is how you rise, learn, and continue. The dream remains within reach."

    elif "success" in question or "achieve" in question or "accomplish" in question:
        return "Success is built moment by moment. Celebrate small wins and stay focused — your commitment makes the outcome inevitable."

    elif "change" in question or "shift" in question or "transformation" in question:
        return "Change is not to be feared — it is the universe inviting you to grow. Embrace it gently, and you'll find your strength evolving too."

    elif "destiny" in question or "fate" in question or "future" in question:
        return f"Your destiny is not fixed; it's shaped by every choice. Your desire to become a {future_goal} is no coincidence — it’s a thread already woven into your path."

    else:
        return "That is a deep question. The answer lies within your own heart. Reflect on what your positive moments have taught you."



@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://future-predictor-frontend.s3-website-us-west-2.amazonaws.com'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,GET,POST'
    return response

# Optionally, handle OPTIONS requests for all routes
@app.route('/<path:path>', methods=['OPTIONS'])
def options_handler(path):
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = 'http://future-predictor-frontend.s3-website-us-west-2.amazonaws.com'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,GET,POST'
    return response, 200
    
# --- API Routes ---
@app.route("/")
def index():
    """Render the main chat page."""
    return render_template("index.html")

# Lambda handler for AWS Lambda deployments
def lambda_handler(event, context):
    import aws_lambda_wsgi
    return aws_lambda_wsgi.response(app, event, context)


@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        return '', 204
    data = request.get_json()
    # Replace this with your actual prediction logic
    prediction = generate_prediction(data)
    return jsonify({'answer': prediction})

@app.route('/ask', methods=['POST', 'OPTIONS'])
def ask():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = 'http://future-predictor-frontend.s3-website-us-west-2.amazonaws.com'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        return response

    data = request.get_json()
    question = data.get("question")
    details = data.get("details", {})
    answer = handle_question(question, details)

    response = jsonify({'answer': answer})
    response.headers['Access-Control-Allow-Origin'] = 'http://future-predictor-frontend.s3-website-us-west-2.amazonaws.com'
    return response

# --- Run the App ---
if __name__ == "__main__":
    app.run(debug=True)