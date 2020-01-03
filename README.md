# EXC-MapReduce-using-Hadoop-Streaming
#### Using MapReduce and Hadoop Streaming to solve problems using a big dataset, which is the IMDB database

In this project we will use MapReduce, because helps us easly write parallel applications. Basically MapReduce as three functions:
  - Map(string key, string value)
  - Combiner(string key, iterator values)
  - Reducer(string key, iterator values)
  
![MapReduce example](https://github.com/pereverges/EXC-MapReduce-using-Hadoop-Streaming/blob/master/MapReduceExample.png)

One important thing to take into account are how the keys are ordered and distributed to the reduce workers, since in most cases ordering and sorting the input of the reducer will help us reduce the number of operations and the memory used in the computations. 

For more informations of how MapReduce works read the [MapReducePaper](https://github.com/pereverges/EXC-MapReduce-using-Hadoop-Streaming/blob/master/MapReducePaper.pdf).

# Tasks

We have to do four tasks using the IMBD database as the data input to the MapReduce. The data we have looks like:
![IMBD data](https://github.com/pereverges/EXC-MapReduce-using-Hadoop-Streaming/blob/master/IMDBdata.png)

For more specific information of the assignment read the [Assignment paper](https://github.com/pereverges/EXC-MapReduce-using-Hadoop-Streaming/blob/master/Assignment.pdf)

### Task 1
Calculate the average maximum and minimum runtime duration for all titles per movie genre.

The output should look like: ```[avg runtime:float | max runtime:int | min runtime:int | genre:str]```


### Task 2
Print the titles of the movies which were released between 1990 and 2018 (inclusive), have an average rating
of 7.5 or more, and have received 500000 votes or more.

The output should look like: ```[title:str]```


### Task 3
Print the top rated movie of each genre for each decade between 1900 and 1999.

The output should look like: ```[decade:int | genre:str | title:str]```


### Task 4
Print the names of the top 10 most popular writers, based on the votes of their single most popular title
they are known-for as writers.

The output should look like: ```[votes:int | writer name:str]```

