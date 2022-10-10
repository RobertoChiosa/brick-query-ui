import rdflib
from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__, static_url_path='/static')


@app.route("/")
def main():
    # initialize the query editor with a simple query
    query_editor_text = """SELECT ?ahu ?sat  WHERE {
    ?ahu a brick:AHU .
  	?ahu  brick:hasPoint  ?sat .
  	?sat  a  brick:Supply_Air_Temperature_Sensor .
}"""
    return render_template('index.html', query_editor_text=query_editor_text)


@app.route("/query", methods=['POST', 'GET'])
def query():
    if request.method == 'POST':
        query_editor_text = request.form['query_editor_text']  # keep the query on editor

        g = rdflib.Graph()
        g.parse('brick-query-ui/static/ttl/dbc_brick_expanded.ttl', format='ttl')
        res = g.query(request.form['query_editor_text'])
        res_dict = [dict(item) for item in res.bindings]

        query_result_text = json.dumps(res_dict, indent=1)

    return render_template('index.html', query_editor_text=query_editor_text, query_result_text=query_result_text)


if __name__ == "__main__":
    app.run(host='localhost', port='5000', debug=True, use_reloader=TRUE)
