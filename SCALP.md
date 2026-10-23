# Range-Scalp Bot

*Updated Fri Oct 23 04:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29787 | 25930 | 3857 (39) | 6 | $-8783.71 | -4.7% |
| **+10¢** | 22325 | 17861 | 4464 (55) | 8 | $-7906.06 | -5.6% |
| **+15¢** | 18695 | 13903 | 4792 (78) | 8 | $-7066.21 | -6.0% |
| **+20¢** | 16547 | 11525 | 5022 (101) | 8 | $-6381.40 | -6.1% |
| **+10¢ (15¢ stop)** | 36562 | 36503 | 59 (32) | 5 | $-13791.10 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 04:55 | +10 stop | HYPE | UP | 0.61 | open |  |
| 10-23 04:55 | +10 stop | DOGE | DOWN | 0.61 | open |  |
| 10-23 04:55 | +10 stop | SOL | DOWN | 0.54 | open |  |
| 10-23 04:55 | +10 stop | XRP | DOWN | 0.70 | open |  |
| 10-23 04:55 | +10 | XRP | DOWN | 0.70 | open |  |
| 10-23 04:54 | +10 stop | HYPE | UP | 0.49 | 0.65 | 1.26 |
| 10-23 04:54 | +10 stop | XRP | UP | 0.49 | 0.61 | 0.85 |
| 10-23 04:54 | +15 | XRP | UP | 0.49 | open |  |
| 10-23 04:54 | +10 | XRP | UP | 0.49 | 0.61 | 0.85 |
| 10-23 04:54 | +10 stop | DOGE | UP | 0.55 | 0.67 | 0.86 |
| 10-23 04:52 | +10 stop | HYPE | UP | 0.51 | 0.62 | 0.71 |
| 10-23 04:52 | +10 stop | DOGE | DOWN | 0.60 | 0.31 | -3.22 |
| 10-23 04:52 | +10 | DOGE | DOWN | 0.60 | open |  |
| 10-23 04:52 | +5 | DOGE | DOWN | 0.60 | open |  |
| 10-23 04:51 | +10 stop | SOL | DOWN | 0.48 | 0.25 | -2.62 |
| 10-23 04:51 | +10 | SOL | DOWN | 0.48 | open |  |
| 10-23 04:51 | +10 stop | ZEC | UP | 0.71 | 0.82 | 0.84 |
| 10-23 04:51 | +5 | XRP | DOWN | 0.71 | open |  |
| 10-23 04:51 | +10 stop | BTC | DOWN | 0.64 | open |  |
| 10-23 04:51 | +10 | BTC | DOWN | 0.64 | open |  |
| 10-23 04:51 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 10-23 04:51 | +5 | SOL | DOWN | 0.62 | open |  |
| 10-23 04:50 | +10 stop | BNB | DOWN | 0.64 | 0.77 | 1.00 |
| 10-23 04:49 | +5 | HYPE | DOWN | 0.65 | open |  |
| 10-23 04:49 | +5 | XRP | DOWN | 0.53 | 0.65 | 0.86 |
| 10-23 04:49 | +10 stop | ZEC | DOWN | 0.61 | 0.46 | -1.85 |
| 10-23 04:49 | +10 | ZEC | DOWN | 0.61 | open |  |
| 10-23 04:49 | +5 | ZEC | DOWN | 0.61 | open |  |
| 10-23 04:49 | +5 | DOGE | DOWN | 0.64 | 0.71 | 0.38 |
| 10-23 04:49 | +10 stop | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-23 04:49 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-23 04:49 | +5 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-23 04:49 | +10 stop | XRP | DOWN | 0.58 | 0.71 | 0.97 |
| 10-23 04:49 | +10 | XRP | DOWN | 0.58 | 0.71 | 0.97 |
| 10-23 04:49 | +5 | XRP | DOWN | 0.58 | 0.65 | 0.36 |
| 10-23 04:48 | +10 stop | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 10-23 04:47 | +10 stop | ETH | DOWN | 0.57 | 0.67 | 0.66 |
| 10-23 04:47 | +20 | ETH | DOWN | 0.57 | 0.79 | 1.90 |
| 10-23 04:47 | +15 | ETH | DOWN | 0.57 | 0.79 | 1.90 |
| 10-23 04:47 | +10 | ETH | DOWN | 0.57 | 0.67 | 0.66 |
