# Range-Scalp Bot

*Updated Sat Nov 14 23:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60027 | 52360 | 7667 (107) | 0 | $-16347.89 | -4.3% |
| **+10¢** | 44849 | 35868 | 8981 (143) | 1 | $-15417.84 | -5.5% |
| **+15¢** | 37578 | 27893 | 9685 (181) | 2 | $-14058.03 | -6.0% |
| **+20¢** | 33481 | 23321 | 10160 (233) | 2 | $-12388.15 | -5.9% |
| **+10¢ (15¢ stop)** | 73080 | 72937 | 143 (82) | 1 | $-26871.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 23:41 | +10 stop | ZEC | DOWN | 0.39 | 0.56 | 1.37 |
| 11-14 23:41 | +10 | ZEC | DOWN | 0.39 | 0.56 | 1.35 |
| 11-14 23:41 | +5 | ZEC | DOWN | 0.39 | 0.56 | 1.35 |
| 11-14 23:38 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.42 |
| 11-14 23:38 | +10 stop | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-14 23:36 | +10 stop | HYPE | UP | 0.69 | 0.92 | 2.05 |
| 11-14 23:36 | +15 | HYPE | UP | 0.69 | 0.92 | 2.05 |
| 11-14 23:36 | +10 | HYPE | UP | 0.66 | 0.77 | 0.81 |
| 11-14 23:35 | +10 stop | ZEC | DOWN | 0.55 | 0.69 | 1.07 |
| 11-14 23:34 | +5 | HYPE | UP | 0.71 | 0.77 | 0.32 |
| 11-14 23:34 | +5 | DOGE | DOWN | 0.67 | 0.73 | 0.32 |
| 11-14 23:33 | +10 | ETH | DOWN | 0.70 | 0.84 | 1.15 |
| 11-14 23:33 | +5 | ETH | DOWN | 0.70 | 0.77 | 0.42 |
| 11-14 23:33 | +10 stop | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-14 23:33 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.89 |
| 11-14 23:33 | +15 | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 11-14 23:33 | +10 stop | XRP | DOWN | 0.60 | 0.84 | 2.13 |
| 11-14 23:32 | +10 stop | HYPE | UP | 0.58 | 0.69 | 0.77 |
| 11-14 23:32 | +20 | HYPE | UP | 0.58 | 0.92 | 3.11 |
| 11-14 23:32 | +15 | HYPE | UP | 0.58 | 0.73 | 1.18 |
| 11-14 23:32 | +10 | HYPE | UP | 0.58 | 0.69 | 0.77 |
| 11-14 23:32 | +5 | HYPE | UP | 0.58 | 0.63 | 0.15 |
| 11-14 23:31 | +10 stop | NEAR | DOWN | 0.71 | open |  |
| 11-14 23:31 | +20 | NEAR | DOWN | 0.71 | open |  |
| 11-14 23:31 | +15 | NEAR | DOWN | 0.71 | open |  |
| 11-14 23:31 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-14 23:31 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 11-14 23:31 | +10 stop | XRP | DOWN | 0.70 | 0.52 | -2.13 |
| 11-14 23:31 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.93 |
| 11-14 23:31 | +15 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 11-14 23:31 | +10 | XRP | DOWN | 0.70 | 0.84 | 1.15 |
| 11-14 23:31 | +5 | XRP | DOWN | 0.71 | 0.84 | 1.05 |
| 11-14 23:31 | +10 stop | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 11-14 23:31 | +20 | BNB | DOWN | 0.69 | 0.91 | 1.99 |
| 11-14 23:31 | +15 | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 11-14 23:31 | +10 | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 11-14 23:31 | +5 | BNB | DOWN | 0.69 | 0.78 | 0.62 |
| 11-14 23:31 | +10 stop | ZEC | DOWN | 0.66 | 0.51 | -1.84 |
| 11-14 23:31 | +20 | ZEC | DOWN | 0.66 | open |  |
| 11-14 23:31 | +15 | ZEC | DOWN | 0.67 | open |  |
