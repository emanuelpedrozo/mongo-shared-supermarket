rs.initiate(
    {
       _id: "shard02",
       version: 1,
       members: [
          { _id: 0, host : "mongo-shard2a:27019" },
          { _id: 1, host : "mongo-shard2b:27019" },
       ]
    }
 )