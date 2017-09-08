# Running spark job on a kubernete cluster. 

The document describes the procedure to run a spark job on a DL Workspace cluster. Please note that the procedure below will be significantly updated in a future release to stream line the process. 

1. Launch Yarn resource manager and node manager
  ```
  deploy.py kubernetes start yarnresourcemanager
  deploy.py kubernetes start yarnnodemanager
  ```
  You may disable yarn resource manager and node manager by running:
  ```
  deploy.py kubernetes stop yarnresourcemanager
  deploy.py kubernetes stop yarnnodemanager
  ```

2. Launch Spark container
  ```
  deploy.py kubernetes start spark
  ```

3. Launch Spark container
  ```
  deploy.py kubernetes start spark
  ```

4. Ssh into spark container, go to spark directory
  ```
  deploy.py kubectl exec -ti spark-pod
  cd /usr/local/spark/bin
  ```

5. You can validate yarn resource manager to be operational by running:
  ```
  yarn node -list -all
  ```
  This should list all yarn node ready for execution.  You should be able to execute spark command, e.g., 
  ```
  cd /usr/local/spark
  ./bin/spark-submit --class org.apache.spark.examples.SparkPi --master yarn --deploy-mode cluster --driver-memory 4g --executor-memory 2g --executor-cores 1 --queue thequeue examples/jars/spark-examples*.jar 10
  ```
