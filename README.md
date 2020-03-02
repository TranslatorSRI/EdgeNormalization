[![Build Status](https://travis-ci.com/TranslatorIIPrototypes/EdgeNormalization.svg?branch=master)](https://travis-ci.com/TranslatorIIPrototypes/EdgeNormalization)

# EdgeNormalization

A service for producing relationships compliant with the biolink model.

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
        
