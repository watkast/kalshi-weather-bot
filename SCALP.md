# Range-Scalp Bot

*Updated Tue Oct 20 07:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25298 | 22027 | 3271 (31) | 0 | $-7397.49 | -4.6% |
| **+10¢** | 19038 | 15257 | 3781 (46) | 0 | $-6574.01 | -5.5% |
| **+15¢** | 15934 | 11861 | 4073 (70) | 0 | $-5921.42 | -5.9% |
| **+20¢** | 14087 | 9823 | 4264 (88) | 0 | $-5315.80 | -6.0% |
| **+10¢ (15¢ stop)** | 31034 | 30982 | 52 (30) | 0 | $-11504.57 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 07:24 | +10 stop | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 10-20 07:24 | +10 | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 10-20 07:24 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 10-20 07:24 | +5 | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 10-20 07:24 | +10 stop | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-20 07:24 | +10 stop | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-20 07:24 | +20 | ZEC | DOWN | 0.71 | 0.96 | 2.32 |
| 10-20 07:24 | +15 | ZEC | DOWN | 0.71 | 0.89 | 1.58 |
| 10-20 07:24 | +10 stop | DOGE | UP | 0.35 | 0.53 | 1.46 |
| 10-20 07:23 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-20 07:23 | +10 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-20 07:23 | +5 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-20 07:23 | +5 | DOGE | DOWN | 0.60 | 0.65 | 0.17 |
| 10-20 07:23 | +10 stop | DOGE | DOWN | 0.60 | 0.34 | -2.93 |
| 10-20 07:23 | +10 | DOGE | DOWN | 0.58 | 0.82 | 2.11 |
| 10-20 07:23 | +5 | DOGE | DOWN | 0.54 | 0.67 | 0.96 |
| 10-20 07:22 | +10 stop | XRP | DOWN | 0.60 | 0.74 | 1.08 |
| 10-20 07:22 | +10 stop | NEAR | DOWN | 0.59 | 0.71 | 0.89 |
| 10-20 07:22 | +20 | NEAR | DOWN | 0.59 | 0.79 | 1.72 |
| 10-20 07:22 | +15 | NEAR | DOWN | 0.59 | 0.79 | 1.72 |
| 10-20 07:22 | +10 | NEAR | DOWN | 0.59 | 0.71 | 0.89 |
| 10-20 07:22 | +5 | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 10-20 07:22 | +10 stop | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 10-20 07:22 | +20 | ETH | DOWN | 0.60 | 0.82 | 1.92 |
| 10-20 07:22 | +10 | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 10-20 07:22 | +5 | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 10-20 07:22 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 10-20 07:22 | +5 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 10-20 07:22 | +5 | XRP | DOWN | 0.56 | 0.74 | 1.48 |
| 10-20 07:20 | +15 | ETH | DOWN | 0.71 | 0.89 | 1.58 |
| 10-20 07:20 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 10-20 07:19 | +10 stop | XRP | DOWN | 0.69 | 0.54 | -1.83 |
| 10-20 07:19 | +5 | XRP | DOWN | 0.69 | 0.75 | 0.31 |
| 10-20 07:19 | +10 stop | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 10-20 07:19 | +10 | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 10-20 07:19 | +5 | ETH | DOWN | 0.61 | 0.68 | 0.37 |
| 10-20 07:19 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-20 07:18 | +10 stop | ETH | DOWN | 0.50 | 0.61 | 0.75 |
| 10-20 07:18 | +20 | ETH | DOWN | 0.51 | 0.71 | 1.67 |
| 10-20 07:18 | +15 | ETH | DOWN | 0.51 | 0.68 | 1.36 |
