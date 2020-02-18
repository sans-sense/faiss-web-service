# Faiss Web Service

Fork of https://github.com/plippe/faiss-web-service.git.
Don't want PRs to interfere, so creating a new repo with similar code.

### Differences
Focus is not on docker but on running it locally. Renamed faiss_index.py to resolve module and file name problems. Made long() to int() for python 3.x

## To Run
### Setup
<pre>
conda install faiss-cpu -c pytorch
</pre>

### Start
Copy the default-faiss-service.ini to project root folder (same place as this readme.md), name it faiss-service.ini.  Copy the index and ids_vectors.p file from resources to the folders referenced in faiss-service.ini file.
<pre>
export PYTHON_PATH=$PYTHON_PATH:./src
python src/app.py
</pre>


### Healthcheck
<pre>
curl 'localhost:5000/ping'
</pre>

### Faiss search for ids 1, 2, and 3
<pre>
curl 'localhost:5000/faiss/search' -X POST -d '{"k": 5, "ids": [1, 2, 3]}'
</pre>
### Faiss search for a vector
<pre>
curl 'localhost:5000/faiss/search' -X POST -d '{"k": 5, "vectors": [[54.7, 0.3, 0.6, 0.4, 0.1, 0.7, 0.2, 0.0, 0.6, 0.5, 0.3, 0.2, 0.1, 0.9, 0.3, 0.6, 0.2, 0.9, 0.5, 0.0, 0.9, 0.1, 0.9, 0.1, 0.5, 0.5, 0.8, 0.8, 0.5, 0.2, 0.6, 0.2, 0.2, 0.7, 0.1, 0.7, 0.8, 0.2, 0.9, 0.0, 0.4, 0.4, 0.9, 0.0, 0.6, 0.4, 0.4, 0.6, 0.6, 0.2, 0.5, 0.0, 0.1, 0.6, 0.0, 0.0, 0.4, 0.7, 0.5, 0.7, 0.2, 0.5, 0.5, 0.7]]}'
```
</pre>

### Production
The application runs with Flask's build in server. Flask's documentation clearly states [it is not suitable for production](http://flask.pocoo.org/docs/1.1.x/deploying/).
