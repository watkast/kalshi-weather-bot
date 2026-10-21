# Range-Scalp Bot

*Updated Wed Oct 21 19:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27621 | 24054 | 3567 (39) | 2 | $-8032.41 | -4.6% |
| **+10¢** | 20768 | 16650 | 4118 (55) | 0 | $-7069.21 | -5.4% |
| **+15¢** | 17394 | 12961 | 4433 (78) | 0 | $-6320.37 | -5.8% |
| **+20¢** | 15398 | 10752 | 4646 (98) | 0 | $-5667.15 | -5.9% |
| **+10¢ (15¢ stop)** | 33887 | 33828 | 59 (32) | 0 | $-12593.39 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 19:09 | +10 stop | BNB | UP | 0.69 | 0.47 | -2.53 |
| 10-21 19:09 | +5 | BNB | UP | 0.69 | open |  |
| 10-21 19:09 | +10 stop | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-21 19:09 | +10 stop | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-21 19:09 | +10 stop | BNB | UP | 0.43 | 0.63 | 1.65 |
| 10-21 19:09 | +5 | BNB | UP | 0.43 | 0.63 | 1.65 |
| 10-21 19:08 | +10 stop | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-21 19:08 | +20 | HYPE | DOWN | 0.71 | 0.91 | 1.83 |
| 10-21 19:08 | +15 | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-21 19:08 | +10 | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-21 19:08 | +5 | HYPE | DOWN | 0.71 | 0.78 | 0.42 |
| 10-21 19:08 | +10 stop | BNB | UP | 0.63 | 0.74 | 0.79 |
| 10-21 19:08 | +5 | BNB | UP | 0.63 | 0.74 | 0.79 |
| 10-21 19:08 | +10 stop | ZEC | UP | 0.64 | 0.43 | -2.45 |
| 10-21 19:07 | +10 stop | DOGE | UP | 0.65 | 0.30 | -3.80 |
| 10-21 19:07 | +5 | DOGE | UP | 0.61 | open |  |
| 10-21 19:07 | +10 stop | BNB | DOWN | 0.46 | 0.59 | 0.95 |
| 10-21 19:07 | +5 | BNB | DOWN | 0.46 | 0.59 | 0.95 |
| 10-21 19:07 | +5 | DOGE | DOWN | 0.46 | 0.62 | 1.25 |
| 10-21 19:05 | +10 stop | DOGE | DOWN | 0.64 | 0.45 | -2.25 |
| 10-21 19:05 | +10 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-21 19:05 | +5 | DOGE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-21 19:05 | +20 | ZEC | DOWN | 0.66 | 0.87 | 1.86 |
| 10-21 19:05 | +5 | BNB | DOWN | 0.51 | 0.59 | 0.45 |
| 10-21 19:05 | +10 stop | ZEC | DOWN | 0.70 | 0.54 | -1.96 |
| 10-21 19:05 | +15 | ZEC | DOWN | 0.71 | 0.87 | 1.38 |
| 10-21 19:05 | +10 | ZEC | DOWN | 0.69 | 0.85 | 1.33 |
| 10-21 19:05 | +5 | ZEC | DOWN | 0.69 | 0.75 | 0.28 |
| 10-21 19:03 | +10 stop | BNB | DOWN | 0.63 | 0.46 | -2.05 |
| 10-21 19:03 | +20 | BNB | DOWN | 0.63 | 0.90 | 2.47 |
| 10-21 19:03 | +15 | BNB | DOWN | 0.63 | 0.90 | 2.47 |
| 10-21 19:03 | +10 | BNB | DOWN | 0.63 | 0.90 | 2.47 |
| 10-21 19:03 | +5 | BNB | DOWN | 0.63 | 0.72 | 0.58 |
| 10-21 19:03 | +10 stop | DOGE | DOWN | 0.70 | 0.83 | 1.05 |
| 10-21 19:03 | +20 | DOGE | DOWN | 0.70 | 0.97 | 2.49 |
| 10-21 19:03 | +15 | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
| 10-21 19:03 | +10 | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-21 19:03 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-21 19:01 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-21 19:01 | +10 stop | BNB | DOWN | 0.62 | 0.77 | 1.20 |
