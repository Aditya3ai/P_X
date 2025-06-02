from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import json

app = Flask(__name__)

# Configure file upload folder
UPLOAD_FOLDER = 'static/images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# PostgreSQL connection string
# 🔑 Replace with your actual connection details
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://p_xdatabase_user:cDK4tqGkZvrZzEkd6sMX2POTI7QM32oc@dpg-d0uo473ipnbc73el9mjg-a.oregon-postgres.render.com:5432/p_xdatabase'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Couple model
class Couple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    bride = db.Column(db.String(100), nullable=False)
    groom = db.Column(db.String(100), nullable=False)
    wedding_date = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    story = db.Column(db.Text, nullable=True)
    cover_image = db.Column(db.String(255), nullable=True)
    events = db.Column(db.JSON, nullable=True)  # Stores list of event dicts

# Create tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        bride = request.form['bride']
        groom = request.form['groom']
        date = request.form['wedding_date']
        city = request.form['city']
        story = request.form.get('story', '')
        events = []
        for e in ['Haldi', 'Mehendi', 'Wedding']:
            edate = request.form.get(f'{e.lower()}_date')
            if edate:
                events.append({'name': e, 'date': edate})

        cover = request.files['cover_image']
        filename = f"{groom}-{bride}-{cover.filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        cover.save(filepath)

        slug = f"{groom.lower()}-weds-{bride.lower()}"

        # Save to database
        new_couple = Couple(
            slug=slug,
            bride=bride,
            groom=groom,
            wedding_date=date,
            city=city,
            story=story,
            cover_image=filename,
            events=events
        )
        db.session.add(new_couple)
        db.session.commit()

        return redirect(url_for('invitation', slug=slug))

    return render_template('register.html')

@app.route('/<slug>')
def invitation(slug):
    couple = Couple.query.filter_by(slug=slug).first()
    if not couple:
        return "Invitation not found.", 404

    # Convert events JSON to Python list if needed
    data = {
        'slug': couple.slug,
        'bride': couple.bride,
        'groom': couple.groom,
        'wedding_date': couple.wedding_date,
        'city': couple.city,
        'story': couple.story,
        'cover_image': couple.cover_image,
        'events': couple.events
    }

    return render_template('invitation.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
