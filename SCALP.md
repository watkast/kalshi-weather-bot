# Range-Scalp Bot

*Updated Sat Nov 14 23:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60030 | 52362 | 7668 (107) | 0 | $-16352.83 | -4.3% |
| **+10¢** | 44853 | 35870 | 8983 (143) | 0 | $-15429.63 | -5.5% |
| **+15¢** | 37582 | 27894 | 9688 (181) | 0 | $-14077.44 | -6.0% |
| **+20¢** | 33485 | 23321 | 10164 (233) | 0 | $-12413.51 | -5.9% |
| **+10¢ (15¢ stop)** | 73084 | 72941 | 143 (82) | 0 | $-26876.28 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 23:44 | +10 stop | ETH | DOWN | 0.43 | 0.62 | 1.55 |
| 11-14 23:44 | +20 | ETH | DOWN | 0.47 | yes | -4.88 |
| 11-14 23:44 | +15 | ETH | DOWN | 0.47 | 0.62 | 1.15 |
| 11-14 23:44 | +10 | ETH | DOWN | 0.47 | 0.62 | 1.15 |
| 11-14 23:44 | +5 | ETH | DOWN | 0.51 | 0.62 | 0.75 |
| 11-14 23:42 | +10 stop | XRP | DOWN | 0.66 | 0.29 | -4.01 |
| 11-14 23:42 | +20 | XRP | DOWN | 0.63 | yes | -6.47 |
| 11-14 23:42 | +15 | XRP | DOWN | 0.63 | yes | -6.47 |
| 11-14 23:42 | +10 | XRP | DOWN | 0.62 | yes | -6.37 |
| 11-14 23:42 | +5 | XRP | DOWN | 0.62 | yes | -6.37 |
| 11-14 23:42 | +10 stop | ZEC | UP | 0.62 | 0.72 | 0.68 |
| 11-14 23:42 | +10 | ZEC | UP | 0.62 | 0.72 | 0.68 |
| 11-14 23:42 | +5 | ZEC | UP | 0.62 | 0.72 | 0.68 |
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
| 11-14 23:31 | +10 stop | NEAR | DOWN | 0.71 | 0.42 | -3.23 |
| 11-14 23:31 | +20 | NEAR | DOWN | 0.71 | yes | -7.25 |
| 11-14 23:31 | +15 | NEAR | DOWN | 0.71 | yes | -7.25 |
| 11-14 23:31 | +10 | NEAR | DOWN | 0.71 | yes | -7.25 |
| 11-14 23:31 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
