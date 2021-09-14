# DBTron
- A Package that allows to access Cloud as well as Local Databases and allows user to Performs Operation using prebuilt functions, Currently the available Databases are MySql and MongoDB.'
    This is basically the Automation of SQL and  NoSQL Database Queries

## :desktop_computer:	Installation

## :gear: Setting up environment for project

1. Create a Environment using below Command
```
$ conda create -n YourEnvName python=3.6
```

2. Activate Your Environment
```
$ conda activate EnvName
```

3. Install the Package using pip or pip3

```
$ pip install DBTron
```

4. How to use the package after installing

### MongoDB

```
# Importing Class from package
$ from DBTron.mongoDBOps import MongoDBOps

# Creating class object with appropriate arguments
$ mongo_obj = MongoDBOps(url,password)

# Calling the function using class object with appropriaters arguments
$ mongo_obj.func(parameters)

# NOTE: In our case class object can also be called as connection object
```

### MySQL

```
# Importing Class from package
$ from DBTron.sqlOps import SqlOps

# Creating class object with appropriate arguments
$ sql_obj = SqlOps(host, user, password)

# Calling the function using class object with appropriaters arguments
$ sql_obj.func(parameters)

# NOTE: In our case class object can also be called as connection object
```

### List of Function available in DBTron as of now are as follows:

In MongoDB

```

$ getMongoDBClientObject()
$ closeMongoDBconnection(mongo_client)
$ isDatabasePresent(db_name)
$ createDatabase(db_name)
$ dropDatabase(db_name)
$ getDatabase(db_name)
$ getCollection(collection_name, db_name)
$ isCollectionPresent(collection_name, db_name)
$ createCollection(collection_name, db_name)
$ dropCollection(collection_name, db_name)
$ insertRecord(db_name, collection_name, record)
$ insertRecords(db_name, collection_name, records)
$ findfirstRecord(db_name, collection_name,query=None)
$ findAllRecords(db_name, collection_name)
$ findRecordOnQuery(db_name, collection_name, query)
$ updateOneRecord(db_name, collection_name, previous_record, new_record)
$ updateMultipleRecord(db_name, collection_name, previous_record, new_record)
$ deleteRecord(db_name, collection_name, query)
$ deleteRecords(db_name, collection_name, query)
$ getDatabaseList()
$ getCollectionList(db_name)
$ getDataFrameOfCollection(db_name, collection_name)
$ saveDataFrameIntoCollection(collection_name, db_name, dataframe)
$ getResultToDisplayOnBrowser(db_name, collection_name)
$ downloadDataFromCollection(db_name, collection_name, file_name)

```

In MySQL

```

$ sql_show_db()
$ sql_show_tables(db)
$ sql_create_db(db_name)
$ sql_delete_db(db_name)
$ sql_create_table(db_name , table_name , columns)
$ sql_delete_table(db_name , table_name)
$ sql_insert_table(db_name , table_name , values)
$ sql_display_all_data(db_name, table_name)
$ sql_update_data(db_name, table_name ,set_value , where_value)
$ sql_download_data(db_name , table_name , new_filename="sql_data")

```


## Contributors <img src="https://raw.githubusercontent.com/TheDudeThatCode/TheDudeThatCode/master/Assets/Developer.gif" width=35 height=25> 

- Suraj Jaiswal