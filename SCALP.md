# Range-Scalp Bot

*Updated Fri Oct 16 09:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19019 | 16530 | 2489 (28) | 1 | $-5705.09 | -4.8% |
| **+10¢** | 14332 | 11450 | 2882 (40) | 2 | $-5178.59 | -5.7% |
| **+15¢** | 12004 | 8906 | 3098 (59) | 2 | $-4653.42 | -6.2% |
| **+20¢** | 10648 | 7401 | 3247 (78) | 3 | $-4132.14 | -6.2% |
| **+10¢ (15¢ stop)** | 23400 | 23350 | 50 (29) | 2 | $-9023.01 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 09:11 | +5 | BTC | DOWN | 0.56 | 0.68 | 0.86 |
| 10-16 09:10 | +10 stop | BTC | DOWN | 0.65 | open |  |
| 10-16 09:10 | +10 | BTC | DOWN | 0.65 | open |  |
| 10-16 09:10 | +5 | BTC | DOWN | 0.65 | 0.73 | 0.50 |
| 10-16 09:09 | +10 stop | ZEC | DOWN | 0.61 | open |  |
| 10-16 09:09 | +10 stop | HYPE | DOWN | 0.62 | 0.75 | 0.99 |
| 10-16 09:08 | +10 stop | ZEC | UP | 0.68 | 0.49 | -2.20 |
| 10-16 09:08 | +10 stop | HYPE | UP | 0.59 | 0.38 | -2.44 |
| 10-16 09:08 | +10 stop | SOL | DOWN | 0.67 | 0.80 | 1.02 |
| 10-16 09:08 | +20 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 10-16 09:08 | +15 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 10-16 09:08 | +10 | SOL | DOWN | 0.67 | 0.80 | 1.02 |
| 10-16 09:08 | +5 | SOL | DOWN | 0.67 | 0.80 | 1.02 |
| 10-16 09:08 | +10 stop | BTC | DOWN | 0.61 | 0.72 | 0.78 |
| 10-16 09:08 | +20 | BTC | DOWN | 0.61 | open |  |
| 10-16 09:08 | +15 | BTC | DOWN | 0.61 | open |  |
| 10-16 09:08 | +10 | BTC | DOWN | 0.61 | 0.72 | 0.78 |
| 10-16 09:08 | +5 | BTC | DOWN | 0.61 | 0.67 | 0.27 |
| 10-16 09:04 | +10 stop | HYPE | DOWN | 0.52 | 0.35 | -2.04 |
| 10-16 09:03 | +10 stop | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-16 09:03 | +10 | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-16 09:03 | +5 | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-16 09:02 | +5 | ZEC | DOWN | 0.62 | open |  |
| 10-16 09:01 | +5 | SOL | DOWN | 0.67 | 0.76 | 0.61 |
| 10-16 09:01 | +10 stop | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 10-16 09:01 | +20 | SOL | DOWN | 0.60 | 0.81 | 1.82 |
| 10-16 09:01 | +15 | SOL | DOWN | 0.60 | 0.76 | 1.30 |
| 10-16 09:01 | +10 | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 10-16 09:01 | +5 | SOL | DOWN | 0.60 | 0.65 | 0.17 |
| 10-16 09:01 | +10 stop | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-16 09:01 | +20 | DOGE | DOWN | 0.65 | 0.86 | 1.85 |
| 10-16 09:01 | +15 | DOGE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-16 09:01 | +10 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-16 09:01 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
| 10-16 09:01 | +10 stop | ZEC | DOWN | 0.64 | 0.47 | -2.04 |
| 10-16 09:01 | +20 | ZEC | DOWN | 0.64 | open |  |
| 10-16 09:01 | +15 | ZEC | DOWN | 0.64 | open |  |
| 10-16 09:01 | +10 | ZEC | DOWN | 0.64 | open |  |
| 10-16 09:01 | +5 | ZEC | DOWN | 0.64 | 0.71 | 0.39 |
| 10-16 09:01 | +10 stop | NEAR | DOWN | 0.63 | 0.77 | 1.10 |
