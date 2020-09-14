## Application Code Description

This is the Smart Bot. It uses nltk to give replies to basic questions as per its user's requirement. It has a text to speech functionality as well. It has a smart audio analysis system where it can remove background noise and tell whether a person's area is suitable for video calls or not. Also it has a face detection and recognition branch as well where it can identify who is chatting with it...ofcourse with the user's content!!

Its still a work in progress.


## An overview of Code used
* Text To Summary: Using nltk and frequency based method for finding the summary  
    * create_dictionary_table: For creating the dictionary(frequenct table)
    * calculate_sentence_scores: Finding the scores of the sentence with the help of sentence and frequency table
    * calculate_average_score: Finding the average score
    * run_article_summary: Creating the summary with the help of threshold(average score) and the original text
  
* Summary To Audio: Using gtts and IPython for converting text to audio file

* Chatbot: Using nltk and stopwords for finding the keypoints
   * title.split(): For splitting the setence into words
   * PorterStemmer(): For finding the root word from the keywords
   * corpus.append(): storing the final keywords in the corpus
   



* Data sources
  * https://i.dell.com/sites/doccontent/shared-content/data-sheets/en/Documents/Dell_data_protection_cloud_edition__data_sheet_HR.pdf (data for text summary)
  * Laptop Testing Data from DELL(data for text summary)
  * https://www.codegrip.tech/(online code review)


## Audio analysis

Removes simple background noises like fast air passing on the mic, background music, generator noise, etc.
Also its capable of detecting if the background is suitable or not for voice calls (if noise level exceeds a certain threshold).

Reference
noisereduce 1.1.0 <https://pypi.org/project/noisereduce/>


# Face-Recognition
Identify and recognize the face

A simple model which Uses OpenCV, DNN and a trainer to detect faces and recognize them.

Run the first .py file so that its able to capture first 60 frames of the person's face as dataset.
Run the second .py file to train the model on this dataset.
Run the third file to recognize face using the web cam.

I just used DNN face detectinon model instead of the haar cascades he used to detect faces for faster better results. Also I tweeked some settings.

THE LINK TO THE ORIGINAL Article by Marcelo
:https://towardsdatascience.com/real-time-face-recognition-an-end-to-end-project-b738bb0f7348


