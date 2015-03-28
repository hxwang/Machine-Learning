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

### Visit HDFS
- Throught HTTP
  - direct visit
  - through HDFS proxies
- Read data through HDFS URL
- Read data through Filesystem API

### FSDataInputStream
- extends `java.io.DataInputStream`
- `seek()`: jump to any absolute position, this is an expensive operation!
- `skip()`: jump to relative position
- `read()`: read at most length, store to the buffer with offset position
- `create()`: create files

### FSDataOutputStream
- cannot index a random position in a file, because HDFS only allow write in order

### Other operations
- FileStatus
- ListStatus
- GlobeStatus
  - return those matched
- PathFilter: excludes those unwanted

### Data Stream
- use `open()` to open the files
  - distributed system call namenode via RPC
- user `create()` to create file
  - distributed ystem call namenode via RPC
  - namenode will check whether the file exists, if exists, it will throw IOException
  - `DistributedFileSystem` return a `FSDataOutputStream` to client, client then uses it to write data. `FSDataOutputStream` has a `DFOutPutStream` which will responsible for the communication between datanode and namenode.

### Synchronization
- `syn()`: syn the data in datanode, including buffer

### Import Data
- Flume: Apache Flume
- Apache Sqoop

### Distcp parallel copy
- scenario: transmit data between two HDFS clusters
  - note these two HDFS should have the same version, because the RPC protocol are not compatible

### Hadoop Archive
- archive small files to HDFS blocks, HAR file
- another solution for dealing with small files (they may exhaust the namenode space) is to use `CombineFileInputFormat`
