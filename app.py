from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles requests to the main page.
    GET: Renders the initial page.
    POST: Processes form submission and renders the page with the result.
    """
    submitted_text = ""  # Variable to hold the text submitted by the user
    display_result = ""  # Variable to hold the formatted text to display

    if request.method == 'POST':
        # Get the text from the form field named 'user_text'
        submitted_text = request.form.get('user_text', '') # Use get with default ''
        if submitted_text: # Only format if text was actually entered
            display_result = f"You entered: {submitted_text}"
        # Keep submitted_text to repopulate the input field if desired

    # Render the HTML template, passing the variables to it
    # 'current_input' will repopulate the text box
    # 'result' will display the message below the form
    return render_template('index.html', current_input=submitted_text, result=display_result)

if __name__ == '__main__':
    # Run the app in debug mode (for development)
    # host='0.0.0.0' makes it accessible on your network/Replit
    # port=8080 is a common alternative port
    app.run(debug=True, host='0.0.0.0', port=8080)