OUTPUT_DIR=/user/s1998230/assignment/task3
OUTPUT_DIR_AUX=/user/s1998230/assignment/temp_task3
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR
hdfs dfs -rm -r $OUTPUT_DIR_AUX

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapreduce.job.name=s1998230_task3_aux \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.map.output.key.field.separator="|" \
    -D mapreduce.partition.keypartitioner.options=-k1,1 \
    -input /data/large/imdb/title.basics.tsv \
    -input /data/large/imdb/title.ratings.tsv \
    -output $OUTPUT_DIR_AUX \
    -mapper mapper1.py \
    -reducer reducer1.py \
    -file mapper1.py \
    -file reducer1.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapreduce.job.name=s1998230_task3 \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.map.output.key.field.separator="|" \
    -D mapreduce.partition.keypartitioner.options=-k1,2 \
    -D mapreduce.partition.keycomparator.options="-k1,1 -k2,2 -k3,3nr" \
    -D mapred.reduce.tasks=1 \
    -input $OUTPUT_DIR_AUX \
    -output $OUTPUT_DIR \
    -mapper mapper2.py \
    -combiner combiner2.py \
    -reducer reducer2.py \
    -file mapper2.py \
    -file combiner2.py \
    -file reducer2.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat ${OUTPUT_DIR}/part-* | sort> $OUTPUT_FILE
cat $OUTPUT_FILE
