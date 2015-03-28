## Chap 3: Hadoop Distributed File system

### Overview
- Handle large file: in the scale of hundreds of MB, GB
- Visit data in streaming
- Latency: the data are often latency tolerate
- Many small size file
- Only one writer
  - writing appends in the end of file
  - does not support random write
