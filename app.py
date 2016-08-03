import os
from flask import Flask, request, Response, jsonify
import wikipedia
import json

app = Flask(__name__)

SLACKPEDIA_BOT_DEBUG = False


@app.route('/slackpedia', methods=['post'])
def slackpedia():
    query = request.values.get('text')
    result = get_query_result(query)
    
    #resp = jsonify(text="result", response_type="in_channel")
    #data = {"text": result, "response_type": "in_channel"}
    
    ret = {'text':result,'response_type':"in_channel"}
    data = json.dumps(ret)

    resp = Response(response=data,
                    status=200,
                    mimetype="application/json")

    #return Response(result, content_type='charset=utf-8; text/plain')
                #"text":"Partly cloudy today and tomorrow"
    return resp


def get_query_result(query):
    try:
        result = wikipedia.summary(query)
        return get_found_response(result)

    except wikipedia.exceptions.DisambiguationError as error:
        return get_suggested_response(error.options)

    except wikipedia.exceptions.PageError as error:
        return get_notfound_response(query)

    except wikipedia.exceptions.WikipediaException as error:
        return get_emptyquery_response()


def get_found_response(result):
    header_text = ":satisfied: Hey Bryan! <!channel>.\n {}"

    return header_text.format(result)


def get_suggested_response(options):
    header_text = ":grin: Hi Buddy! Sorry, but you must be a little more precise: \n{}"
    suggested_queries = get_suggested_options(options, 5)
    suggested_response = header_text.format(get_suggested_string(suggested_queries))

    return suggested_response


def get_notfound_response(query):
    header_text = ":sweat: Well, that's awkward. I couldn't find definition for: {}."

    return header_text.format(query)


def get_emptyquery_response():
    return "You must give me a term to search Wikipedia for!"


def get_suggested_options(result, max_length):
    return result[:max_length]


def get_suggested_string(query):
    suggested = ''

    for element in query:
        suggested += "\t{}\n".format(element)

    return suggested


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=SLACKPEDIA_BOT_DEBUG)
