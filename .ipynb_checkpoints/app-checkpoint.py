{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5ef4a0d4-1dd9-47e3-bf3b-7d5e8d852961",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with watchdog (windowsapi)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template\n",
    "import numpy as np\n",
    "import pickle\n",
    "\n",
    "app = Flask(__name__)\n",
    "model = pickle.load(open(\"xgb_ev_model.pkl\", \"rb\"))\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    try:\n",
    "        features = [\n",
    "            float(request.form['port']),\n",
    "            float(request.form['lat']),\n",
    "            float(request.form['lon']),\n",
    "            float(request.form['duration']),\n",
    "            float(request.form['charging'])\n",
    "        ]\n",
    "        prediction = model.predict(np.array([features]))[0]\n",
    "        return render_template('index.html', prediction_text=f'Predicted Energy (kWh): {prediction:.2f}')\n",
    "    except Exception as e:\n",
    "        return render_template('index.html', prediction_text=f'Error: {e}')\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7af9399f-d6d9-4a08-9560-3412f4121fb0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3893c61-65e3-4a7b-8068-efa7121ddaaa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
