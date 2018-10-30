# ASE
How is the frequency of English 26 letters distributed in a novel? What are the words that often appear in a type of article? What is the most common vocabulary of a author? What are the most commonly used phrases in Harry Potter, and so on. There are some programs to solve this problem.
## step0: *Outputs the frequency of the 26 letters in an English text file.*

### Usage:
   	python wf.py [-c] [-n <num>] <path> 
_____________________________________________ 
    -c:Count character occurrences.  
    -n <num>: Output only the top <num> items. (default: n=10)
    <path>: The path to the input file if -d is not specified. 
### Examples:
	cd step0
    python wf.py -c gone_with_the_wind.txt
    python wf.py -c -6 gone_with_the_wind.txt
### Output:
	File name:gone_with_the_wind.txt
	-------------------
	|   The Rank List   |
	|character|Frequency|
	|e        |12.70%   |
	|t        |8.96%    |
	|a        |8.16%    |
	|o        |7.30%    |
	|n        |6.94%    |
	|h        |6.81%    |
	|s        |6.32%    |
	|i        |6.08%    |
	|r        |5.89%    |
	|d        |4.82%    |
	-------------------
	Time Consuming:0.304344

	File name:gone_with_the_wind.txt
	-------------------
	|   The Rank List   |
	|character|Frequency|
	|e        |12.70%   |
	|t        |8.96%    |
	|a        |8.16%    |
	|o        |7.30%    |
	|n        |6.94%    |
	|h        |6.81%    |
	-------------------
	Time Consuming:0.177941
## step1: *Output the top N most frequently occurring English words in a single file*
### Usages:

	python wf.py -f <path> : Output all non-repeating words in the file  
	python wf.py -d <directory> : Specify the file directory ,and perform the same operation for each file in the directory  
	python wf.py -d -s <directory> :Recursively traverse all subdirectories under the directory
	python wf.py [-f|-d][-s][-n] : Output only the top <num> items. (default: n=10)
### Examples:
	cd step1  
	python wf.py -f gone_with_the_wind.txt
	python wf.py -d examples
	python wf.py -d -s examples
### Output:
	File name:gone_with_the_wind.txt
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |4.53%    |
	|and      |3.75%    |
	|to       |2.36%    |
	|of       |2.03%    |
	|she      |1.99%    |
	|her      |1.96%    |
	|a        |1.81%    |
	|in       |1.42%    |
	|was      |1.41%    |
	|i        |1.27%    |
	-------------------
	Time Consuming:0.783432
____________________________________________________
	File name:examples\gone_with_the_wind.txt
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |4.53%    |
	|and      |3.75%    |
	|to       |2.36%    |
	|of       |2.03%    |
	|she      |1.99%    |
	|her      |1.96%    |
	|a        |1.81%    |
	|in       |1.42%    |
	|was      |1.41%    |
	|i        |1.27%    |
	-------------------
	Time Consuming:0.359091
	File name:examples\The Count of Monte Cristo - Alexandre Dumas père.txt
	--------------------------
	|      The Rank List      |
	|words       |Frequency   |
	|the         |5.44%       |
	|to          |2.61%       |
	|and         |2.55%       |
	|of          |2.52%       |
	|a           |1.87%       |
	|i           |1.78%       |
	|you         |1.72%       |
	|he          |1.42%       |
	|in          |1.32%       |
	|that        |1.13%       |
	--------------------------
	Time Consuming:0.406497
	File name:examples\The Old Man and the Sea.txt
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |8.62%    |
	|and      |4.69%    |
	|he       |4.34%    |
	|of       |2.03%    |
	|i        |1.89%    |
	|it       |1.84%    |
	|to       |1.70%    |
	|his      |1.66%    |
	|was      |1.62%    |
	|a        |1.48%    |
	-------------------
	Time Consuming:0.026848
