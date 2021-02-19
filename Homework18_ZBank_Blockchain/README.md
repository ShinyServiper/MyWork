# GAINING ACCESS TO THE MATHNET BLOCKAIN NETWORK FOR ZBANK


### Node 1 Public Key:


###  Node 2 Public Key:



## To start up the nodes, execute the following commands in your terminal window GitBash for Windows users):

## Command 1:
####./geth --datadir node1 --unlock " 0xFddAF50Df523aaBbeC1016B49a65Afd23dc28909" --mine --rpc --port 30307 --allow-insecure-unlock

#### <span style="color:red">some **This is Red Bold.** text</span>

## Command 2:
#### ./geth --datadir node2 --unlock "0x04A1a1C7a28e1aCb304A9f9E620446787d1577e8" --port 30308 --bootnodes "enode://c8c49f1ad52fb94abbcf85a9c84e4e5c46212b91014eed01d70775e3cc04661810a8497e4b47269b2d126da0ea2f91b8038b96b37d09bd50f6eacf6126fcd989@127.0.0.1:30307"

## To avoid any issues with other applications using the 30303 and 30304 ports, nodes 1 and 2 have been set to run on ports 30307 and 30308 respectively
