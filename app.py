from pymongo import MongoClient


client = MongoClient()
db = client.Playlister
playlists = db.playlists

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# OUR MOCK ARRAY OF PROJECTS
# app.py

# playlists = [
#   { 'title': 'Great Playlist' },
#   { 'title': 'Next Playlist' }
# ]

@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists.find())

@app.route('/playlists/new')
def playlists_new():
    """Get new playlists."""
    return render_template('playlists_new.html')

@app.route('/playlists', methods=['POST'])
def playlists_submit():
    """Submit a new playlist."""
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    playlists.insert_one(playlist)
    return redirect(url_for('playlists_index'))

if __name__ == '__main__':
    app.run(debug=True)
