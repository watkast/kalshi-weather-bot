# Range-Scalp Bot

*Updated Sat Nov 14 00:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58778 | 51284 | 7494 (106) | 2 | $-15879.05 | -4.3% |
| **+10¢** | 43912 | 35149 | 8763 (139) | 2 | $-14850.12 | -5.4% |
| **+15¢** | 36802 | 27362 | 9440 (174) | 2 | $-13429.47 | -5.8% |
| **+20¢** | 32785 | 22874 | 9911 (226) | 2 | $-11817.79 | -5.7% |
| **+10¢ (15¢ stop)** | 71558 | 71420 | 138 (82) | 2 | $-26341.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 00:45 | +10 stop | ZEC | DOWN | 0.64 | open |  |
| 11-14 00:45 | +20 | ZEC | DOWN | 0.64 | open |  |
| 11-14 00:45 | +15 | ZEC | DOWN | 0.64 | open |  |
| 11-14 00:45 | +10 | ZEC | DOWN | 0.64 | open |  |
| 11-14 00:45 | +5 | ZEC | DOWN | 0.64 | open |  |
| 11-14 00:45 | +10 stop | ETH | DOWN | 0.53 | open |  |
| 11-14 00:45 | +20 | ETH | DOWN | 0.53 | open |  |
| 11-14 00:45 | +15 | ETH | DOWN | 0.53 | open |  |
| 11-14 00:45 | +10 | ETH | DOWN | 0.53 | open |  |
| 11-14 00:45 | +5 | ETH | DOWN | 0.53 | open |  |
| 11-14 00:43 | +10 | BTC | UP | 0.67 | 0.82 | 1.23 |
| 11-14 00:43 | +5 | BTC | UP | 0.69 | 0.82 | 1.04 |
| 11-14 00:43 | +10 stop | NEAR | UP | 0.70 | 0.85 | 1.26 |
| 11-14 00:43 | +15 | NEAR | UP | 0.70 | 0.85 | 1.26 |
| 11-14 00:43 | +10 | NEAR | UP | 0.70 | 0.85 | 1.26 |
| 11-14 00:43 | +5 | NEAR | UP | 0.67 | 0.79 | 0.92 |
| 11-14 00:43 | +10 stop | BTC | UP | 0.68 | 0.82 | 1.13 |
| 11-14 00:43 | +20 | BTC | UP | 0.68 | 0.91 | 2.11 |
| 11-14 00:43 | +15 | BTC | UP | 0.68 | 0.91 | 2.11 |
| 11-14 00:41 | +10 stop | XRP | UP | 0.49 | 0.60 | 0.75 |
| 11-14 00:41 | +20 | XRP | UP | 0.49 | 0.72 | 1.97 |
| 11-14 00:41 | +15 | XRP | UP | 0.49 | 0.72 | 1.97 |
| 11-14 00:41 | +10 | XRP | UP | 0.49 | 0.60 | 0.75 |
| 11-14 00:41 | +5 | XRP | UP | 0.49 | 0.56 | 0.34 |
| 11-14 00:41 | +10 stop | ZEC | UP | 0.47 | 0.57 | 0.64 |
| 11-14 00:41 | +10 | ZEC | UP | 0.44 | 0.54 | 0.64 |
| 11-14 00:41 | +5 | ZEC | UP | 0.45 | 0.54 | 0.54 |
| 11-14 00:40 | +10 stop | HYPE | UP | 0.62 | 0.78 | 1.30 |
| 11-14 00:40 | +10 stop | ZEC | DOWN | 0.48 | 0.60 | 0.85 |
| 11-14 00:40 | +15 | ZEC | DOWN | 0.48 | 0.64 | 1.25 |
| 11-14 00:40 | +10 | ZEC | DOWN | 0.48 | 0.60 | 0.85 |
| 11-14 00:40 | +5 | ZEC | DOWN | 0.48 | 0.60 | 0.85 |
| 11-14 00:39 | +10 stop | DOGE | UP | 0.66 | 0.80 | 1.12 |
| 11-14 00:39 | +10 stop | HYPE | DOWN | 0.70 | 0.55 | -1.83 |
| 11-14 00:39 | +10 | HYPE | DOWN | 0.70 | yes | -7.15 |
| 11-14 00:39 | +5 | HYPE | DOWN | 0.70 | yes | -7.15 |
| 11-14 00:36 | +5 | BNB | DOWN | 0.55 | 0.65 | 0.69 |
| 11-14 00:36 | +10 stop | DOGE | UP | 0.56 | 0.25 | -3.42 |
| 11-14 00:36 | +5 | DOGE | UP | 0.56 | 0.61 | 0.15 |
| 11-14 00:36 | +10 stop | ZEC | DOWN | 0.69 | 0.87 | 1.57 |
