# Range-Scalp Bot

*Updated Mon Nov 23 03:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69532 | 60668 | 8864 (146) | 3 | $-18743.85 | -4.3% |
| **+10¢** | 51880 | 41525 | 10355 (189) | 6 | $-17442.11 | -5.3% |
| **+15¢** | 43472 | 32318 | 11154 (244) | 7 | $-15590.20 | -5.7% |
| **+20¢** | 38715 | 26989 | 11726 (306) | 7 | $-13889.15 | -5.7% |
| **+10¢ (15¢ stop)** | 84648 | 84458 | 190 (118) | 0 | $-31102.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 03:33 | +10 stop | ETH | UP | 0.70 | 0.80 | 0.73 |
| 11-23 03:33 | +10 stop | SOL | UP | 0.70 | 0.83 | 1.04 |
| 11-23 03:32 | +10 stop | BTC | UP | 0.57 | 0.69 | 0.87 |
| 11-23 03:32 | +10 stop | BNB | UP | 0.61 | 0.76 | 1.20 |
| 11-23 03:32 | +5 | BNB | UP | 0.61 | 0.76 | 1.18 |
| 11-23 03:32 | +5 | DOGE | UP | 0.62 | 0.71 | 0.60 |
| 11-23 03:32 | +5 | ZEC | UP | 0.58 | 0.65 | 0.36 |
| 11-23 03:32 | +10 stop | DOGE | UP | 0.51 | 0.71 | 1.67 |
| 11-23 03:32 | +10 | DOGE | UP | 0.51 | 0.71 | 1.67 |
| 11-23 03:32 | +5 | DOGE | UP | 0.50 | 0.56 | 0.24 |
| 11-23 03:32 | +10 stop | ETH | UP | 0.47 | 0.57 | 0.64 |
| 11-23 03:32 | +5 | NEAR | UP | 0.57 | 0.62 | 0.16 |
| 11-23 03:31 | +10 stop | XRP | UP | 0.68 | 0.79 | 0.82 |
| 11-23 03:31 | +10 stop | SOL | UP | 0.70 | 0.53 | -2.03 |
| 11-23 03:31 | +5 | BTC | UP | 0.66 | 0.71 | 0.19 |
| 11-23 03:31 | +10 stop | XRP | DOWN | 0.58 | 0.42 | -1.96 |
| 11-23 03:31 | +20 | XRP | DOWN | 0.58 | open |  |
| 11-23 03:31 | +15 | XRP | DOWN | 0.57 | open |  |
| 11-23 03:31 | +10 | XRP | DOWN | 0.57 | open |  |
| 11-23 03:31 | +5 | XRP | DOWN | 0.58 | open |  |
| 11-23 03:31 | +10 stop | SOL | DOWN | 0.55 | 0.40 | -1.85 |
| 11-23 03:31 | +20 | SOL | DOWN | 0.55 | open |  |
| 11-23 03:31 | +15 | SOL | DOWN | 0.55 | open |  |
| 11-23 03:31 | +10 | SOL | DOWN | 0.55 | open |  |
| 11-23 03:31 | +5 | SOL | DOWN | 0.55 | open |  |
| 11-23 03:31 | +10 stop | ETH | DOWN | 0.59 | 0.44 | -1.85 |
| 11-23 03:31 | +20 | ETH | DOWN | 0.59 | open |  |
| 11-23 03:31 | +15 | ETH | DOWN | 0.59 | open |  |
| 11-23 03:31 | +10 | ETH | DOWN | 0.59 | open |  |
| 11-23 03:31 | +5 | ETH | DOWN | 0.59 | open |  |
| 11-23 03:31 | +10 stop | BTC | DOWN | 0.51 | 0.34 | -2.04 |
| 11-23 03:31 | +20 | BTC | DOWN | 0.51 | open |  |
| 11-23 03:31 | +15 | BTC | DOWN | 0.51 | open |  |
| 11-23 03:31 | +10 | BTC | DOWN | 0.51 | open |  |
| 11-23 03:31 | +5 | BTC | DOWN | 0.51 | 0.60 | 0.55 |
| 11-23 03:31 | +10 stop | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 11-23 03:31 | +20 | ZEC | UP | 0.64 | 0.85 | 1.86 |
| 11-23 03:31 | +15 | ZEC | UP | 0.64 | 0.79 | 1.21 |
| 11-23 03:31 | +10 | ZEC | UP | 0.64 | 0.79 | 1.21 |
| 11-23 03:31 | +5 | ZEC | UP | 0.64 | 0.72 | 0.48 |
