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

##Data cleaning - pandas

The pandas documentation does a wonderful job explaining how to work with missing values - a problem for languages like R, Stata, and SAS.

I will merely reference it [here](http://pandas.pydata.org/pandas-docs/dev/missing_data.html), since the examples are robust and complete. 

##Data cleaning - strings

Cleaning strings on the other hand is challenging for many languages geared towards statistics.  Where other languages fail, python succeeds.  The string processing utilities available in python are in my humble opinion the most powerful and intuitive.  

The string object - methods:

```
>>> for i in dir(""):
...     print i
... 
__add__
__class__
__contains__
__delattr__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__getnewargs__
__getslice__
__gt__
__hash__
__init__
__le__
__len__
__lt__
__mod__
__mul__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__rmod__
__rmul__
__setattr__
__sizeof__
__str__
__subclasshook__
_formatter_field_name_split
_formatter_parser
capitalize
center
count
decode
encode
endswith
expandtabs
find
format
index
isalnum
isalpha
isdigit
islower
isspace
istitle
isupper
join
ljust
lower
lstrip
partition
replace
rfind
rindex
rjust
rpartition
rsplit
rstrip
split
splitlines
startswith
strip
swapcase
title
translate
upper
zfill
```

The number of methods listed above shows all the things you can do with builtin strings.  You should learn all of them but we'll focus on just a few:

join, split,strip,replace

###Splitting things

The most powerful of the string methods is the split.  With this method we can do a lot of very powerful things.

```
to_process = "hello,there,this,has,many,commas"
print to_process.split(",")
```
Let's look at some examples of when this might be useful:

1) Splitting on individual words

```
to_process = "This sentence isn't very interesting, but it's also got some important data: 591821"
print to_process.split("data:")[1]
```

2) Splitting on multiple words

```
to_process = "This sentence is also somewhat boring, but we have meaningful data here: 15098123 and then a bunch of garbage here."
print to_process.split("here:")[1].split("and")[0]
```

3) Combining with other methods

As you saw in the last example, we left some white space in our result.  Let's remove that, because sometimes people are picky:

```
to_process = "This sentence is also somewhat boring, but we have meaningful data here: 15098123 and then a bunch of garbage here."
print to_process.split("here:")[1].split("and")[0].strip()
```

This will remove any white space characters from the front and end of the string in question.

Now that we know how to split things up, let's learn how to put them back together.

###Joining things

Just like in sql, you can join on strings.  

Here are some simple, yet powerful joins:

1) the do nothing join:

```
result = ''.join([elem for elem in "hello there"])
print result
```

2) joining on data

```
to_process = "There is some meaningful data here: 123985 and here: 1290841 but also here: 102394"
new_listing = []
for elem in to_process.split("here:")[1:]:
    tmp = elem.split()
    for i in tmp:
        if i.isdigit():
            new_listing.append(i)
print ",".join(new_listing)

###Replacing things

The replace method is another extremely powerful method.  We'll touch on one brief example here.  

```
to_process = "Hello there, my name is Eric.  Is your name Eric too?"
print to_process.replace("Eric","Connor")
print to_process.replace("Connor","")
```

##Feature Engineering

Now that we know how to process strings (at least), let's move onto feature extraction.  This is the process of transforming non-mathematical data like text or images into something a mathematical function can process.  

Since feature extraction is extremely well covered we'll only mention one example and then reference [the tutorial on sklearns website](http://scikit-learn.org/stable/modules/feature_extraction.html), which is fantastic.

```
def doc_comparison(new_document,doc_list):
    total = 0.0
    for doc in doc_list:
        total += consine_similarity(new_document,doc)[1]
    if total/len(doc_list) > 0.5: #play with this
        return "is similar enough"
    else:
        return "is not similar enough"
    
def cosine_similarity(documentA,documentB):
    docs = [documentA,documentB]
    tfidf = TfidfVectorizer().fit_transform(docs) 
    cosine_similarities = linear_kernel(tfidf[0:1], tfidf).flatten() 
    return cosine_similarities

print doc_comparison("Hello there my Name is Eric","Hi, my name is Eric Schles and I like data science")
```

In the above example we make use of [Tf-idf](http://www.tfidf.com/) vectorization to transform the words in the documents into mathematical objects. 

##Modeling

###Linear Regression

There are a number of ways you can do linear regression in python.  The simplest is probably [statsmodels](http://stackoverflow.com/questions/19991445/run-an-ols-regression-with-pandas-data-frame) which leads you work directly with dataframes.  That being said, there are good reasons to use the [sklearn linear regression package](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) - not least of all being the number of linear regression models available to a user. 

Something important to note: At the present time sklearn does not provide summary statistics.

###K-nearest neighbors

There are 


