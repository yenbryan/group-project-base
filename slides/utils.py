from models import SlideDeck, Slide


def create_slide_deck():
    SlideDeck.objects.create(name="Welcome", week=1, order=0)
    SlideDeck.objects.create(name="Python Programs", week=1, order=1)
    SlideDeck.objects.create(name="Object-Oriented Python I", week=1, order=2)
    SlideDeck.objects.create(name="Object-Oriented Python II: Inheritance", week=1, order=3)
    SlideDeck.objects.create(name="Object-Oriented Python II: Methods", week=1, order=4)
    SlideDeck.objects.create(name="File Manipulation", week=2, order=0)
    SlideDeck.objects.create(name="Regex & CSV", week=2, order=1)
    SlideDeck.objects.create(name="Intro to DBs: Tables and Queries", week=2, order=2)
    SlideDeck.objects.create(name="Intro to DBs: Functions and Relationships", week=2, order=3)
    SlideDeck.objects.create(name="ORM: Intro to Models", week=2, order=4)
    SlideDeck.objects.create(name="ORM: Models and Relationships", week=2, order=5)
    SlideDeck.objects.create(name="Django Admin", week=2, order=6)
    SlideDeck.objects.create(name="Migrations", week=2, order=7)
    SlideDeck.objects.create(name="Introduction to Web Frameworks and Django URLS, views, and templates", week=2, order=8)
    SlideDeck.objects.create(name="Basic Django App: index, create, detail", week=2, order=9)
    SlideDeck.objects.create(name="Basic Django App: edit, delete", week=3, order=0)
    SlideDeck.objects.create(name="Django Forms", week=3, order=1)
    SlideDeck.objects.create(name="Django Templating: Logic, Filters, and Tags", week=3, order=2)
    SlideDeck.objects.create(name="Django Templating: Inheritance and Static Files", week=3, order=3)
    SlideDeck.objects.create(name="Users: Built-In Django Auth", week=3, order=4)
    SlideDeck.objects.create(name="Users: Customizing and Relationships", week=3, order=5)
    SlideDeck.objects.create(name="Lab: Django App", week=3, order=6)

