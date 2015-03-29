## Chap 4: Hadoop I/O Operation

### Data Integrity
- use check-sum to verity whether data is broken
  - note that it is possible that check-sum is also broken, but it has low probability since it has much smaller length
  - usually, we can use CRC-32 to check integrity
- `io.bytes.per.checksum`
  - the default target input is 512 byte
  - the crc is 4 byte, thus the cost is less than 1%
- datanode will computethe checksum of data when receive it
- clients will verify the checksum when read the data
- LocalFileSystem
  - When create a file, a hidden file name `.filename.crc` will be created as well
  - if we do not want to compute the crc, we can use `RawLocalFileSystem`
  
### Data Compression
- Types 
  - DEFLATE
    - zlip
  - gzip
    - incremental of DEFLATE, by adding a file head and tail
- Devisible?
  - This is important, because it will be very suitable for MapReduce
- Codec compress-decompresee approach
  - use CompressionCodeC to compress/decompress
  - use CompressionCodeCFactory to decide which codec to use
- CodecPool
  - if frequent compression/decompression are required, we can use `CodecPool`, it supprts compression/decompression
