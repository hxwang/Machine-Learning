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
