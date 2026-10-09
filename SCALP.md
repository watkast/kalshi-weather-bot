# Range-Scalp Bot

*Updated Fri Oct 09 17:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9251 | 7988 | 1263 (17) | 8 | $-3099.36 | -5.3% |
| **+10¢** | 6988 | 5508 | 1480 (29) | 11 | $-3003.73 | -6.8% |
| **+15¢** | 5889 | 4330 | 1559 (42) | 11 | $-2478.08 | -6.7% |
| **+20¢** | 5238 | 3619 | 1619 (53) | 12 | $-2062.47 | -6.3% |
| **+10¢ (15¢ stop)** | 11333 | 11301 | 32 (20) | 0 | $-4364.54 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 17:43 | +10 stop | DOGE | UP | 0.63 | 0.83 | 1.73 |
| 10-09 17:43 | +10 | DOGE | UP | 0.63 | 0.83 | 1.73 |
| 10-09 17:43 | +10 stop | SOL | UP | 0.42 | 0.59 | 1.35 |
| 10-09 17:43 | +10 | SOL | UP | 0.42 | 0.59 | 1.35 |
| 10-09 17:43 | +5 | SOL | UP | 0.42 | 0.59 | 1.35 |
| 10-09 17:42 | +10 stop | HYPE | UP | 0.62 | 0.42 | -2.35 |
| 10-09 17:42 | +10 | HYPE | UP | 0.62 | no | -6.37 |
| 10-09 17:42 | +5 | HYPE | UP | 0.62 | no | -6.37 |
| 10-09 17:42 | +20 | ETH | DOWN | 0.70 | 0.95 | 2.28 |
| 10-09 17:42 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-09 17:42 | +10 | ETH | DOWN | 0.69 | 0.84 | 1.25 |
| 10-09 17:42 | +5 | ETH | DOWN | 0.69 | 0.84 | 1.25 |
| 10-09 17:42 | +10 stop | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 10-09 17:42 | +10 stop | SOL | UP | 0.50 | 0.64 | 1.05 |
| 10-09 17:42 | +20 | SOL | UP | 0.50 | no | -5.18 |
| 10-09 17:42 | +15 | SOL | UP | 0.50 | no | -5.18 |
| 10-09 17:42 | +10 | SOL | UP | 0.50 | 0.64 | 1.05 |
| 10-09 17:42 | +5 | SOL | UP | 0.50 | 0.64 | 1.05 |
| 10-09 17:41 | +10 stop | HYPE | UP | 0.47 | 0.58 | 0.74 |
| 10-09 17:41 | +10 | HYPE | UP | 0.47 | 0.58 | 0.74 |
| 10-09 17:41 | +5 | HYPE | UP | 0.47 | 0.58 | 0.74 |
| 10-09 17:41 | +10 stop | DOGE | UP | 0.65 | 0.49 | -1.94 |
| 10-09 17:41 | +10 | DOGE | UP | 0.65 | 0.76 | 0.81 |
| 10-09 17:41 | +5 | DOGE | UP | 0.65 | 0.76 | 0.81 |
| 10-09 17:40 | +10 stop | NEAR | DOWN | 0.59 | 0.19 | -4.28 |
| 10-09 17:39 | +5 | ZEC | DOWN | 0.66 | yes | -6.76 |
| 10-09 17:39 | +10 stop | BNB | UP | 0.70 | 0.55 | -1.87 |
| 10-09 17:39 | +10 | BNB | UP | 0.70 | 0.82 | 0.90 |
| 10-09 17:39 | +5 | BNB | UP | 0.70 | 0.82 | 0.90 |
| 10-09 17:39 | +10 stop | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-09 17:38 | +10 stop | NEAR | DOWN | 0.35 | 0.54 | 1.59 |
| 10-09 17:38 | +10 stop | NEAR | DOWN | 0.62 | 0.28 | -3.72 |
| 10-09 17:38 | +10 stop | ZEC | DOWN | 0.58 | 0.34 | -2.72 |
| 10-09 17:38 | +10 stop | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 10-09 17:37 | +10 stop | DOGE | UP | 0.60 | 0.39 | -2.44 |
| 10-09 17:37 | +10 stop | SOL | UP | 0.60 | 0.44 | -1.95 |
| 10-09 17:37 | +10 stop | BTC | UP | 0.65 | 0.46 | -2.24 |
| 10-09 17:36 | +10 stop | ETH | DOWN | 0.56 | 0.41 | -1.85 |
| 10-09 17:36 | +10 stop | NEAR | UP | 0.60 | 0.42 | -2.15 |
| 10-09 17:36 | +10 stop | DOGE | DOWN | 0.57 | 0.41 | -1.95 |
