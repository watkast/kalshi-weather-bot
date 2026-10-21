# Range-Scalp Bot

*Updated Wed Oct 21 23:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27905 | 24314 | 3591 (39) | 4 | $-8018.01 | -4.6% |
| **+10¢** | 20968 | 16821 | 4147 (55) | 4 | $-7055.88 | -5.4% |
| **+15¢** | 17564 | 13100 | 4464 (78) | 4 | $-6293.32 | -5.7% |
| **+20¢** | 15549 | 10871 | 4678 (98) | 4 | $-5622.86 | -5.8% |
| **+10¢ (15¢ stop)** | 34266 | 34207 | 59 (32) | 0 | $-12787.67 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 23:43 | +5 | BNB | UP | 0.22 | 0.65 | 4.01 |
| 10-21 23:42 | +10 stop | ETH | UP | 0.60 | 0.45 | -1.85 |
| 10-21 23:42 | +10 stop | BNB | DOWN | 0.53 | 0.33 | -2.31 |
| 10-21 23:42 | +5 | BNB | DOWN | 0.53 | 0.61 | 0.48 |
| 10-21 23:42 | +10 stop | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-21 23:42 | +20 | HYPE | DOWN | 0.62 | 0.89 | 2.46 |
| 10-21 23:42 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-21 23:42 | +10 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-21 23:42 | +5 | HYPE | DOWN | 0.61 | 0.78 | 1.40 |
| 10-21 23:40 | +10 stop | BNB | DOWN | 0.68 | 0.52 | -1.94 |
| 10-21 23:40 | +10 stop | ETH | DOWN | 0.68 | 0.52 | -1.94 |
| 10-21 23:40 | +15 | ETH | DOWN | 0.68 | 0.86 | 1.55 |
| 10-21 23:40 | +10 | ETH | DOWN | 0.68 | 0.86 | 1.55 |
| 10-21 23:40 | +5 | ETH | DOWN | 0.68 | 0.86 | 1.55 |
| 10-21 23:40 | +10 stop | DOGE | DOWN | 0.59 | 0.44 | -1.85 |
| 10-21 23:39 | +10 stop | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-21 23:39 | +10 stop | DOGE | UP | 0.68 | 0.36 | -3.53 |
| 10-21 23:39 | +15 | DOGE | UP | 0.68 | open |  |
| 10-21 23:39 | +10 | DOGE | UP | 0.68 | open |  |
| 10-21 23:39 | +5 | DOGE | UP | 0.68 | open |  |
| 10-21 23:39 | +10 stop | XRP | UP | 0.47 | 0.58 | 0.74 |
| 10-21 23:39 | +5 | XRP | UP | 0.48 | 0.58 | 0.64 |
| 10-21 23:39 | +10 stop | ZEC | DOWN | 0.69 | 0.83 | 1.15 |
| 10-21 23:39 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-21 23:39 | +15 | ZEC | DOWN | 0.71 | 0.89 | 1.59 |
| 10-21 23:39 | +10 | ZEC | DOWN | 0.71 | 0.83 | 0.96 |
| 10-21 23:39 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.23 |
| 10-21 23:38 | +10 stop | BTC | UP | 0.55 | 0.38 | -2.05 |
| 10-21 23:38 | +10 stop | XRP | UP | 0.58 | 0.68 | 0.66 |
| 10-21 23:38 | +5 | XRP | UP | 0.58 | 0.68 | 0.66 |
| 10-21 23:38 | +10 stop | SOL | UP | 0.58 | 0.39 | -2.25 |
| 10-21 23:38 | +10 stop | HYPE | DOWN | 0.57 | 0.42 | -1.90 |
| 10-21 23:38 | +15 | HYPE | DOWN | 0.57 | 0.83 | 2.28 |
| 10-21 23:38 | +10 | HYPE | DOWN | 0.57 | 0.83 | 2.28 |
| 10-21 23:38 | +5 | HYPE | DOWN | 0.57 | 0.63 | 0.21 |
| 10-21 23:37 | +10 stop | XRP | DOWN | 0.56 | 0.66 | 0.66 |
| 10-21 23:37 | +5 | XRP | DOWN | 0.55 | 0.66 | 0.76 |
| 10-21 23:37 | +10 stop | BTC | DOWN | 0.67 | 0.51 | -1.94 |
| 10-21 23:37 | +10 stop | ETH | UP | 0.62 | 0.79 | 1.43 |
| 10-21 23:37 | +5 | ETH | UP | 0.62 | 0.79 | 1.43 |
