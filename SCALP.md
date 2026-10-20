# Range-Scalp Bot

*Updated Tue Oct 20 19:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26123 | 22752 | 3371 (32) | 1 | $-7614.50 | -4.6% |
| **+10¢** | 19662 | 15768 | 3894 (47) | 3 | $-6718.07 | -5.4% |
| **+15¢** | 16455 | 12264 | 4191 (71) | 3 | $-5999.90 | -5.8% |
| **+20¢** | 14559 | 10167 | 4392 (90) | 4 | $-5379.67 | -5.9% |
| **+10¢ (15¢ stop)** | 32008 | 31955 | 53 (30) | 2 | $-11747.18 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 19:55 | +10 stop | BNB | DOWN | 0.68 | open |  |
| 10-20 19:55 | +10 | BNB | DOWN | 0.68 | open |  |
| 10-20 19:55 | +5 | BNB | DOWN | 0.68 | open |  |
| 10-20 19:55 | +10 stop | BTC | DOWN | 0.71 | open |  |
| 10-20 19:55 | +10 | BTC | DOWN | 0.71 | open |  |
| 10-20 19:55 | +5 | BTC | DOWN | 0.71 | 0.79 | 0.53 |
| 10-20 19:55 | +10 stop | ETH | UP | 0.45 | 0.28 | -2.03 |
| 10-20 19:55 | +10 | ETH | UP | 0.45 | open |  |
| 10-20 19:55 | +5 | ETH | UP | 0.45 | 0.53 | 0.44 |
| 10-20 19:53 | +10 stop | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 10-20 19:53 | +20 | DOGE | UP | 0.71 | open |  |
| 10-20 19:53 | +15 | DOGE | UP | 0.71 | open |  |
| 10-20 19:53 | +10 | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 10-20 19:53 | +5 | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 10-20 19:53 | +10 | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-20 19:53 | +5 | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-20 19:53 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 10-20 19:52 | +10 stop | BTC | UP | 0.69 | 0.82 | 1.04 |
| 10-20 19:51 | +10 stop | BNB | UP | 0.69 | 0.81 | 0.94 |
| 10-20 19:51 | +20 | BNB | UP | 0.69 | open |  |
| 10-20 19:51 | +15 | BNB | UP | 0.69 | open |  |
| 10-20 19:51 | +10 | BNB | UP | 0.69 | 0.81 | 0.94 |
| 10-20 19:51 | +5 | BNB | UP | 0.69 | 0.76 | 0.42 |
| 10-20 19:50 | +10 stop | ETH | UP | 0.65 | 0.75 | 0.70 |
| 10-20 19:50 | +20 | ETH | UP | 0.65 | open |  |
| 10-20 19:50 | +15 | ETH | UP | 0.65 | open |  |
| 10-20 19:50 | +10 | ETH | UP | 0.65 | 0.75 | 0.70 |
| 10-20 19:50 | +5 | ETH | UP | 0.65 | 0.70 | 0.19 |
| 10-20 19:49 | +10 stop | BTC | UP | 0.60 | 0.45 | -1.85 |
| 10-20 19:49 | +10 | BTC | UP | 0.60 | 0.74 | 1.09 |
| 10-20 19:49 | +5 | BTC | UP | 0.60 | 0.67 | 0.37 |
| 10-20 19:49 | +10 stop | BTC | DOWN | 0.46 | 0.56 | 0.64 |
| 10-20 19:49 | +20 | BTC | DOWN | 0.46 | 0.71 | 2.17 |
| 10-20 19:49 | +15 | BTC | DOWN | 0.46 | 0.64 | 1.45 |
| 10-20 19:49 | +10 | BTC | DOWN | 0.46 | 0.56 | 0.64 |
| 10-20 19:49 | +5 | BTC | DOWN | 0.46 | 0.56 | 0.64 |
| 10-20 19:48 | +5 | ETH | UP | 0.63 | 0.74 | 0.79 |
| 10-20 19:47 | +5 | BNB | UP | 0.70 | 0.75 | 0.21 |
| 10-20 19:47 | +5 | ETH | UP | 0.56 | 0.64 | 0.45 |
| 10-20 19:47 | +10 stop | SOL | UP | 0.66 | 0.77 | 0.81 |
