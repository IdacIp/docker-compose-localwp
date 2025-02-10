from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

CSV_FILE = 'registration_data.csv'

@app.route('/receive_data', methods=['POST'])
def receive_data():
    """
    Receives registration data from the WordPress form and stores it in a CSV file.
    """
    try:
        data = request.get_json()  # Get JSON data from the request body
        name = data['name']
        age = data['age']
        gender = data['gender']
        email = data['email']

        # Append data to CSV
        with open('recieved_data.csv', 'a', newline='') as csvfile:
            fieldnames = ['Name', 'Age', 'Gender', 'Email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header if the file is empty
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        print(f"Received and stored data: {name}, {age}, {gender}, {email}")
        return jsonify({'message': 'Data received and stored successfully!'}), 200  # Return JSON response

    except Exception as e:
        print(f"Error processing data: {e}")
        return jsonify({'error': str(e)}), 500 # Return JSON formatted error with http code 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
