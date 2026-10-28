# Range-Scalp Bot

*Updated Wed Oct 28 11:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38038 | 33190 | 4848 (46) | 2 | $-10708.47 | -4.5% |
| **+10¢** | 28378 | 22769 | 5609 (68) | 2 | $-9570.31 | -5.4% |
| **+15¢** | 23741 | 17719 | 6022 (93) | 3 | $-8521.50 | -5.7% |
| **+20¢** | 21054 | 14748 | 6306 (118) | 4 | $-7495.77 | -5.7% |
| **+10¢ (15¢ stop)** | 46579 | 46512 | 67 (35) | 1 | $-17756.94 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 11:41 | +10 stop | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 10-28 11:41 | +20 | BTC | DOWN | 0.63 | open |  |
| 10-28 11:41 | +15 | BTC | DOWN | 0.63 | 0.81 | 1.52 |
| 10-28 11:41 | +10 | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 10-28 11:41 | +5 | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 10-28 11:41 | +10 stop | BNB | UP | 0.62 | open |  |
| 10-28 11:41 | +10 stop | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 10-28 11:41 | +10 | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 10-28 11:41 | +5 | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 10-28 11:40 | +10 stop | NEAR | UP | 0.42 | 0.52 | 0.64 |
| 10-28 11:40 | +15 | NEAR | UP | 0.42 | open |  |
| 10-28 11:40 | +10 | NEAR | UP | 0.42 | 0.52 | 0.64 |
| 10-28 11:40 | +5 | NEAR | UP | 0.43 | 0.52 | 0.54 |
| 10-28 11:39 | +10 stop | HYPE | UP | 0.58 | 0.42 | -1.93 |
| 10-28 11:38 | +10 stop | ZEC | UP | 0.46 | 0.57 | 0.74 |
| 10-28 11:37 | +5 | HYPE | DOWN | 0.64 | 0.86 | 1.94 |
| 10-28 11:36 | +10 stop | NEAR | UP | 0.57 | 0.71 | 1.07 |
| 10-28 11:36 | +10 stop | SOL | UP | 0.61 | 0.76 | 1.20 |
| 10-28 11:36 | +10 stop | HYPE | DOWN | 0.63 | 0.40 | -2.64 |
| 10-28 11:36 | +15 | XRP | UP | 0.65 | 0.81 | 1.37 |
| 10-28 11:36 | +10 stop | BTC | UP | 0.65 | 0.77 | 0.91 |
| 10-28 11:36 | +20 | BTC | UP | 0.64 | 0.85 | 1.84 |
| 10-28 11:36 | +15 | BTC | UP | 0.64 | 0.83 | 1.63 |
| 10-28 11:36 | +10 | BTC | UP | 0.64 | 0.77 | 1.00 |
| 10-28 11:36 | +5 | BTC | UP | 0.64 | 0.77 | 1.00 |
| 10-28 11:35 | +10 stop | ZEC | DOWN | 0.64 | 0.45 | -2.25 |
| 10-28 11:33 | +10 stop | BNB | UP | 0.60 | 0.86 | 2.34 |
| 10-28 11:33 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-28 11:33 | +10 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-28 11:33 | +10 stop | NEAR | UP | 0.69 | 0.54 | -1.83 |
| 10-28 11:33 | +5 | XRP | UP | 0.69 | 0.77 | 0.52 |
| 10-28 11:33 | +10 stop | HYPE | UP | 0.57 | 0.39 | -2.15 |
| 10-28 11:33 | +10 stop | SOL | UP | 0.68 | 0.52 | -1.94 |
| 10-28 11:33 | +10 stop | ETH | UP | 0.70 | 0.82 | 0.94 |
| 10-28 11:33 | +15 | ETH | UP | 0.70 | 0.85 | 1.26 |
| 10-28 11:33 | +10 | ETH | UP | 0.70 | 0.82 | 0.94 |
| 10-28 11:33 | +5 | ETH | UP | 0.70 | 0.77 | 0.42 |
| 10-28 11:33 | +5 | BTC | UP | 0.69 | 0.74 | 0.21 |
| 10-28 11:32 | +10 stop | ZEC | UP | 0.57 | 0.39 | -2.15 |
| 10-28 11:32 | +10 stop | NEAR | DOWN | 0.59 | 0.40 | -2.24 |
