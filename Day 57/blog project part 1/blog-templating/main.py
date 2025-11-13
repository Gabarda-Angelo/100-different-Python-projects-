from flask import Flask, render_template
from post import Post
import requests


app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template("index.html")

blog_post_list = []
@app.route("/")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    print(all_posts)
    for post in all_posts:
        blog_post = Post(post["id"],post["title"],post["subtitle"], post["body"])
        blog_post_list.append(blog_post)

    return render_template("index.html", posts=blog_post_list)

@app.route("/post/<int:num>")
def get_post(num):
    return render_template("post.html", posts=blog_post_list[int(num - 1)])

if __name__ == "__main__":
    app.run(debug=True)
