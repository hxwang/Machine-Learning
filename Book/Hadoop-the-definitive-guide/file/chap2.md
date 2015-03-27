## Introduction to MapReduce

### Preliminary
- Hadoop provides parallel computing ability
  - It is a framework
  
### Map and Reduce
- Map
  - Process the data of interest
  - The data will act as input for reduce process
  - write the output to local disk
- Reduce
  - write the output to HDFS

### jobtracker and tasktracker
- jobtracker schedule tasktracker 
- tasktracker exceutes task and report the progress to jobtracker
