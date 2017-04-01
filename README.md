# proj-api
This is the simplest possible API to interact with the UI (that will soon be commited) in [proj](https://github.com/mef79/proj/)

## Requirements
- Python 2.7
- Python's `pip` library
  - It might be installed with Python already - try just running the command `pip` to test
  - If that fails, [Pip Installation Guide](https://pip.pypa.io/en/stable/installing/)
- `virtualenv` ([Flask's documentation on `virtualenv`](http://flask.pocoo.org/docs/0.12/installation/) is my favorite)
- MongoDB ([Documentation](https://docs.mongodb.com/manual/installation/)), confirm installation by running `mongod`

## Starting the API
- Start Mongo with `mongod`
- From the project directory, create/activate a virtual environment (step-by-step instructions also in [Flask's `virtualenv` docs](http://flask.pocoo.org/docs/0.12/installation/))
- Install the project dependencies with `pip install -r requirements.txt`
- Start the API with `python app.py`
- Confirm that it is running by accessing [`http://localhost:5000/`](http://localhost:5000/)
- Use any REST client to make API calls (I use [Insomnia](https://insomnia.rest/))
