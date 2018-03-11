# Pitchfork-ML
Machine Learning applied to Pitchfork dataset using Natural Language Processing.

## Goal
Produce a mock Pitchfork Review as learned by our Machine Learning algo.

## Hypothesis
Our AI/Machine will produce a review by checking against the statistical data we accrue during review analysis so as to gauge accuracy.

## Data management process

### Data break down
  
  SD = Standard Deviation
  
  avg = average
  
  Paragraphs
  
  - We identify and break up each review by paragraphs
    - We will determine the SD of how many paragraphs are featured in each review
    - Determine avg number of each paragraphs per review
  
  Sentences
  
  - Identify the avg # of sentences per these identified paragraphs.
  - Identify the avg/SD # of sentences per review
  
  Words
   
   - avg number of words per sentence of each paragraph (excluding special marks)
   - Identify trends of the parts of speech used for every sentence (i.e., nouns, verbs, pronouns, etc.)
   
  Cleanup
  
  - We'll need to think about cleaning up the data for any superfluous content
    - Punctuation is one of them
    - Others have yet to be determined
    - Here's a helpful article on it: https://machinelearningmastery.com/clean-text-machine-learning-python/

### Storage
  Pickling
   - We're using the method of pickling to flatten the data for easier access since there's _a lot_ of it.

## Methods

### Algos
   
   - Mention of using Naive Bayes so far.
   - A more appropriate algo may be chosen upon further research
   
### ???
   
   - Who can say? Machine Learning is difficult work!
   
