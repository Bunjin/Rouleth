#  WHYSOS3RIOUS   PRESENTS :   
# The ROULETH 

Full interface on : www.rouleth.com

Launch GIF : http://i.imgur.com/uQdcJXm.gifv

Current contract address :
http://etherscan.io/address/0x05240da139d30034eaae15737610bfbe68b97910

  Play the Roulette on ethereum blockchain !
  (or become an investor in the Casino and share the profits/losses.) 


   website : www.rouleth.com
               with a flashy roulette :) !

 *** coded by WhySoS3rious, 2016.                                       ***//
 *** please do not copy without authorization                          ***//
 *** contact : reddit    /u/WhySoS3rious                               ***//
 

  Stake : Variable, check on website for the max bet.
  Current max stake is 0.25 ETH, there is no min bet, you can play for free (except transaction fees from ethereum)


#How to play ?


  1) Simplest (via transactions from your wallet, not an exchange) : 
  Just send the value you want to bet to the contract and add enough gas 
  (you can enter the max gas amount of  300 000, any excess is refunded anyways)
  This will by default place a bet on number on red
  Once your bet has been recorded wait 15 secs (1 block) and send (with 200 000) 1 wei (or any amount, it will be refunded)
  This will spin the wheel and you will receive 2 times your bet if you win.
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
   
   

   
   Finally note that this is only an autonomous contract uploaded to ethereum blockchain. It's experimental software
   and not a safe investment. If you chose to participate, take the time to read the code and do so under your own responsability.

   Any questions, concerns, comments and criticizisms ? Contact me :  whysos3rious  \at whysos3rious.com
   
