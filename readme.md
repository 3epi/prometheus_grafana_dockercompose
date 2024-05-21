kafka : 
    kafka is a event streaming platform used to stream data in real time, main concepts are topic , partitions , broker , producer and consumer. basically you use a producer to provide/make data then give the data to a kafka broker which then stores it in one or more topics (as you have configured). for reliability and scalability so it divides the data into even partitions in a topic which makes it faster and more reliable. after that you can consume that data from the topic in your kafka broker/brokers and use it however you want.
    you gotta use zookeeper which is for handling the brokers or you can use kraft (i used zookeeper in this project).
    using a python producer i produced random data and gave it to a single kafka broker and after that with a consumer stored that data into a database. for making consumer and producer i used kafka-python library.
    the hardest part between these was connecting the producer and consumer containers to the kafka broker :D, what fixed the problem was checking the server.properties file of kafka.
    note that when you use docker everything is located in the /opt directory.

mongoDB:
    i used mongoDB cause it was easy to use and also the data i wanted to store were some random lengthed unstructured strings.
    for mongoDB and python , pymongo is the official library and its easy to use.
    and for seeing the data base you can do these steps : 
    1. docker exec -it mongo mongosh -> to run the mongodb script.
    2. show dbs -> showing all the available databases 
    3. use "the data base you want" -> switches to the desired database
    4. show collections -> shows all your collections
    5.  var collections = db.getCollectionNames();
        for(var i = 0; i< collections.length; i++) {    
        print('Collection: ' + collections[i]); // print the name of each collection
        db.getCollection(collections[i]).find().forEach(printjson); //and then print     the json of each of its elements
        } 
        -> shows everything that is in all the available collections.
