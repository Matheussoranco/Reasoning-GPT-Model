import re
import operator
from collections import defaultdict
from typing import List, Dict, Union
import spacy
from nltk.corpus import wordnet as wn
from sympy import symbols, Eq, solve, sqrt as sympy_sqrt, log as sympy_log

nlp = spacy.load("en_core_web_sm")
