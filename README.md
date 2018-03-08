# Pitchfork-ML
Machine Learning applied to Pitchfork dataset using Natural Language Processing.

## Goal
Produce a mock Pitchfork Review as learned my our Machine Learning algo.

## Data management process

### Data break down
  
  SD = Standard Deviation
  
  avg = average
  
  Paragraphs
  
  - We identify and break up each review by paragraphs
    - We will determine the SD of how many paragraphs are featured in each review
    - Determine average number of each paragraphs per review
  
  Sentences
  
  - Identify the avg # of sentences per these identified paragraphs.
  - Identify the avg/SD # of sentences
  
  Words
   
   - avg number of words per sentence of each paragraph (excluding special marks)
   - Identify trends of the parts of speech used for every sentence
   
  Cleanup
  
  - We'll need to think about cleaning up the data for any superflous content
    - Punctuation is one of them
    - Others have yet to be determined

### Stoage
  Pickling
   - We're using the method of pickling to flatten the data for easier access since there's _a lot_ of it.

## Methods

### Algos
   
   - Mention of using Naive Bayes so far.
   - A more appropriate algo may be chosen upon further researching the data
   
### ???
   
   - Who can say? Machine Learning is difficult work!
   
