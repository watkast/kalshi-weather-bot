# Range-Scalp Bot

*Updated Tue Oct 13 12:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14636 | 12658 | 1978 (27) | 2 | $-4723.06 | -5.1% |
| **+10¢** | 11081 | 8784 | 2297 (39) | 2 | $-4425.05 | -6.3% |
| **+15¢** | 9314 | 6855 | 2459 (57) | 3 | $-3951.13 | -6.8% |
| **+20¢** | 8286 | 5725 | 2561 (72) | 4 | $-3407.89 | -6.6% |
| **+10¢ (15¢ stop)** | 17987 | 17938 | 49 (29) | 1 | $-7016.26 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 12:36 | +10 stop | BTC | UP | 0.51 | open |  |
| 10-13 12:36 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 10-13 12:35 | +10 stop | BTC | DOWN | 0.51 | 0.62 | 0.75 |
| 10-13 12:35 | +10 stop | ETH | UP | 0.56 | 0.70 | 1.07 |
| 10-13 12:35 | +10 stop | XRP | UP | 0.56 | 0.68 | 0.86 |
| 10-13 12:35 | +10 stop | SOL | UP | 0.53 | 0.65 | 0.86 |
| 10-13 12:35 | +10 stop | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 10-13 12:34 | +10 stop | NEAR | UP | 0.60 | 0.74 | 1.09 |
| 10-13 12:33 | +10 stop | HYPE | DOWN | 0.55 | 0.33 | -2.56 |
| 10-13 12:33 | +10 stop | BNB | DOWN | 0.51 | 0.35 | -1.94 |
| 10-13 12:32 | +10 stop | DOGE | DOWN | 0.64 | 0.42 | -2.55 |
| 10-13 12:32 | +10 stop | HYPE | DOWN | 0.68 | 0.51 | -2.04 |
| 10-13 12:32 | +5 | NEAR | DOWN | 0.70 | open |  |
| 10-13 12:32 | +10 stop | BTC | DOWN | 0.67 | 0.51 | -1.94 |
| 10-13 12:32 | +10 stop | ETH | DOWN | 0.65 | 0.40 | -2.83 |
| 10-13 12:32 | +10 stop | XRP | DOWN | 0.65 | 0.48 | -2.04 |
| 10-13 12:32 | +10 stop | ZEC | UP | 0.50 | 0.60 | 0.65 |
| 10-13 12:32 | +10 stop | SOL | DOWN | 0.66 | 0.51 | -1.84 |
| 10-13 12:31 | +10 stop | DOGE | UP | 0.66 | 0.44 | -2.54 |
| 10-13 12:31 | +20 | DOGE | UP | 0.66 | 0.89 | 2.07 |
| 10-13 12:31 | +15 | DOGE | UP | 0.66 | 0.81 | 1.23 |
| 10-13 12:31 | +10 | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 10-13 12:31 | +5 | DOGE | UP | 0.66 | 0.72 | 0.29 |
| 10-13 12:31 | +10 stop | HYPE | UP | 0.66 | 0.37 | -3.27 |
| 10-13 12:31 | +20 | HYPE | UP | 0.66 | 0.87 | 1.82 |
| 10-13 12:31 | +15 | HYPE | UP | 0.66 | 0.87 | 1.82 |
| 10-13 12:31 | +10 | HYPE | UP | 0.66 | 0.77 | 0.77 |
| 10-13 12:31 | +5 | HYPE | UP | 0.66 | 0.74 | 0.46 |
| 10-13 12:31 | +10 stop | NEAR | DOWN | 0.62 | 0.40 | -2.52 |
| 10-13 12:31 | +20 | NEAR | DOWN | 0.62 | open |  |
| 10-13 12:31 | +15 | NEAR | DOWN | 0.61 | open |  |
| 10-13 12:31 | +10 | NEAR | DOWN | 0.59 | open |  |
| 10-13 12:31 | +5 | NEAR | DOWN | 0.59 | 0.65 | 0.31 |
| 10-13 12:31 | +10 stop | XRP | UP | 0.65 | 0.41 | -2.73 |
| 10-13 12:31 | +20 | XRP | UP | 0.65 | open |  |
| 10-13 12:31 | +15 | XRP | UP | 0.65 | 0.81 | 1.33 |
| 10-13 12:31 | +10 | XRP | UP | 0.66 | 0.78 | 0.91 |
| 10-13 12:31 | +5 | XRP | UP | 0.66 | 0.72 | 0.29 |
| 10-13 12:31 | +10 stop | ZEC | UP | 0.70 | 0.55 | -1.85 |
| 10-13 12:31 | +20 | ZEC | UP | 0.71 | 0.92 | 1.84 |
