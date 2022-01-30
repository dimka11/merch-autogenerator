from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

mod = Blueprint('simple-page', __name__, template_folder='templates/')


@mod.route('/')
def home():
    return render_template("base.html")


@mod.route('/main')
def main():
    return render_template("main-page.html")
