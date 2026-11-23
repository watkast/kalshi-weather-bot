# Range-Scalp Bot

*Updated Mon Nov 23 23:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70242 | 61298 | 8944 (147) | 0 | $-18873.44 | -4.3% |
| **+10¢** | 52411 | 41965 | 10446 (190) | 0 | $-17517.44 | -5.3% |
| **+15¢** | 43913 | 32665 | 11248 (246) | 0 | $-15595.30 | -5.7% |
| **+20¢** | 39096 | 27257 | 11839 (311) | 0 | $-13977.08 | -5.7% |
| **+10¢ (15¢ stop)** | 85564 | 85368 | 196 (118) | 0 | $-31492.04 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 23:02 | +10 stop | NEAR | UP | 0.66 | 0.82 | 1.33 |
| 11-23 23:02 | +20 | NEAR | UP | 0.67 | 0.87 | 1.76 |
| 11-23 23:02 | +15 | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 11-23 23:02 | +10 | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 11-23 23:02 | +5 | NEAR | UP | 0.68 | 0.82 | 1.12 |
| 11-23 22:58 | +10 stop | DOGE | UP | 0.56 | 0.85 | 2.63 |
| 11-23 22:56 | +10 stop | NEAR | UP | 0.69 | 0.86 | 1.46 |
| 11-23 22:55 | +10 stop | DOGE | UP | 0.63 | 0.46 | -2.05 |
| 11-23 22:54 | +10 stop | ZEC | UP | 0.59 | 0.73 | 1.09 |
| 11-23 22:54 | +15 | ZEC | UP | 0.60 | 0.79 | 1.61 |
| 11-23 22:54 | +10 | ZEC | UP | 0.60 | 0.73 | 0.99 |
| 11-23 22:54 | +5 | ZEC | UP | 0.60 | 0.73 | 0.99 |
| 11-23 22:54 | +10 stop | NEAR | UP | 0.68 | 0.78 | 0.72 |
| 11-23 22:54 | +10 stop | ETH | UP | 0.71 | 0.87 | 1.37 |
| 11-23 22:54 | +10 | ETH | UP | 0.71 | 0.87 | 1.37 |
| 11-23 22:54 | +5 | ETH | UP | 0.71 | 0.77 | 0.32 |
| 11-23 22:53 | +10 stop | DOGE | UP | 0.48 | 0.63 | 1.15 |
| 11-23 22:53 | +10 stop | NEAR | UP | 0.70 | 0.51 | -2.23 |
| 11-23 22:52 | +5 | XRP | UP | 0.59 | 0.79 | 1.74 |
| 11-23 22:51 | +10 stop | HYPE | DOWN | 0.53 | 0.25 | -3.12 |
| 11-23 22:51 | +10 stop | BTC | UP | 0.56 | 0.74 | 1.48 |
| 11-23 22:51 | +5 | NEAR | DOWN | 0.62 | yes | -6.40 |
| 11-23 22:50 | +5 | XRP | UP | 0.51 | 0.58 | 0.34 |
| 11-23 22:50 | +10 stop | ETH | UP | 0.65 | 0.76 | 0.81 |
| 11-23 22:50 | +10 | ETH | UP | 0.66 | 0.76 | 0.71 |
| 11-23 22:50 | +5 | ETH | UP | 0.66 | 0.76 | 0.71 |
| 11-23 22:50 | +10 stop | BTC | UP | 0.61 | 0.45 | -1.95 |
| 11-23 22:50 | +5 | NEAR | DOWN | 0.54 | 0.62 | 0.45 |
| 11-23 22:50 | +10 stop | NEAR | DOWN | 0.61 | 0.45 | -1.95 |
| 11-23 22:49 | +10 stop | XRP | UP | 0.51 | 0.79 | 2.50 |
| 11-23 22:49 | +10 stop | SOL | DOWN | 0.69 | 0.88 | 1.67 |
| 11-23 22:49 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 11-23 22:49 | +5 | XRP | UP | 0.52 | 0.58 | 0.24 |
| 11-23 22:48 | +10 stop | BNB | UP | 0.56 | 0.82 | 2.30 |
| 11-23 22:48 | +5 | NEAR | DOWN | 0.51 | 0.65 | 1.06 |
| 11-23 22:48 | +10 stop | HYPE | UP | 0.62 | 0.44 | -2.15 |
| 11-23 22:48 | +10 stop | ETH | DOWN | 0.46 | 0.59 | 0.95 |
| 11-23 22:48 | +10 | ETH | DOWN | 0.46 | 0.59 | 0.95 |
| 11-23 22:48 | +5 | ETH | DOWN | 0.46 | 0.59 | 0.95 |
| 11-23 22:48 | +5 | NEAR | DOWN | 0.52 | 0.59 | 0.40 |
