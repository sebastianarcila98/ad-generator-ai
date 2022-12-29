import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        product_description = request.form["animal"]
        personality = request.form["personality"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(product_description, personality),
            temperature=0.3,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(product_description, personality):
    print('Personality >>>', personality,
          '\nProduct description >>>', product_description)
    return """Write a persuasive product description targeting someone who wants to {} based on the following product description:
    product description: {} 
    persuasive description: 
    """.format(
        personality, product_description
    )
