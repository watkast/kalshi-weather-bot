# Range-Scalp Bot

*Updated Fri Oct 16 05:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18732 | 16268 | 2464 (28) | 1 | $-5714.82 | -4.8% |
| **+10¢** | 14115 | 11267 | 2848 (40) | 4 | $-5159.86 | -5.8% |
| **+15¢** | 11833 | 8768 | 3065 (59) | 7 | $-4671.47 | -6.3% |
| **+20¢** | 10507 | 7299 | 3208 (78) | 9 | $-4102.61 | -6.2% |
| **+10¢ (15¢ stop)** | 23069 | 23019 | 50 (29) | 3 | $-8911.07 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 05:39 | +10 | XRP | UP | 0.54 | 0.64 | 0.65 |
| 10-16 05:39 | +5 | XRP | UP | 0.54 | 0.64 | 0.65 |
| 10-16 05:39 | +10 stop | ZEC | DOWN | 0.56 | open |  |
| 10-16 05:38 | +10 stop | DOGE | UP | 0.67 | open |  |
| 10-16 05:38 | +10 stop | XRP | UP | 0.69 | open |  |
| 10-16 05:38 | +10 stop | SOL | DOWN | 0.46 | 0.68 | 1.86 |
| 10-16 05:38 | +10 | SOL | DOWN | 0.46 | 0.68 | 1.86 |
| 10-16 05:38 | +5 | SOL | DOWN | 0.46 | 0.68 | 1.86 |
| 10-16 05:38 | +10 stop | DOGE | DOWN | 0.37 | 0.61 | 2.06 |
| 10-16 05:37 | +10 stop | XRP | DOWN | 0.64 | 0.38 | -2.94 |
| 10-16 05:37 | +5 | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-16 05:37 | +10 stop | SOL | DOWN | 0.57 | 0.71 | 1.07 |
| 10-16 05:37 | +20 | SOL | DOWN | 0.57 | open |  |
| 10-16 05:37 | +15 | SOL | DOWN | 0.57 | open |  |
| 10-16 05:37 | +10 | SOL | DOWN | 0.57 | 0.71 | 1.07 |
| 10-16 05:37 | +5 | SOL | DOWN | 0.57 | 0.71 | 1.07 |
| 10-16 05:37 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-16 05:35 | +10 stop | ZEC | DOWN | 0.62 | 0.78 | 1.31 |
| 10-16 05:35 | +10 stop | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 10-16 05:35 | +5 | BTC | DOWN | 0.56 | 0.62 | 0.25 |
| 10-16 05:34 | +10 stop | XRP | UP | 0.59 | 0.34 | -2.83 |
| 10-16 05:34 | +20 | XRP | UP | 0.59 | open |  |
| 10-16 05:34 | +15 | XRP | UP | 0.59 | open |  |
| 10-16 05:34 | +10 | XRP | UP | 0.59 | 0.71 | 0.88 |
| 10-16 05:34 | +5 | XRP | UP | 0.59 | 0.65 | 0.27 |
| 10-16 05:34 | +10 stop | DOGE | UP | 0.63 | 0.47 | -1.95 |
| 10-16 05:34 | +20 | DOGE | UP | 0.62 | open |  |
| 10-16 05:34 | +15 | DOGE | UP | 0.62 | open |  |
| 10-16 05:34 | +10 | DOGE | UP | 0.62 | open |  |
| 10-16 05:34 | +5 | DOGE | UP | 0.62 | 0.68 | 0.27 |
| 10-16 05:34 | +10 stop | BNB | UP | 0.68 | 0.48 | -2.38 |
| 10-16 05:34 | +20 | BNB | UP | 0.68 | open |  |
| 10-16 05:34 | +15 | BNB | UP | 0.68 | open |  |
| 10-16 05:34 | +10 | BNB | UP | 0.68 | open |  |
| 10-16 05:34 | +5 | BNB | UP | 0.68 | 0.77 | 0.57 |
| 10-16 05:34 | +10 stop | ETH | UP | 0.67 | 0.81 | 1.13 |
| 10-16 05:34 | +20 | ETH | UP | 0.67 | open |  |
| 10-16 05:34 | +15 | ETH | UP | 0.67 | open |  |
| 10-16 05:34 | +10 | ETH | UP | 0.67 | 0.81 | 1.13 |
| 10-16 05:34 | +5 | ETH | UP | 0.67 | 0.81 | 1.13 |
