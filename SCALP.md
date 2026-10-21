# Range-Scalp Bot

*Updated Wed Oct 21 04:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26726 | 23275 | 3451 (33) | 2 | $-7808.78 | -4.6% |
| **+10¢** | 20116 | 16131 | 3985 (48) | 2 | $-6885.27 | -5.4% |
| **+15¢** | 16838 | 12552 | 4286 (72) | 3 | $-6120.55 | -5.8% |
| **+20¢** | 14906 | 10413 | 4493 (91) | 3 | $-5489.81 | -5.9% |
| **+10¢ (15¢ stop)** | 32754 | 32701 | 53 (30) | 0 | $-12026.11 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 04:57 | +10 stop | ZEC | DOWN | 0.53 | 0.34 | -2.24 |
| 10-21 04:57 | +15 | ZEC | DOWN | 0.50 | open |  |
| 10-21 04:57 | +10 | ZEC | DOWN | 0.44 | 0.58 | 1.04 |
| 10-21 04:57 | +5 | ZEC | DOWN | 0.44 | 0.58 | 1.04 |
| 10-21 04:55 | +10 stop | ZEC | DOWN | 0.59 | 0.72 | 0.98 |
| 10-21 04:55 | +20 | ZEC | DOWN | 0.59 | open |  |
| 10-21 04:55 | +15 | ZEC | DOWN | 0.59 | 0.74 | 1.19 |
| 10-21 04:55 | +10 | ZEC | DOWN | 0.58 | 0.72 | 1.05 |
| 10-21 04:55 | +5 | ZEC | DOWN | 0.58 | 0.67 | 0.54 |
| 10-21 04:55 | +10 stop | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 10-21 04:53 | +10 stop | SOL | UP | 0.65 | 0.75 | 0.70 |
| 10-21 04:53 | +10 stop | ETH | UP | 0.66 | 0.79 | 1.02 |
| 10-21 04:51 | +10 stop | DOGE | DOWN | 0.64 | 0.40 | -2.74 |
| 10-21 04:51 | +10 stop | XRP | UP | 0.65 | 0.76 | 0.81 |
| 10-21 04:51 | +15 | XRP | UP | 0.65 | 0.80 | 1.22 |
| 10-21 04:51 | +10 | XRP | UP | 0.65 | 0.76 | 0.81 |
| 10-21 04:51 | +5 | XRP | UP | 0.65 | 0.72 | 0.39 |
| 10-21 04:49 | +10 stop | BNB | UP | 0.64 | 0.74 | 0.69 |
| 10-21 04:49 | +10 | BNB | UP | 0.64 | 0.74 | 0.69 |
| 10-21 04:49 | +5 | BNB | UP | 0.64 | 0.71 | 0.38 |
| 10-21 04:49 | +10 stop | NEAR | UP | 0.51 | 0.31 | -2.32 |
| 10-21 04:49 | +10 stop | ETH | UP | 0.59 | 0.43 | -1.95 |
| 10-21 04:49 | +10 stop | SOL | UP | 0.63 | 0.42 | -2.45 |
| 10-21 04:49 | +10 | SOL | UP | 0.63 | 0.75 | 0.89 |
| 10-21 04:49 | +5 | SOL | UP | 0.63 | 0.68 | 0.17 |
| 10-21 04:49 | +5 | BTC | UP | 0.67 | 0.72 | 0.19 |
| 10-21 04:49 | +10 stop | DOGE | UP | 0.63 | 0.39 | -2.74 |
| 10-21 04:49 | +20 | DOGE | UP | 0.63 | 0.88 | 2.25 |
| 10-21 04:49 | +15 | DOGE | UP | 0.63 | 0.78 | 1.20 |
| 10-21 04:49 | +10 | DOGE | UP | 0.63 | 0.78 | 1.20 |
| 10-21 04:49 | +5 | DOGE | UP | 0.63 | 0.78 | 1.20 |
| 10-21 04:48 | +10 stop | HYPE | DOWN | 0.59 | 0.70 | 0.74 |
| 10-21 04:48 | +10 | HYPE | DOWN | 0.59 | 0.70 | 0.74 |
| 10-21 04:48 | +10 stop | NEAR | DOWN | 0.58 | 0.42 | -1.96 |
| 10-21 04:48 | +10 stop | ETH | DOWN | 0.58 | 0.36 | -2.54 |
| 10-21 04:48 | +20 | ETH | DOWN | 0.57 | open |  |
| 10-21 04:48 | +15 | ETH | DOWN | 0.57 | open |  |
| 10-21 04:48 | +10 | ETH | DOWN | 0.57 | open |  |
| 10-21 04:48 | +5 | ETH | DOWN | 0.57 | open |  |
| 10-21 04:47 | +5 | HYPE | DOWN | 0.66 | 0.72 | 0.29 |
