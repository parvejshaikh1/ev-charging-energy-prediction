from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('ev_charging.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            port INTEGER,
            latitude REAL,
            longitude REAL,
            duration INTEGER,
            charging_time INTEGER,
            predicted_energy REAL
        )
    ''')
    conn.commit()
    conn.close()

def predict_energy(port, lat, lon, duration, charging_time):
    # Dummy prediction formula - replace with your actual model prediction code
    predicted = round((charging_time / 3600) * 2.5, 2)
    return predicted

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        port = int(request.form['port'])
        lat = float(request.form['lat'])
        lon = float(request.form['lon'])
        duration = int(request.form['duration'])
        charging_time = int(request.form['charging'])

        predicted_energy = predict_energy(port, lat, lon, duration, charging_time)

        conn = sqlite3.connect('ev_charging.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO predictions (port, latitude, longitude, duration, charging_time, predicted_energy)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (port, lat, lon, duration, charging_time, predicted_energy))
        conn.commit()
        conn.close()

        prediction_text = f"⚡ Predicted Energy (kWh): {predicted_energy}"
        return render_template('index.html', prediction_text=prediction_text)
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
