#Chapter 1 - Scripting data science, a crash course

This book will be unlike other books.  It assumes you know what you are doing.  Here we will treat you like an adult.  The assumption is, you are already working with data on a day to day basis and you have some knowledge of coding.  You may not care about computer science, but you do care about doing interesting and powerful analysis.

Throughout the text we will introduce you to increasingly more powerful tools so that you cannot not only do your job, but do it extremely well.  Essentially, the intention is to prepare you for those hard to get jobs - the ones that pay well and require true brilliance.  

##Conventions && ETL

The first thing we'll do here is review how to bring data into memory.  This first chapter will focus on Python, in later chapters we will see R, Scala, Julia, Java, Haskell, C++, Javascript, Rust, Go, and other languages.

###Pandas

Every data scientist needs to be familar with a few primitives.  The most important of these, is the dataframe, which is powerful for understanding and manipulating tabular data.  The hope is one day the data frame will be a standard data structure, shipping with every language in the world, much like the list and the hash map do now.  

##Sending Data to a dataframe

```
import pandas as pd
import random as rand


#Initialize your dataframe
df = pd.DataFrame()

#add data to the dataframe
for i in xrange(10):
    data = {
        "column_one":rand.randint(0,500),
        "column two":rand.randint(0,500)
    }
    df = df.append(data,ignore_index=True)

```

As you can see here sending data to a dataframe is extremely easy.  Simply initialize the dataframe with `df = pd.DataFrame()` and then you can begin passing in data.  The dataframe accepts data in a similar form to that of a python dictionary.  Notice that we must set the dataframe equal to the new dataframe in order for our new data to be recorded via the append method.  Also notice that we passed in `ignore_index=True`.  This allows us to dynamically add new fields to our dataframe.  So if we decided to add a third column later, we could do so.  

##Saving data to a persistant store

Now that we have all our data in a dataframe we can either do further analysis in python or we can pass our data to some persistent store.  

```
import pandas as pd
import random as rand


#Initialize your dataframe
df = pd.DataFrame()

#add data to the dataframe
for i in xrange(10):
    data = {
        "column_one":rand.randint(0,500),
        "column two":rand.randint(0,500)
    }
    df = df.append(data,ignore_index=True)

df.to_csv("first.csv")
```

As you can see the only new thing here is the method call to `to_csv` with the filename of the csv.  This is all that is required!  The pandas dataframe comes equipped with many methods for storing data persistently.  Below is a list of methods:

to_json
to_pickle
to_sql
to_csv
to_excel
to_html
to_latex

There are a few other persistent transformations, but they are experimental and therefore not mentioned here.  
