## Application Code Description

An overview of Code used
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
   
* Online Code Review Tools(CodeGrip): It is an automated code review tool
   * Allows the user to directly connect and import repositories from different platforms(GitHub,BitBucket)
   * One click to analyse all the code to find issues-bugs,smells etc.
   * Detailed Solution to the problems


* Data sources
  * https://i.dell.com/sites/doccontent/shared-content/data-sheets/en/Documents/Dell_data_protection_cloud_edition__data_sheet_HR.pdf (data for text summary)
  * Laptop Testing Data from DELL(data for text summary)
  * https://www.codegrip.tech/(online code review)
