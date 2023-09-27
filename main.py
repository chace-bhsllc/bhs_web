'''
This is the main file of the website.
'''
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
# Home page
@app.route('/')
def home():
    return render_template('index.html')
# Contact us page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process form submission
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Send email or save message to database
        return redirect(url_for('thank_you'))
    return render_template('contact.html')
# Thank you page
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')
# IT tools page
@app.route('/it-tools')
def it_tools():
    return render_template('it_tools.html')
# DIY page
@app.route('/diy', methods=['GET', 'POST'])
def diy():
    if request.method == 'POST':
        # Process form submission
        username = request.form['username']
        password = request.form['password']
        # Validate username and password
        if username == 'admin' and password == 'password':
            # Redirect to DIY content page
            return redirect(url_for('diy_content'))
        else:
            # Show error message
            error_message = 'Invalid username or password'
            return render_template('diy.html', error_message=error_message)
    return render_template('diy.html')
# DIY content page
@app.route('/diy/content')
def diy_content():
    return render_template('diy_content.html')
if __name__ == '__main__':
    app.run(debug=True)