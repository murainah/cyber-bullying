from flask import Flask, request, render_template
import pickle


# Create flask app
flask_app = Flask(__name__)

# Importing our model
model = pickle.load(open("cyber_bully.pkl", "rb"))


@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    tweet = request.form.values()
    prediction = model.predict(tweet)

    if prediction == ['not_cyberbullying']:
        prediction = "this text is not cyberbullying".upper()
    elif prediction == ['relegion']:
        prediction = "this text has been flagged as an religious cyberbullying".upper()
    elif prediction == ['age']:
        prediction = "this text has been flagged as an age cyberbullying".upper()
    elif prediction==['ethnicity']:
        prediction="this text has been flagged as an Ethnicity cyberbullying".upper()
    if request is None:
        return render_template("index.html")
    else:
        return render_template("index.html",text = request.get_data(), prediction_text = prediction)







if __name__ == "__main__":
    flask_app.run(debug=True)