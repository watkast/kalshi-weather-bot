# Range-Scalp Bot

*Updated Sat Oct 03 23:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1426 | 1238 | 188 (2) | 2 | $-438.16 | -4.8% |
| **+10¢** | 1095 | 889 | 206 (4) | 2 | $-269.49 | -3.9% |
| **+15¢** | 923 | 703 | 220 (5) | 2 | $-217.27 | -3.7% |
| **+20¢** | 815 | 576 | 239 (7) | 2 | $-248.50 | -4.8% |
| **+10¢ (15¢ stop)** | 1781 | 1780 | 1 (1) | 1 | $-739.88 | -6.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 23:28 | +10 stop | BTC | DOWN | 0.52 | open |  |
| 10-03 23:27 | +10 stop | BTC | UP | 0.52 | 0.63 | 0.75 |
| 10-03 23:25 | +10 stop | BNB | UP | 0.53 | 0.15 | -4.07 |
| 10-03 23:22 | +5 | DOGE | UP | 0.64 | 0.69 | 0.18 |
| 10-03 23:22 | +10 stop | DOGE | UP | 0.66 | 0.83 | 1.45 |
| 10-03 23:22 | +5 | SOL | UP | 0.60 | 0.85 | 2.28 |
| 10-03 23:21 | +10 stop | BNB | DOWN | 0.56 | 0.19 | -4.04 |
| 10-03 23:21 | +10 | BNB | DOWN | 0.56 | 0.84 | 2.47 |
| 10-03 23:21 | +5 | BNB | DOWN | 0.56 | 0.84 | 2.47 |
| 10-03 23:20 | +10 stop | DOGE | DOWN | 0.59 | 0.70 | 0.78 |
| 10-03 23:20 | +10 stop | ETH | DOWN | 0.55 | 0.18 | -3.99 |
| 10-03 23:20 | +20 | ETH | DOWN | 0.55 | open |  |
| 10-03 23:20 | +15 | ETH | DOWN | 0.55 | open |  |
| 10-03 23:20 | +10 | ETH | DOWN | 0.55 | open |  |
| 10-03 23:20 | +5 | ETH | DOWN | 0.55 | open |  |
| 10-03 23:18 | +10 stop | XRP | UP | 0.67 | 0.81 | 1.13 |
| 10-03 23:18 | +10 | XRP | UP | 0.67 | 0.81 | 1.13 |
| 10-03 23:18 | +5 | XRP | UP | 0.67 | 0.81 | 1.13 |
| 10-03 23:18 | +10 stop | SOL | UP | 0.70 | 0.85 | 1.26 |
| 10-03 23:18 | +10 | SOL | UP | 0.70 | 0.85 | 1.26 |
| 10-03 23:18 | +5 | SOL | UP | 0.70 | 0.75 | 0.21 |
| 10-03 23:17 | +10 stop | HYPE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-03 23:17 | +20 | HYPE | DOWN | 0.65 | 0.85 | 1.75 |
| 10-03 23:17 | +15 | HYPE | DOWN | 0.65 | 0.83 | 1.54 |
| 10-03 23:17 | +10 | HYPE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-03 23:17 | +5 | HYPE | DOWN | 0.65 | 0.70 | 0.19 |
| 10-03 23:17 | +10 stop | DOGE | UP | 0.58 | 0.42 | -1.96 |
| 10-03 23:17 | +20 | DOGE | UP | 0.58 | 0.83 | 2.22 |
| 10-03 23:17 | +15 | DOGE | UP | 0.58 | 0.74 | 1.28 |
| 10-03 23:17 | +10 | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 10-03 23:17 | +5 | DOGE | UP | 0.58 | 0.64 | 0.25 |
| 10-03 23:16 | +10 stop | SOL | UP | 0.68 | 0.78 | 0.71 |
| 10-03 23:16 | +20 | SOL | UP | 0.68 | 0.89 | 1.87 |
| 10-03 23:16 | +15 | SOL | UP | 0.68 | 0.85 | 1.45 |
| 10-03 23:16 | +10 | SOL | UP | 0.68 | 0.78 | 0.71 |
| 10-03 23:16 | +5 | SOL | UP | 0.68 | 0.78 | 0.71 |
| 10-03 23:16 | +10 stop | HYPE | UP | 0.37 | 0.58 | 1.75 |
| 10-03 23:16 | +20 | HYPE | UP | 0.37 | 0.58 | 1.75 |
| 10-03 23:16 | +15 | HYPE | UP | 0.39 | 0.58 | 1.55 |
| 10-03 23:16 | +10 | HYPE | UP | 0.39 | 0.58 | 1.55 |
