## Chap 5: MapReduce Application

### Configuration
- `hadoop-localhost.xml`
  - set `namenode` and `jobtracker`
- `GenericOptionsParser`
- `ToolRunner`

### MRUnit unit test
- MapDriver.runTest()
- ReducerDriver.runTest()

### Execute in Local
- implements `Tool` interface
- create job
- setMapperClass
- setCombinerClass
- setReducerClass
- ...

### Execute in Cluster
- tar job
  - tar job to `jar`, and send to clusters
    - Hadoop will automatically find the jar file
  - or use setJar()
    - use `maven` command
- run job
  - use `-conf` to select clusters
- job id
  - `jobtracker` maintain the job id counter 
- jobtracker web GUI
  - `http://jobtracker-host:50030/`
- every execute history will be kept in `logs/history`
