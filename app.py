from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def main():
    # initialize the query editor with a simple query
    query_editor_text = """SELECT ?x WHERE {
    ?x a brick:
}"""
    return render_template('index.html', query_editor_text=query_editor_text)


@app.route("/query", methods=['POST', 'GET'])
def query():
    if request.method == 'POST':
        query_editor_text = request.form['query_editor_text']  # keep the query on editor
        query_result_text = request.form['query_editor_text']  # process query

    return render_template('index.html', query_editor_text=query_editor_text, query_result_text=query_result_text)


if __name__ == "__main__":
    app.run(host='localhost', port='5000', debug=True, use_reloader=TRUE)
