sh.addShard("mongo1:27017")
sh.addShard("mongo2:27017")
sh.addShard("mongo3:27017")

sh.enableSharding("supermercado")

sh.shardCollection("supermercado.produtos", { "filial_id": 1 })