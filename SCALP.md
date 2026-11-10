# Range-Scalp Bot

*Updated Tue Nov 10 17:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54803 | 47807 | 6996 (91) | 1 | $-14899.35 | -4.3% |
| **+10¢** | 40946 | 32784 | 8162 (121) | 5 | $-13811.59 | -5.4% |
| **+15¢** | 34321 | 25523 | 8798 (155) | 5 | $-12558.83 | -5.8% |
| **+20¢** | 30556 | 21324 | 9232 (204) | 5 | $-10988.67 | -5.7% |
| **+10¢ (15¢ stop)** | 66763 | 66649 | 114 (70) | 1 | $-24696.68 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 17:26 | +5 | BTC | UP | 0.64 | 0.73 | 0.59 |
| 11-10 17:26 | +10 stop | BTC | UP | 0.61 | 0.73 | 0.89 |
| 11-10 17:26 | +10 stop | DOGE | UP | 0.70 | open |  |
| 11-10 17:26 | +10 | DOGE | UP | 0.70 | open |  |
| 11-10 17:26 | +5 | DOGE | UP | 0.69 | 0.76 | 0.42 |
| 11-10 17:25 | +10 stop | ETH | DOWN | 0.51 | 0.61 | 0.65 |
| 11-10 17:25 | +5 | ETH | DOWN | 0.49 | 0.61 | 0.85 |
| 11-10 17:24 | +5 | ETH | UP | 0.54 | 0.67 | 0.96 |
| 11-10 17:24 | +10 stop | NEAR | DOWN | 0.63 | 0.48 | -1.85 |
| 11-10 17:24 | +10 stop | BTC | UP | 0.63 | 0.28 | -3.82 |
| 11-10 17:24 | +5 | BTC | UP | 0.61 | 0.68 | 0.37 |
| 11-10 17:24 | +10 stop | ETH | UP | 0.63 | 0.36 | -3.04 |
| 11-10 17:24 | +10 | ETH | UP | 0.60 | open |  |
| 11-10 17:24 | +5 | ETH | UP | 0.60 | 0.65 | 0.17 |
| 11-10 17:24 | +10 stop | DOGE | UP | 0.68 | 0.51 | -2.03 |
| 11-10 17:24 | +10 | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 11-10 17:24 | +5 | DOGE | UP | 0.67 | 0.75 | 0.50 |
| 11-10 17:22 | +10 stop | SOL | UP | 0.62 | 0.80 | 1.51 |
| 11-10 17:21 | +5 | BTC | UP | 0.64 | 0.73 | 0.59 |
| 11-10 17:21 | +5 | ETH | UP | 0.63 | 0.70 | 0.38 |
| 11-10 17:21 | +5 | DOGE | UP | 0.64 | 0.71 | 0.38 |
| 11-10 17:21 | +5 | BTC | UP | 0.61 | 0.66 | 0.17 |
| 11-10 17:21 | +10 stop | ETH | UP | 0.61 | 0.73 | 0.89 |
| 11-10 17:21 | +10 | ETH | UP | 0.61 | 0.73 | 0.89 |
| 11-10 17:21 | +5 | ETH | UP | 0.61 | 0.67 | 0.27 |
| 11-10 17:21 | +10 stop | DOGE | UP | 0.63 | 0.75 | 0.93 |
| 11-10 17:21 | +10 | DOGE | UP | 0.62 | 0.75 | 0.95 |
| 11-10 17:21 | +5 | DOGE | UP | 0.59 | 0.66 | 0.37 |
| 11-10 17:18 | +10 stop | SOL | UP | 0.66 | 0.51 | -1.84 |
| 11-10 17:18 | +10 stop | NEAR | UP | 0.69 | 0.52 | -2.03 |
| 11-10 17:18 | +20 | NEAR | UP | 0.69 | open |  |
| 11-10 17:18 | +15 | NEAR | UP | 0.69 | open |  |
| 11-10 17:18 | +10 | NEAR | UP | 0.69 | open |  |
| 11-10 17:18 | +5 | NEAR | UP | 0.69 | 0.75 | 0.31 |
| 11-10 17:18 | +10 stop | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-10 17:18 | +20 | ETH | UP | 0.70 | open |  |
| 11-10 17:18 | +15 | ETH | UP | 0.70 | open |  |
| 11-10 17:18 | +10 | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-10 17:18 | +5 | ETH | UP | 0.71 | 0.77 | 0.32 |
| 11-10 17:17 | +10 stop | SOL | UP | 0.51 | 0.62 | 0.75 |
