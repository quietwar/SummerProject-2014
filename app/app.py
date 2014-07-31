__author__ = 'kilimanjaro'


from flask import Flask, request

# adding the static_url_path = ''
app = Flask(__name__, static_url_path='')



# Define Custom Functions Here


# default route to load 'index.html'
@app.route('/')
def root():
    return app.send_static_file('index.html')


# Define and Implement Routes and Functions to Handle Form Submissions





if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')