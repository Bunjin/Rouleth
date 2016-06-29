**INVESTMENTS MUST BE MADE ONLY FROM A REGULAR ETHEREUM ADDRESS THAT YOU OWN. NO CONTRACTS, NO EXCHANGES**

www.rouleth.com/how_to_invest.pdf

#Why invest ?
Investments allow to increase the payroll and rise the maximum allowed bet. This will provide a better experience for all players and benefit investors in return.
Like any casino, the rouleth consists in investors putting money on the table to reward players bets. Individual players win and some lose, but on average the house has a small edge of 2.5% to pay for its service. This edge rewards the investors for the risk they are taking (if the players are extremely lucky the casino could lose money). This profit of the casino also rewards the casino for the entertaining experience it provides to its users.
The casino should be profitable in the long run (with 99% confidence). The maximum bet allowed has been computed through statistical analysis to yield high confidence in the long run survival of the casino. The maximum bet is always smaller than the current payroll of the casino * 35 (max pay multiplier) * casinoStatisticalLimit (statistical sample size that allows to have  enough confidence in survival, set at 20 at start, should increase to 200 when we have more investors to increase the safety).

#Investment rules
 
 You will become an investor and share the profits and losses of the roulette
   proportionally to your investment. There is a 2% fee on investment to help with the server/website
   cost and also 2% on profit that go to the developper.
   The rest of your investment goes directly to the payroll and 98% of profits are shared between 
   investors relatively to their share of total. Losses are split similarly.
   You can withdraw your funds at any time after the initial lock period (set initially to 1 month)
   You can specify the amount you want to withdraw in Wei.
   If your withdraw brings your investment under 10 eth (the min invest, subject to change)
   then you will execute a full withdraw and stop being an investor.
   If you don't specify an amount this will do a full withdraw of your balance.
   Check your current investor balance in Mist by using the information functions on the left side
   Note that balances are only updated to the lastest state after each invest or withdraw.
   
   At start there is a limit of 50 investors (can be changed via settings up to 250)
   If there is no open position and you want to invest, you can try to buyout a current investor.
   To buyout, you have to invest more than any investor whose funds are unlocked (after lock period)
   If there are no remaining open position and all investors are under grace period, it is not possible to 
   become a new investor in the casino.

   At any time an investor can add funds to his investment with the invest function (>min invest amount).
   Doing so will refresh the lock period and secure your position.
   
#Investment Risks :
**Provably fair and Cheat proof:** 
The contract uses future block hashes as a source of pseudo randomness. Miners could try to cheat and have better odds than normal players. We investigated this issue and it resulted that only miners with more than 3% of the network's power could do so profitably. There are only 7 pools that are of this size or bigger. There is a way to monitor cheating in this way through blockchain data analysis. We thus consider this risk to be non very likely. The results of the analysis can be found here : https://github.com/Bunjin/Rouleth/blob/master/Provably_Fair_No_Cheating.md

**Contract safety (can the funds be hacked ?) :** This is the second version of the rouleth and the first version was live for a month with ~200 Ether and no funds have been stolen in any way. The contract was already immune to the hack that affected the DAO and any other known exploit but we hardened the security of the contract for this release. The contract was reviewed extensively by several ethereum developers and no concerns were expressed so far. Also, there are failsafes that allow investors to withdraw funds immediatly in case we notice there is a problem so we can always act preventively.
All details on contract security can be found here : https://github.com/Bunjin/Rouleth/blob/master/Security.md
   
#How to invest ? 
**INVESTMENTS MUST BE MADE ONLY FROM A REGULAR ETHEREUM ADDRESS THAT YOU OWN. NO CONTRACTS, NO EXCHANGES**

*1) Without Mist* Send the amount you want to invest to the rouleth contract address (check on the address on the website) and add the following transaction data 0xe8b5e51f also set the gas to 1million. 
At any time after the lock period, you can use a transaction to withdraw fully your funds. Send a transaction to the rouleth contract address (check on the address on the website) with the following data 0x2037fcbf0000000000000000000000000000000000000000000000000000000000000000 and add 1million gas but not ether.

However without mist wallet you will not be able to check your balances nor to perform partial withdraws. 
   
*2) With Mist wallet :*
   Import the contract in Mist Wallet using the code of the ABI (link on my website)
   Use the Invest function and the withdraw function to manage your balance.
   Use the information functions to check your balance and check the profit and loss not yet updated.
   

   Finally note that this is only an autonomous contract uploaded to ethereum blockchain. It's experimental software
   and not a safe investment. If you chose to participate, take the time to read the code and do so under your own responsability.
   
   **INVESTMENTS MUST BE MADE ONLY FROM A REGULAR ETHEREUM ADDRESS THAT YOU OWN. NO CONTRACTS, NO EXCHANGES**
