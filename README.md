# The TSUZURU NLP engine
NLP engine repository for TSUZURU,
a reading-focused language learning service for foreign language learners.
> Our goal is...
>   
> Not to reduce translation,  
> but to reduce reading-time questions.

# Links
[Project summary](#project-summary)  
[Tech](#Tech)

[frontend](https://github.com/Tsuzuru-Note/Frontend)  
[backend](https://github.com/Tsuzuru-Note/BackEnd)

# Project summary

# Tech
Python 3.10.19

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
$ python -m tests.nlpengine # For testing the Basic of the NLPengine
```
