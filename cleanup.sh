#!/usr/bin/env bash
dir=${PWD}
hadoop fs -put /home/hadoopuser/Search-Engine/search_keywords.txt  /user/hadoopuser
hadoop fs -rm -R /user/hadoopuser/query_result          # remove all files AND directory
