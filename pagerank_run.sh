#!/usr/bin/env bash

hadoop fs -put /home/hadoopuser/Search-Engine/search_keywords.txt  /user/hadoopuser

STREAM="hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -conf conf/hadoop-localhost.xml" \

hdfs dfs -rm -R /user/hadoopuser/pagerank_result

$STREAM \
  -files pagerank_mapper.py,\
pagerank_reducer.py \
  -input books_inverted_index \
  -output pagerank_result \
  -mapper pagerank_mapper.py \
  -reducer pagerank_reducer.py

# display the output
hadoop fs -cat hdfs://hadoop-master:9000/user/hadoopuser/pagerank_result/part-00000

