#  WHYSOS3RIOUS   PRESENTS :   
# The ROULETH 

Full interface on : www.whysos3rious.com/rouleth

Launch GIF : http://i.imgur.com/uQdcJXm.gifv

Current contract address :
http://etherscan.io/address/0x6dfaa563d04a77aff4c4ad2b17cf4c64d2983dc8

                      , ; ,   .-'"""'-.   , ; ,
                      \\|/  .'          '.  \|//
                        \-;-/   ()   ()   \-;-/
                        // ;               ; \\
                       //__; :.         .; ;__\\
                      `-----\'.'-.....-'.'/-----'
                             '.'.-.-,_.'.'
                               '(  (..-'                                 '-'

  Play the Roulette on ethereum blockchain !
  (or become an investor in the Casino and share the profits/losses.) 


   website : www.whysos3rious.com/rouleth
               with a flashy roulette :) !

 *** coded by WhySoS3rious, 2016.                                       ***//
 *** please do not copy without authorization                          ***//
 *** contact : reddit    /u/WhySoS3rious                               ***//
 

  Stake : Variable, check on website for the max bet.
  Current max stake is 0.15 ETH


#How to play ?


  1) Simplest (via transactions from your wallet, not an exchange) : 
  Just send the value you want to bet to the contract and add enough gas 
  (you can enter the max gas amount of ~4,5Million, any excess is refunded anyways)
  This will by default place a bet on number 7
  Wait 2 minutes (6 blocks) and send (with enough gas) 1 wei (or any amount, it will be refunded)
  This will spin the wheel and you will receive * 35 your bet if you win.
  Don't wait more than 200 blocks before you spin the wheel or your bet will expire.



  2) Advanced (via contract functions, e.g. Mist, cf. tutorial on my website for more details) :
    Import the contract in Mist wallet using the code of the ABI (link on my website)
  Use the functions (betOnNumber, betOnColor ...) to place any type of bet you want
  Provide the appropriate input (ex: check box Red or Black)
  add the amount you want to bet.
  wait 6 blocks, then use the function spinTheWheel, this will solve the bet.
  You can only place one bet at a time before you spin the wheel.
  Don't wait more than 200 blocks before you spin the wheel or your bet will expire.



   Use the website to track your bets and the results of the spins


#How to invest ?
   
   Import the contract in Mist Wallet using the code of the ABI (link on my website)
   Use the Invest function with an amount >10 Ether (can change, check on my website)
   You will become an investor and share the profits and losses of the roulette
   proportionally to your investment. There is a 2% fee on investment to help with the server/website
   cost and also 2% on profit that go to the developper.
   The rest of your investment goes directly to the payroll and 98% of profits are shared between 
   investors relatively to their share of total. Losses are split similarly.
   You can withdraw your funds at any time after the initial lock period (set to 1 week)
   To withdraw use the function withdraw and specify the amoutn you want to withdraw in Wei.
   If your withdraw brings your investment under 10 eth (the min invest, subject to change)
   then you will execute a full withdraw and stop being an investor.
   Check your current investor balance in Mist by using the information functions on the left side
   If you want to update the balances to the last state (otherwise they are automatically
   updated after each invest or withdraw), you can use the function manualUpdateBalances in Mist.
   
   The casino should be profitable in the long run (with 99% confidence). The maximum bet allowed has been computed
   through statistical analysis to yield high confidence in the long run survival of the casino. The maximum bet is 
   always smaller than the current payroll of the casino * 35 (max pay multiplier) * casinoStatisticalLimit (statistical sample size that allows to have  enough confidence in survival, set at 20 at start, should increase to 200 when we have more investors to increase the safety).
   
   At start there is a limit of 50 investors (can be changed via settings up to 150)
   If there is no open position and you want to invest, you can try to buyout a current investor.
   To buyout, you have to invest more than any investor whose funds are unlocked (after 1 week grace lock period)
   If there are no remaining open position and all investors are under grace period, it is not possible to 
   become a new investor in the casino.

   At any time an investor can add funds to his investment with the invest function (>min invest amount).
   Doing so will refresh the lock period and secure your position.
   
   


#A provably fair roulette :  note on Random Number Generation.
   The roulette result is based on the hash of the 6th block after the player commits his bet.
   This guarantees a provably fair roulette with equiprobable results and non predictable
   unless someone has more computing power than all the Ethereum Network.
  Yet Miners could try to exploit their position in 2 ways.
   First they could try to mine 7 blocks in a row (to commit their bet based on result for a sure win),
   but this is highly improbable and not predictible.
   Second they could commit a bet, then wait 6 blocks and hope that they will be the one forming the 
   block on which their commited bet depends. If this is the case and the hash they find is not a
   winning one, they could decide to not share the block with the network but would lose 5 ether. But then they could still submit the same block as an uncle block and get 4.375 ether. So the cost of cheating is 0.625 eth per block.
   
   To counter this potential miner edge we just have to keep the expected reward of cheating under 0.625 eth per block.
   To do so we keep wager amounts small so that the miner prefers to get his block reward than cheat.
   Note that a miner could place several bets on the same block to increase his potential profit from dropping a block
   For this reason we limit the number of bets per block to 2 at start (configurable later if needed).
   
   The expectation per block of cheating for a miner is equal to :
   EV (cheating) = betValuePerBlock * 
                   [    (1-proba_miner_finds_block) * base_proba_to_win 
                     + proba_miner_finds_block (base_proba_to_win + base_proba_to_win^2) ]
            
   For a miner like Dwarfpool (with 50% computational power) and a bet on Red, this makes a EV of ~1/4 * betValuePerBlock
   Since this has to be smaller than 0.625 ether, we can increase the maximum bet Value per block to 4*0.625 which is 
   2,5 ether. (we would need a payroll of >1000 Ether to guarantee the statistical survival of the casino for such 
   maximum bet).
   
   Finally note that this is only an autonomous contract uploaded to ethereum blockchain. It's experimental software
   and not a safe investment. If you chose to participate, take the time to read the code and do so under your own responsability.
   
#Contract Security :
   
   Following the DAO hack, ethereum users have realized that the security oif smart contracts is something that should not be taken lightly. The hack of the DAO was performed due to a badly written smart contract and is not at all a bug of ethereum.
   The rouleth contract incorporates several security features that makes it secure against several potential attacks on smart contracts that have been identified by the community. I will list those potential threats below and explain how I secured the contract against them.
   
   1) Recursive call attack : (DAO ATTACK) --> ROULETH IS NOT VULNERABLE
   http://vessenes.com/more-ethereum-attacks-race-to-empty-is-the-real-deal/
   The attacker exploits the fact that when a contract sends ether to another contract it also executes the code in the destination contract. If the destination contract is malicious, it could try to ask the first contract to send the money again. If the first contract does not update the balances before sending, the attacker is allowed to withdraw several times a single amount.
   The rouleth code is immune to such attack for several reasons. First of all, all balances are updated before the money is sent. So even if the attacker was able to call the rouleth contract again for a second reccursive withdraw, he will not be able to withdraw more than his total balance. Moreover, since we use basic send() functions in the rouleth contract (and not call() like in the DAO), the rouleth would not send enough gas to the attacker contract, so the attacker will not be able to execute the rouleth functions again.
   
   2) Silent failing sends : call stack attacks
   http://martin.swende.se/blog/Devcon1-and-contract-security.html
   There is a limit specifying how deep contracts can call other contracts; currently set to 1024. If a contract invokes another contract (either via CALL or CALLCODE), the operation will fail if the call stack depth limit has been reached. The failure is signalled to the caller by putting a 0 on the stack (the regular stack).
   This behaviour makes it possible to subject a contract to a “call stack attack”. In such an attack, an attacker first creates a suitable depth of the stack, e.g. by recursive calls. After this step, the attacker invokes the targeted contract. If the targeted calls another contract, that call will fail. If the return value is not properly checked to see if the call was successfull, the consequences could be damaging.
   For instance, if the Rouleth was vulnerable to this threat, when the investor array is full and a new investor wants to buyout a previous investor, this new investor could devise a call stack attack to make the send to the previous investor fail. The previous investor money would stay (and be stucked) in the rouleth but the previous investor would be erased from the investors list. This would however not benefit the attacker since he could not withdraw the amount.
   In any case, I have used a method of safe send using the following code " if (previous.send(balance[previous])==false) throw; " . This code would cancel the whole transaction if an attacker were to try such an attack. If the send to the previous investor fails, this calls a "throw" which reverts the whole operation (the investor that was supposed to be buyout would not be and would this be in the investor list with the ability to withdraw his/her funds).
   
   3) Griefing attacks :
   http://vessenes.com/ethereum-griefing-wallets-send-w-throw-considered-harmful/
   The previous threat and the solution we implemented (using if ( .send(balance[previous])==false) ) could however expose the contract to an other vulnerability. A failed send reverts the whole transaction. One could invest in the rouleth from a contract that makes any send to its address fail. If the execution of the whole contract was dependent on this send, the whole contract would be stalled and investors could not withdraw because of this investor's griefing wallet. However the Rouleth is immune to this attack because every investor can withdraw their funds individually and don't trigger transactions to other users. So in the case of such an attack, only the attacker would loose funds and the rest of the contract would keep running as before.
   The only benefit that an attacker could have through this method is that he could secure himself an investor seat in the casino by causing any buyout attempt to fail. But I have the ability to increase the array of investors if needed and allow more investor to come in. Also this small potential benefit would not harm the casino in any ways, since balances, withdraws, investments and plays would not be affected.
   

   
   4) Stalled contracts : (Governmental Fail)
   https://www.reddit.com/r/ethereum/comments/4ghzhv/governmentals_1100_eth_jackpot_payout_is_stuck/
   In the Ethereum Virtual Machine, we pay transaction fees (gas) for any computation the contract code runs. There is a limit of currently a bit less than 5Million per block. Hence if the contract has to execute more computations than that, it will not be able to work anymore and be stalled.
   When he designs a smart contract, the developper must be sure that his contract can scale. Operations that are at first rather inexpensive (such as reading a list of players of 2 elements) can become very expensive when there are many users (ex. the same player list can now be composed of 1000 elements). So from the start, the developper has to create contract mechanics that scale well to avoid such computationnal cost growth.
   In the Rouleth, we have decentralized the execution of the code and every player has to make the computation for his play only. The gas cost of playing should remain the same no matter how many players played before you.
   Only 2 features of the contracts are more gas expensive and require the use of a list of elements. To avoid any scaling problem, I have thus made sure that these lists will always be short enough such that the maximum possible list will still be short enough to execute within the gas per block limits. The first of these 2 features is the investor array. We have to keep a list of all investors in the rouleth in order to share profits and losses in the right maner. We could have used a token system with an ICO, but the Rouleth implements a dynamic investment mechanism where you can join, leave, and join again at (almost) any time. For this purpose we keep track of the profit and losses and when there is a change in the investor structure, we update all investors balances using the list of investors. To avoid any problem of gas for this operation, the list of investor is currently limited to 50 elements and can be extended up to 150. This way we will always be under the gas limits per block.
   The second feature that requires some loop over a list of elements is the resolution of expired gambles when the player does not spin the wheel in the imparted time of 200 blocks currently. However because of the limit of 200 blocks (which can be lowered if needed) we can make sure that the number of gambles we have to scan will always be small enough in terms of gas costs.
   
   That's it for the list of known and important issues. If more were to be found, I will scan the contract immediatly to make sure it's not vulnerable to them. Also at any time we can use the disable betting function to stop the contract if there was some kind of cheating or hacking via the playing functions. If the investment/withdraw functions were at risk, I can also set the lockPeriod to 0, such that any investor can withdraw their funds from the contract immediatly (and does not have to wait before splitting).
   
   Any questions, concerns, comments and criticizisms ? Contact me at whysos3rious@whysos3rious.com
   
