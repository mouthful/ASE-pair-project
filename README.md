# ASE
How is the frequency of English 26 letters distributed in a novel? What are the words that often appear in a type of article? What is the most common vocabulary of a author? What are the most commonly used phrases in Harry Potter, and so on. There are some programs to solve this problem.
## step0 *Outputs the frequency of the 26 letters in an English text file.*

### Usage:
    usage:main.py [-c] [-n <num>] <path>  
    -c:Count character occurrences. 统计字母频率  
    -n <num>: Output only the top <num> items. 只输出前n个item  (default: n=10)
    <path>: The path to the input file if -d is not specified. path是最后一个参数，在未给定文件夹时给定输入文件  
### examples:
    python wf.py -c gone_with_the_wind.txt
    python wf.py -c -6 gone_with_the_wind.txt
### output:
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
## step1 Output the top N most frequently occurring English words in a single file




