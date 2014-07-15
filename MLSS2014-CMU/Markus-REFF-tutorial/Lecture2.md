REEF Tutorial
=============

* Lecturer: Markus Weimer
* Recorded by: Huangxin
* Date: 07/15/2014

### Procedure
- Platform: in terminal.com
- Procedure
	- terminal has installed  Java7, git,
	- install maven
	```
	apt-get install maven
	```
		
	- copy jason
	```
	wget http://1drv.ms/1ktxSxe
	```
	or vim mlss.jason, copy contents from https://onedrive.live.com/?cid=5801726772bfc3da&id=5801726772BFC3DA%21144442&ithint=file,.json&authkey=!APUIX96qEKigA1g
	
	- download git
	```
	git clone https://github.com/Microsoft-CISL/TANG.git   
	```
	
	- install jdk-7
	```
	apt-get install openjdk-7-jdk   
	```
	
	- compile and install 
	```
	mvn -DeskipTests clean install
	```
	
	
	- get WAKE, compile
	```
	git clone https://github.com/Microsoft-CISL/WAKE 
	mvn -DeskipTests clean install	 
	```
	- get REEF, in REEF, checkout MLSS, compile
	```
	git clone https://github.com/Microsoft-CISL/REEF
	cd REEF
	git checkout MLSS
	mvn -DeskipTests clean install	
	```
	- run hello-reff locally
	```
	java -cp reef-examples/target/reef-examples-0.6-SNAPSHOT-shaded.jar com.microsoft.reef.examples.hello.HelloREEF
	```
	- where is hello-reff
	```
	cat REEF_LOCAL_RUNTIME/HelloREEF-[#]/Node-1-[#]/STDOUT.txt
	```
	