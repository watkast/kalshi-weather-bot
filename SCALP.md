# Range-Scalp Bot

*Updated Sun Oct 18 23:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23122 | 20099 | 3023 (30) | 2 | $-6934.19 | -4.8% |
| **+10¢** | 17386 | 13898 | 3488 (44) | 3 | $-6230.34 | -5.7% |
| **+15¢** | 14581 | 10821 | 3760 (66) | 3 | $-5671.58 | -6.2% |
| **+20¢** | 12911 | 8979 | 3932 (84) | 3 | $-5052.76 | -6.2% |
| **+10¢ (15¢ stop)** | 28456 | 28405 | 51 (30) | 0 | $-10868.39 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 23:43 | +5 | BTC | UP | 0.45 | 0.68 | 1.96 |
| 10-18 23:43 | +10 stop | SOL | DOWN | 0.51 | 0.64 | 0.95 |
| 10-18 23:43 | +20 | SOL | DOWN | 0.51 | 0.82 | 2.81 |
| 10-18 23:43 | +15 | SOL | DOWN | 0.51 | 0.82 | 2.81 |
| 10-18 23:43 | +10 | SOL | DOWN | 0.52 | 0.64 | 0.85 |
| 10-18 23:43 | +5 | SOL | DOWN | 0.53 | 0.58 | 0.14 |
| 10-18 23:42 | +10 stop | ETH | DOWN | 0.63 | 0.90 | 2.48 |
| 10-18 23:42 | +20 | ETH | DOWN | 0.63 | 0.90 | 2.48 |
| 10-18 23:42 | +15 | ETH | DOWN | 0.63 | 0.90 | 2.48 |
| 10-18 23:42 | +10 | ETH | DOWN | 0.63 | 0.90 | 2.48 |
| 10-18 23:42 | +5 | ETH | DOWN | 0.63 | 0.90 | 2.48 |
| 10-18 23:42 | +5 | DOGE | DOWN | 0.61 | 0.89 | 2.56 |
| 10-18 23:42 | +10 stop | BTC | UP | 0.65 | 0.30 | -3.81 |
| 10-18 23:42 | +15 | BTC | UP | 0.63 | open |  |
| 10-18 23:42 | +10 | BTC | UP | 0.63 | open |  |
| 10-18 23:42 | +5 | BTC | UP | 0.63 | 0.69 | 0.28 |
| 10-18 23:42 | +10 stop | BTC | DOWN | 0.47 | 0.66 | 1.56 |
| 10-18 23:42 | +10 | BTC | DOWN | 0.47 | 0.66 | 1.56 |
| 10-18 23:42 | +5 | BTC | DOWN | 0.47 | 0.66 | 1.56 |
| 10-18 23:42 | +10 stop | BNB | UP | 0.70 | 0.85 | 1.26 |
| 10-18 23:41 | +10 stop | BTC | DOWN | 0.44 | 0.54 | 0.64 |
| 10-18 23:41 | +15 | BTC | DOWN | 0.43 | 0.66 | 1.96 |
| 10-18 23:41 | +10 | BTC | DOWN | 0.43 | 0.54 | 0.74 |
| 10-18 23:41 | +5 | BTC | DOWN | 0.43 | 0.54 | 0.74 |
| 10-18 23:40 | +10 stop | BNB | DOWN | 0.63 | 0.44 | -2.25 |
| 10-18 23:40 | +10 stop | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 10-18 23:40 | +15 | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 10-18 23:40 | +10 | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 10-18 23:40 | +5 | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 10-18 23:40 | +15 | DOGE | DOWN | 0.71 | 0.89 | 1.58 |
| 10-18 23:40 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.32 |
| 10-18 23:39 | +10 stop | NEAR | DOWN | 0.34 | 0.52 | 1.46 |
| 10-18 23:39 | +20 | NEAR | DOWN | 0.34 | open |  |
| 10-18 23:39 | +15 | NEAR | DOWN | 0.34 | 0.52 | 1.46 |
| 10-18 23:39 | +10 | NEAR | DOWN | 0.34 | 0.52 | 1.46 |
| 10-18 23:39 | +5 | NEAR | DOWN | 0.34 | 0.52 | 1.46 |
| 10-18 23:39 | +10 stop | BNB | DOWN | 0.66 | 0.47 | -2.24 |
| 10-18 23:39 | +20 | BNB | DOWN | 0.66 | open |  |
| 10-18 23:39 | +15 | BNB | DOWN | 0.66 | open |  |
| 10-18 23:39 | +10 | BNB | DOWN | 0.66 | open |  |
