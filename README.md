# EdgeNormalization

A service for producing relationships compliant with the biolink model.

[![Build Status](https://travis-ci.com/TranslatorIIPrototypes/EdgeNormalization.svg?branch=master)](https://travis-ci.com/TranslatorIIPrototypes/EdgeNormalization)
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
    
Run

    docker run -it \ 
        -p <port>:8145 \ 
        edgenormalization 
        
