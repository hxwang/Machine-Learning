## Chap 3: Hadoop Distributed File system

### Overview
- Handle large file: in the scale of hundreds of MB, GB
- Visit data in streaming
- Latency: the data are often latency tolerate
- Many small size file
- Only one writer
  - writing appends in the end of file
  - does not support random write

### HDFS design
- block: 64MB
  - the size is large, thus the time for addressing is low
  - the size cannot be too large, because each map reduce deal with one block; too large size means small amount of task
- files are divided into chunk

### Namenode and Datanode
- Namenode
  - record the information of each file in each block
  - the information may change
  - client visit file system by interating with namenode
- Datanode
  - store or search data block according to user request or name node
  - send the list it stores to namenode periodically
- If namenode lost, then all files in the file system will lost since we do not know how to rebuilt it using datanode
  - One approach is to backup the units that consistuted the file system
  - The other approach is to execute another namenode which cannot be use as namenode. This extra namenode wil help edit log and combine mirror, in order to avoid large logs. This extra namenode will be in another physical machine since it requires high CPU time.