_____________________________________________
	File name:examples\gone_with_the_wind.txt
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |4.53%    |
	|and      |3.75%    |
	|to       |2.36%    |
	|of       |2.03%    |
	|she      |1.99%    |
	|her      |1.96%    |
	|a        |1.81%    |
	|in       |1.42%    |
	|was      |1.41%    |
	|i        |1.27%    |
	-------------------
	Time Consuming:0.382316
	File name:examples\The Count of Monte Cristo - Alexandre Dumas père.txt
	--------------------------
	|      The Rank List      |
	|words       |Frequency   |
	|the         |5.44%       |
	|to          |2.61%       |
	|and         |2.55%       |
	|of          |2.52%       |
	|a           |1.87%       |
	|i           |1.78%       |
	|you         |1.72%       |
	|he          |1.42%       |
	|in          |1.32%       |
	|that        |1.13%       |
	--------------------------
	Time Consuming:0.380621
	File name:examples\The Old Man and the Sea.txt
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |8.62%    |
	|and      |4.69%    |
	|he       |4.34%    |
	|of       |2.03%    |
	|i        |1.89%    |
	|it       |1.84%    |
	|to       |1.70%    |
	|his      |1.66%    |
	|was      |1.62%    |
	|a        |1.48%    |
	-------------------
	Time Consuming:0.020142
	File name:examples\sub_dir\The Odyssey - Homer.txt
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |4.45%    |
	|and      |4.08%    |
	|to       |2.54%    |
	|of       |2.46%    |
	|i        |1.55%    |
	|you      |1.54%    |
	|he       |1.48%    |
	|a        |1.46%    |
	|in       |1.30%    |
	|for      |1.05%    |
	-------------------
	Time Consuming:0.114352
	File name:examples\sub_dir\subsubdir\Jane Eyre(简·爱).txt
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |4.06%    |
	|i        |3.75%    |
	|and      |3.43%    |
	|to       |2.70%    |
	|a        |2.31%    |
	|of       |2.26%    |
	|you      |1.55%    |
	|in       |1.43%    |
	|was      |1.31%    |
	|it       |1.25%    |
	-------------------
	Time Consuming:0.168821
	File name:examples\sub_dir\subsubdir\The Further Adventures of Robinson Crusoe - Daniel Defoe.txt
	--------------------------
	|      The Rank List      |
	|words       |Frequency   |
	|the         |4.41%       |
	|and         |3.95%       |
	|to          |3.32%       |
	|of          |2.60%       |
	|i           |1.89%       |
	|they        |1.67%       |
	|a           |1.66%       |
	|that        |1.57%       |
	|in          |1.54%       |
	|was         |1.26%       |
	--------------------------
	Time Consuming:0.081468

## step2: *Meet the requirement--stop words*
### Usages: 
    python wf.py -x <stopwordfile> -f <file> :Skip these words when counting frequencies
### Examples:
	cd step2
	python wf.py -x stopword.txt -f gone_with_the_wind.txt
### Output:
	File name:gone_with_the_wind.txt
	--------------------------
	|      The Rank List      |
	|words       |Frequency   |
	|a           |1.81%       |
	|in          |1.42%       |
	|was         |1.41%       |
	|i           |1.27%       |
	|you         |1.24%       |
	|he          |1.16%       |
	|that        |1.08%       |
	|had         |1.06%       |
	|it          |1.06%       |
	|s           |0.89%       |
	--------------------------
	Time Consuming:0.496648
## step3: *Find the phrase that appears most frequently*
### Usage:
	python wf.py -p <number> <path>: <number>--parameter  indicates the phrase consisting of how many words,   
	<path>-- parameter is filename or directory 
### Example:
	cd step3  
	python wf.py -p -2 gone_with_the_wind.txt  

### Output:
	File name:gone_with_the_wind.txt
	---------------------------------------------
	|               The Rank List               |
	|Phrases              |Frequency            |
	|of the               |0.48%                |
	|in the               |0.47%                |
	|and the              |0.32%                |
	|she had              |0.30%                |
	|to the               |0.23%                |
	|it was               |0.22%                |
	|she was              |0.21%                |
	|on the               |0.21%                |
	|he was               |0.18%                |
	|and she              |0.18%                |
	---------------------------------------------
	Time Consuming:1.394913
## step4: *Put the verbs into their prototypes, then count the frequencies*
### Usage:
    python wf.py -p <num> -v <verb file> <path>
### Example:
	cd step4
	python wf.py -p 2 -v verbs.txt
### Output:
	File name:gone_with_the_wind.txt
	----------------------------------------------------
	|                  The Rank List                  |
	|Phrases                 |Frequency               |
	|she have                |0.85%                   |
	|have be                 |0.72%                   |
	|it be                   |0.69%                   |
	|she be                  |0.65%                   |
	|be a                    |0.63%                   |
	|there be                |0.58%                   |
	|he be                   |0.57%                   |
	|do not                  |0.45%                   |
	|to be                   |0.45%                   |
	|go to                   |0.45%                   |
	----------------------------------------------------
	Time Consuming:1.676186
## step5: *Counting "Verb Phrases"*
The definition of "Verb Phrases" is as follows:

	VerbPhrase := Verb + Spaces + Preposition
	Spaces := Space+
	Space := ' ' | '\t' | '\r' | '\n'
	Preposition := <any one from the list of prepositions>
	Verb := <any one in any tense FROM THE DICTIONARY>
### Usage:
    python wf.py -q <preposition-list> -v <verb-dict> <path>
### Example:

    python main.py -q prepositions.txt -v verbs.txt gone_with_the_wind.txt
### Output:
	File name:gone_with_the_wind.txt
	----------------------------------------------------
	|                  The Rank List                  |
	|VerbPre                 |Frequency               |
	|go to                   |0.45%                   |
	|want to                 |0.27%                   |
	|be in                   |0.25%                   |
	|think of                |0.23%                   |
	|try to                  |0.23%                   |
	|have to                 |0.23%                   |
	|look at                 |0.17%                   |
	|come to                 |0.16%                   |
	|back to                 |0.11%                   |
	|be as                   |0.11%                   |
	----------------------------------------------------
	Time Consuming:1.449712












