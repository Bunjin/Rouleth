# ROULETH Smart Contract



Current contract address :
http://etherscan.io/address/0x18a672e11d637fffadccc99b152f4895da069601

 Roulette on ethereum blockchain !
  (with full DAO membership structure) 

   website : www.rouleth.com
   with a gorgeous roulette :) !


  Stake : Variable, check on website for the max bet.
  There is no min bet, you can play for free (except transaction fees from ethereum blockchain of about 0.003eth per full game)


#How to play ?

  0) Simplest : Use Metamask plugin

Other way to play :

  1)(via transactions from your wallet, **not an exchange nor a contract**) : 
  Just *send the value you want to bet* (check max bet on website) *to the contract address* and add enough gas 
  (you can enter the max *gas amount of  300 000*, any excess is refunded anyways)
  This will by default place a *bet on number on red*
  Once your bet has been recorded wait 15 secs (1 block) and send (with 200 000) 1 wei (or any amount, it will be refunded)
  This will spin the wheel and you will receive 2 times your bet if you win.
  Don't wait more than 50 blocks before you spin the wheel or your bet will expire.
  Any amount you send in excess of the max bet or when spinning the wheel is immediatly refunded.



  2) Easy Play with website www.rouleth.com :
  Use the website to select a bet on the board. Use the transaction data displayed in your favorite wallet and send the amount you want to bet (check the max bet on the website). Be sure to add the amount of gas displayed on the website.
  Enter your wallet's address on the website and verify that your bet has been recorded (wait for the ethereum blockchain to update). After 12 secs you can use the new transaction informations displayed on the website to spin the wheel sending a new transaction.
  Once the ethereum blockchain has solved your bet (~10secs), you can see the wheel spin and check the result by using the update button on the website (if you haven't changed the entered address).
  If you want to play again, just select a new bet and follow the same process.
  
  3) Advanced with Mist : 
  Import the contract in Mist wallet using the code of the ABI (link on my website)
  Use the functions (betOnNumber, betOnColor ...) to place any type of bet you want
  Provide the appropriate input (ex: check box Red or Black)
  add the amount you want to bet.
  wait 1 blocks, then use the function spinTheWheel, this will solve the bet.
  You can only place one bet at a time before you spin the wheel.
  Don't wait more than 50 blocks before you spin the wheel or your bet will expire.
  
  Use the website to track your bets and the results of the spins

  4) You can also join Rouleth DAO, that will increase the payroll and the maximum bet !

  Have fun and play responsibly. Remember this is a betting game and don't bet more than you can afford !
  
  This game in its current form is designed essentially as a proof of concept for ethereum.
