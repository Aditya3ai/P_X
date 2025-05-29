from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)
DATA_FILE = 'data/couples.json'
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load existing data
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({"couples": []}, f)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Registration form
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

        # Save cover image
        cover = request.files['cover_image']
        filename = f"{groom}-{bride}-{cover.filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        cover.save(filepath)

        # Create slug and save data
        slug = f"{groom.lower()}-weds-{bride.lower()}"
        with open(DATA_FILE) as f:
            data = json.load(f)
        data['couples'].append({
            'slug': slug,
            'bride': bride,
            'groom': groom,
            'wedding_date': date,
            'city': city,
            'story': story,
            'cover_image': filename,
            'events': events
        })
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f)

        return redirect(url_for('invitation', slug=slug))
    return render_template('register.html')

# Invitation page
@app.route('/<slug>')
def invitation(slug):
    with open(DATA_FILE) as f:
        data = json.load(f)
    couple = next((c for c in data['couples'] if c['slug'] == slug), None)
    if not couple:
        return "Invitation not found.", 404
    return render_template('invitation.html', data=couple)

if __name__ == '__main__':
    app.run(debug=True)
