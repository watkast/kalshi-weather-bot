# Range-Scalp Bot

*Updated Mon Oct 26 21:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35434 | 30930 | 4504 (43) | 4 | $-9887.28 | -4.4% |
| **+10¢** | 26498 | 21286 | 5212 (65) | 4 | $-8725.78 | -5.2% |
| **+15¢** | 22174 | 16564 | 5610 (89) | 2 | $-7821.79 | -5.6% |
| **+20¢** | 19661 | 13782 | 5879 (112) | 3 | $-6878.44 | -5.6% |
| **+10¢ (15¢ stop)** | 43451 | 43389 | 62 (33) | 0 | $-16543.21 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 21:12 | +10 stop | NEAR | UP | 0.68 | 0.50 | -2.14 |
| 10-26 21:11 | +10 stop | ZEC | UP | 0.55 | 0.74 | 1.58 |
| 10-26 21:11 | +10 stop | SOL | UP | 0.65 | 0.79 | 1.13 |
| 10-26 21:11 | +10 stop | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 10-26 21:10 | +10 | ETH | UP | 0.67 | 0.84 | 1.44 |
| 10-26 21:10 | +10 stop | ETH | UP | 0.70 | 0.84 | 1.15 |
| 10-26 21:10 | +20 | ETH | UP | 0.70 | 0.91 | 1.86 |
| 10-26 21:10 | +15 | ETH | UP | 0.70 | 0.89 | 1.68 |
| 10-26 21:10 | +10 stop | DOGE | DOWN | 0.37 | 0.61 | 2.06 |
| 10-26 21:10 | +5 | XRP | UP | 0.57 | 0.71 | 1.07 |
| 10-26 21:09 | +10 stop | ZEC | DOWN | 0.66 | 0.47 | -2.25 |
| 10-26 21:09 | +10 stop | XRP | UP | 0.57 | 0.71 | 1.07 |
| 10-26 21:09 | +20 | XRP | UP | 0.57 | 0.80 | 2.00 |
| 10-26 21:09 | +15 | XRP | UP | 0.57 | 0.73 | 1.28 |
| 10-26 21:09 | +5 | XRP | UP | 0.57 | 0.63 | 0.25 |
| 10-26 21:09 | +10 stop | NEAR | DOWN | 0.64 | 0.41 | -2.64 |
| 10-26 21:09 | +15 | BNB | UP | 0.71 | 0.86 | 1.26 |
| 10-26 21:09 | +10 | BNB | UP | 0.71 | 0.82 | 0.84 |
| 10-26 21:09 | +5 | BNB | UP | 0.71 | 0.82 | 0.84 |
| 10-26 21:08 | +10 stop | BNB | UP | 0.69 | 0.82 | 1.04 |
| 10-26 21:08 | +5 | XRP | DOWN | 0.51 | 0.62 | 0.75 |
| 10-26 21:08 | +5 | XRP | DOWN | 0.59 | 0.68 | 0.57 |
| 10-26 21:07 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-26 21:06 | +10 stop | XRP | DOWN | 0.63 | 0.38 | -2.84 |
| 10-26 21:06 | +10 | XRP | DOWN | 0.63 | open |  |
| 10-26 21:06 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 10-26 21:06 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-26 21:06 | +10 stop | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 10-26 21:06 | +10 stop | BNB | DOWN | 0.59 | 0.44 | -1.85 |
| 10-26 21:06 | +10 stop | SOL | DOWN | 0.69 | 0.46 | -2.63 |
| 10-26 21:06 | +10 | SOL | DOWN | 0.69 | open |  |
| 10-26 21:06 | +5 | SOL | DOWN | 0.69 | open |  |
| 10-26 21:06 | +5 | ETH | DOWN | 0.55 | open |  |
| 10-26 21:05 | +10 stop | ETH | UP | 0.46 | 0.58 | 0.84 |
| 10-26 21:05 | +15 | ETH | UP | 0.46 | 0.73 | 2.38 |
| 10-26 21:05 | +10 | ETH | UP | 0.47 | 0.58 | 0.74 |
| 10-26 21:05 | +5 | ETH | UP | 0.47 | 0.55 | 0.44 |
| 10-26 21:05 | +10 stop | ZEC | DOWN | 0.62 | 0.80 | 1.51 |
| 10-26 21:05 | +10 stop | BNB | UP | 0.59 | 0.39 | -2.34 |
| 10-26 21:05 | +20 | BNB | UP | 0.59 | 0.82 | 2.02 |
