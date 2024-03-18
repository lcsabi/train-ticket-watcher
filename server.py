from flask import Flask, jsonify

import parser

app = Flask(__name__)


@app.route('/offers', methods=['GET'])
def get_offers():
    # Call the function to extract data from the third-party API
    data = parser.extract_data()
    print(data)
    # Return the extracted data as JSON response
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
