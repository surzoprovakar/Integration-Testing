MAKEFLAGS += --silent

datalog:
	g++ -o datalog Datalog/DatalogGen.cpp
	./datalog 6 > ils.dl
	souffle ils.dl
ils:
	g++ -o interleave Datalog/IlGen.cpp

api:
	javac -d . Library-API/APITest.java


# all:	init datalog ils crdt 
# 		sleep 60 
# 		./interleave

all:	datalog ils api
		./interleave
		java APITest
clean:
	@rm -rf datalog interleave APITest.class ils.dl *.csv 
	@rm -rf *.sum *.rdb interleavings/ 