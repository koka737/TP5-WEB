from flask import Flask, render_template, redirect, request  
import movies  

app = Flask(__name__)  
db_path = './movies.json'  
movies_db = movies.MoviesDB(db_path)  

@app.route('/movie-details/<int:id>')  
def movie_details(id):  
    movie = movies_db.read(int(id))  
    return render_template('movie-details.html', movie=movie)  

@app.route('/')
def movie_list(): 
    movies=movies_db.list()
    return render_template('movie-list.html', movies=movies)

@app.route('/add-movie-form', methods=['GET'])
def add_movie_form():
    return render_template('add-movie-form.html')

@app.route('/add-movie', methods=['GET'])
def add_movie():
    
    title = request.args.get('title')
    year = request.args.get('year')
    actors = request.args.get('actors', '')
    plot = request.args.get('plot', '')
    poster = request.args.get('poster', '')
    
    movies_db.create(title, year, actors, plot, poster)
    movies_db.save(db_path)
    
    return redirect('/')  


@app.route('/edit-movie-form/<int:id>')
def edit_movie_form(id):
    movie = movies_db.read(id)
    return render_template('edit-movie-form.html', movie=movie)

@app.route('/edit-movie/<int:id>', methods=['GET'])
def edit_movie(id):
    title = request.args.get('title')
    year = request.args.get('year')
    actors = request.args.get('actors', '')
    plot = request.args.get('plot', '')
    poster = request.args.get('poster', '')
    
    movies_db.update(id, title, year, actors, plot, poster)
    movies_db.save(db_path)
    
    return redirect('/')



@app.route('/delete-movie-form/<int:id>')
def delete_movie_form(id):  
    movie = movies_db.read(id)
    return render_template('delete-movie-form.html', movie=movie)

@app.route('/delete-movie/<int:id>', methods=['GET'])
def delete_movie(id):
    movies_db.delete(id)
    movies_db.save(db_path)
    return redirect('/')
