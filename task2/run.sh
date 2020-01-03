OUTPUT_DIR=/user/s1998230/assignment/task2
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapreduce.job.name=s1998230_task2 \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.map.output.key.field.separator="|" \
    -D stream.num.map.output.key.fields=2 \
    -D num.key.fields.for.partition=1 \
    -D mapreduce.partition.keypartitioner.options=-k1,1 \
    -D mapreduce.partition.keycomparator.options="-k1,1 -k2,2" \
    -input /data/large/imdb/title.basics.tsv \
    -input /data/large/imdb/title.ratings.tsv \
    -output $OUTPUT_DIR \
    -mapper mapper.py \
    -reducer reducer.py \
    -file mapper.py \
    -file reducer.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner


hdfs dfs -cat ${OUTPUT_DIR}/part-*| sort> $OUTPUT_FILE
cat $OUTPUT_FILE
