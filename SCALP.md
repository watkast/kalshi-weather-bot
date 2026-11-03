# Range-Scalp Bot

*Updated Tue Nov 03 18:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46182 | 40213 | 5969 (72) | 4 | $-13289.55 | -4.6% |
| **+10¢** | 34469 | 27552 | 6917 (96) | 6 | $-12157.28 | -5.6% |
| **+15¢** | 28852 | 21416 | 7436 (124) | 6 | $-11081.69 | -6.1% |
| **+20¢** | 25630 | 17835 | 7795 (164) | 6 | $-9822.14 | -6.1% |
| **+10¢ (15¢ stop)** | 56341 | 56248 | 93 (56) | 0 | $-21130.00 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 18:51 | +10 stop | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-03 18:51 | +5 | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-03 18:50 | +10 stop | ETH | DOWN | 0.65 | 0.82 | 1.43 |
| 11-03 18:50 | +10 stop | BNB | DOWN | 0.45 | 0.55 | 0.69 |
| 11-03 18:50 | +5 | BNB | DOWN | 0.45 | 0.55 | 0.69 |
| 11-03 18:49 | +10 stop | SOL | DOWN | 0.70 | 0.84 | 1.15 |
| 11-03 18:49 | +10 stop | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-03 18:48 | +5 | BTC | UP | 0.34 | open |  |
| 11-03 18:48 | +5 | HYPE | DOWN | 0.70 | 0.76 | 0.28 |
| 11-03 18:48 | +10 stop | BTC | UP | 0.59 | 0.32 | -3.03 |
| 11-03 18:48 | +20 | BTC | UP | 0.59 | open |  |
| 11-03 18:48 | +15 | BTC | UP | 0.59 | open |  |
| 11-03 18:48 | +10 | BTC | UP | 0.59 | open |  |
| 11-03 18:48 | +5 | BTC | UP | 0.59 | 0.64 | 0.16 |
| 11-03 18:47 | +5 | HYPE | DOWN | 0.57 | 0.65 | 0.46 |
| 11-03 18:46 | +5 | XRP | UP | 0.56 | open |  |
| 11-03 18:46 | +10 stop | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 11-03 18:46 | +20 | NEAR | DOWN | 0.60 | 0.81 | 1.82 |
| 11-03 18:46 | +15 | NEAR | DOWN | 0.60 | 0.81 | 1.82 |
| 11-03 18:46 | +10 | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 11-03 18:46 | +5 | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 11-03 18:46 | +10 stop | SOL | UP | 0.60 | 0.32 | -3.13 |
| 11-03 18:46 | +20 | SOL | UP | 0.60 | open |  |
| 11-03 18:46 | +15 | SOL | UP | 0.60 | open |  |
| 11-03 18:46 | +10 | SOL | UP | 0.60 | open |  |
| 11-03 18:46 | +5 | SOL | UP | 0.60 | open |  |
| 11-03 18:46 | +10 stop | ETH | UP | 0.60 | 0.30 | -3.32 |
| 11-03 18:46 | +20 | ETH | UP | 0.59 | open |  |
| 11-03 18:46 | +15 | ETH | UP | 0.59 | open |  |
| 11-03 18:46 | +10 | ETH | UP | 0.59 | open |  |
| 11-03 18:46 | +5 | ETH | UP | 0.59 | open |  |
| 11-03 18:46 | +10 stop | DOGE | UP | 0.54 | 0.22 | -3.51 |
| 11-03 18:46 | +20 | DOGE | UP | 0.54 | open |  |
| 11-03 18:46 | +15 | DOGE | UP | 0.54 | open |  |
| 11-03 18:46 | +10 | DOGE | UP | 0.54 | open |  |
| 11-03 18:46 | +5 | DOGE | UP | 0.54 | 0.63 | 0.55 |
| 11-03 18:46 | +10 stop | BNB | UP | 0.63 | 0.47 | -1.95 |
| 11-03 18:46 | +20 | BNB | UP | 0.63 | open |  |
| 11-03 18:46 | +15 | BNB | UP | 0.63 | open |  |
| 11-03 18:46 | +10 | BNB | UP | 0.63 | open |  |
