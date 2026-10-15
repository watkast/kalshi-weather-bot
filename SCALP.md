# Range-Scalp Bot

*Updated Thu Oct 15 19:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18004 | 15627 | 2377 (28) | 0 | $-5535.04 | -4.9% |
| **+10¢** | 13602 | 10849 | 2753 (40) | 0 | $-5024.96 | -5.9% |
| **+15¢** | 11409 | 8448 | 2961 (59) | 0 | $-4534.69 | -6.3% |
| **+20¢** | 10142 | 7045 | 3097 (77) | 0 | $-3940.26 | -6.2% |
| **+10¢ (15¢ stop)** | 22166 | 22116 | 50 (29) | 0 | $-8579.09 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 19:11 | +10 stop | NEAR | UP | 0.71 | 0.47 | -2.73 |
| 10-15 19:11 | +10 stop | ETH | DOWN | 0.71 | 0.50 | -2.43 |
| 10-15 19:11 | +10 stop | NEAR | DOWN | 0.48 | 0.64 | 1.25 |
| 10-15 19:11 | +20 | NEAR | DOWN | 0.48 | 0.83 | 3.22 |
| 10-15 19:11 | +15 | NEAR | DOWN | 0.49 | 0.64 | 1.15 |
| 10-15 19:11 | +10 | NEAR | DOWN | 0.49 | 0.64 | 1.15 |
| 10-15 19:11 | +5 | NEAR | DOWN | 0.49 | 0.64 | 1.15 |
| 10-15 19:11 | +10 stop | XRP | DOWN | 0.65 | 0.42 | -2.64 |
| 10-15 19:11 | +10 stop | SOL | UP | 0.63 | 0.73 | 0.69 |
| 10-15 19:11 | +10 stop | ETH | DOWN | 0.69 | 0.53 | -1.93 |
| 10-15 19:10 | +5 | XRP | DOWN | 0.66 | yes | -6.76 |
| 10-15 19:09 | +10 stop | ETH | DOWN | 0.58 | 0.70 | 0.87 |
| 10-15 19:09 | +10 stop | SOL | UP | 0.67 | 0.51 | -1.94 |
| 10-15 19:09 | +20 | SOL | UP | 0.67 | 0.93 | 2.40 |
| 10-15 19:09 | +15 | SOL | UP | 0.67 | 0.93 | 2.40 |
| 10-15 19:09 | +10 | SOL | UP | 0.67 | 0.81 | 1.13 |
| 10-15 19:09 | +5 | SOL | UP | 0.67 | 0.73 | 0.30 |
| 10-15 19:09 | +10 stop | XRP | DOWN | 0.60 | 0.40 | -2.34 |
| 10-15 19:09 | +20 | XRP | DOWN | 0.60 | yes | -6.17 |
| 10-15 19:09 | +15 | XRP | DOWN | 0.60 | yes | -6.17 |
| 10-15 19:09 | +10 | XRP | DOWN | 0.60 | yes | -6.21 |
| 10-15 19:09 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 10-15 19:08 | +10 stop | BNB | DOWN | 0.60 | 0.80 | 1.71 |
| 10-15 19:08 | +20 | BNB | DOWN | 0.60 | 0.80 | 1.71 |
| 10-15 19:08 | +15 | BNB | DOWN | 0.60 | 0.80 | 1.71 |
| 10-15 19:08 | +10 | BNB | DOWN | 0.60 | 0.80 | 1.71 |
| 10-15 19:08 | +5 | BNB | DOWN | 0.60 | 0.80 | 1.71 |
| 10-15 19:08 | +10 stop | ETH | UP | 0.68 | 0.47 | -2.44 |
| 10-15 19:08 | +20 | ETH | UP | 0.68 | 0.94 | 2.37 |
| 10-15 19:08 | +15 | ETH | UP | 0.68 | 0.94 | 2.37 |
| 10-15 19:08 | +10 | ETH | UP | 0.68 | 0.94 | 2.37 |
| 10-15 19:08 | +5 | ETH | UP | 0.68 | 0.94 | 2.37 |
| 10-15 19:03 | +10 stop | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 10-15 19:02 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-15 19:02 | +10 | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-15 19:02 | +5 | ETH | UP | 0.64 | 0.71 | 0.38 |
| 10-15 19:01 | +10 stop | ZEC | DOWN | 0.60 | 0.38 | -2.54 |
| 10-15 19:01 | +20 | ZEC | DOWN | 0.60 | yes | -6.17 |
| 10-15 19:01 | +15 | ZEC | DOWN | 0.60 | yes | -6.17 |
| 10-15 19:01 | +10 | ZEC | DOWN | 0.60 | yes | -6.17 |
