# Range-Scalp Bot

*Updated Wed Oct 07 12:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6404 | 5566 | 838 (9) | 0 | $-1888.51 | -4.7% |
| **+10¢** | 4869 | 3884 | 985 (16) | 0 | $-1759.98 | -5.7% |
| **+15¢** | 4091 | 3050 | 1041 (20) | 0 | $-1470.50 | -5.7% |
| **+20¢** | 3659 | 2568 | 1091 (27) | 0 | $-1203.69 | -5.2% |
| **+10¢ (15¢ stop)** | 7767 | 7752 | 15 (9) | 0 | $-2714.83 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 12:21 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-07 12:21 | +15 | NEAR | DOWN | 0.71 | 0.87 | 1.37 |
| 10-07 12:21 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-07 12:21 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.42 |
| 10-07 12:18 | +10 stop | HYPE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-07 12:18 | +20 | HYPE | DOWN | 0.70 | 0.91 | 1.87 |
| 10-07 12:18 | +15 | HYPE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-07 12:18 | +10 | HYPE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-07 12:18 | +5 | HYPE | DOWN | 0.70 | 0.76 | 0.32 |
| 10-07 12:17 | +10 stop | NEAR | DOWN | 0.71 | 0.89 | 1.58 |
| 10-07 12:17 | +20 | NEAR | DOWN | 0.71 | 0.93 | 2.01 |
| 10-07 12:17 | +15 | NEAR | DOWN | 0.71 | 0.89 | 1.58 |
| 10-07 12:17 | +10 | NEAR | DOWN | 0.71 | 0.89 | 1.58 |
| 10-07 12:17 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.42 |
| 10-07 12:16 | +10 stop | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-07 12:16 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-07 12:16 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-07 12:16 | +10 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-07 12:16 | +5 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-07 12:13 | +10 stop | HYPE | DOWN | 0.51 | 0.05 | -4.82 |
| 10-07 12:11 | +5 | HYPE | UP | 0.66 | 0.95 | 2.66 |
| 10-07 12:11 | +10 stop | HYPE | UP | 0.66 | 0.38 | -3.13 |
| 10-07 12:11 | +10 stop | BNB | DOWN | 0.59 | 0.73 | 1.09 |
| 10-07 12:11 | +20 | BNB | DOWN | 0.59 | yes | -6.07 |
| 10-07 12:11 | +15 | BNB | DOWN | 0.59 | 0.75 | 1.29 |
| 10-07 12:11 | +10 | BNB | DOWN | 0.59 | 0.73 | 1.09 |
| 10-07 12:11 | +5 | BNB | DOWN | 0.59 | 0.73 | 1.09 |
| 10-07 12:10 | +10 stop | HYPE | DOWN | 0.68 | 0.46 | -2.54 |
| 10-07 12:10 | +10 stop | XRP | UP | 0.68 | 0.83 | 1.24 |
| 10-07 12:09 | +10 stop | ETH | UP | 0.63 | 0.46 | -2.05 |
| 10-07 12:09 | +5 | ETH | UP | 0.63 | 0.74 | 0.79 |
| 10-07 12:09 | +10 stop | SOL | UP | 0.64 | 0.49 | -1.85 |
| 10-07 12:09 | +10 stop | HYPE | DOWN | 0.54 | 0.65 | 0.76 |
| 10-07 12:08 | +10 stop | DOGE | UP | 0.68 | 0.87 | 1.66 |
| 10-07 12:08 | +10 stop | BNB | DOWN | 0.64 | 0.83 | 1.63 |
| 10-07 12:07 | +10 stop | NEAR | DOWN | 0.64 | 0.44 | -2.35 |
| 10-07 12:07 | +10 stop | DOGE | UP | 0.47 | 0.64 | 1.35 |
| 10-07 12:06 | +10 stop | HYPE | DOWN | 0.63 | 0.76 | 0.96 |
| 10-07 12:06 | +10 stop | SOL | DOWN | 0.61 | 0.36 | -2.84 |
| 10-07 12:06 | +10 stop | BNB | DOWN | 0.57 | 0.67 | 0.66 |
