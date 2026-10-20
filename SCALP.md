# Range-Scalp Bot

*Updated Tue Oct 20 12:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25638 | 22328 | 3310 (31) | 1 | $-7485.59 | -4.6% |
| **+10¢** | 19291 | 15470 | 3821 (46) | 2 | $-6601.35 | -5.4% |
| **+15¢** | 16150 | 12035 | 4115 (70) | 2 | $-5910.13 | -5.8% |
| **+20¢** | 14285 | 9979 | 4306 (88) | 3 | $-5262.83 | -5.9% |
| **+10¢ (15¢ stop)** | 31458 | 31405 | 53 (30) | 0 | $-11613.26 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 12:42 | +5 | DOGE | UP | 0.59 | 0.69 | 0.68 |
| 10-20 12:41 | +10 stop | BTC | UP | 0.64 | 0.93 | 2.69 |
| 10-20 12:41 | +10 | BTC | UP | 0.63 | 0.93 | 2.80 |
| 10-20 12:41 | +10 stop | SOL | UP | 0.42 | 0.59 | 1.35 |
| 10-20 12:41 | +20 | SOL | UP | 0.42 | 0.73 | 2.78 |
| 10-20 12:41 | +15 | SOL | UP | 0.42 | 0.59 | 1.35 |
| 10-20 12:41 | +10 | SOL | UP | 0.42 | 0.59 | 1.35 |
| 10-20 12:41 | +5 | SOL | UP | 0.42 | 0.59 | 1.35 |
| 10-20 12:41 | +5 | BTC | UP | 0.57 | 0.64 | 0.35 |
| 10-20 12:41 | +10 stop | DOGE | DOWN | 0.46 | 0.30 | -1.93 |
| 10-20 12:41 | +20 | DOGE | DOWN | 0.46 | open |  |
| 10-20 12:41 | +15 | DOGE | DOWN | 0.46 | open |  |
| 10-20 12:41 | +10 | DOGE | DOWN | 0.46 | open |  |
| 10-20 12:41 | +5 | DOGE | DOWN | 0.46 | 0.54 | 0.44 |
| 10-20 12:40 | +10 stop | BTC | UP | 0.47 | 0.60 | 0.95 |
| 10-20 12:40 | +20 | BTC | UP | 0.47 | 0.71 | 2.07 |
| 10-20 12:40 | +15 | BTC | UP | 0.47 | 0.64 | 1.35 |
| 10-20 12:40 | +10 | BTC | UP | 0.49 | 0.60 | 0.75 |
| 10-20 12:40 | +5 | BTC | UP | 0.50 | 0.56 | 0.24 |
| 10-20 12:40 | +10 stop | XRP | DOWN | 0.62 | 0.81 | 1.62 |
| 10-20 12:40 | +20 | XRP | DOWN | 0.62 | open |  |
| 10-20 12:40 | +15 | XRP | DOWN | 0.62 | 0.81 | 1.62 |
| 10-20 12:40 | +10 | XRP | DOWN | 0.62 | 0.81 | 1.62 |
| 10-20 12:40 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 10-20 12:40 | +10 stop | HYPE | UP | 0.65 | 0.44 | -2.44 |
| 10-20 12:39 | +10 stop | HYPE | DOWN | 0.38 | 0.59 | 1.76 |
| 10-20 12:39 | +10 stop | ETH | UP | 0.58 | 0.75 | 1.38 |
| 10-20 12:38 | +10 stop | HYPE | UP | 0.64 | 0.32 | -3.53 |
| 10-20 12:38 | +5 | HYPE | UP | 0.64 | 0.71 | 0.38 |
| 10-20 12:37 | +10 stop | HYPE | UP | 0.62 | 0.72 | 0.68 |
| 10-20 12:37 | +5 | BTC | DOWN | 0.62 | 0.70 | 0.48 |
| 10-20 12:36 | +10 stop | SOL | DOWN | 0.52 | 0.64 | 0.85 |
| 10-20 12:36 | +20 | SOL | DOWN | 0.52 | 0.73 | 1.78 |
| 10-20 12:36 | +15 | SOL | DOWN | 0.52 | 0.71 | 1.57 |
| 10-20 12:36 | +10 | SOL | DOWN | 0.52 | 0.64 | 0.85 |
| 10-20 12:36 | +5 | SOL | DOWN | 0.52 | 0.60 | 0.45 |
| 10-20 12:36 | +10 stop | XRP | DOWN | 0.49 | 0.61 | 0.80 |
| 10-20 12:36 | +20 | XRP | DOWN | 0.49 | 0.75 | 2.28 |
| 10-20 12:36 | +15 | XRP | DOWN | 0.49 | 0.75 | 2.28 |
| 10-20 12:36 | +10 | XRP | DOWN | 0.49 | 0.61 | 0.85 |
