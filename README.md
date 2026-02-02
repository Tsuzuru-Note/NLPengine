# The TSUZURU NLP engine

[![Package CI](https://github.com/Tsuzuru-Note/NLPengine/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/Tsuzuru-Note/NLPengine/actions/workflows/python-package-conda.yml)

NLP engine repository for TSUZURU,
a reading-focused language learning service for foreign language learners.
> Our goal is...
>   
> Not to reduce translation,  
> but to reduce reading-time questions.

# Links
[Project summary](#project-summary)  
[Tech](#Tech)  
[API Specification](#API-Specification)  
[frontend](https://github.com/Tsuzuru-Note/Frontend)  
[backend](https://github.com/Tsuzuru-Note/BackEnd)

# Project summary

# API Specification
`POST /nlpengine/`
Analyze a Japanese text and return sentence-level NLP results.

# Tech
Python 3.10.19
FastAPI
Uvicorn
MeCab

Unix Domain Socket (UDS)

# Local Testing (Based Conda with Ubuntu 22.04)
```bash
# Install MeCab (System dependency)
$ sudo apt update
$ sudo apt install -y mecab libmecab-dev mecab-ipadic-utf8

$ mecab -D # If this command fails, then resolve the MeCab installation issue first.

# Install Python Dependencies
$ cd < Path of The Project's root >
$ conda create -n NLPengine python=3.10.19
$ conda activate NLPengine
$ pip install -r requirement.txt

# Test the NLPengine's basic functions 
$ python -m tests.nlpengine # For testing the Basic of the NLPengine
```


# Run the API Server (with. Unix Domain Socket)
Start the FastAPI server using Uvicorn with UDS:
```bash
uvicorn server:app \
  --uds /tmp/nlp_engine.sock
```

- `server:app` : Execuute FastAPI with server.py
- `--uds` : Bind server to UDS
