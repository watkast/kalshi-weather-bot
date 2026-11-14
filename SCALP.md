# Range-Scalp Bot

*Updated Sat Nov 14 04:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59028 | 51499 | 7529 (106) | 1 | $-15973.67 | -4.3% |
| **+10¢** | 44104 | 35303 | 8801 (139) | 2 | $-14931.34 | -5.4% |
| **+15¢** | 36957 | 27471 | 9486 (174) | 4 | $-13543.52 | -5.8% |
| **+20¢** | 32925 | 22966 | 9959 (226) | 4 | $-11923.67 | -5.8% |
| **+10¢ (15¢ stop)** | 71859 | 71721 | 138 (82) | 0 | $-26400.32 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 04:40 | +10 stop | NEAR | DOWN | 0.48 | 0.60 | 0.85 |
| 11-14 04:40 | +20 | NEAR | DOWN | 0.48 | open |  |
| 11-14 04:40 | +15 | NEAR | DOWN | 0.48 | open |  |
| 11-14 04:40 | +10 | NEAR | DOWN | 0.48 | 0.60 | 0.85 |
| 11-14 04:40 | +5 | NEAR | DOWN | 0.48 | 0.60 | 0.85 |
| 11-14 04:40 | +10 stop | BNB | UP | 0.61 | 0.81 | 1.72 |
| 11-14 04:40 | +20 | BNB | UP | 0.61 | 0.81 | 1.72 |
| 11-14 04:40 | +15 | BNB | UP | 0.61 | 0.81 | 1.72 |
| 11-14 04:40 | +10 | BNB | UP | 0.61 | 0.81 | 1.72 |
| 11-14 04:40 | +5 | BNB | UP | 0.61 | 0.81 | 1.72 |
| 11-14 04:39 | +10 stop | SOL | UP | 0.54 | 0.79 | 2.20 |
| 11-14 04:39 | +10 stop | ZEC | DOWN | 0.69 | 0.86 | 1.46 |
| 11-14 04:39 | +10 | ZEC | DOWN | 0.69 | 0.86 | 1.46 |
| 11-14 04:39 | +5 | ZEC | DOWN | 0.69 | 0.86 | 1.46 |
| 11-14 04:38 | +10 stop | ZEC | DOWN | 0.49 | 0.62 | 0.95 |
| 11-14 04:38 | +20 | ZEC | DOWN | 0.49 | 0.70 | 1.77 |
| 11-14 04:38 | +15 | ZEC | DOWN | 0.49 | 0.70 | 1.77 |
| 11-14 04:38 | +10 | ZEC | DOWN | 0.49 | 0.62 | 0.95 |
| 11-14 04:38 | +5 | ZEC | DOWN | 0.49 | 0.62 | 0.95 |
| 11-14 04:38 | +5 | SOL | UP | 0.71 | 0.79 | 0.53 |
| 11-14 04:38 | +10 stop | SOL | UP | 0.70 | 0.54 | -1.93 |
| 11-14 04:38 | +20 | SOL | UP | 0.71 | open |  |
| 11-14 04:38 | +15 | SOL | UP | 0.71 | open |  |
| 11-14 04:38 | +10 | SOL | UP | 0.71 | open |  |
| 11-14 04:36 | +5 | HYPE | UP | 0.66 | 0.77 | 0.81 |
| 11-14 04:35 | +10 stop | XRP | DOWN | 0.61 | 0.37 | -2.74 |
| 11-14 04:35 | +20 | XRP | DOWN | 0.63 | open |  |
| 11-14 04:35 | +15 | XRP | DOWN | 0.63 | open |  |
| 11-14 04:35 | +10 | XRP | DOWN | 0.63 | open |  |
| 11-14 04:35 | +5 | XRP | DOWN | 0.63 | open |  |
| 11-14 04:32 | +5 | SOL | DOWN | 0.69 | 0.84 | 1.25 |
| 11-14 04:32 | +10 stop | ZEC | DOWN | 0.60 | 0.85 | 2.24 |
| 11-14 04:32 | +20 | ZEC | DOWN | 0.60 | 0.85 | 2.24 |
| 11-14 04:32 | +15 | ZEC | DOWN | 0.60 | 0.85 | 2.24 |
| 11-14 04:32 | +10 | ZEC | DOWN | 0.60 | 0.85 | 2.24 |
| 11-14 04:32 | +5 | ZEC | DOWN | 0.60 | 0.85 | 2.24 |
| 11-14 04:32 | +10 stop | DOGE | DOWN | 0.69 | 0.82 | 1.04 |
| 11-14 04:32 | +20 | DOGE | DOWN | 0.69 | open |  |
| 11-14 04:32 | +15 | DOGE | DOWN | 0.70 | open |  |
| 11-14 04:32 | +10 | DOGE | DOWN | 0.70 | 0.82 | 0.95 |
