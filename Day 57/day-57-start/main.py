from flask import Flask, render_template
from datetime import datetime
import requests

import random
app = Flask(__name__)


@app.route('/guess/<name>')
def home(name):
    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    age_response.raise_for_status()
    age_data = age_response.json()

    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    gender_response.raise_for_status()
    gender_data = gender_response.json()

    # Get the current year
    current_year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template(
        'index.html', num=random_number, year=current_year,person_gender = gender_data, person_age = age_data)
@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)


