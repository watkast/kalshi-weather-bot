# Range-Scalp Bot

*Updated Tue Nov 03 04:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45543 | 39655 | 5888 (69) | 1 | $-13148.02 | -4.6% |
| **+10¢** | 33998 | 27174 | 6824 (91) | 1 | $-12041.91 | -5.6% |
| **+15¢** | 28446 | 21104 | 7342 (119) | 1 | $-11049.83 | -6.2% |
| **+20¢** | 25263 | 17570 | 7693 (154) | 1 | $-9835.87 | -6.2% |
| **+10¢ (15¢ stop)** | 55567 | 55478 | 89 (53) | 1 | $-20942.17 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 04:01 | +10 stop | XRP | DOWN | 0.66 | open |  |
| 11-03 04:01 | +20 | XRP | DOWN | 0.66 | open |  |
| 11-03 04:01 | +15 | XRP | DOWN | 0.65 | open |  |
| 11-03 04:01 | +10 | XRP | DOWN | 0.65 | open |  |
| 11-03 04:01 | +5 | XRP | DOWN | 0.65 | open |  |
| 11-03 03:50 | +10 | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 11-03 03:50 | +5 | HYPE | UP | 0.67 | 0.75 | 0.50 |
| 11-03 03:46 | +5 | HYPE | UP | 0.71 | 0.77 | 0.32 |
| 11-03 03:45 | +10 stop | BTC | UP | 0.66 | 0.83 | 1.44 |
| 11-03 03:45 | +20 | BTC | UP | 0.66 | 0.86 | 1.75 |
| 11-03 03:45 | +15 | BTC | UP | 0.66 | 0.83 | 1.44 |
| 11-03 03:45 | +10 | BTC | UP | 0.66 | 0.83 | 1.44 |
| 11-03 03:45 | +5 | BTC | UP | 0.66 | 0.72 | 0.29 |
| 11-03 03:45 | +10 stop | HYPE | UP | 0.64 | 0.77 | 1.00 |
| 11-03 03:45 | +20 | HYPE | UP | 0.64 | 0.86 | 1.94 |
| 11-03 03:45 | +15 | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 11-03 03:45 | +10 | HYPE | UP | 0.64 | 0.77 | 1.00 |
| 11-03 03:45 | +5 | HYPE | UP | 0.64 | 0.69 | 0.18 |
| 11-03 03:40 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-03 03:39 | +10 stop | DOGE | DOWN | 0.53 | 0.66 | 0.96 |
| 11-03 03:39 | +20 | DOGE | DOWN | 0.53 | 0.78 | 2.19 |
| 11-03 03:39 | +15 | DOGE | DOWN | 0.53 | 0.71 | 1.47 |
| 11-03 03:39 | +10 | DOGE | DOWN | 0.53 | 0.66 | 0.96 |
| 11-03 03:39 | +5 | DOGE | DOWN | 0.53 | 0.58 | 0.14 |
| 11-03 03:38 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 11-03 03:38 | +20 | XRP | DOWN | 0.64 | 0.84 | 1.73 |
| 11-03 03:38 | +15 | XRP | DOWN | 0.64 | 0.81 | 1.42 |
| 11-03 03:38 | +10 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-03 03:38 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 11-03 03:36 | +10 stop | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 11-03 03:36 | +20 | NEAR | UP | 0.69 | 0.93 | 2.16 |
| 11-03 03:36 | +15 | NEAR | UP | 0.69 | 0.86 | 1.46 |
| 11-03 03:36 | +10 | NEAR | UP | 0.71 | 0.86 | 1.26 |
| 11-03 03:36 | +5 | NEAR | UP | 0.71 | 0.77 | 0.32 |
| 11-03 03:36 | +10 stop | ZEC | DOWN | 0.54 | 0.33 | -2.44 |
| 11-03 03:36 | +20 | ZEC | DOWN | 0.54 | yes | -5.58 |
| 11-03 03:36 | +15 | ZEC | DOWN | 0.54 | yes | -5.58 |
| 11-03 03:36 | +10 | ZEC | DOWN | 0.54 | yes | -5.58 |
| 11-03 03:36 | +5 | ZEC | DOWN | 0.53 | yes | -5.48 |
| 11-03 03:35 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
