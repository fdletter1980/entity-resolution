# entity-resolution

his readme file was generated on 02/05/2024 by Fred De Letter

The following instructions aim to help you run zingg.ai on GCP. 

1. Data requirements:
a. a table or .csv with your raw customer data (e.g. customer_er.csv)
b. an optional labelled data set for a pre-learning stage (training.csv)



2. Change config files with your schema etc.
a. findTrainingData.json
b. customer.py
c. zingg.conf


3. GCP compute & persisted disk which can be leveraged:

Computed host storage should have a folder called "artifacts" which should contain all the relevant files you want to move into the zingg container.

Post-model run you should transfer model output and docs from the container into the persisted computed host storage (and potentially GCP bucket).

Command for model output (for example for model107c): sudo docker cp <CONTAINER ID>:/zingg-0.4.0/models/er-customer/ ~/model107c
Command for model metadata (for example for model107c): sudo docker cp <CONTAINER ID>:/zingg-0.4.0/models/107/ ~/model107c 



4. Open Google SDK for GCE compute and run zingg container:

Command: sudo docker run -it zingg/zingg:0.4.0 bash



5. Open another Google SDK for GCE compute for moving files into container:

Create a new dir called "er-customer" under container "model" directory with command: mkdir er-customer 

Command to ID your container: sudo docker ps

Command to move files to container: sudo docker cp artifacts//<INPUT FILE.csv> <CONTAINER ID>:/zingg-0.4.0/models/er-customer/



6. Create pre-trained data set (Optional)

Currently a pre-trained data set exists called "training.csv".



7. Run --phase findTrainingData

Command: zingg.sh --properties-file /zingg-0.4.0/models/er-customer/zingg.conf --phase findTrainingData --conf /zingg-0.4.0/models/er-customer/findTrainingData.json



8. Run --phase label

Command: zingg.sh --properties-file /zingg-0.4.0/models/er-customer/zingg.conf --phase label --conf /zingg-0.4.0/models/er-customer/findTrainingData.json 



9. Run --phase train

Command: zingg.sh --properties-file /zingg-0.4.0/models/er-customer/zingg.conf --phase train --conf /zingg-0.4.0/models/er-customer/findTrainingData.json 



10. Run --phase match

Command: zingg.sh --properties-file /zingg-0.4.0/models/er-customer/zingg.conf --phase match --conf /zingg-0.4.0/models/er-customer/findTrainingData.json



11. Run --phase generateDocs

Command: zingg.sh --properties-file /zingg-0.4.0/models/er-customer/zingg.conf --phase generateDocs --conf /zingg-0.4.0/models/er-customer/findTrainingData.json 
