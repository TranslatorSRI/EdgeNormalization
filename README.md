[![Build Status](https://travis-ci.com/TranslatorIIPrototypes/EdgeNormalization.svg?branch=master)](https://travis-ci.com/TranslatorIIPrototypes/EdgeNormalization)

# EdgeNormalization

## Introduction

The [Biolink Model](https://biolink.github.io/biolink-model/) defines allowed predicates in the Translator ecosystem.  Ingesting data from arbitrary sources requires mapping predicates in those sources to Translator predicates.

The [Edge Normalization Service](https://edgenormalization-sri.renci.org/apidocs) can find predicates if they have an exact mapping in the model.  The EdgeNormalization service takes this a step further, and attempts to find the best match to a Biolink predicate, even if there is not an explicit mapping.

Most users will use the [public service](https://edgenormalization-sri.renci.org), but instructions for deploying a new instance are given below.

Examples of calling the service are given in the [examples notebook](documentation/EdgeNormalization.ipynb).

## Installation

Create a virtual environment and activate.
    
    python -m venv venv
    source venv/bin/activate

Install dependencies
    
    pip install -r requirements.txt
    
    
Run web server.

    python main.py --host 0.0.0.0 --port 8145 
    


## Docker 

Build image locally 
    
    docker build --tag edgenormalization .
    
#### Launch

    docker run -it \ 
        -p <port>:8145 \ 
        edgenormalization 

#### Usage

http://"host name or IP":"port"/apidocs
        
### Kubernetes 
Deployment files for Kubernetes are available in the \kubernetes directory.
        
