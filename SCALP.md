# Range-Scalp Bot

*Updated Tue Oct 06 15:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5113 | 4428 | 685 (7) | 2 | $-1596.23 | -4.9% |
| **+10¢** | 3919 | 3119 | 800 (12) | 2 | $-1469.26 | -6.0% |
| **+15¢** | 3295 | 2448 | 847 (15) | 2 | $-1259.11 | -6.1% |
| **+20¢** | 2950 | 2068 | 882 (22) | 2 | $-1000.94 | -5.4% |
| **+10¢ (15¢ stop)** | 6256 | 6241 | 15 (9) | 0 | $-2252.96 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 15:52 | +10 stop | NEAR | DOWN | 0.60 | 0.75 | 1.19 |
| 10-06 15:51 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 10-06 15:50 | +10 | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-06 15:50 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 10-06 15:50 | +5 | SOL | DOWN | 0.66 | 0.78 | 0.91 |
| 10-06 15:49 | +10 stop | NEAR | UP | 0.56 | 0.40 | -1.95 |
| 10-06 15:48 | +10 stop | NEAR | DOWN | 0.42 | 0.54 | 0.84 |
| 10-06 15:48 | +10 stop | BNB | UP | 0.61 | 0.46 | -1.85 |
| 10-06 15:48 | +20 | BNB | UP | 0.61 | open |  |
| 10-06 15:48 | +15 | BNB | UP | 0.61 | open |  |
| 10-06 15:48 | +10 | BNB | UP | 0.61 | open |  |
| 10-06 15:48 | +5 | BNB | UP | 0.61 | open |  |
| 10-06 15:47 | +5 | SOL | DOWN | 0.51 | 0.62 | 0.75 |
| 10-06 15:47 | +10 stop | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-06 15:47 | +10 | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-06 15:47 | +10 stop | ZEC | DOWN | 0.60 | 0.76 | 1.29 |
| 10-06 15:47 | +20 | ZEC | DOWN | 0.60 | 0.88 | 2.54 |
| 10-06 15:47 | +15 | ZEC | DOWN | 0.60 | 0.76 | 1.29 |
| 10-06 15:47 | +10 | ZEC | DOWN | 0.60 | 0.76 | 1.29 |
| 10-06 15:47 | +5 | ZEC | DOWN | 0.60 | 0.68 | 0.46 |
| 10-06 15:47 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-06 15:47 | +10 stop | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 10-06 15:47 | +20 | SOL | DOWN | 0.57 | 0.78 | 1.79 |
| 10-06 15:47 | +15 | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 10-06 15:47 | +10 | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 10-06 15:47 | +5 | SOL | DOWN | 0.58 | 0.63 | 0.15 |
| 10-06 15:47 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-06 15:47 | +20 | DOGE | DOWN | 0.62 | 0.83 | 1.83 |
| 10-06 15:47 | +15 | DOGE | DOWN | 0.62 | 0.77 | 1.20 |
| 10-06 15:47 | +10 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-06 15:47 | +5 | DOGE | DOWN | 0.62 | 0.70 | 0.48 |
| 10-06 15:46 | +10 stop | HYPE | DOWN | 0.48 | 0.30 | -2.16 |
| 10-06 15:46 | +20 | HYPE | DOWN | 0.48 | 0.69 | 1.74 |
| 10-06 15:46 | +15 | HYPE | DOWN | 0.48 | 0.69 | 1.74 |
| 10-06 15:46 | +10 | HYPE | DOWN | 0.48 | 0.61 | 0.92 |
| 10-06 15:46 | +5 | HYPE | DOWN | 0.48 | 0.61 | 0.92 |
| 10-06 15:46 | +10 stop | BTC | DOWN | 0.53 | 0.63 | 0.65 |
| 10-06 15:46 | +20 | BTC | DOWN | 0.53 | 0.75 | 1.88 |
| 10-06 15:46 | +15 | BTC | DOWN | 0.53 | 0.71 | 1.47 |
| 10-06 15:46 | +10 | BTC | DOWN | 0.53 | 0.63 | 0.65 |
