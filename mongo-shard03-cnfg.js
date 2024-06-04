rs.initiate(
    {
       _id: "shard03",
       version: 1,
       members: [
          { _id: 0, host : "mongo-shard3a:27020" },
          { _id: 1, host : "mongo-shard3b:27020" },
       ]
    }
 )