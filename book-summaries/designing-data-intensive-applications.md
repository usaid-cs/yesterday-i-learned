# Designing Data-Intensive Applications

## Chapter 1: Reliable, Scalable, and Maintainable Applications

* Some programs are data-intensive, while some are compute-intensive. Data-intensive applications are the ones where CPU power is not the bottleneck.

### Reliability

* "Reliable" applications continue to work correctly, even if things go wrong (faults).
* "Faults" are not the same as "failures": faults are the program deviating from its spec. A failure is the program not working altogether.
* We generally (i.e. not always) prefer preventing faults over tolerating faults.
* There are different kinds of faults: hardware (e.g. failing hard drives), software (e.g. bugs, other processes taking up all the resources, cascading failures from another component), and human (e.g. configuration errors).
* There are situations where we don't need reliability. While prototyping, for example. We also wouldn't spend that much money when the product isn't making any money.

#### Building reliable applications

* Chaos Monkey: deliberately introduce faults into the system, and fix your system such that it holds up to those random attacks.
* Production monitoring / telemetry: use tools to monitor faults and resolve them.
* Design APIs to "do the right thing" to reduce human errors.
* Have a way to roll back your system.

### Scalability

* "Scalable" programs can cope with increased load.
* There are many kinds of load. We can't say "X scales" or "Y doesn't scale".
* "Head-of-line blocking": if you have 10 requests, and the first one takes 10 seconds blocking the entire server, while the other nine requests take 1ms, then while the server reports having taken one second per request, all your clients waited for 10 seconds. So **make sure you measure performance on the client side**.
* There is no such thing as a one-size-fits-all scalable architecture.

#### Measuring performance

* You can either measure (how a metric is impacted when a load parameter is increased), or (how much resource you need to add to keep the metric the same, when a load parameter is increased).
* For things like response time (which is not the same as "latency", the book insists), try to measure them in percentiles, so you know how good the performance *typically* is.
* Note that your most loyal users use your system the most, and thus have the most data with you... which means they have the worst performance. So you want to take care of these people with high *tail latencies*.
* Test clients used to measure performance should send requests with no regard to the server's response time. Waiting for the server to complete artificially decreases the load on the test server.

#### Building scalable applications

* Look carefully at what your system does, and design accordingly to what happens more common / rare: "a system that is designed to handle 100,000 requests per second, each 1 kB in size, looks very different from a system that is designed for 3 requests per minute, each 2 GB in size—even though the two systems have the same data throughput."
* Prioritise data structures for reading (or writing, whichever one occurs more frequently). Look up Twitter fan-out.
* Caching.
* Use more powerful hardware (scaling up).
* Shared-nothing architecture: distributing load across multiple machines (scaling out). This can also be adjusted *elastically*.

The bad news is a system designed to handle a certain amount of load is often unable to handle 10 times that, and you need to redesign the system every so often.

### Maintainability

No one likes to maintain legacy applications, but we can make it in ways that minimise that pain.

#### Operability

Make the system easier for the operations team to run smoothly.

* Give them good monitoring.
* Have good documentation on behaviours, and how to fix something if something bad happens.
* Make runtime behaviours visible to them.
* Give them good automation tools, and integration with standard tools.
* Avoid using a machine in a way that it can never be taken down for maintenance.
* Have good default behaviour (minimise surprises), but let operators override that behaviour.

#### Simplicity

Make it easy to work with, especially for junior devs.

* Complexity slows down everyone working on a system, and further increases complexity on the system (plus, introducing more bugs).
* Use abstraction to remove some "accidental complexity". ("However, finding good abstractions is very hard.")

#### Evolvability (aka extensibility, plasticity)

Make it easy to add unanticipated features. Something about being agile helps.

## Chapter 2: Data Models and Query Languages

There's the relational model (mostly just SQL), and then there's the document model (NoSQL).

### Relational model

* Choose the relational model for any case that the document model is not particular good at solving.
* Use the ORM to map the tables, rows, and columns to your application code.
* An SQL standard after SQL:1999 allowed storing structured data types like JSON and XML in a column in a row. This makes schema design more interesting than before.
* "Normalisation" is just removing duplication of the data stored, in a way.
* CSS selectors are actually like SQL: you tell it what you want, and then it just goes and gets it.

