from flask import Flask, jsonify, request
from collections import Counter


app = Flask(__name__)


@app.route('/api/')
def main():
    str = request.args.get('name')

    length = len(str)
    stringLower= str.lower()
    makingSplit = stringLower.split()
    finalString = "".join(makingSplit)
    reverseString = ''.join(reversed(finalString))
    collection = Counter(stringLower)


    if finalString == reverseString:

        return jsonify(name=str,
                       palindrome=True,
                       length= length,
                       sorted= collection)
    else:
        return jsonify(name=str,
                       palindrome=False)


if __name__ == '__main__': 
    app.run(host="0.0.0.0", port=4000, debug=True)

