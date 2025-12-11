# 💊 MediSafe – Health & Medicine Tracking Web App

MediSafe is a smart and user-friendly web application designed to help users track their daily medications, manage appointments, and maintain essential health information.  
The project is built using **HTML, CSS, JavaScript (Frontend)** and **Flask (Backend)**.

---

## 🚀 Features

### 🔐 User Authentication  
- User Signup  
- User Login  
- Backend validation using Flask  

### 💊 Medication Tracking  
- Add new medications (name, dosage, time)  
- View list of stored medications  
- Data handled by Flask API  

### 📅 Appointment Management  
- Add doctor appointments  
- View scheduled appointments  
- Stored and retrieved via Flask routes  

### 📊 Clean User Dashboard  
- Easy navigation  
- Mobile-friendly UI  
- Organized card-based design  

---

## 🛠 Technologies Used

### **Frontend**
- HTML  
- CSS  
- JavaScript  

### **Backend**
- Python  
- Flask Framework  
- REST APIs  

### **Tools**
- VS Code  
- Chrome Browser  
- GitHub  

---

## 📡 API Endpoints (Flask)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/signup` | Registers a new user |
| POST | `/login` | Authenticates a user |
| POST | `/add_medication` | Adds a medication |
| GET  | `/get_medications` | Gets all medications |
| POST | `/add_appointment` | Stores an appointment |
| GET  | `/get_appointments` | Fetches all appointments |

---

## 📁 Project Structure

```
MediSafe/
│── app.py                    # Flask backend server
│── templates/
│     └── p.html              # Main HTML frontend
│── static/                   # Optional CSS/JS assets
│── README.md                 # Project documentation
```

---

## 🔧 How to Run the Project

### 1️⃣ Install dependencies  
```bash
pip install flask flask-cors
```

### 2️⃣ Start the Flask server  
```bash
python app.py
```

### 3️⃣ Open the app in browser  
```
http://127.0.0.1:5000/
```

---

## 🧠 How the Backend Works

- The frontend uses JavaScript `fetch()` to send data to Flask.
- Flask receives user input, processes it, and returns a JSON response.
- Login, signup, medication add, and appointment add are all handled through APIs.
- The UI updates automatically based on the backend response.

---

## 🚀 Future Enhancements

- Add database storage (MongoDB / MySQL)  
- Add notification reminders  
- Add health analytics/charts  
- Deploy to cloud hosting platforms  

---

## 👩‍💻 Developer

**Spoorthi M S**  
Health & Medicine Tracking Web Application  
Final Year Project  

---

⭐ *If you like this project, don’t forget to star the repository!*  
