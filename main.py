from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace these values with your own
user_id = "john_doe_17091999"
college_email = "john@xyz.com"
college_roll_number = "ABCD123"

def find_highest_alphabet(data):
    alphabets = [char for char in data if char.isalpha()]
    if alphabets:
        return [max(alphabets, key=lambda x: x.lower())]
    else:
        return []

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        request_data = request.get_json()
        data = request_data.get("data", [])
        highest_alphabet = find_highest_alphabet(data)

        response = {
            "Status": "Success",
            "User ID": user_id,
            "College Email ID": college_email,
            "College Roll Number": college_roll_number,
            "Array for Numbers": [x for x in data if x.isdigit()],
            "Array for Alphabets": [x for x in data if x.isalpha()],
            "Highest Alphabet": highest_alphabet
        }

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
