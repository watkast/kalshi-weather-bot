# Range-Scalp Bot

*Updated Sun Nov 22 12:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68628 | 59881 | 8747 (142) | 1 | $-18481.70 | -4.3% |
| **+10¢** | 51239 | 41023 | 10216 (186) | 1 | $-17139.10 | -5.3% |
| **+15¢** | 42941 | 31930 | 11011 (237) | 3 | $-15378.02 | -5.7% |
| **+20¢** | 38227 | 26658 | 11569 (295) | 3 | $-13689.81 | -5.7% |
| **+10¢ (15¢ stop)** | 83588 | 83403 | 185 (116) | 0 | $-30782.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 12:14 | +10 stop | SOL | DOWN | 0.13 | 0.66 | 5.07 |
| 11-22 12:13 | +10 stop | ZEC | DOWN | 0.58 | 0.25 | -3.61 |
| 11-22 12:13 | +10 stop | SOL | UP | 0.52 | 0.68 | 1.26 |
| 11-22 12:12 | +10 stop | ZEC | UP | 0.35 | 0.57 | 1.86 |
| 11-22 12:11 | +10 stop | SOL | DOWN | 0.50 | 0.28 | -2.53 |
| 11-22 12:10 | +10 stop | ZEC | UP | 0.59 | 0.43 | -1.95 |
| 11-22 12:10 | +5 | ZEC | UP | 0.62 | 0.68 | 0.29 |
| 11-22 12:09 | +5 | HYPE | UP | 0.66 | 0.71 | 0.19 |
| 11-22 12:09 | +10 stop | HYPE | UP | 0.59 | 0.71 | 0.88 |
| 11-22 12:09 | +20 | HYPE | UP | 0.58 | 0.88 | 2.74 |
| 11-22 12:09 | +15 | HYPE | UP | 0.59 | 0.74 | 1.19 |
| 11-22 12:09 | +10 | HYPE | UP | 0.60 | 0.71 | 0.78 |
| 11-22 12:09 | +5 | HYPE | UP | 0.61 | 0.67 | 0.27 |
| 11-22 12:09 | +10 stop | ZEC | DOWN | 0.54 | 0.36 | -2.15 |
| 11-22 12:09 | +10 stop | SOL | DOWN | 0.67 | 0.46 | -2.44 |
| 11-22 12:09 | +20 | SOL | DOWN | 0.67 | open |  |
| 11-22 12:09 | +15 | SOL | DOWN | 0.67 | open |  |
| 11-22 12:09 | +10 | SOL | DOWN | 0.67 | open |  |
| 11-22 12:09 | +5 | SOL | DOWN | 0.67 | open |  |
| 11-22 12:08 | +10 stop | DOGE | DOWN | 0.45 | 0.59 | 1.05 |
| 11-22 12:08 | +20 | DOGE | DOWN | 0.46 | open |  |
| 11-22 12:08 | +15 | DOGE | DOWN | 0.46 | open |  |
| 11-22 12:08 | +10 | DOGE | DOWN | 0.46 | 0.59 | 0.95 |
| 11-22 12:08 | +5 | DOGE | DOWN | 0.46 | 0.59 | 0.95 |
| 11-22 12:08 | +5 | ETH | UP | 0.65 | 0.85 | 1.75 |
| 11-22 12:07 | +10 stop | ZEC | DOWN | 0.70 | 0.54 | -1.93 |
| 11-22 12:07 | +5 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-22 12:07 | +5 | ETH | UP | 0.68 | 0.73 | 0.20 |
| 11-22 12:07 | +15 | BTC | UP | 0.70 | 0.85 | 1.26 |
| 11-22 12:07 | +5 | BTC | UP | 0.70 | 0.84 | 1.15 |
| 11-22 12:07 | +10 stop | SOL | DOWN | 0.67 | 0.81 | 1.14 |
| 11-22 12:05 | +5 | XRP | UP | 0.61 | 0.82 | 1.82 |
| 11-22 12:05 | +5 | XRP | UP | 0.51 | 0.57 | 0.24 |
| 11-22 12:04 | +10 stop | BTC | UP | 0.70 | 0.84 | 1.15 |
| 11-22 12:04 | +10 | BTC | UP | 0.70 | 0.84 | 1.15 |
| 11-22 12:04 | +5 | BTC | UP | 0.70 | 0.76 | 0.32 |
| 11-22 12:04 | +10 stop | SOL | UP | 0.64 | 0.43 | -2.45 |
| 11-22 12:04 | +10 stop | XRP | UP | 0.59 | 0.82 | 2.02 |
| 11-22 12:04 | +10 | XRP | UP | 0.59 | 0.82 | 2.02 |
| 11-22 12:04 | +5 | XRP | UP | 0.59 | 0.66 | 0.37 |
