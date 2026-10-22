# Range-Scalp Bot

*Updated Thu Oct 22 20:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29211 | 25432 | 3779 (39) | 7 | $-8570.68 | -4.7% |
| **+10¢** | 21909 | 17536 | 4373 (55) | 7 | $-7693.28 | -5.6% |
| **+15¢** | 18342 | 13644 | 4698 (78) | 7 | $-6884.21 | -6.0% |
| **+20¢** | 16238 | 11313 | 4925 (100) | 7 | $-6213.97 | -6.1% |
| **+10¢ (15¢ stop)** | 35865 | 35806 | 59 (32) | 1 | $-13534.30 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 20:12 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 10-22 20:12 | +5 | ZEC | DOWN | 0.67 | open |  |
| 10-22 20:10 | +10 stop | ETH | DOWN | 0.63 | 0.75 | 0.89 |
| 10-22 20:09 | +10 stop | ETH | UP | 0.71 | 0.56 | -1.83 |
| 10-22 20:09 | +15 | ETH | UP | 0.71 | open |  |
| 10-22 20:09 | +10 | ETH | UP | 0.71 | open |  |
| 10-22 20:09 | +5 | ETH | UP | 0.71 | open |  |
| 10-22 20:09 | +10 stop | HYPE | UP | 0.55 | 0.20 | -3.80 |
| 10-22 20:09 | +10 stop | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 10-22 20:09 | +15 | BNB | DOWN | 0.56 | 0.79 | 1.96 |
| 10-22 20:09 | +10 | BNB | DOWN | 0.56 | 0.69 | 0.93 |
| 10-22 20:09 | +5 | BNB | DOWN | 0.56 | 0.69 | 0.93 |
| 10-22 20:08 | +10 stop | SOL | DOWN | 0.67 | 0.46 | -2.44 |
| 10-22 20:08 | +10 stop | ZEC | UP | 0.70 | 0.48 | -2.53 |
| 10-22 20:07 | +5 | ZEC | UP | 0.64 | 0.72 | 0.48 |
| 10-22 20:07 | +10 stop | BNB | DOWN | 0.57 | 0.75 | 1.48 |
| 10-22 20:07 | +10 stop | ETH | DOWN | 0.66 | 0.51 | -1.84 |
| 10-22 20:07 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 10-22 20:06 | +10 stop | HYPE | DOWN | 0.69 | 0.49 | -2.34 |
| 10-22 20:06 | +5 | ZEC | UP | 0.63 | 0.72 | 0.58 |
| 10-22 20:05 | +10 stop | ETH | DOWN | 0.51 | 0.61 | 0.65 |
| 10-22 20:05 | +5 | ETH | DOWN | 0.52 | 0.61 | 0.55 |
| 10-22 20:05 | +10 stop | HYPE | DOWN | 0.59 | 0.73 | 1.09 |
| 10-22 20:05 | +10 stop | XRP | DOWN | 0.56 | 0.76 | 1.69 |
| 10-22 20:05 | +5 | ZEC | UP | 0.60 | 0.65 | 0.17 |
| 10-22 20:04 | +10 stop | DOGE | DOWN | 0.69 | 0.46 | -2.63 |
| 10-22 20:04 | +10 stop | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 10-22 20:03 | +10 stop | NEAR | UP | 0.54 | 0.29 | -2.83 |
| 10-22 20:03 | +10 | NEAR | UP | 0.54 | open |  |
| 10-22 20:03 | +5 | NEAR | UP | 0.54 | open |  |
| 10-22 20:03 | +5 | DOGE | UP | 0.54 | open |  |
| 10-22 20:02 | +10 stop | HYPE | UP | 0.62 | 0.42 | -2.35 |
| 10-22 20:02 | +20 | HYPE | UP | 0.62 | open |  |
| 10-22 20:02 | +15 | HYPE | UP | 0.62 | open |  |
| 10-22 20:02 | +10 | HYPE | UP | 0.66 | open |  |
| 10-22 20:02 | +5 | HYPE | UP | 0.66 | open |  |
| 10-22 20:02 | +10 stop | ETH | UP | 0.55 | 0.36 | -2.25 |
| 10-22 20:02 | +10 stop | BNB | UP | 0.60 | 0.43 | -2.05 |
| 10-22 20:02 | +10 stop | DOGE | UP | 0.58 | 0.43 | -1.86 |
| 10-22 20:02 | +20 | DOGE | UP | 0.57 | open |  |
