# Social Media Analysis based on COVID-19 with Sentiment Analysis, Named Entity Recognition and Information Extraction
This repository contains the social media data scraper and the notebooks of this analysis. Where we analise the Social Media posts - tweets with Sentiment Analysis then we analyse this results with Named Entity Recognition (NER) and Information Extraction methods to get a more accurate and detailed picture of this sentiment results.

### Excerpt from the diploma thesis and from the article, which was made from it.

### TextBlob

TextBlob is a powerful NLP library for Python that builds on NLTK and provides an easy-to-use interface to the NLTK library. With this tool, we can perform variety of NLP tasks, from tagging parts of speech to sentiment analysis, and from language translation to different text classifications, but we focus on sentiment analysis. TextBlob is a lexicon-based approach and offers two emotional metrics, polarity and subjectivity, it ignores the words that does not belongs to the lexicon and focuses only to the known words to produce a score for polarity and subjectivity measures. If we perform an sentiment analysis, we actually determine the polarity value of the sentences, where this value can be between -1 and 1. The data can then be labeled with the appropriate sentiment value (positive, negative, or neutral). Here, we have expanded the given scale for a more detailed result with ‘strongly positive and negative’ and ‘weakly positive and negative’ options, and also adjusted accordingly the polarity categories.

### Natural Language Toolkit (NLTK) - Valence Aware Dictionary and sEntiment Reasoner (VADER)

NLTK stands for Natural Language Toolkit. This toolkit is one of the most powerful NLP libraries which contains packages to make machines understand human language and reply to it with an appropriate response. Now, we use VADER  Lexicon and focus on sentiment analysis with the 'SentimentIntensityAnalyzer'. VADER (Valence Aware Dictionary and sEntiment Reasoner) is a part of the Natural Language Toolkit (NLTK) packages, it is a lexicon and rule based sentiment analysis tool commonly used to analyze the sentiments expressed in social media, but it works well on texts from other domains as well.
    
VADER takes into account the polarity and intensity of emotions expressed in context, and performs particularly well when analyzing unique characters used in tweets, such as emoticons or slang. This tool produces a compound score, which scales between -1 and +1 just like in TextBlob.

### Recurrent Neural Network (RNN)

When we talk about traditional neural networks, all outputs and inputs are independent of each other. But in the case of recurrent neural networks, the hidden layer on the previous run become part of the input to the same hidden layer in the next run.

What is Recurrent Neural Network (RNN) - A neural network that is intentionally run multiple times, where parts of each run feed into the next run. Specifically, hidden layers from the previous run provide part of the input to the same hidden layer in the next run. Recurrent neural networks are particularly useful for evaluating sequences, so that the hidden layers can learn from previous runs of the neural network on earlier parts of the sequence.

The ‘positive’, ‘neutral’, ‘negative’ labels were expanded in this case as well,just like in the previous models with ‘strongly positive and negative’ and with ‘weakly positive and negative’ labels. Furthermore, it should be mentioned, unlike the previous models, the sentiment value (predicted compound value) here scales between 0 and +1, instead of -1 and +1 values.

#### RNN Build

We have used tools provided by Keras and Tensorflow to build the model. Where we created a Sequential model by passing a list of layer instances. (A Sequential model is appropriate for a plain stack of layers where each layer has exactly one input tensor and one output tensor.) The first layer was the Embedding layer which, can be used for neural networks on text data. Embedding layer enables us to convert each word into a fixed length vector of defined size. It requires that the input data be integer encoded, so that each word is represented by a unique integer. Then we used Bidirectional layer, which is a wrapper for RNNs. We used LSTM layers with the Bidirectional layers. The Long Short-Term Memory (LSTM) is an RNN 'architecture', this networks are type of recurrent neural network, and capable of learning order dependence in sequence prediction problems. Next is the Dense and Dropout layers. A dense layer is a classic fully connected neural network layer, each input node is connected to each output node. A dropout layer is similar except that when the layer is used, the activations are set to zero for some random nodes. This is a way to prevent overfitting. We used a Dense layer with 'relu' activation, then a Dropout layer, and again a Dense layer with 'sigmoid' activation.

We also save our trained models in '.h5' format to reuse that, if we need to.

### Bidirectional Encoder Representations from Transformers (BERT)

Unlike traditional NLP models, which follow a one-way approach, i.e. reading the text from left to right or right to left, BERT reads the entire word sequence at once. BERT makes use of a Transformer, which is essentially a mechanism for building relationships between words in a dataset. In a simplest form, BERT consists two processing models - an encoder and a decoder. The encoder reads the input text and the decoder generates the predictions. However, since the main purpose of BERT is to create a pre-trained model, the encoder takes precedence over the decoder. BERT is a remarkable breakthrough in NLP.
