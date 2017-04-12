## Cracking Passwords with Recurrent Neural Networks

Among the many problems with account passwords today is the fact that they are often stored as hashes in databases which can be easily cracked using modern computing. One of the ways to test password strength is to build a **dictionary** of commonly used words and hash each one to find a match.

Inspired by other experiments in this field, I trained a **recurrent neural network** that learns how humans construct passwords. From this trained model, I was able to generate a new dictionary of potential passwords which successfully cracked real passwords from leaked hash databases.

See my [blog post](https://www.hasanhaq.com/pass-rnn/) for more information.

## Repository Details

There is no Jupyter notebook or single script to pull this project together. The analysis was done in a [torch-rnn](https://github.com/jcjohnson/torch-rnn) Docker container on an Ubuntu nVidia GPU instance. All the data used in the analysis are saved in this repo.

**Main Project**
* [Crackstation_Model.t7](Crackstation_Model.t7)
  * Torch7 recurrent neural network which can be loaded into torch-rnn to generate passwords
* [Sample.py](scripts/sample.py)
  * Simple Python script to make it easier to run the torch-rnn model and output a large number of results to a text file 
* [Crackstation-Human-Only.txt](Crackstation-Human-Only.txt)
  * Original list of 65 million real human passwords from [Crackstation](https://crackstation.net/buy-crackstation-wordlist-password-cracking-dictionary.htm)
* [Crackstation-Human-Stemmed.txt](Crackstation-Human-Stemmed.txt)
  * The "base words" from Crackstation's password list after using epixoip's [bash command](https://hashcat.net/forum/thread-1305.html) to remove numbers and special characters
  * This is the password list that I trained the model on
* [eHarmony-Hashes.txt](eHarmony-Hashes.txt)
  * The leaked eHarmony password database breach with over 1.5 million MD5 hashed passwords
* [Generated_List.txt](Generated_List.txt)
  * The new dictionary that was generated from the model
* [Pass_Pres.pdf](Pass_Pres.pdf)
  * Class presentation in PDF format
  * You can find it in Reveal.js format [here](http://pass.hh2010.me/)
  
**Future Project ([/scripts](/scripts) folder)**

These files can be used for a different analysis in which we generate passwords based on a list of commonly used words (as opposed to generating passwords randomly which I do in the Main Project).

* [Sample_Oneword.lua](scripts/sample_oneword.lua)
  * Slightly edited version of torch-rnn sampling script to initialize the model on a single word
* [Sample_Oneword.py](scripts/sample_oneword.py)
  * Python script that takes a text file and feed words one at a time into sample_oneword.lua

## Contact
If you have any questions or comments on this project, you can find me below:

E-mail: [hasan.haq@gmail.com](mailto:hasan.haq@gmail.com)

Twitter: [@hhaq2010](http://www.twitter.com/hhaq2010)

Website: [www.hasanhaq.com](http://www.hasanhaq.com)
