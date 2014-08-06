__author__ = 'kilimanjaro'


from flask import Flask, request, json, Response, jsonify

# adding the static_url_path = ''
app = Flask(__name__, static_url_path='')



# Define Custom Functions Here


# default route to load 'index.html'
@app.route('/')
def root():
    return app.send_static_file('index.html')


# Define and Implement Routes and Functions to Handle Form Submissions

@app.route('/form_submit', methods=['POST'])
def handle_form_submit():
    f_name = request.form['name']
    f_email = request.form['email_add']

    print "\t\t\t **** f_name = %s" % f_name

    json_return = ''

    #  Note: The Example below is just a demonstration on how to return a success or error message to your
    #         form input.  For your implementation, you will need to

    if f_name == 'bad_email':
        json_return = {'success': False, 'errors': {'email': 'Problem with email. Please update email and resubmit form.'}}
    elif f_name == 'fail':
        json_return = {'success': False, 'errors': {'message': 'Internal Error. Please resubmit form.'}}
    else:
        json_return = {'success': True, 'message':'Thank you ' + f_name + ' , we will contact you shortly'}


    return json.dumps(json_return)






if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')