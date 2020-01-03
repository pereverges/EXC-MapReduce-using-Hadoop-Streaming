# EXC-MapReduce-using-Hadoop-Streaming
#### Using MapReduce and Hadoop Streaming to solve problems using a big dataset, which is the IMDB database

In this project we will use MapReduce, because helps us easly write parallel applications. Basically MapReduce as three functions:
  - Map(string key, string value)
  - Combiner(string key, iterator values)
  - Reducer(string key, iterator values)
  
![MapReduce example](https://github.com/pereverges/EXC-MapReduce-using-Hadoop-Streaming/blob/master/MapReduceExample.png)

One important thing to take into account are how the keys are ordered and distributed to the reduce workers, since in most cases ordering and sorting the input of the reducer will help us reduce the number of operations and the memory used in the computations. 

For more informations of how MapReduce works read the following paper.

