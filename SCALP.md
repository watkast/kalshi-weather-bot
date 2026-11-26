# Range-Scalp Bot

*Updated Thu Nov 26 10:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72509 | 63300 | 9209 (158) | 2 | $-19222.58 | -4.2% |
| **+10¢** | 54074 | 43320 | 10754 (203) | 2 | $-17801.97 | -5.2% |
| **+15¢** | 45278 | 33694 | 11584 (261) | 5 | $-15881.69 | -5.6% |
| **+20¢** | 40302 | 28102 | 12200 (327) | 6 | $-14280.83 | -5.6% |
| **+10¢ (15¢ stop)** | 88282 | 88073 | 209 (128) | 2 | $-32409.96 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 10:20 | +10 stop | NEAR | UP | 0.63 | open |  |
| 11-26 10:19 | +5 | HYPE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-26 10:18 | +5 | ZEC | DOWN | 0.60 | open |  |
| 11-26 10:18 | +10 stop | NEAR | UP | 0.54 | 0.66 | 0.86 |
| 11-26 10:17 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.85 |
| 11-26 10:17 | +20 | XRP | DOWN | 0.67 | open |  |
| 11-26 10:17 | +15 | XRP | DOWN | 0.66 | 0.86 | 1.75 |
| 11-26 10:17 | +10 | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 11-26 10:17 | +5 | XRP | DOWN | 0.66 | 0.71 | 0.19 |
| 11-26 10:16 | +10 stop | ZEC | DOWN | 0.55 | open |  |
| 11-26 10:16 | +20 | ZEC | DOWN | 0.55 | open |  |
| 11-26 10:16 | +15 | ZEC | DOWN | 0.56 | open |  |
| 11-26 10:16 | +10 | ZEC | DOWN | 0.56 | open |  |
| 11-26 10:16 | +5 | ZEC | DOWN | 0.56 | 0.61 | 0.15 |
| 11-26 10:16 | +10 stop | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-26 10:16 | +20 | BNB | DOWN | 0.62 | open |  |
| 11-26 10:16 | +15 | BNB | DOWN | 0.62 | open |  |
| 11-26 10:16 | +10 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-26 10:16 | +5 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-26 10:16 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-26 10:16 | +20 | DOGE | DOWN | 0.65 | open |  |
| 11-26 10:16 | +15 | DOGE | DOWN | 0.66 | open |  |
| 11-26 10:16 | +10 | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-26 10:16 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-26 10:16 | +10 stop | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-26 10:16 | +20 | HYPE | DOWN | 0.63 | open |  |
| 11-26 10:16 | +15 | HYPE | DOWN | 0.63 | open |  |
| 11-26 10:16 | +10 | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-26 10:16 | +5 | HYPE | DOWN | 0.63 | 0.71 | 0.48 |
| 11-26 10:16 | +10 stop | NEAR | DOWN | 0.67 | 0.41 | -2.93 |
| 11-26 10:16 | +20 | NEAR | DOWN | 0.67 | open |  |
| 11-26 10:16 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-26 10:16 | +10 | NEAR | DOWN | 0.69 | open |  |
| 11-26 10:16 | +5 | NEAR | DOWN | 0.69 | open |  |
| 11-26 10:14 | +10 stop | XRP | DOWN | 0.64 | 0.42 | -2.55 |
| 11-26 10:13 | +5 | DOGE | DOWN | 0.67 | 0.90 | 2.08 |
| 11-26 10:12 | +10 stop | SOL | UP | 0.66 | 0.77 | 0.83 |
| 11-26 10:12 | +10 stop | XRP | UP | 0.60 | 0.77 | 1.40 |
| 11-26 10:12 | +10 stop | DOGE | UP | 0.40 | 0.64 | 2.06 |
| 11-26 10:11 | +10 stop | DOGE | DOWN | 0.58 | 0.39 | -2.25 |
