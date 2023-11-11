- Build docker image
```bash
docker build -t myhadoop .
```

- Run docker image
```bash
docker run -it myhadoop bash
```

- In container image  
  - Check version hadoop
```bash
hadoop version
```  
  - start hadoop
```bash
bash start-hadoop.sh
```  

  - check file
```bash
hdfs dfs -ls /
```

  - put file
```bash
hdfs dfs -put -f ./iuh.txt /
```
  - Run map
```bash
hadoop jar $JARs -input /iuh.txt -output output -mapper /test/mapper.py -reducer /test/reducer.py
```
  - Remove output
```bash
hdfs dfs -rmr /user/root/output
```