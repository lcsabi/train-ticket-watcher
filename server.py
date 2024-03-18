from flask import Flask, jsonify

import logger_config
import parser

app = Flask(__name__)


@app.route('/offers', methods=['GET'])
def get_offers():
    logger.info('Consumer called /offers endpoint')
    # Extract data from the third-party API
    data = parser.extract_data()
    print(data)
    if data:
        logger.info('Parsed data successfully forwarded to consumer')
        return jsonify(data), 200
    else:
        logger.error('No content could be forwarded to consumer')
        return None, 204


if __name__ == '__main__':
    logger = logger_config.setup_logger()
    app.run(debug=True)
