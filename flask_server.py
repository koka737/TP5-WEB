from flask import Flask, render_template  
import movies  

app = Flask(__name__)  
db_path = './movies.json'  
movies_db = movies.MoviesDB(db_path)  

@app.route('/movie-details/<id>')  
def movie_details(id):  
    movie = movies_db.read(int(id))  
    return render_template('movie-details.html', movie=movie)  

