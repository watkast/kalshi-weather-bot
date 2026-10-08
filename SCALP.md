# Range-Scalp Bot

*Updated Thu Oct 08 01:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7063 | 6133 | 930 (13) | 1 | $-2092.85 | -4.7% |
| **+10¢** | 5352 | 4263 | 1089 (20) | 3 | $-1981.74 | -5.9% |
| **+15¢** | 4491 | 3342 | 1149 (28) | 3 | $-1622.54 | -5.8% |
| **+20¢** | 4011 | 2813 | 1198 (35) | 3 | $-1288.60 | -5.1% |
| **+10¢ (15¢ stop)** | 8543 | 8521 | 22 (14) | 0 | $-3006.65 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 00:53 | +10 stop | NEAR | UP | 0.54 | 0.36 | -2.15 |
| 10-08 00:50 | +10 stop | NEAR | UP | 0.60 | 0.41 | -2.24 |
| 10-08 00:47 | +10 stop | NEAR | DOWN | 0.58 | 0.31 | -3.03 |
| 10-08 00:47 | +10 stop | NEAR | UP | 0.45 | 0.58 | 0.94 |
| 10-08 00:47 | +10 stop | SOL | UP | 0.64 | 0.76 | 0.90 |
| 10-08 00:47 | +10 stop | BNB | UP | 0.57 | 0.76 | 1.59 |
| 10-08 00:47 | +5 | SOL | UP | 0.64 | 0.73 | 0.59 |
| 10-08 00:47 | +10 stop | BTC | UP | 0.66 | 0.76 | 0.71 |
| 10-08 00:47 | +20 | BTC | UP | 0.66 | 0.86 | 1.75 |
| 10-08 00:47 | +15 | BTC | UP | 0.66 | 0.81 | 1.23 |
| 10-08 00:47 | +10 | BTC | UP | 0.66 | 0.76 | 0.71 |
| 10-08 00:47 | +5 | BTC | UP | 0.66 | 0.72 | 0.29 |
| 10-08 00:46 | +10 stop | NEAR | DOWN | 0.65 | 0.46 | -2.24 |
| 10-08 00:46 | +20 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 10-08 00:46 | +15 | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 10-08 00:46 | +10 | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 10-08 00:46 | +5 | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 10-08 00:46 | +10 stop | SOL | DOWN | 0.56 | 0.39 | -2.05 |
| 10-08 00:46 | +20 | SOL | DOWN | 0.56 | open |  |
| 10-08 00:46 | +15 | SOL | DOWN | 0.56 | open |  |
| 10-08 00:46 | +10 | SOL | DOWN | 0.56 | open |  |
| 10-08 00:46 | +5 | SOL | DOWN | 0.56 | 0.65 | 0.56 |
| 10-08 00:46 | +10 stop | DOGE | DOWN | 0.46 | 0.24 | -2.51 |
| 10-08 00:46 | +20 | DOGE | DOWN | 0.46 | open |  |
| 10-08 00:46 | +15 | DOGE | DOWN | 0.46 | open |  |
| 10-08 00:46 | +10 | DOGE | DOWN | 0.46 | open |  |
| 10-08 00:46 | +5 | DOGE | DOWN | 0.46 | 0.54 | 0.44 |
| 10-08 00:46 | +10 stop | BNB | DOWN | 0.65 | 0.45 | -2.34 |
| 10-08 00:46 | +20 | BNB | DOWN | 0.65 | open |  |
| 10-08 00:46 | +15 | BNB | DOWN | 0.65 | open |  |
| 10-08 00:46 | +10 | BNB | DOWN | 0.65 | open |  |
| 10-08 00:46 | +5 | BNB | DOWN | 0.65 | open |  |
| 10-08 00:42 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.18 |
| 10-08 00:42 | +10 stop | HYPE | UP | 0.69 | 0.54 | -1.83 |
| 10-08 00:41 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 10-08 00:38 | +10 stop | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-08 00:38 | +10 stop | HYPE | DOWN | 0.67 | 0.33 | -3.72 |
| 10-08 00:38 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-08 00:38 | +10 | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-08 00:38 | +5 | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
