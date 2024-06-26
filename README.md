# JetBrains internship task

Author: Roman Gellert

I used Colab Pro for fine-tuning, here is the link to the notebook:
https://colab.research.google.com/drive/1wMJutEiXuZ2c9FkgoMKJPIOC1ZyrxcPG?usp=sharing

### Repo content: 
- <ins>kotlin_dataset_downloader</ins>.py - python script to download several kotlin open source projects
- <ins>kotlin_files</ins>.zip - downloaded kotlin files zipped 
- <ins>fine_tuning_and_testing</ins>.ipynb - ipynb notebook with sequential code for dataset parsing, fine-tuning and output generation
- Analysis is in this README

### Approach:

- I took several open source datasets: Kotlin, v2rayNG, Seal, KernelSU, ViMusic
- I tested Phi 1.5 on several manually selected prompts
- Considering the nature of dataset I fine-tuned it in an unsupervised way
- I tested Phi 1.5 again on manually selected prompts

I chose not to use some form of distance between two strings to assess the performance, because after testing
this approach it didn't produce any meaningful results for Phi 1.5.

### Analysis:

I spent around 2 hours fine-tuning with mostly default parameters.

Key takeaways:

- Phi 1.5 is generally not aligned well with user's preferences (like for example ChatGPT). It is nevertheless impressive considering 
a relatively small parameter count. It is very hard, however, to make practical use of the answers.
- Before fine-tuning python questions were answered relatively well (at least they made some sense). Some Kotlin 
prompts were answered more or less adequately although in some cases the output was in python and java instead.
- After fine-tuning (at least the way I did it) it is hard to say if there was a big improvement or not. Some answers just 
contained relevant text, but had nothing to do with the code. Some python responses starting to look like Kotlin. Some 
answers remained more or less the same. Generally the answers started to produce something resembling Kotlin, but it didn't 
make them more useful overall.

What could be done to make it better? 

- Quality data. Ideally a big dataset with ground truth data to fine-tune the model in a supervised QA way
- Bigger and better model
- Longer fine-tuning time and better hyperparameters

My personal answer highlight:

![img_29.png](img_29.png)


I list here the prompts I consider interesting to analyse before and after fine-tuning:

Prompts were as following, some are in Kotlin train set, some not:

```Python
prompts_list = [
    f"Write a sample program in Python",
    f"Write a program to sum two numbers in Python",
    f'''def print_prime(n):
        """
        Print all primes between 1 and n
        """''',
    f'''def close(self):
        """
        Close the socket.
        """''',
    f'''def _init_client(self, from_archive=False):
        """
        Init client
        """''',
    f'''def setUp(self):
        """
        Initialize the parser, required arguments
        """''',
    f"Write a sample program in Kotlin",
    f"Write a program to sum two numbers in Kotlin",
    f'''Complete the following function in Kotlin: 
    fun isPrime(number: Int): Boolean''',
    f'''Complete the following function in Kotlin: 
    fun sumTwoNumbers(number1: Int, number2: Int): Int''',
    # in training set
    f'''complete the following code in Kotlin 
        val x = 1;
        val s = "";

        when (x) ???
        ???

        мal z = 1''',
    # in training set
    f'''
    Complete the following two fucntions in Kotlin:
    fun test4() 

    fun test5() 
    ''',
    # in training set
    f'''
    class KTypeProjectionTest 
    ''',
]
```

--- 

<ins>Prompt</ins> :
```Write a sample program in Python```

<ins>Output before fine tuning</ins> :

![img_1.png](img_1.png)

<ins>Output after fine tuning</ins>

![img_16.png](img_16.png)

--- 

<ins>Prompt</ins> :
```Write a program to sum two numbers in Python```

<ins>Output before fine tuning</ins> :

![img_2.png](img_2.png)

<ins>Output after fine tuning</ins> :

![img_17.png](img_17.png)

--- 

<ins>Prompt</ins> :
```
def print_prime(n):
"""
Print all primes between 1 and n
"""
```

<ins>Output before fine tuning</ins> :

![img_4.png](img_4.png)

<ins>Output after fine tuning</ins> :

![img_18.png](img_18.png)

--- 

<ins>Prompt</ins> :
```
def close(self):
"""
Close the socket.
"""
```

<ins>Output before fine tuning</ins> :

![img_6.png](img_6.png)

<ins>Output after fine tuning</ins> :

![img_19.png](img_19.png)

--- 

<ins>Prompt</ins> :
```
def _init_client(self, from_archive=False):
"""
Init client
"""
```

<ins>Output before fine tuning</ins> :

![img_7.png](img_7.png)

<ins>Output after fine tuning</ins> :

![img_20.png](img_20.png)

--- 

<ins>Prompt</ins> :
```
def setUp(self):
"""
Initialize the parser, required arguments
"""
```

<ins>Output before fine tuning</ins> :

![img_8.png](img_8.png)

<ins>Output after fine tuning</ins> :

![img_21.png](img_21.png)

--- 

<ins>Prompt</ins> :
```
Write a sample program in Kotlin
```

<ins>Output before fine tuning</ins> :

![img_9.png](img_9.png)

<ins>Output after fine tuning</ins> :

![img_22.png](img_22.png)

--- 

<ins>Prompt</ins> :
```
Write a program to sum two numbers in Kotlin
```

<ins>Output before fine tuning</ins> :

![img_10.png](img_10.png)

<ins>Output after fine tuning</ins> :

![img_23.png](img_23.png)

--- 

<ins>Prompt</ins> :
```
Complete the following function in Kotlin: 
    fun isPrime(number: Int): Boolean
```

<ins>Output before fine tuning</ins> :

![img_11.png](img_11.png)

<ins>Output after fine tuning</ins> :

![img_24.png](img_24.png)

--- 

<ins>Prompt</ins> :
```
Complete the following function in Kotlin: 
    fun sumTwoNumbers(number1: Int, number2: Int): Int
```

<ins>Output before fine tuning</ins> :

![img_12.png](img_12.png)

<ins>Output after fine tuning</ins> :

![img_25.png](img_25.png)

--- 

<ins>Prompt</ins> :
```
complete the following code in Kotlin 
val x = 1;
val s = "";

when (x) ???
???

мal z = 1
```

<ins>Output before fine tuning</ins> :

![img_13.png](img_13.png)

<ins>Output after fine tuning</ins> :

![img_26.png](img_26.png)

--- 

<ins>Prompt</ins> :
```
Complete the following two fucntions in Kotlin:
fun test4() 

fun test5()
```

<ins>Output before fine tuning</ins> :

![img_14.png](img_14.png)

<ins>Output after fine tuning</ins> :

![img_27.png](img_27.png)

---

<ins>Prompt</ins> :
```
class KTypeProjectionTest 
```

<ins>Output before fine tuning</ins> :

![img_15.png](img_15.png)

<ins>Output after fine tuning</ins> :

![img_28.png](img_28.png)





