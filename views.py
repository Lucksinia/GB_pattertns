"""
This one is deprecated in place of Flask-esque routing
"""
from my_framework.templator import render


class Index:
    def __call__(self, request):
        return "200 OK", render(
            "index.html",
            date=request.get("date", None),
            weather=request.get("weather", None),
        )


class About:
    def __call__(self, request):
        return "200 OK", render("examples.html")


class Contacts:
    def __call__(self, request):
        return "200 OK", render("contact.html")
