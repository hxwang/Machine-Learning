## Chap 5: MapReduce Application

### Configuration
- `hadoop-localhost.xml`
  - set `namenode` and `jobtracker`
- `GenericOptionsParser`
- `ToolRunner`

### MRUnit unit test
- MapDriver.runTest()
- ReducerDriver.runTest()

### Execute 
- implements `Tool` interface
- create job
- setMapperClass
- setCombinerClass
- setReducerClass
- ...
