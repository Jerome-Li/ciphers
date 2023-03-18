from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/shift')
def shift():
    return render_template("shift.html")

@views.route('/mono')
def mono():
    return render_template("mono.html")

@views.route('/vigenere')
def vigenere():
    return render_template("vigenere.html")