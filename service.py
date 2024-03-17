from flask import Flask, jsonify, request

from recommender import extract_keywords, recommend_job_role

app = Flask(__name__)


@app.route('/', methods=['POST'])
def recommend():
    args = request.args

    keywords = extract_keywords(args.get('text'))

    recommendation = recommend_job_role(keywords)

    return jsonify(
        {
            'keywords': f'{keywords}',
            'text': f'{recommendation}'
        })


@app.route('/', methods=['GET'])
def hello():
    return '<h2>Recommender</h2>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=65535)
