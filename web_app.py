# to handle the web server
from flask import Flask, render_template_string
#handles form data
from flask import request
#render_template_string
from flask import render_template

from main.data_loader import load_dataset
from main.llm_interface import ask_about_data

# Create a Flask web application instance
app = Flask(__name__)

# Define the home route (/) for both displaying the form and processing it
df = load_dataset()
@app.route('/', methods=['GET', 'POST'])
def index():
    question = ""
    answer = None

    # If the user submitted the form, process the question
    if request.method == 'POST':
        question = request.form['question'].strip()

        if question.lower() in ['exit', 'quit']:
            answer = "Thanks for using the app. Feel free to close the browser window."
        else:
            answer = ask_about_data(df, question)

    # a basic HTML form to display the answer if available
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ask the LLM</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 700px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            input[type="text"] {
                width: 100%;
                padding: 10px;
                font-size: 1rem;
                margin-top: 10px;
            }
            input[type="submit"] {
                padding: 10px 20px;
                font-size: 1rem;
                margin-top: 10px;
            }
            .answer {
                margin-top: 20px;
                padding: 15px;
                background-color: #fff;
                border-left: 4px solid #007BFF;
            }
        </style>
    </head>
    <body>
        <h1>Ask a question about the dataset</h1>
        <form method="post">
            <input type="text" name="question" placeholder="Type your question..." value="{{ question }}"/>
            <input type="submit" value="Ask"/>
        </form>

        {% if answer %}
        <div class="answer">
            <h2>LLM's Answer:</h2>
            <p>{{ answer }}</p>
        </div>
        {% endif %}
    </body>
    </html>
    """, answer=answer, question=question)

# Launch the web app if this script is run directly
if __name__ == '__main__':
    app.run(debug=True)