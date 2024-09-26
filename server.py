from flask import Flask, request, jsonify, session
import db
import ai
import crypto
import os
import secrets
from ai import Difficulty

app = Flask(__name__)

# Check if the CCSecretKey environment variable is set, and if not, create and set it
if 'CCSecretKey' not in os.environ:
    # Generate a random secret key
    app.secret_key = secrets.token_hex(32)  # Generates a 64-character hex string (256-bit key)
    
    # Set the CCSecretKey environment variable
    os.environ['CCSecretKey'] = app.secret_key
else:
    # Retrieve the existing key from the environment
    app.secret_key = os.environ['CCSecretKey']

# Default route to index. Assume index file is in the static folder
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Request message to sign
@app.route('/login/request_message', methods=['POST'])
def request_login_message():
    address = request.json['address'].upper()
    user = db.get_user_by_address(address)

    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    message = crypto.generate_message()
    session['address'] = address
    session['message'] = message
    return jsonify({'message': message})

# Verify signature
@app.route('/login/verify', methods=['POST'])
def verify_login():
    signature = request.json['signature']
    message = session['message']

    account = crypto.extract_account(message, signature)
    user = db.get_user_by_address(session['address'])
    if account != user['address']:
        return jsonify({'error': 'Invalid signature'}), 400

    session['user_id'] = user['id']
    return jsonify({'message': 'Login successful'})

@app.route('/session_data', methods=['GET'])
def session_data():
    if 'user_id' in session:
        return jsonify({'user_id': session['user_id']})
    else:
        return jsonify({'user_id': None}), 401
    
# Registration
@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    email = request.json['email']
    address = request.json['address'].upper()

    user = db.get_user_by_address(address)
    if user is not None:
        return jsonify({'error': 'User already exists'}), 400

    db.add_user(username, email, address)
    return jsonify({'message': 'User registered successfully'})

# Get list of completed quizzes
@app.route('/quizzes/completed', methods=['GET'])
def get_quizes():
    id = session['user_id']
    if id is None:
        return jsonify({'error': 'User not found'}), 404
    quizes = db.get_quizes()
    return jsonify(quizes)

# Get active quiz if there is one
@app.route('/quizzes/active', methods=['GET'])
def get_active_quiz():
    id = session['user_id']
    if id is None:
        return jsonify({'error': 'User not found'}), 404
       
    quiz, history = db.get_active_quiz(id)
    # Check if the quiz date is expired
    if quiz and quiz['created_at'] + 600 < time.time():
        # Score quiz
        #score = ai.score_quiz(quiz['question'], quiz['difficulty'], history)
        #db.set_quiz_completed(quiz['id'], score)
        # Should return quiz and score
        return jsonify({'error': 'Quiz expired'}), 400
    return jsonify({'quiz': quiz, 'history': history})

# Get quiz details
@app.route('/quizzes/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    quiz = db.get_quiz(quiz_id)
    if quiz is None:
        return jsonify({'error': 'Quiz not found'}), 404
    return jsonify(quiz)

# Respond to quiz question
@app.route('/quizzes/continue', methods=['POST'])
def continue_quiz():
    id = session['user_id']
    if id is None:
        return jsonify({'error': 'User not found'}), 404
    
    message = request.json['message']
    # Get the active quiz
    quiz, history = db.get_active_quiz(id)
    if quiz is None:
        return jsonify({'error': 'No active quiz found'}), 404
    
    messages = []
    for entry in history:
        messages.append({"role": entry['role'], "content": entry['content']})
    messages.append({"role": "user", "content": message})

    response = ai.respond_to_student(quiz['question'], quiz['difficulty'], messages)
    db.update_quiz_history(quiz['id'], 'user', message)
    db.update_quiz_history(quiz['id'], 'assistant', response)
    # Check if the quiz is completed
    if ai.check_if_complete(quiz['question'], quiz['difficulty'], messages):
        print("Quiz is complete")
        # Set the active quiz to none.
        
    return jsonify(response)

# Start the quiz
@app.route('/quizzes/start', methods=['POST'])
def start_quiz():
    user_id = session['user_id']
    if user_id is None:
        return jsonify({'error': 'User not found'}), 404

    # Check if the user has an active quiz
    quiz, history = db.get_active_quiz(user_id)
    if quiz is not None:
        print("User already has an active quiz")
        return jsonify({'error': 'User already has an active quiz'}), 400    
    
    # Create a new quiz
    difficulty = request.json['difficulty']
    # Make sure the difficulty is valid
    if difficulty not in [Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD]:
        print(f"Invalid difficulty: {difficulty}")
        return jsonify({'error': 'Invalid difficulty'}), 400
    
    question = ai.generate_question(difficulty)
    quiz_id = db.create_quiz(user_id, question, difficulty)
    db.update_quiz_history(quiz_id, 'assistant', f"You have chosen {difficulty} difficulty level. The question to consider is as follows. {question}")
    return jsonify({'question': question, 'quiz_id': quiz_id})

if __name__ == '__main__':
    db.init_db()
    app.run(debug=True)
