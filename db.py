import sqlite3

def dict_factory(cursor, row):
    """Convert a row to a dictionary."""
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create Users Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT,
            address TEXT,
            active_quiz_id INTEGER
        );
    ''')

    # Create Quizzes Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quizzes (
            id INTEGER PRIMARY KEY, 
            question TEXT,
            difficulty TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed BOOLEAN DEFAULT FALSE,
            pass BOOLEAN
        );
    ''')

    # Create Quiz Messages Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz_messages (
            id INTEGER PRIMARY KEY, 
            quiz_id INTEGER,
            role TEXT,
            content TEXT,
            FOREIGN KEY (quiz_id) REFERENCES quizzes(id) ON DELETE CASCADE
        );
    ''')

    # Create Quiz Scoring Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz_scoring (
            id INTEGER PRIMARY KEY,
            quiz_id INTEGER,
            scoring TEXT,
            FOREIGN KEY (quiz_id) REFERENCES quizzes(id) ON DELETE CASCADE
        );
    ''')

    conn.commit()
    conn.close()

def get_user(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM users WHERE id = ?
    ''', (id,))

    user = cursor.fetchone()
    conn.close()

    return user

def get_user_by_address(address):
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, username, email, address FROM users WHERE address = ?
    ''', (address,))

    user = cursor.fetchone()
    conn.close()

    return user

def get_user_address(id):
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM users WHERE id = ?
    ''', (id,))

    user = cursor.fetchone()
    conn.close()

    return user

def add_user(username, email, address):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (username, email, address) VALUES (?, ?, ?)
    ''', (username, email, address))

    conn.commit()
    conn.close()

def update_email(id, email):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE users SET email = ? WHERE id = ?
    ''', (email, id))

    conn.commit()
    conn.close()

def update_address(id, address):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE users SET address = ? WHERE id = ?
    ''', (address, id))

    conn.commit()
    conn.close()

def get_quizes(id):
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM quizzes
    ''')

    quizzes = cursor.fetchall()
    conn.close()

    return quizzes

# Get the active quiz for the given user: does not work...
def get_active_quiz(id):
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    cursor.execute('''
        SELECT active_quiz_id FROM users WHERE id = ?
    ''', (id,))

    quiz_id = cursor.fetchone()
    
    cursor.execute('''
        SELECT * FROM quizzes WHERE id = ?
    ''', (quiz_id['active_quiz_id'],))

    quiz = cursor.fetchone()

    if quiz is None or quiz['completed']:
        conn.close()
        return None, None
    
    # Get the quiz history
    cursor.execute('''
        SELECT id, role, content FROM quiz_messages WHERE quiz_id = ?
    ''', (id,))
    messages = cursor.fetchall()

    conn.close()

    return quiz, messages

def set_active_quiz(id, quiz_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE users SET active_quiz_id = ? WHERE id = ?
    ''', (quiz_id, id))

    conn.commit()
    conn.close()

def set_quiz_completed(quiz_id, pass_quiz):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE quizzes SET completed = TRUE, pass = ? WHERE id = ?
    ''', (pass_quiz, quiz_id))

    conn.commit()
    conn.close()

def get_quiz_history(quiz_id):
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM quiz_messages WHERE quiz_id = ?
    ''', (quiz_id,))

    messages = cursor.fetchall()
    conn.close()

    return messages

def update_quiz_history(quiz_id, role, content):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    print(f'Updating quiz history: {quiz_id}, {role}, {content}')
    cursor.execute('''
        INSERT INTO quiz_messages (quiz_id, role, content) VALUES (?, ?, ?)
    ''', (quiz_id, role, content))

    conn.commit()
    conn.close()

# Create new quiz
def create_quiz(user_id, question, difficulty):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO quizzes (question, difficulty) VALUES (?, ?)
    ''', (question, difficulty))

    conn.commit()
    # Get the ID of the new quiz
    cursor.execute('''
        SELECT last_insert_rowid()
    ''')
    quiz_id = cursor.fetchone()

    cursor.execute('''
        UPDATE users SET active_quiz_id = ? WHERE id = ?
    ''', (quiz_id[0], user_id))

    conn.close()
    return quiz_id[0]