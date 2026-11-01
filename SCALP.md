# Range-Scalp Bot

*Updated Sun Nov 01 18:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43757 | 38124 | 5633 (64) | 3 | $-12511.76 | -4.5% |
| **+10¢** | 32645 | 26138 | 6507 (85) | 3 | $-11243.72 | -5.5% |
| **+15¢** | 27325 | 20316 | 7009 (112) | 3 | $-10289.82 | -6.0% |
| **+20¢** | 24267 | 16925 | 7342 (146) | 3 | $-9086.74 | -6.0% |
| **+10¢ (15¢ stop)** | 53365 | 53279 | 86 (51) | 3 | $-20147.77 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 18:01 | +10 stop | BTC | DOWN | 0.50 | open |  |
| 11-01 18:01 | +20 | BTC | DOWN | 0.51 | open |  |
| 11-01 18:01 | +15 | BTC | DOWN | 0.54 | open |  |
| 11-01 18:01 | +10 | BTC | DOWN | 0.55 | open |  |
| 11-01 18:01 | +5 | BTC | DOWN | 0.56 | open |  |
| 11-01 18:00 | +5 | NEAR | DOWN | 0.70 | open |  |
| 11-01 18:00 | +10 stop | NEAR | DOWN | 0.70 | open |  |
| 11-01 18:00 | +20 | NEAR | DOWN | 0.70 | open |  |
| 11-01 18:00 | +15 | NEAR | DOWN | 0.70 | open |  |
| 11-01 18:00 | +10 | NEAR | DOWN | 0.70 | open |  |
| 11-01 18:00 | +10 stop | ETH | DOWN | 0.65 | open |  |
| 11-01 18:00 | +20 | ETH | DOWN | 0.65 | open |  |
| 11-01 18:00 | +15 | ETH | DOWN | 0.65 | open |  |
| 11-01 18:00 | +10 | ETH | DOWN | 0.65 | open |  |
| 11-01 18:00 | +5 | ETH | DOWN | 0.66 | open |  |
| 11-01 17:51 | +10 stop | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 11-01 17:51 | +20 | NEAR | DOWN | 0.64 | 0.87 | 2.05 |
| 11-01 17:51 | +15 | NEAR | DOWN | 0.64 | 0.87 | 2.05 |
| 11-01 17:51 | +10 | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 11-01 17:51 | +5 | NEAR | DOWN | 0.64 | 0.73 | 0.59 |
| 11-01 17:51 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-01 17:51 | +10 stop | ZEC | DOWN | 0.57 | 0.68 | 0.76 |
| 11-01 17:48 | +5 | NEAR | DOWN | 0.70 | 0.79 | 0.63 |
| 11-01 17:48 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-01 17:48 | +10 stop | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-01 17:47 | +10 stop | BNB | DOWN | 0.57 | 0.72 | 1.17 |
| 11-01 17:47 | +20 | BNB | DOWN | 0.57 | 0.81 | 2.11 |
| 11-01 17:47 | +15 | BNB | DOWN | 0.57 | 0.72 | 1.17 |
| 11-01 17:47 | +10 | BNB | DOWN | 0.57 | 0.72 | 1.17 |
| 11-01 17:47 | +5 | BNB | DOWN | 0.57 | 0.72 | 1.17 |
| 11-01 17:47 | +5 | SOL | UP | 0.56 | no | -5.78 |
| 11-01 17:46 | +10 stop | BTC | UP | 0.63 | 0.32 | -3.43 |
| 11-01 17:46 | +20 | BTC | UP | 0.63 | no | -6.47 |
| 11-01 17:46 | +15 | BTC | UP | 0.63 | no | -6.47 |
| 11-01 17:46 | +10 | BTC | UP | 0.63 | no | -6.47 |
| 11-01 17:46 | +5 | BTC | UP | 0.63 | no | -6.47 |
| 11-01 17:46 | +10 stop | XRP | UP | 0.62 | 0.36 | -2.94 |
| 11-01 17:46 | +20 | XRP | UP | 0.62 | no | -6.37 |
| 11-01 17:46 | +15 | XRP | UP | 0.62 | no | -6.37 |
| 11-01 17:46 | +10 | XRP | UP | 0.62 | no | -6.37 |
