import sqlite3
from flask import Flask, render_template, request, jsonify, g

app = Flask(__name__) #Here we create the Flask app
DATABASE = 'skillswipe.db' # Database file

# --- Database Helper Functions ---
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row # Lets us access columns by name
    return db
# @ means "at application context teardown" and in python it is called a decorator, the use of decorators is to modify the behavior of functions or methods
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# --- Run this ONCE to create your tables ---
# In your terminal, type: flask --app app init-db
@app.cli.command('init-db')
def init_db_command():
    """Clear existing data and create new tables."""
    with sqlite3.connect(DATABASE) as db:
        with open('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
    print('Database initialized.')

# --- Create the "Main App" Route ---
@app.route('/')
def index():
    # This is the fake login
    # You will open: http://127.0.0.1:5000/?user=priya
    # And in another browser: http://127.0.0.1:5000/?user=rohan
    
    current_user_name = request.args.get('user')
    if not current_user_name:
        return "Please specify a user, e.g., ?user=priya or ?user=rohan", 400

    db = get_db()
    # Get the current user's details
    me = db.execute('SELECT * FROM users WHERE name = ?', (current_user_name,)).fetchone()
    
    # Get all OTHER users for swiping
    other_users = db.execute('SELECT * FROM users WHERE name != ?', (current_user_name,)).fetchall()

    return render_template('index.html', me=me, other_users=other_users)

# --- This is the "Brain" ---
@app.route('/swipe', methods=['POST']) 
def swipe():
    data = request.json
    my_id = data['my_id']
    their_id = data['their_id']
    direction = data['direction']

    if direction == 'right':
        db = get_db()
        # 1. Save our "like" to the database
        db.execute('INSERT INTO swipes (liker_id, liked_id) VALUES (?, ?)', (my_id, their_id))
        db.commit()

        # 2. Check if THEY liked US
        match_check = db.execute(
            'SELECT * FROM swipes WHERE liker_id = ? AND liked_id = ?',
            (their_id, my_id)
        ).fetchone()

        if match_check:
            # IT'S A MATCH!
            their_name = db.execute('SELECT name FROM users WHERE id = ?', (their_id,)).fetchone()['name']
            return jsonify({'match': True, 'name': their_name})

    # No match
    return jsonify({'match': False})

if __name__ == '__main__':
    app.run(debug=True) # Runs the app