### Document model (NoSQL)

* You can choose the document model if your application routinely works with mostly-flat data structures, with one-to-many structures and *no* many-to-many structures, that can be represented as a document. The document model also excels when you almost always need the entire document (since you won't need to join anything to get it).
* The document model is faster than the relational model (by data locality), and has flexible schema.
* Well, there are no joins, so reads are typically faster.
* Some NoSQL systems (notably, RethinkDB) support joins.
* The fact that it has no schema removes *impedance mismatch* between the database and application code, but it has its own problems.
* Since documents are essentially fully-denormalised data, it is hard to turn a document back into relational entities after the fact.
* The document model is not *schemaless*. It has schema-on-read, rather than schema-on-write like in the relational model. Your database fucks your application when you read your data, not when you write it in.
* "The moral of the story is that a NoSQL system may find itself accidentally reinventing SQL, albeit in disguise."

### MapReduce

* It's just `map()` followed by a `reduce()`, where `map` and `reduce` are pure functions that only uses the daa given to them as input, and cannot make additional queries elsewhere.

### Graph-like data models

* Used to store information with a lot of M2M relationships, where anything might be related to anything else.
* Graph databases typically don't enforce a schema.
* You can implement edges and vertices with M2M relationships in a relational database. Of course, there are off-the-shelf graph databases like Neo4j, which uses the Cypher query language.

## Chapter 3: Storage and Retrieval

* An index is a data structure that is derived from your primary data. Every index speeds up reads. **Every index slows down writes.**
* The most common type of index is the B-tree. A B-tree must be balanced to be efficient; "balanced" in this case means the branching factor at each node is roughly the same, and that finding something in a balanced B-tree with `n` items is always `O(log n)` because of that.
* Databases like postgres use a write-ahead log (WAL), which is an append-only file, to ensure the database's B trees are overwritten only if all write operations are done (or something like that). Other databases like LMDB do copy-on-write.
* With that said, LSM-trees are probably worth a mention since they are (thought to be) faster than B-trees for writes. Every B-tree index update must write something twice: once to the WAL, and once to the tree itself.
* The chapter discusses log-structured indexes, hash indexes, compaction, SSTables and LSM-trees, but since they aren't relevant in most cases, you can read up on them on your own time.
* In a "clustered index" arrangement, the index *contains* the values of a row (i.e. the data for the table is stored in an index, not a heap). This speeds up lookups by primary key (or whichever column you decide to index that way) at a cost of write overhead. In all popular relational databases, you can have at most one clustered index per table.

### Transactions vs Analytics

* Transactions apparently just means low-latency reads and writes, as opposed to batch processing jobs. Transactions almost always carries the ACID meaning, but it wasn't the case before.
* Traditional application databases are designed to read a small number of rows, and then maybe write something according to user input ("OLTP"). Analytics, or data warehousing, does a large number of reads and no writes ("OLAP").
* The ETL database, despite having the same data as the production database, can (somehow) be tuned to optimise for OLAP. Enterprise databases like SAP HANA and Amazon RedShift often support this as a dedicated mode.
* Lots of big companies store their warehouse data as events, called *fact tables*. The fact table is the central table of a *star schema* / *snowflake schema* (multi-level stars), where some columns can branch off to another table ("dimension tables"), to give a row additional context.
* Since the fact table can have hundreds of columns, accessing data by row starts being costly. Companies like SAP make columnar databases that allow you to access certain columns for all rows, faster than a row-based database can.
* The fact that columnar databases keep column values together, means that the data is very compressible (if you want to compress it), and since data is often repeated, you can build very fast indexes that are essentially bitmasks. Or you can do both! You can compress the data into bits, and look them up directly with the bitmask.
* Columnar databases also make use of *vectorised processing*, where the data, which is highly compressed and can fit in a CPU's L1 cache, can be processed in chunks, inside a tight loop, without leaving the cache.
* Sorting rows in a columnar database helps with data compression.
* Use materialised views (cached views derived from other data, basically) to speed up reporting in OLAP. It is not practical in OLTP because data is written from time to time, forcing the views to update, but no such problem exists in OLAP.
* There is a technique called the data cube, where aggregates of multiple fields combine to make these questions easier: total sales of a specific product, total sales on a day across all products, total of totals, and so on.

## Chapter 4: Encoding and Evolution

* Backward compatibility: newer code can read data written by older code.
* Forward compatibility: older code can read data written by newer code.
* JSON doesn't support binary representation of something, so there's MessagePack, who advertises itself as "like JSON, but binary", and other random products.
* More aggressive binary formats, like ProtoBuf (Google) and Thrift (Facebook), require schema declaration.
* Thrift and ProtoBuf schemas require a tag number for each field because you will release new versions of the software one day, and this schema may need to change. When you do that, the data still needs to be read by new and old versions alike. You can only add an optional field to not break old code; you can only remove an optional field to not break the new code.
* There is also a format called Avro, which does not tag fields with numbers. It achieves this by differentiating between a *writer's schema* and a *reader's schema*, resolves the difference between the two, and outputs a message that the reader understands. You can include the schema number in the data so the reader knows which version of the schema to compare against.
* Statically-typed languages generate type-safe boilerplate to work with these schemas. Dynamically-typed languages don't need to do that, and really shouldn't. (I'm look at you gRPC/protobuf)

### Modes of Dataflow

* For machines that don't share memory, you pass data from one machine to another through: databases, service calls (like REST or RPC), and messages (like queues and stuff).

#### Dataflow Through Databases

* In this case, a system writes the message to the db, and then another (possibly the same) process reads it back. Backwards compatibility is a must.
* If a new process sends a message with a new field, and an older process reads it and writes it back again, then the message will have lost the new field. So *make sure your old system retains fields it doesn't understand*.
* *Data outlives code*: you may have services that have been deployed for a month, but your data may be there for years. You need to take care of backward compatibility.
* Migrate all your data to the latest known schema when you archive it. You are not going to touch it again; you may as well.

#### Dataflow Through Services

* Typically used to communicate through a network. Browsers connect to APIs.
* Service-oriented architecture (SOA) is just microservices, except microservices has a "smaller" connotation.
* SOA makes the application easier to upgrade and maintain by allowing individual services to be upgraded independently. Teams can also work on services separately.
* "WSDL" is the XML specification used by SOAP services. It allows code generation for statically-typed languages to use the service, which is against the grain for dynamically-typed languages.
* RPC, or the idea of executing remote code as it is on the same local machine, is fundamentally flawed: a) there are network problems, like unreachability or timeouts, which leads to b) idempotent functions not being consistently idempotent, which means you need the concept of *retries*, c) execution times can be wildly different depending on network conditions, d) you can't pass complex objects around anymore, and e) the data types you use is entirely at the mercy of the common format you have chosen, i.e. if you don't support big ints, we don't know whose fault that is.
* gRPC and Finagle make it explicit that their version of RPC *is not* the same as calling a local function by implementing *steams* and *promises*, respectively, which requires you to think about code flow.
* REST is better than RPC for experimentation, debugging (since everyone has browsers and curl), and network tooling support, making it the predominant style for public APIs.

