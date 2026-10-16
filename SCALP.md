# Range-Scalp Bot

*Updated Fri Oct 16 01:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18514 | 16082 | 2432 (28) | 3 | $-5609.33 | -4.8% |
| **+10¢** | 13970 | 11157 | 2813 (40) | 3 | $-5054.90 | -5.7% |
| **+15¢** | 11712 | 8686 | 3026 (59) | 4 | $-4558.90 | -6.2% |
| **+20¢** | 10400 | 7234 | 3166 (78) | 4 | $-3969.31 | -6.1% |
| **+10¢ (15¢ stop)** | 22803 | 22753 | 50 (29) | 0 | $-8785.80 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 01:56 | +10 stop | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-16 01:55 | +10 stop | NEAR | DOWN | 0.60 | 0.80 | 1.71 |
| 10-16 01:55 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 10-16 01:55 | +10 stop | XRP | DOWN | 0.71 | 0.89 | 1.58 |
| 10-16 01:54 | +10 stop | ETH | DOWN | 0.56 | 0.68 | 0.86 |
| 10-16 01:54 | +10 stop | NEAR | UP | 0.52 | 0.35 | -2.04 |
| 10-16 01:54 | +10 stop | ZEC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-16 01:53 | +10 stop | BNB | DOWN | 0.65 | 0.79 | 1.15 |
| 10-16 01:53 | +10 stop | SOL | DOWN | 0.62 | 0.77 | 1.20 |
| 10-16 01:53 | +10 | SOL | DOWN | 0.62 | 0.77 | 1.20 |
| 10-16 01:53 | +5 | SOL | DOWN | 0.62 | 0.77 | 1.20 |
| 10-16 01:53 | +10 stop | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
| 10-16 01:53 | +20 | DOGE | DOWN | 0.70 | 0.91 | 1.93 |
| 10-16 01:53 | +15 | DOGE | DOWN | 0.70 | 0.85 | 1.26 |
| 10-16 01:53 | +10 | DOGE | DOWN | 0.70 | 0.85 | 1.26 |
| 10-16 01:53 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 10-16 01:52 | +10 stop | ZEC | DOWN | 0.38 | 0.54 | 1.25 |
| 10-16 01:52 | +10 stop | ZEC | UP | 0.46 | 0.57 | 0.74 |
| 10-16 01:51 | +10 stop | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 10-16 01:51 | +10 | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 10-16 01:51 | +5 | BTC | DOWN | 0.66 | 0.71 | 0.19 |
| 10-16 01:51 | +15 | BNB | DOWN | 0.66 | 0.86 | 1.76 |
| 10-16 01:51 | +10 stop | HYPE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-16 01:51 | +10 stop | BNB | DOWN | 0.66 | 0.48 | -2.14 |
| 10-16 01:51 | +10 | BNB | DOWN | 0.66 | 0.79 | 1.02 |
| 10-16 01:51 | +5 | BNB | DOWN | 0.66 | 0.79 | 1.02 |
| 10-16 01:50 | +10 stop | XRP | UP | 0.64 | 0.46 | -2.15 |
| 10-16 01:50 | +10 | XRP | UP | 0.64 | open |  |
| 10-16 01:50 | +5 | XRP | UP | 0.64 | open |  |
| 10-16 01:50 | +10 stop | ETH | UP | 0.60 | 0.40 | -2.34 |
| 10-16 01:49 | +10 stop | BTC | DOWN | 0.57 | 0.71 | 1.07 |
| 10-16 01:49 | +20 | BTC | DOWN | 0.57 | 0.78 | 1.79 |
| 10-16 01:49 | +15 | BTC | DOWN | 0.57 | 0.73 | 1.28 |
| 10-16 01:49 | +10 | BTC | DOWN | 0.57 | 0.71 | 1.07 |
| 10-16 01:49 | +5 | BTC | DOWN | 0.57 | 0.62 | 0.15 |
| 10-16 01:49 | +10 stop | ZEC | DOWN | 0.64 | 0.43 | -2.45 |
| 10-16 01:49 | +10 | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-16 01:49 | +5 | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-16 01:48 | +5 | BNB | DOWN | 0.59 | 0.64 | 0.16 |
| 10-16 01:48 | +5 | DOGE | DOWN | 0.63 | 0.74 | 0.78 |
