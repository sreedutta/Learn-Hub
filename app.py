
from flask import Flask, render_template

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Courses Route
@app.route('/courses')
def courses():
    return render_template('courses.html')

#Login Route
@app.route('/login')
def login_page():
    return render_template('login.html')

#view-course Route
@app.route('/view-course')
def view_course():
    return render_template('view-course.html')

#buy Route
@app.route('/buy')
def buy():
    return render_template('buy.html')

# Course Details Route
@app.route('/course-details')
def course_details():
    return render_template('course-details.html')

# Trainers Route
@app.route('/trainers')
def trainers():
    return render_template('trainers.html')

# Events Route
@app.route('/events')
def events():
    return render_template('events.html')

# Pricing Route
@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

# Contact Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Starter Page Route
@app.route('/starter-page')
def starter_page():
    return render_template('starter-page.html')

# New Folder Route
@app.route('/folder-name')
def folder_name():
    return render_template('folder-name/index.html')  # Adjust folder structure as necessary

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)