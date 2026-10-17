# Range-Scalp Bot

*Updated Sat Oct 17 19:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21482 | 18720 | 2762 (29) | 0 | $-6126.97 | -4.5% |
| **+10¢** | 16151 | 12956 | 3195 (41) | 0 | $-5472.34 | -5.4% |
| **+15¢** | 13501 | 10055 | 3446 (61) | 0 | $-4981.32 | -5.9% |
| **+20¢** | 11959 | 8347 | 3612 (80) | 0 | $-4438.28 | -5.9% |
| **+10¢ (15¢ stop)** | 26356 | 26306 | 50 (29) | 0 | $-10018.40 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 19:30 | +10 stop | HYPE | UP | 0.61 | 0.77 | 1.30 |
| 10-17 19:30 | +20 | HYPE | UP | 0.60 | 0.84 | 2.09 |
| 10-17 19:30 | +15 | HYPE | UP | 0.62 | 0.77 | 1.20 |
| 10-17 19:30 | +10 | HYPE | UP | 0.62 | 0.77 | 1.16 |
| 10-17 19:30 | +5 | HYPE | UP | 0.62 | 0.68 | 0.23 |
| 10-17 19:27 | +10 stop | ETH | UP | 0.67 | 0.23 | -4.69 |
| 10-17 19:27 | +20 | ETH | UP | 0.67 | no | -6.86 |
| 10-17 19:27 | +15 | ETH | UP | 0.67 | no | -6.86 |
| 10-17 19:27 | +10 | ETH | UP | 0.67 | no | -6.86 |
| 10-17 19:27 | +5 | ETH | UP | 0.67 | no | -6.87 |
| 10-17 19:27 | +10 stop | DOGE | DOWN | 0.60 | 0.79 | 1.59 |
| 10-17 19:27 | +15 | DOGE | DOWN | 0.60 | 0.79 | 1.59 |
| 10-17 19:27 | +10 | DOGE | DOWN | 0.61 | 0.79 | 1.51 |
| 10-17 19:27 | +5 | DOGE | DOWN | 0.60 | 0.79 | 1.61 |
| 10-17 19:26 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 10-17 19:26 | +10 stop | DOGE | UP | 0.49 | 0.64 | 1.15 |
| 10-17 19:26 | +20 | DOGE | UP | 0.49 | no | -5.08 |
| 10-17 19:26 | +15 | DOGE | UP | 0.48 | 0.64 | 1.25 |
| 10-17 19:26 | +10 | DOGE | UP | 0.48 | 0.64 | 1.25 |
| 10-17 19:26 | +5 | DOGE | UP | 0.48 | 0.64 | 1.26 |
| 10-17 19:25 | +10 stop | SOL | UP | 0.70 | 0.39 | -3.42 |
| 10-17 19:25 | +20 | SOL | UP | 0.70 | no | -7.15 |
| 10-17 19:25 | +15 | SOL | UP | 0.70 | no | -7.15 |
| 10-17 19:25 | +10 | SOL | UP | 0.70 | no | -7.15 |
| 10-17 19:25 | +5 | SOL | UP | 0.70 | 0.79 | 0.63 |
| 10-17 19:25 | +10 stop | BTC | DOWN | 0.49 | 0.73 | 2.08 |
| 10-17 19:25 | +10 stop | NEAR | DOWN | 0.68 | 0.88 | 1.76 |
| 10-17 19:24 | +10 stop | ZEC | UP | 0.47 | 0.59 | 0.85 |
| 10-17 19:24 | +15 | ZEC | UP | 0.47 | no | -4.88 |
| 10-17 19:24 | +10 | ZEC | UP | 0.47 | 0.59 | 0.85 |
| 10-17 19:24 | +5 | ZEC | UP | 0.47 | 0.59 | 0.85 |
| 10-17 19:23 | +10 stop | BTC | UP | 0.63 | 0.43 | -2.35 |
| 10-17 19:23 | +10 stop | NEAR | UP | 0.61 | 0.37 | -2.70 |
| 10-17 19:23 | +15 | NEAR | UP | 0.61 | no | -6.23 |
| 10-17 19:23 | +10 | NEAR | UP | 0.61 | no | -6.23 |
| 10-17 19:21 | +10 stop | XRP | UP | 0.65 | 0.76 | 0.81 |
| 10-17 19:21 | +10 | XRP | UP | 0.65 | 0.76 | 0.81 |
| 10-17 19:21 | +5 | XRP | UP | 0.65 | 0.73 | 0.50 |
| 10-17 19:21 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-17 19:20 | +10 stop | XRP | UP | 0.57 | 0.68 | 0.76 |
