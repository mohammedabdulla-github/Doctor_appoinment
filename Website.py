from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# Create a list of doctors
doctors = ["Dr. Mohammed", "Dr. Srikaanth", "Dr. Sabari", "Dr. Sri"]

# Create a list of appointment times
times = ["9:00 AM", "10:00 AM", "11:00 AM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM"]

# Create a dictionary to store appointments
appointments = {}


# Define the home page route
@app.route('/')
def home():
    return render_template('home.html', doctors=doctors, times=times)


# Define the appointment submission route
@app.route('/submit', methods=['POST'])
def submit():
    # Get the form data
    doctor = request.form['doctor']
    time = request.form['time']
    name = request.form['name']
    phone = request.form['phone']

    # Check if the appointment time is already taken
    if time in appointments.keys():
        for appt in appointments[time]:
            if appt['doctor'] == doctor:
                return render_template('error.html', message=doctor +" is already assigned to this appointment time. Please choose another doctor or time.")
    else:
        appointments[time] = []

    # Add the appointment to the dictionary
    appointments[time].append({'doctor': doctor, 'name': name, 'phone': phone})

    # Display the confirmation page
    return render_template('confirmation.html', time=time, doctor=doctor, name=name, phone=phone)


# Define the appointments page route
@app.route('/appointments')
def appointments_page():
    return render_template('appointments.html', appointments=appointments)


if __name__ == '__main__':
    app.run(debug=True)
