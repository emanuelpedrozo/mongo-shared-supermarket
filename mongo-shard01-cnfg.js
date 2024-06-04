rs.initiate(
    {
       _id: "shard01",
       version: 1,
       members: [
          { _id: 0, host : "mongo-shard1a:27018" },
          { _id: 1, host : "mongo-shard1b:27018" },
       ]
    }
 )