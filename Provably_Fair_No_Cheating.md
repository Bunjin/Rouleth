#A provably fair roulette :  note on Random Number Generation.
   The roulette result is based on the hash of the next block after the player commits his bet.
   This guarantees a provably fair roulette with equiprobable results and non predictable
   unless someone has more computing power than all the Ethereum Network.
   
   Yet Miners could try to exploit their position of block makers.
   They could commit a bet, then wait 1 block and hope that they will be the one forming the 
   block on which their commited bet depends. If this is the case and the hash they find is not a
   winning one, they could decide to not share the block with the network but would lose 5 ether. But then they could still submit the same block as an uncle block and get 4.375 ether. So the cost of cheating is roughly 0.625 eth per block. (The uncle reward and cheating mechanism is a bit more complex than that, depending on who and when the uncle block is included in the chain but we'll skip the detail here.)
   
   To counter this potential miner edge we just have to keep the expected reward of cheating negative for the miner to disincentivize this behavior. We have run a simulation of the potential payoffs of miner cheating and the results can be found on the rouleth's github (with a python script used for the test).
   This analysis concluded that miner cheating requires at least 3% of the hashrate of the whole network to be successful.
   If the miner has 3% of the network power, he needs to bet at least 23 ether per block to be able to extract a profit from dropping losing blocks. This bet limit (to disincentivize cheating by miner) however drops rapidly when the % of mining controlled by the cheating miner increases. A miner with 10% power only needs a bet size of 2 ether per block to be profitable, with 25% power the limit is at 1.2 ether per block.  For a miner with 51% power the required bet size to cheat is only 0.5 ether but if a miner gets this big and malicious, the whole network is already at risk and not only the rouleth !
   
   We will thus keep wager amounts small enough to make miners cheating strategies unprofitable.
   Note that a miner could place several bets on the same block to increase his potential profit from dropping a block
   For this reason we limit the number of bets per block to 2 at start (configurable later if needed).
   
   At the time of writing, there are 7 pools with more than 3% mining.
   http://etherscan.io/stats/miner?range=7
   
   We have a way to monitor cheating by the miners.
   First if they put several bets in the same block we can monitor this on the contract itself and lower the limits to prevent this type of cheating.
   Second, we can analyze the correlation between the uncles of each of these miners with the bets on the rouleth. If we notice that a miner's uncle block occur often after a bet has been placed on the rouleth we will know that something is going on.
   This analysis will be done on the blockchain frequently and any pool that tries to cheat will suffer a reputation harm when this cheating is revealed.
