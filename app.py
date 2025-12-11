from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple in-memory data storage (can be replaced with MongoDB later)
users = {}
medications = []
appointments = []


@app.route("/")
def index():
    return render_template("p.html")


# -------------------------
# USER SIGNUP
# -------------------------
@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    email = data["email"]
    password = data["password"]

    if email in users:
        return jsonify({"success": False, "message": "User already exists"})

    users[email] = password
    return jsonify({"success": True, "message": "Signup successful"})


# -------------------------
# USER LOGIN
# -------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data["email"]
    password = data["password"]

    if email not in users or users[email] != password:
        return jsonify({"success": False, "message": "Invalid email or password"})

    return jsonify({"success": True, "message": "Login successful"})


# -------------------------
# ADD MEDICATION
# -------------------------
@app.route("/add_medication", methods=["POST"])
def add_medication():
    data = request.json
    medications.append(data)
    return jsonify({"success": True, "message": "Medication added"})


# -------------------------
# GET ALL MEDICATIONS
# -------------------------
@app.route("/get_medications", methods=["GET"])
def get_medications():
    return jsonify({"success": True, "data": medications})


# -------------------------
# ADD APPOINTMENT
# -------------------------
@app.route("/add_appointment", methods=["POST"])
def add_appointment():
    data = request.json
    appointments.append(data)
    return jsonify({"success": True, "message": "Appointment added"})


# -------------------------
# GET ALL APPOINTMENTS
# -------------------------
@app.route("/get_appointments", methods=["GET"])
def get_appointments():
    return jsonify({"success": True, "data": appointments})


if __name__ == "__main__":
    app.run(debug=True)