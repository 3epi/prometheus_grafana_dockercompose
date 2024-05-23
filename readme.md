# Readme

## Kafka 

*Kafka* is a event streaming platform used to stream data in real time, main concepts are topic , partitions , broker , producer and consumer. basically you use a producer to provide/make data then give the data to a kafka broker which then stores it in one or more topics (as you have configured). for reliability and scalability so it divides the data into even partitions in a topic which makes it faster and more reliable. after that you can consume that data from the topic in your kafka broker/brokers and use it however you want.

You gotta use zookeeper which is for handling the brokers or you can use kraft (i used zookeeper in this project).
using a python producer I produced random data and gave it to a single kafka broker, after that with a consumer stored that data into a database. For making consumer and producer i used kafka-python library.

The hardest part between these was connecting the producer and consumer containers to the kafka broker :D, what fixed the problem was checking the server.properties file of kafka.
note that when you use docker everything is located in the /opt directory.

## MongoDB

I used mongoDB cause it was easy to use and also the data i wanted to store were some random lengthed unstructured strings.
for mongoDB and python , pymongo is the official library and its easy to use.
and for seeing the data base you can do these steps : 

1. Running the mongodb script within the docker container : `docker exec -it mongo mongosh`
2. Showing all the available databases : `show dbs` 
3. Switching to the desired database : `use "the database you want"`
4. Showing all your collections : `show collections`
5.  Showin everything that exists in all the available collections :
```
var collections = db.getCollectionNames();
for(var i = 0; i< collections.length; i++) {    
print('Collection: ' + collections[i]); // print the name of each collection
db.getCollection(collections[i]).find().forEach(printjson); //and then print the json of each of its elements}
```

## Docker

while making a docker compose file its a best practice to specify the image or dependency versions, using no version or the `latest` version is not the best approach because it can cause instability or security issues. you can read more in [here](https://www.linkedin.com/advice/1/how-do-you-handle-dependencies-updates-your-dockerfile-ensure)
It's better to use a `requirements.txt` file for your dependencies and not just putting them in the middle of the Dockerfile. 