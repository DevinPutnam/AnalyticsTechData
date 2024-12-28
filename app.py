from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for Projects Page
@app.route('/projects')
def projects():
    return render_template('projects.html')  # Render a separate template for the Projects page

# Route for About Me Page
@app.route('/about_me')
def about_me():
    return render_template('about_me.html')  # Render a separate template for the About Me page

# Route for Request Data Analysis Page
@app.route('/request_data_analysis')
def request_data_analysis():
    return render_template('request_data_analysis.html')  # Render a separate template for Request Data Analysis page

# Route for Contact Us Page
@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')  # Render a separate template for Contact Us page

if __name__ == '__main__':
    app.run(debug=True)
