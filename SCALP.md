# Range-Scalp Bot

*Updated Wed Oct 14 00:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15176 | 13130 | 2046 (27) | 2 | $-4898.46 | -5.1% |
| **+10¢** | 11474 | 9099 | 2375 (39) | 2 | $-4582.38 | -6.3% |
| **+15¢** | 9642 | 7101 | 2541 (58) | 2 | $-4068.52 | -6.7% |
| **+20¢** | 8574 | 5920 | 2654 (74) | 2 | $-3557.72 | -6.6% |
| **+10¢ (15¢ stop)** | 18605 | 18555 | 50 (29) | 0 | $-7181.00 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 00:06 | +10 stop | NEAR | DOWN | 0.60 | 0.32 | -3.13 |
| 10-14 00:05 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 10-14 00:05 | +10 | SOL | UP | 0.66 | 0.76 | 0.71 |
| 10-14 00:05 | +5 | SOL | UP | 0.67 | 0.74 | 0.40 |
| 10-14 00:04 | +10 stop | NEAR | UP | 0.68 | 0.37 | -3.43 |
| 10-14 00:04 | +10 | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 10-14 00:04 | +5 | NEAR | UP | 0.68 | 0.77 | 0.61 |
| 10-14 00:03 | +10 stop | BNB | UP | 0.63 | 0.76 | 1.00 |
| 10-14 00:03 | +10 stop | HYPE | UP | 0.70 | 0.91 | 1.81 |
| 10-14 00:02 | +10 stop | SOL | UP | 0.59 | 0.75 | 1.29 |
| 10-14 00:02 | +20 | SOL | UP | 0.59 | 0.84 | 2.23 |
| 10-14 00:02 | +15 | SOL | UP | 0.61 | 0.76 | 1.20 |
| 10-14 00:02 | +10 | SOL | UP | 0.61 | 0.75 | 1.09 |
| 10-14 00:02 | +5 | SOL | UP | 0.61 | 0.68 | 0.37 |
| 10-14 00:02 | +5 | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 10-14 00:02 | +5 | XRP | UP | 0.61 | 0.67 | 0.22 |
| 10-14 00:01 | +10 stop | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 10-14 00:01 | +20 | NEAR | UP | 0.58 | 0.79 | 1.80 |
| 10-14 00:01 | +15 | NEAR | UP | 0.58 | 0.77 | 1.59 |
| 10-14 00:01 | +10 | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 10-14 00:01 | +5 | NEAR | UP | 0.58 | 0.63 | 0.15 |
| 10-14 00:01 | +10 stop | ZEC | UP | 0.64 | 0.77 | 1.00 |
| 10-14 00:01 | +20 | ZEC | UP | 0.64 | 0.87 | 2.05 |
| 10-14 00:01 | +15 | ZEC | UP | 0.64 | 0.87 | 2.05 |
| 10-14 00:01 | +10 | ZEC | UP | 0.64 | 0.77 | 1.00 |
| 10-14 00:01 | +5 | ZEC | UP | 0.64 | 0.77 | 1.00 |
| 10-14 00:01 | +10 stop | DOGE | UP | 0.65 | 0.79 | 1.12 |
| 10-14 00:01 | +20 | DOGE | UP | 0.65 | 0.88 | 2.06 |
| 10-14 00:01 | +15 | DOGE | UP | 0.65 | 0.84 | 1.64 |
| 10-14 00:01 | +10 | DOGE | UP | 0.65 | 0.79 | 1.12 |
| 10-14 00:01 | +5 | DOGE | UP | 0.65 | 0.79 | 1.12 |
| 10-14 00:01 | +10 stop | HYPE | DOWN | 0.54 | 0.35 | -2.24 |
| 10-14 00:00 | +10 stop | BNB | DOWN | 0.60 | 0.44 | -1.96 |
| 10-14 00:00 | +20 | BNB | DOWN | 0.60 | open |  |
| 10-14 00:00 | +15 | BNB | DOWN | 0.60 | open |  |
| 10-14 00:00 | +10 | BNB | DOWN | 0.60 | open |  |
| 10-14 00:00 | +5 | BNB | DOWN | 0.60 | open |  |
| 10-14 00:00 | +10 stop | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-14 00:00 | +20 | BTC | UP | 0.67 | 0.88 | 1.86 |
| 10-14 00:00 | +15 | BTC | UP | 0.67 | 0.82 | 1.23 |
