from wsgiref.simple_server import make_server
from my_framework.main import API
from my_framework.templator import render
from datetime import date
from urls import get_weather


app = API()


@app.route("/")
def home(request, response):
    response.text = render(
        "index.html",
        date=str(date.today()),
        weather=str(get_weather()),
    )


@app.route("/examples")
def examples(request, response):
    response.text = render("examples.html")


@app.route("/contact")
def contact(request, response):
    response.text = render("contact.html")


@app.route("/page")
def page(request, response):
    response.text = render("page.html")


@app.route("/another_page")
def another_page(request, response):
    response.text = render(
        "another_page.html",
        solid=app.solid,
        kiss=app.kiss,
    )


with make_server("", 8080, app) as httpd:
    print("RUN port 8080...")
    print("link to it: http://127.0.0.1:8080/ ")
    httpd.serve_forever()
