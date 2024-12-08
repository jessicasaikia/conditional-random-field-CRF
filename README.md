# Conditional Random Field (CRF)
This repository implements a Conditional Random Field (CRF) model for performing Parts-of-Speech (POS) Tagging on Assamese-English code-mixed texts.

## Introduction to Parts-of-Speech (PoS) Tagging
PoS tagging is the process of identifying and labeling grammatical roles of words in texts, supporting applications like machine translation and sentiment analysis. While different languages may have their own PoS tags, I have used my own custom PoS tags for this model. The Table below defines the custom PoS tags used in this model-

![Table](https://github.com/jessicasaikia/hidden-markov-model-HMM/blob/main/Custom%20PoS%20tags%20Table.png)

## About Conditional Random Field (CRF)
The CRF is a type of probabilistic graphical model that is often applied in Natural Language Processing and computer vision tasks. CRFs can capture dependencies between words and handle sequential data thus making it adaptable to variations in mixed-language patterns. 

**Algorithm**:
1.	The model imports the libraries and reads the dataset.
2.	The CRF model is initialised using the suitable implementation such as sklearn-crfsuite.
3.	For each sentence in the training set, the features are extracted for each token based on the previously defined feature set.
4.	The feature sets and the corresponding POS tags are fed into the CRF model.
5.	The CRF model uses a log-linear model to predict the most likely sequence of POS tags given the sequence of input features. This is achieved by maximising the conditional log-likelihood.

## Where should you run this code?
I used Google Colab for this Model:
1. Create a new notebook (or file) on Google Colab.
2. Paste the code.
3. Upload your CSV dataset file to Google Colab.
4. Please make sure that you update the "path for the CSV" part of the code based on your CSV file name and file path.
5. Run the code.
6. The output will be displayed and saved as a different CSV file.

You can also VScode or any other platform (this code is just a python code):
1. In this case, you will have to make sure you have the necessary libraries installed and datasets loaded correctly.
2. Run the program for the output.

## Additional Notes from me
If you need any help or questions, feel free to reach out to me in the comments or via my socials. My socials are:
- Discord: jessicasaikia
- Instagram: jessicasaikiaa
- LinkedIn: jessicasaikia (www.linkedin.com/in/jessicasaikia-787a771b2)

Additionally, you can find the custom dictionaries that I have used in this project and the dataset in their respective repositories on my profile. Have fun coding and good luck! :D
