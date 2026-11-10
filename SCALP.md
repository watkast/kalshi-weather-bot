# Range-Scalp Bot

*Updated Tue Nov 10 14:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54600 | 47631 | 6969 (91) | 1 | $-14839.14 | -4.3% |
| **+10¢** | 40791 | 32657 | 8134 (121) | 1 | $-13779.20 | -5.4% |
| **+15¢** | 34195 | 25425 | 8770 (155) | 2 | $-12539.77 | -5.8% |
| **+20¢** | 30447 | 21246 | 9201 (204) | 3 | $-10955.30 | -5.7% |
| **+10¢ (15¢ stop)** | 66525 | 66411 | 114 (70) | 0 | $-24593.18 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 14:23 | +10 stop | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 11-10 14:22 | +10 stop | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-10 14:22 | +5 | DOGE | DOWN | 0.60 | 0.78 | 1.49 |
| 11-10 14:22 | +10 stop | XRP | UP | 0.64 | 0.34 | -3.33 |
| 11-10 14:21 | +10 stop | ZEC | UP | 0.69 | 0.51 | -2.13 |
| 11-10 14:20 | +10 stop | DOGE | DOWN | 0.71 | 0.56 | -1.83 |
| 11-10 14:20 | +20 | DOGE | DOWN | 0.71 | open |  |
| 11-10 14:20 | +15 | DOGE | DOWN | 0.70 | 0.88 | 1.57 |
| 11-10 14:20 | +10 | DOGE | DOWN | 0.70 | 0.88 | 1.57 |
| 11-10 14:20 | +5 | DOGE | DOWN | 0.70 | 0.76 | 0.32 |
| 11-10 14:20 | +10 stop | ZEC | UP | 0.70 | 0.54 | -1.93 |
| 11-10 14:20 | +10 stop | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 11-10 14:20 | +20 | ETH | DOWN | 0.70 | 0.90 | 1.78 |
| 11-10 14:20 | +15 | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 11-10 14:20 | +10 | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 11-10 14:20 | +5 | ETH | DOWN | 0.70 | 0.77 | 0.42 |
| 11-10 14:20 | +10 stop | NEAR | DOWN | 0.69 | 0.88 | 1.65 |
| 11-10 14:20 | +20 | NEAR | DOWN | 0.69 | 0.89 | 1.78 |
| 11-10 14:20 | +15 | NEAR | DOWN | 0.69 | 0.88 | 1.67 |
| 11-10 14:20 | +10 | NEAR | DOWN | 0.70 | 0.88 | 1.57 |
| 11-10 14:20 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 11-10 14:19 | +10 stop | XRP | DOWN | 0.65 | 0.49 | -1.94 |
| 11-10 14:19 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-10 14:19 | +15 | XRP | DOWN | 0.66 | open |  |
| 11-10 14:19 | +10 | XRP | DOWN | 0.66 | 0.79 | 1.02 |
| 11-10 14:19 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.29 |
| 11-10 14:17 | +5 | ZEC | DOWN | 0.57 | open |  |
| 11-10 14:16 | +5 | ETH | DOWN | 0.66 | 0.74 | 0.50 |
| 11-10 14:16 | +10 stop | BTC | DOWN | 0.59 | 0.73 | 1.09 |
| 11-10 14:16 | +20 | BTC | DOWN | 0.59 | 0.79 | 1.71 |
| 11-10 14:16 | +15 | BTC | DOWN | 0.59 | 0.76 | 1.40 |
| 11-10 14:16 | +10 | BTC | DOWN | 0.59 | 0.73 | 1.09 |
| 11-10 14:16 | +5 | BTC | DOWN | 0.59 | 0.73 | 1.09 |
| 11-10 14:16 | +10 stop | ETH | DOWN | 0.54 | 0.65 | 0.76 |
| 11-10 14:16 | +20 | ETH | DOWN | 0.56 | 0.76 | 1.69 |
| 11-10 14:16 | +15 | ETH | DOWN | 0.56 | 0.74 | 1.48 |
| 11-10 14:16 | +10 | ETH | DOWN | 0.56 | 0.74 | 1.48 |
| 11-10 14:16 | +5 | ETH | DOWN | 0.56 | 0.63 | 0.35 |
| 11-10 14:16 | +10 stop | NEAR | DOWN | 0.60 | 0.73 | 0.99 |
| 11-10 14:16 | +20 | NEAR | DOWN | 0.60 | 0.82 | 1.92 |
