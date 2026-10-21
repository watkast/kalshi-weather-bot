# Range-Scalp Bot

*Updated Wed Oct 21 15:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27343 | 23804 | 3539 (39) | 2 | $-8001.46 | -4.6% |
| **+10¢** | 20558 | 16471 | 4087 (55) | 2 | $-7073.52 | -5.5% |
| **+15¢** | 17217 | 12820 | 4397 (78) | 2 | $-6320.96 | -5.8% |
| **+20¢** | 15240 | 10632 | 4608 (98) | 2 | $-5679.45 | -5.9% |
| **+10¢ (15¢ stop)** | 33553 | 33494 | 59 (32) | 0 | $-12463.05 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 15:09 | +10 stop | XRP | DOWN | 0.61 | 0.44 | -2.05 |
| 10-21 15:09 | +20 | XRP | DOWN | 0.61 | open |  |
| 10-21 15:09 | +15 | XRP | DOWN | 0.61 | open |  |
| 10-21 15:09 | +10 | XRP | DOWN | 0.61 | open |  |
| 10-21 15:09 | +5 | XRP | DOWN | 0.61 | open |  |
| 10-21 15:07 | +10 stop | BTC | UP | 0.71 | 0.81 | 0.74 |
| 10-21 15:05 | +10 | BNB | UP | 0.70 | 0.83 | 1.05 |
| 10-21 15:05 | +5 | BNB | UP | 0.67 | 0.73 | 0.27 |
| 10-21 15:05 | +10 stop | ZEC | UP | 0.62 | 0.75 | 0.99 |
| 10-21 15:05 | +15 | ZEC | UP | 0.62 | 0.77 | 1.20 |
| 10-21 15:05 | +10 | ZEC | UP | 0.63 | 0.75 | 0.89 |
| 10-21 15:05 | +5 | ZEC | UP | 0.64 | 0.69 | 0.18 |
| 10-21 15:05 | +5 | BTC | DOWN | 0.65 | open |  |
| 10-21 15:05 | +10 stop | DOGE | UP | 0.47 | 0.57 | 0.67 |
| 10-21 15:05 | +15 | DOGE | UP | 0.46 | 0.63 | 1.36 |
| 10-21 15:05 | +10 | DOGE | UP | 0.39 | 0.55 | 1.25 |
| 10-21 15:05 | +5 | DOGE | UP | 0.39 | 0.55 | 1.25 |
| 10-21 15:05 | +10 stop | HYPE | UP | 0.54 | 0.66 | 0.86 |
| 10-21 15:05 | +5 | HYPE | UP | 0.54 | 0.66 | 0.86 |
| 10-21 15:05 | +5 | SOL | UP | 0.56 | 0.61 | 0.15 |
| 10-21 15:04 | +10 stop | XRP | DOWN | 0.68 | 0.82 | 1.13 |
| 10-21 15:04 | +15 | XRP | DOWN | 0.69 | 0.85 | 1.36 |
| 10-21 15:04 | +10 | XRP | DOWN | 0.69 | 0.82 | 1.04 |
| 10-21 15:04 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 10-21 15:04 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-21 15:03 | +10 stop | HYPE | DOWN | 0.55 | 0.36 | -2.25 |
| 10-21 15:03 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 10-21 15:03 | +10 stop | BTC | DOWN | 0.61 | 0.44 | -2.05 |
| 10-21 15:03 | +20 | BTC | DOWN | 0.61 | open |  |
| 10-21 15:03 | +15 | BTC | DOWN | 0.61 | open |  |
| 10-21 15:03 | +10 | BTC | DOWN | 0.61 | open |  |
| 10-21 15:03 | +5 | BTC | DOWN | 0.61 | 0.68 | 0.37 |
| 10-21 15:02 | +5 | ETH | UP | 0.67 | 0.74 | 0.40 |
| 10-21 15:02 | +10 stop | SOL | UP | 0.59 | 0.41 | -2.14 |
| 10-21 15:02 | +10 | SOL | UP | 0.59 | 0.70 | 0.78 |
| 10-21 15:02 | +5 | SOL | UP | 0.60 | 0.65 | 0.17 |
| 10-21 15:02 | +10 stop | HYPE | UP | 0.63 | 0.42 | -2.46 |
| 10-21 15:02 | +20 | HYPE | UP | 0.64 | 0.85 | 1.86 |
| 10-21 15:02 | +15 | HYPE | UP | 0.64 | 0.80 | 1.33 |
| 10-21 15:02 | +10 | HYPE | UP | 0.63 | 0.80 | 1.39 |
