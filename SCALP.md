# Range-Scalp Bot

*Updated Sat Oct 24 13:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32079 | 27966 | 4113 (40) | 1 | $-9187.31 | -4.5% |
| **+10¢** | 24007 | 19250 | 4757 (58) | 1 | $-8203.56 | -5.4% |
| **+15¢** | 20098 | 14981 | 5117 (81) | 1 | $-7356.93 | -5.8% |
| **+20¢** | 17805 | 12448 | 5357 (103) | 1 | $-6535.92 | -5.8% |
| **+10¢ (15¢ stop)** | 39408 | 39349 | 59 (32) | 1 | $-15077.30 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 13:37 | +5 | BNB | DOWN | 0.66 | 0.73 | 0.40 |
| 10-24 13:37 | +10 stop | BNB | DOWN | 0.58 | 0.69 | 0.77 |
| 10-24 13:37 | +20 | BNB | DOWN | 0.58 | 0.78 | 1.69 |
| 10-24 13:37 | +15 | BNB | DOWN | 0.58 | 0.73 | 1.18 |
| 10-24 13:37 | +10 | BNB | DOWN | 0.58 | 0.69 | 0.77 |
| 10-24 13:37 | +5 | BNB | DOWN | 0.57 | 0.64 | 0.35 |
| 10-24 13:36 | +10 stop | NEAR | UP | 0.65 | open |  |
| 10-24 13:36 | +10 stop | HYPE | DOWN | 0.57 | 0.71 | 1.07 |
| 10-24 13:36 | +20 | HYPE | DOWN | 0.57 | 0.84 | 2.42 |
| 10-24 13:36 | +15 | HYPE | DOWN | 0.57 | 0.75 | 1.48 |
| 10-24 13:36 | +10 | HYPE | DOWN | 0.57 | 0.71 | 1.07 |
| 10-24 13:36 | +5 | HYPE | DOWN | 0.57 | 0.71 | 1.07 |
| 10-24 13:35 | +10 stop | DOGE | DOWN | 0.59 | 0.71 | 0.88 |
| 10-24 13:35 | +10 stop | ETH | DOWN | 0.71 | 0.85 | 1.16 |
| 10-24 13:35 | +20 | ETH | DOWN | 0.71 | 0.91 | 1.79 |
| 10-24 13:35 | +15 | ETH | DOWN | 0.71 | 0.87 | 1.37 |
| 10-24 13:35 | +10 | ETH | DOWN | 0.71 | 0.85 | 1.16 |
| 10-24 13:35 | +5 | ETH | DOWN | 0.71 | 0.80 | 0.63 |
| 10-24 13:34 | +10 stop | DOGE | DOWN | 0.71 | 0.48 | -2.63 |
| 10-24 13:34 | +20 | DOGE | DOWN | 0.71 | 0.92 | 1.89 |
| 10-24 13:34 | +15 | DOGE | DOWN | 0.71 | 0.87 | 1.39 |
| 10-24 13:34 | +10 | DOGE | DOWN | 0.71 | 0.82 | 0.86 |
| 10-24 13:34 | +5 | DOGE | DOWN | 0.71 | 0.79 | 0.55 |
| 10-24 13:34 | +10 stop | SOL | DOWN | 0.58 | 0.38 | -2.35 |
| 10-24 13:34 | +10 | SOL | DOWN | 0.58 | 0.77 | 1.59 |
| 10-24 13:34 | +5 | SOL | DOWN | 0.58 | 0.77 | 1.59 |
| 10-24 13:32 | +5 | NEAR | DOWN | 0.57 | open |  |
| 10-24 13:32 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-24 13:32 | +10 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-24 13:32 | +5 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-24 13:31 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-24 13:31 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.86 |
| 10-24 13:31 | +15 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 10-24 13:31 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-24 13:31 | +5 | XRP | DOWN | 0.70 | 0.79 | 0.63 |
| 10-24 13:31 | +10 stop | ETH | DOWN | 0.57 | 0.80 | 2.00 |
| 10-24 13:31 | +20 | ETH | DOWN | 0.57 | 0.80 | 2.00 |
| 10-24 13:31 | +15 | ETH | DOWN | 0.57 | 0.80 | 2.00 |
| 10-24 13:31 | +10 | ETH | DOWN | 0.57 | 0.80 | 2.00 |
| 10-24 13:31 | +5 | ETH | DOWN | 0.57 | 0.80 | 2.00 |
