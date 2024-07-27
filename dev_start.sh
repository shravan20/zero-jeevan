# Execute this shell script after the setup instrcutions
# flask --app app --debug run

kill -9 $(lsof -ti :5000)
kill -9 $(lsof -ti :5000)
kill -9 $(lsof -ti :5000)
FLASK_APP=run.py FLASK_ENV=development flask run
