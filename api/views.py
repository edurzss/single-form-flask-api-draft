from flask import Blueprint, flash, redirect, render_template, request, url_for
from middleware import model_predict

router = Blueprint("app_router", __name__, template_folder="templates")

@router.route("/", methods=["GET", "POST"])
def index():
    """
    GET: Index endpoint renders frontend UI

    POST: Used in our frontend so we can upload data from the html form.
    After receiving data from the form, it calls our ML model to
    get and display prediction and probability.
    """
    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":

        if "first_name" not in request.form:
            flash("First name not in data")
            return redirect(request.url)

        data_dict = request.form.to_dict()
        prediction, probability = model_predict(data_dict)

        context = {
            "prediction": prediction,
            "probability": probability
        }

        # flash(data_dict)    # Flashes dictionary in frontend
        first_name = data_dict["first_name"]
        return render_template("index.html", context=context, name=first_name)


@router.route("/styles/<filename>")
def load_styles(filename):
    """
    Load source files for styling such as CSS files
    """
    return redirect(url_for("static", filename="styles/" + filename), code=301)