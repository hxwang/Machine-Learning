REEF Tutorial
=============

* Lecturer: Markus Weimer
* Recorded by: Huangxin
* Date: 07/17/2014
* [Slides](http://www.reef-project.org/2014/07/16/slides-from-the-third-day-of-mlss/)

### Submit Job
submit jobs
```
java -cp reef-examples-hdinsight/target/reef-examples-hdinsight-0.6-SNAPSHOT-shaded.jar com.microsoft.reef.examples.hello.HelloHDInsight
```

check for the status of your application
```
 java -jar reef-examples-hdinsight/target/reef-examples-hdinsight-0.6-SNAPSHOT-shaded.jar -status application_1404348844717_0170 
 ```
 
### Design
- Group Communication in REEF
	- Focus: Elasticity
	- Voluntary Elasticity
	- Involuntary Elasticity

### Machine Learning
- Compute the gradient
- Apply the gradient and regulizer to the model

prepare
```
git clone https://github.com/Microsoft-CISL/MLSS.git
cd MLSS/BGD
mvn -DskipTests clean install
```

run it on HDInsight
```
 java -cp target/BGD-1.0-SNAPSHOT-shaded.jar com.microsoft.reef.examples.nggroup.bgd.simple.BGDHDI -input /trainingdata_final/part-r-0005* -dim 11725480 -iterations 10
 -lambda .00005 -memory 3072  -loss weightedLogLoss
```

check status
```
java -jar target/BGD-1.0-SNAPSHOT-shaded.jar com.microsoft.reef.examples.nggroup.bgd.simple.BGDHDI -status application_1404348844717_0203
```




 