#### Dataflow Through Messages

Compared to RPC:

* A broker acts as a buffer between systems if the recipient is temporarily unavailable, or if a recipient is overloaded.
* Messages are automatically redelivered on failure (up to a point).
* Message senders don't need to know where every service is, only where the broker is. This is very useful in cloud environments.
* A message can be sent to multiple recipients.
* **The sender does not expect a reply.**

##### Brokers

* WebSphere??
* RabbitMQ
* Apache Kafka

##### Actor model

The actor model encapsulates logic in actors, who can execute code concurrently.

Each actor:

* Reads one message at a time
* Does not have a thread of its own
* Sends *asynchronous* messages to other actors
* **Assumes messages will get lost**, no matter how safe the broker is

## Chapter 5: (Data) Replication

Replication means you keep multiple copies of the same data across multiple machines on the network. Replication might:

* Improve performance by having multiple machines
* Reduce latency (if you put data close to your users)
* High availability, which is not the same as [fault tolerance][1], apparently. In this case, it means you can have a machine down and keep the service up.

### Leaders and Followers

Database replication can be done in *single-leader* (aka master-slave), *multi-leader*, and *leaderless* modes, each with pros and cons.

Message brokers can also support this pattern: Kafka, RabbitMQ.

#### Single-leader (master-slave)

