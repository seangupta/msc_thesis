# Master's Thesis Project: Combining Neural Reading Comprehension with Symbolic Reasoning

## Implementation using AllenNLP

Dataset reader: drop.py

Model: naqanet.py

Config file: naqanet.jsonnet

Pre-processing: find_number_distribution.py

Post-processing: prediction_processing.py

Sample shell script: untitled.job.sh


## Abstract from Master's thesis

Incorporating numerical reasoning into reading comprehension models is a challenging task at the forefront of current NLP research. Traditional systems have largely ignored this aspect and are hence not well suited to answer questions about natural language text that require an understanding of which numerical values tend to appear in what context, or that require performing symbolic operations over numbers such as adding, counting and sorting. This is a particular challenge in the newly-released DROP (Discrete Reasoning over Paragraphs) dataset. In this thesis, we investigate the application of the so-called Neural Accumulator (NAC) to the DROP dataset, which is a special kind of linear layer within a neural network. It is inductively biased towards sparsity and hence lends itself to performing arithmetic operations with raw numbers extracted from the paragraphs. We provide a quantitative and qualitative analysis of their performance, especially compared to other methods for symbolic reasoning.


