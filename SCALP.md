# Range-Scalp Bot

*Updated Sun Nov 22 15:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68882 | 60120 | 8762 (142) | 8 | $-18445.41 | -4.3% |
| **+10¢** | 51397 | 41161 | 10236 (186) | 8 | $-17098.51 | -5.3% |
| **+15¢** | 43070 | 32033 | 11037 (237) | 8 | $-15363.29 | -5.7% |
| **+20¢** | 38347 | 26749 | 11598 (295) | 8 | $-13675.62 | -5.7% |
| **+10¢ (15¢ stop)** | 83870 | 83685 | 185 (116) | 0 | $-30870.21 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 15:27 | +10 stop | BTC | UP | 0.53 | 0.86 | 3.03 |
| 11-22 15:25 | +10 stop | HYPE | UP | 0.66 | 0.51 | -1.85 |
| 11-22 15:25 | +10 stop | BNB | UP | 0.65 | 0.79 | 1.12 |
| 11-22 15:24 | +10 stop | XRP | UP | 0.71 | 0.82 | 0.84 |
| 11-22 15:24 | +10 stop | BTC | UP | 0.64 | 0.41 | -2.64 |
| 11-22 15:23 | +10 stop | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 11-22 15:22 | +10 stop | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 11-22 15:22 | +10 stop | ETH | UP | 0.65 | 0.87 | 1.96 |
| 11-22 15:22 | +5 | HYPE | DOWN | 0.59 | open |  |
| 11-22 15:22 | +10 stop | SOL | UP | 0.59 | 0.82 | 2.02 |
| 11-22 15:21 | +5 | XRP | DOWN | 0.63 | open |  |
| 11-22 15:21 | +10 stop | ETH | UP | 0.56 | 0.66 | 0.66 |
| 11-22 15:21 | +10 stop | HYPE | DOWN | 0.62 | 0.29 | -3.62 |
| 11-22 15:21 | +10 | HYPE | DOWN | 0.63 | open |  |
| 11-22 15:21 | +5 | HYPE | DOWN | 0.63 | 0.71 | 0.48 |
| 11-22 15:21 | +10 stop | ZEC | UP | 0.65 | 0.80 | 1.22 |
| 11-22 15:20 | +10 stop | BTC | DOWN | 0.65 | 0.45 | -2.34 |
| 11-22 15:20 | +10 | BTC | DOWN | 0.65 | open |  |
| 11-22 15:20 | +5 | BTC | DOWN | 0.65 | open |  |
| 11-22 15:20 | +5 | BNB | DOWN | 0.68 | open |  |
| 11-22 15:19 | +10 stop | DOGE | DOWN | 0.59 | 0.36 | -2.64 |
| 11-22 15:19 | +10 stop | XRP | DOWN | 0.61 | 0.42 | -2.25 |
| 11-22 15:18 | +5 | BNB | DOWN | 0.61 | 0.69 | 0.49 |
| 11-22 15:18 | +5 | BTC | DOWN | 0.69 | 0.77 | 0.52 |
| 11-22 15:18 | +5 | ZEC | DOWN | 0.69 | open |  |
| 11-22 15:17 | +5 | ETH | DOWN | 0.59 | open |  |
| 11-22 15:17 | +10 stop | XRP | DOWN | 0.64 | 0.49 | -1.85 |
| 11-22 15:17 | +20 | XRP | DOWN | 0.64 | open |  |
| 11-22 15:17 | +15 | XRP | DOWN | 0.64 | open |  |
| 11-22 15:17 | +10 | XRP | DOWN | 0.64 | open |  |
| 11-22 15:17 | +5 | XRP | DOWN | 0.64 | 0.69 | 0.18 |
| 11-22 15:16 | +10 stop | DOGE | DOWN | 0.70 | 0.51 | -2.23 |
| 11-22 15:16 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-22 15:16 | +15 | DOGE | DOWN | 0.70 | open |  |
| 11-22 15:16 | +10 | DOGE | DOWN | 0.70 | open |  |
| 11-22 15:16 | +5 | DOGE | DOWN | 0.71 | open |  |
| 11-22 15:16 | +10 stop | ETH | DOWN | 0.60 | 0.43 | -2.05 |
| 11-22 15:16 | +20 | ETH | DOWN | 0.60 | open |  |
| 11-22 15:16 | +15 | ETH | DOWN | 0.60 | open |  |
| 11-22 15:16 | +10 | ETH | DOWN | 0.60 | open |  |