* The leader broadcasts changes to any followers listening. Followers then replicate the changes on their copy of the database.
* Only the leader can be written to. All writes must go through it. All followers are read-only.
  * There can be one leader per partition, though.

#### Synchronous vs Asynchronous replication

Replication can be synchronous (leader waits for follower(s) to finish replicating) or asynchronous (leader sends WAL over and that's it).

|             | Synchronous                                | Asynchronous                                | Semi-asynchronous                                           |
|-------------|--------------------------------------------|---------------------------------------------|-------------------------------------------------------------|
| What is it? | All followers are replicated synchronously | All followers are replicated asynchronously | Only one follower is replicated synchronously; others async |
| Pros        | Data in followers are always up to date    | Able to handle much higher loads            | Limits lag caused by multiple followers                     |
| Cons        | Lag                                        | Potential data loss                         | More complicated                                            |

##### Setting up a new leader

1. Take a dump of the leader's db
2. Load that data into the new follower node
3. Get the follower to connect to the leader and request changes since then (and eventually *catch up*)

#### Handling Node Outages

* Leader: (aka *failover*) configure a follower to be the new leader. Configure all followers to request changes from it, instead of the old leader. Turn the old leader into a follower in case it becomes healthy again.
  * If the old leader had writes that no one else has, then discard them, because they *will* conflict with the new leader's changes since then.
  * Even then, discarding this data can go very wrong, especially if other systems make use of things like primary keys. See the Github example.
* Follower: just let it catch up.

#### Implementation of Replication Logs

The WAL is sent to followers. WAL replication is good because the WAL describes the data at a very low level, i.e. which bytes were changed in which disk blocks. Database version upgrades are therefore often incompatible, and might require some downtime.

You can't just send every query to all your followers to execute, because `RAND()` and `NOW()` won't do the same thing on every machine. Also, queries are highly order-sensitive, so you might be executing an UPDATE before a SELECT if you send them slightly off.

There is also logical (row-based replication), which is a bit like sending updated rows to followers, and trigger-based replication, if you want your application to be in involved.

#### Problems with Replication Lag

Using asynchronous replication, lag in replication means your followers are only *eventually consistent*.

Eventual consistency can be a problem if a user needs fresh data, for example:

* User creates something in the database. This is an INSERT statement and is handled by the leader.
* User creates the same thing from the database. This is a SELECT statement, and is handled by a follower that is currently lagging in replication. Therefore, that data the user just INSERTed is not there.
* Mitigation: **always read your own writes from the leader**. For example, if the user updates their own profile, they should really be reading the profile back from the leader.

##### Monotonic Reads

If you have multiple followers, and one lags behind another more, then the user can achieve the following:

* User 1 UPDATEs something in the leader. Leader broadcasts the change to followers 1 and 2.
* Follower 1 catches up.
* User 2 reads data from follower 1, which is an updated version by user 1.
* User 2 reads data from follower 2, which is still lagging behind. Therefore, from user 2's point of view, the data just went back in time.
* Mitigation: **make sure each user reads the data from the same replica**. Different users can read from different replicas; they just need to stick to one. Reroute the query to another replica if the selected one is unavailable.

##### Consistent Prefix Reads

In a partitioned (sharded) database setup, partitions operate independently, so there is no global ordering of writes. Therefore, if one partition replicates slower than others, then changes may replicate out of order, and SELECT queries from them will return data out of order as well.

* Mitigation: **group related writes to be executed in the same partition**. This is called *consistent prefix reads*: if a series of writes occurred in one order, then people reading those writes will see them in the same order.

##### Solutions for Replication Lag

"Be mindful when needed", basically

#### Multi-Leader Replication

* We allow more than one node to process writes. All nodes must broadcast their changes to all other nodes.
* Use BDR for Postgres.
* Multi-leader configuration is prone to faulty auto-incrementing keys, triggers, integrity constraints, and **should be avoided where possible**.
* Your synced calendars on your devices can be thought of as multi-leader: each device is a master node, and your nodes *very* often go offline. When they go back online, the events in the calendars can be wildly different, to the point of conflict.
* On the Google Docs question: ["If you want to guarantee that there will be no editing conflicts, the application must obtain a lock on the document before a user can edit it. If another user wants to edit the same document, they first have to wait until the first user has committed their changes and released the lock"][2], with the caveat that the lock can be limited to a character, so it does not interrupt other users as much.

|      | Single-leader                                                                    | Multi-leader                                                                   |
|------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Pros | No need for conflict resolution                                                  | Each leader can work on their own if one fails; less prone to network problems |
| Cons | Lag on writes because it relies on the leader; leader is single point of failure | Conflicts                                                                      |

##### Handling Write Conflicts

Write conflicts don't happen in a single-leader configuration. This only happens when there are multiple leaders. There are various application-level strategies to avoid them:

* Avoid conflicts by directing categories of writes to the same leader, but you need to make sure these writes are redirected to a another leader if the designated leader is down.
* Give each write a unique ID. In case of conflict, the write with the highest ID wins. You can also do (timestamp, latest write wins), but the author said this is more prone to data loss.
* Custom application-level resolution.
  * Automatic conflict resolution algorithms, like *CRDTs*, *Mergable persistent data structures*, and *operational transformation* (whatever Google Docs uses).

##### Multi-Leader Replication Topologies

* Circular: writes are forwarded to whichever node the node thinks is "the next node". This replication flow can be disrupted if one node is down.
* Star: writes are forwarded to and from a root node. This replication flow can be disrupted if the root node is down.
* All-to-all: writes are forwarded to every node a node knows about. This is also the only topology where data does not need to travel between more than one level of nodes, but is susceptible to network congestion, and out-of-order replication that comes with it.

#### Leaderless Replication

There may be a coordinator node (which redirects a client's writes to all other nodes), or there may be none (the client sends writes to all nodes on its own). In either case, the coordinator node does not enforce a particular ordering of writes. Version numbers are used to determine which write is newer (wins).

Cassandra has a leaderless replication mode.

* There is no WAL (or single source of truth), so an anti-entropy process looks for differences between replicas, and attempts to minimise the difference in data stored in each replica.
* *Quorum consistency*: for an `n`-node setup, each write should be confirmed by `w` nodes, and reads should be confirmed with `r` nodes. It is common for `n` to be an odd number to make consensus easier. The higher the `r`/`w`, the higher the latency. If the required `r`/`w` cannot be met because too many nodes are down, then the read or write fails.
* If the majority of your nodes decides to be broken, or if your write nodes are not the same as read nodes, then your consensus is broken as well, so there are definitely drawbacks.

##### Sloppy Quorums and Hinted Handoff

Quorum-based leaderless setups can tolerate failure of nodes, or slowness of individual nodes (because it doesn't need all nodes to return quickly). This makes the setup good for high-availability and low-latency work, if the application can tolerate the occasional stale read.

However, a network outage can potentially cause the cluster to drop enough nodes to never reach a quorum.

By allowing writes to temporarily write to nodes that aren't usually the ones to handle writes for a certain value, we achieve *sloppy quorums*... and when network is restored, these writes are synced to their home nodes (aka *hinted handoff*).

##### Multi-datacenter operation, detecting concurrent writes, version vectors, etc

All this stuff is in the book, but since I won't need it any time soon, you are free to read these sections yourself.

## Chapter 6: Partitioning

Partitioning is the same as *sharding*.

* Normally, data goes to designated partitions, making each partition a mini database on its own.
* Partitioning distributes database load across more DB instances. You may also achieve parallel reads for certain queries.
* A node may store more than one partition. We did that once in one of the leader-follower examples, where a leader node contains a follower partition for another leader node.

### Partitioning of Key-Value Data

* The goal of partitioning is to distribute load, so if you don't partition right, and put all your load on some nodes and not others, we call that *skewed* (the busy nodes are called "hot spots").

|            | Partitioning randomly                    | Partitioning by key range                                    | Partitioning by hash                       |
|------------|------------------------------------------|--------------------------------------------------------------|--------------------------------------------|
| What it is | Values are written to random nodes       | Partition by a range, e.g. time, letter of the alphabet, etc | Hash the key and select node based on that |
| Pros       | Load is evenly distributed               | Easy range scans                                             | Load is evenly distributed                 |
| Cons       | You don't know where you wrote the value | Potentially leads to hot spots                               | Ineffective range scans                    |

* Range queries are not *impossible* on hash partitioning; the query will simply be sent to all partitions, which makes it ineffective.
* Workloads continue to be skewed when one particular value is very popular, e.g. a celebrity's page. The book says you'll have to deal with that on your own.

### Partitioning and Secondary Indexes

* Secondary indexes help look up rows by value, but their results don't map nearly to partitions.
* Secondary indexes partitioned by document: since secondary indexes are (more likely than not) individually created on each partition only for the records in it, searching by secondary index becomes *scatter / gather*, and is slow.
* Secondary indexes partitioned by term: a partition can store an index for data that is not in it, but rather pointing to data in another partition. So your query for "red cars" goes to only one partition, who knows where all the records are for red cars.

|            | Partitioning by term ("global index")                                   | Partitioning by document                           |
|------------|-------------------------------------------------------------------------|----------------------------------------------------|
| What it is | Partition keeps secondary index for data on any partition               | Partition keeps secondary index for data on itself |
| Pros       | A query by secondary index does not need to go to all partitions        |                                                    |
| Cons       | Difficult to maintain the index; writes are slower and more complicated | Increased load on reads                            |

* Updates to secondary global indexes are often asynchronous due to the network cost.

### Rebalancing Partitions

Rebalancing moves data from one node to another, e.g. when a new node is added, replaced, or failed (data goes to remaining nodes).

#### Strategies

* The `(hash) mod n` strategy forces many keys to shift between nodes when n changes. This is not a viable strategy.
* Fixed number of partitions: split data in your nodes into thousands of partitions. (Hear the book out.) When a new node is added, it can steal several partitions from existing nodes, and start serving that. Most of the data didn't need to move between nodes. When a node is removed, this happens in reverse.
* Dynamic partitioning: partitions are dynamically split into two as their sizes grow. MongoDB supports this out of the box.
* Partitioning proportionally to nodes: have a fixed number of partitions per node. Adding more nodes makes partitions smaller again. This keeps the size of partitions relatively stable.

## Transactions

Transactions group several reads and writes into a logical unit. With that, the application does not need to worry about partial failures.

### ACID

* Atomicity: all statements in a transaction are executed as a whole. A failure means everything in the transaction is rolled back.
* Consistency: the database is in a good state... like constraints and stuff.
* Isolation: the effects of a partially-executed transaction are not visible to other transactions. (There is a looser definition that says the state of the database should be left the same way as if the queries in parallel transactions were executed serially.)
* Durability: once committed, the effects of a transaction stays in the database, even in case of failure.

Some database systems don't guarantee durability. In particular, leaderless databases will often leave the database in a bad state if it finds itself unable to fix a problem. It then becomes the application's responsibility to be resilient against these errors.

### Weak isolation

Serialisable transactions ("isolation") have a cost, and some database systems don't want to pay that cost. These systems have limited isolation, and the quirks from which have caused bugs that cost companies real money.

| Level                  |                                           |
|------------------------|-------------------------------------------|
| Read committed (1)     | No dirty-reads, no dirty writes           |
| Snapshot isolation (2) | Each transaction reads from a DB snapshot |

* "dirty-read" means transaction A can see what transaction B wrote, but before B is committed.
* "dirty-write" means transaction A can overwrite what transaction B wrote, but before B is committed. (There's a cool ["car dealer" case study][3] in the book.)
* "nonrepeatable read" (write skew) happens when you run two identical queries in a transaction (with no updates in between), but get different values for each, because another transaction updated the values from outside.

[1]: https://www.ibm.com/docs/en/powerha-aix/7.2?topic=aix-high-availability-versus-fault-tolerance
[2]: https://www.goodreads.com/quotes/9471841-if-you-want-to-guarantee-that-there-will-be-no
[3]: https://ebrary.net/64771/computer_science/dirty_writes
