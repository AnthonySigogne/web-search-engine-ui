#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
UI - a simple web search engine.
The goal is to index an infinite list of URLs (web pages), and then be able to quickly search relevant URLs against a query.

See https://github.com/AnthonySigogne/web-search-engine for more information.
"""

__author__ = "Anthony Sigogne"
__copyright__ = "Copyright 2017, Byprog"
__email__ = "anthony@byprog.com"
__license__ = "MIT"
__version__ = "1.0"

import os
import requests
from flask import Flask, request, jsonify, render_template

# init flask app and env variables
app = Flask(__name__)
host = os.getenv("HOST")
port = os.getenv("PORT")

@app.route("/", methods=['GET'])
def search():
    """
    URL : /
    Query engine to find a list of relevant URLs.
    Method : POST or GET (no query)
    Form data :
        - query : the search query
        - hits : the number of hits returned by query
        - start : the start of hits
    Return a template view with the list of relevant URLs.
    """
    # GET data
    query = request.args.get("query", None)
    start = request.args.get("start", 0, type=int)
    hits = request.args.get("hits", 10, type=int)
    if start < 0 or hits < 0 :
        return "Error, start or hits cannot be negative numbers"

    if query :
        # query search engine
        try :
            r = requests.post('http://%s:%s/search'%(host, port), data = {
                'query':query,
                'hits':hits,
                'start':start
            })
        except :
            return "Error, check your installation"

        # get data and compute range of results pages
        data = r.json()
        i = start/hits
        range_pages = range(i-5,i+5) if i >= 6 else range(0,10)

        # show the list of matching results
        return render_template('layout.html', query=query,
            response_time=r.elapsed.total_seconds(),
            total=data["total"],
            hits=hits,
            start=start,
            range_pages=range_pages,
            results=data["results"])

    # return homepage (no query)
    return render_template('layout-empty.html')
