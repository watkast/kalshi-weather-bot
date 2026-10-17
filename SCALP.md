# Range-Scalp Bot

*Updated Sat Oct 17 13:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21005 | 18279 | 2726 (29) | 2 | $-6134.17 | -4.6% |
| **+10¢** | 15813 | 12669 | 3144 (41) | 2 | $-5452.61 | -5.5% |
| **+15¢** | 13220 | 9836 | 3384 (61) | 2 | $-4930.71 | -5.9% |
| **+20¢** | 11719 | 8174 | 3545 (80) | 3 | $-4364.51 | -5.9% |
| **+10¢ (15¢ stop)** | 25805 | 25755 | 50 (29) | 0 | $-9817.89 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 13:12 | +10 stop | HYPE | DOWN | 0.38 | 0.63 | 2.16 |
| 10-17 13:10 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-17 13:10 | +20 | BTC | DOWN | 0.67 | 0.87 | 1.76 |
| 10-17 13:10 | +15 | BTC | DOWN | 0.70 | 0.87 | 1.47 |
| 10-17 13:10 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-17 13:10 | +5 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-17 13:09 | +10 stop | BNB | DOWN | 0.57 | 0.23 | -3.71 |
| 10-17 13:09 | +5 | BNB | DOWN | 0.56 | 0.63 | 0.35 |
| 10-17 13:09 | +5 | SOL | DOWN | 0.66 | open |  |
| 10-17 13:09 | +10 stop | SOL | DOWN | 0.67 | 0.50 | -2.04 |
| 10-17 13:09 | +15 | SOL | DOWN | 0.67 | open |  |
| 10-17 13:09 | +10 | SOL | DOWN | 0.68 | open |  |
| 10-17 13:09 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 10-17 13:08 | +10 stop | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-17 13:08 | +20 | DOGE | DOWN | 0.68 | 0.91 | 2.09 |
| 10-17 13:08 | +15 | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-17 13:08 | +10 | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-17 13:08 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.51 |
| 10-17 13:08 | +10 stop | BNB | UP | 0.52 | 0.35 | -2.04 |
| 10-17 13:08 | +20 | BNB | UP | 0.52 | 0.75 | 1.98 |
| 10-17 13:08 | +15 | BNB | UP | 0.52 | 0.75 | 1.98 |
| 10-17 13:08 | +10 | BNB | UP | 0.52 | 0.75 | 1.98 |
| 10-17 13:08 | +5 | BNB | UP | 0.52 | 0.61 | 0.55 |
| 10-17 13:08 | +10 stop | XRP | UP | 0.40 | 0.57 | 1.35 |
| 10-17 13:08 | +20 | XRP | UP | 0.42 | open |  |
| 10-17 13:08 | +15 | XRP | UP | 0.42 | 0.57 | 1.14 |
| 10-17 13:08 | +10 | XRP | UP | 0.42 | 0.57 | 1.14 |
| 10-17 13:08 | +5 | XRP | UP | 0.42 | 0.57 | 1.14 |
| 10-17 13:08 | +10 stop | SOL | DOWN | 0.54 | 0.69 | 1.17 |
| 10-17 13:08 | +20 | SOL | DOWN | 0.54 | open |  |
| 10-17 13:08 | +15 | SOL | DOWN | 0.54 | 0.69 | 1.17 |
| 10-17 13:08 | +10 | SOL | DOWN | 0.54 | 0.69 | 1.17 |
| 10-17 13:08 | +5 | SOL | DOWN | 0.54 | 0.59 | 0.15 |
| 10-17 13:08 | +10 stop | DOGE | UP | 0.31 | 0.67 | 3.29 |
| 10-17 13:08 | +20 | DOGE | UP | 0.31 | 0.67 | 3.29 |
| 10-17 13:08 | +15 | DOGE | UP | 0.32 | 0.67 | 3.18 |
| 10-17 13:08 | +10 | DOGE | UP | 0.32 | 0.67 | 3.18 |
| 10-17 13:08 | +5 | DOGE | UP | 0.31 | 0.67 | 3.29 |
| 10-17 13:07 | +10 stop | HYPE | DOWN | 0.71 | 0.93 | 2.01 |
| 10-17 13:06 | +10 stop | NEAR | UP | 0.62 | 0.47 | -1.85 |
