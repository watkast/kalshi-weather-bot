# Range-Scalp Bot

*Updated Sun Oct 25 23:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33892 | 29594 | 4298 (43) | 3 | $-9350.24 | -4.4% |
| **+10¢** | 25365 | 20395 | 4970 (65) | 3 | $-8182.19 | -5.1% |
| **+15¢** | 21218 | 15868 | 5350 (89) | 3 | $-7302.58 | -5.5% |
| **+20¢** | 18802 | 13200 | 5602 (111) | 3 | $-6379.83 | -5.4% |
| **+10¢ (15¢ stop)** | 41517 | 41455 | 62 (33) | 0 | $-15788.67 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 23:13 | +10 stop | DOGE | DOWN | 0.15 | 0.57 | 3.93 |
| 10-25 23:13 | +5 | DOGE | DOWN | 0.15 | 0.57 | 3.93 |
| 10-25 23:12 | +10 stop | SOL | UP | 0.55 | 0.65 | 0.66 |
| 10-25 23:12 | +20 | SOL | UP | 0.55 | 0.82 | 2.41 |
| 10-25 23:12 | +15 | SOL | UP | 0.56 | 0.82 | 2.31 |
| 10-25 23:12 | +10 | SOL | UP | 0.56 | 0.82 | 2.31 |
| 10-25 23:12 | +5 | SOL | UP | 0.56 | 0.65 | 0.56 |
| 10-25 23:10 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-25 23:10 | +5 | DOGE | DOWN | 0.69 | 0.76 | 0.42 |
| 10-25 23:09 | +10 stop | SOL | DOWN | 0.56 | 0.70 | 1.07 |
| 10-25 23:09 | +20 | SOL | DOWN | 0.56 | 0.82 | 2.31 |
| 10-25 23:09 | +15 | SOL | DOWN | 0.56 | 0.75 | 1.58 |
| 10-25 23:09 | +10 | SOL | DOWN | 0.56 | 0.70 | 1.07 |
| 10-25 23:09 | +5 | SOL | DOWN | 0.56 | 0.61 | 0.15 |
| 10-25 23:09 | +5 | DOGE | DOWN | 0.55 | 0.65 | 0.66 |
| 10-25 23:05 | +10 stop | DOGE | DOWN | 0.69 | 0.54 | -1.83 |
| 10-25 23:05 | +5 | DOGE | DOWN | 0.69 | 0.75 | 0.31 |
| 10-25 23:05 | +10 stop | ZEC | DOWN | 0.65 | 0.79 | 1.12 |
| 10-25 23:04 | +10 stop | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 10-25 23:03 | +5 | SOL | DOWN | 0.63 | 0.69 | 0.28 |
| 10-25 23:03 | +10 stop | HYPE | DOWN | 0.59 | 0.70 | 0.78 |
| 10-25 23:03 | +10 stop | BNB | DOWN | 0.66 | 0.85 | 1.65 |
| 10-25 23:03 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.19 |
| 10-25 23:03 | +5 | SOL | DOWN | 0.59 | 0.64 | 0.16 |
| 10-25 23:03 | +5 | DOGE | DOWN | 0.51 | 0.60 | 0.55 |
| 10-25 23:03 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-25 23:03 | +15 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 10-25 23:03 | +10 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 10-25 23:03 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 10-25 23:03 | +5 | BTC | DOWN | 0.64 | 0.72 | 0.48 |
| 10-25 23:02 | +10 stop | DOGE | UP | 0.55 | 0.39 | -1.95 |
| 10-25 23:02 | +20 | DOGE | UP | 0.55 | 0.85 | 2.73 |
| 10-25 23:02 | +15 | DOGE | UP | 0.55 | 0.85 | 2.73 |
| 10-25 23:02 | +10 | DOGE | UP | 0.55 | 0.85 | 2.73 |
| 10-25 23:02 | +5 | DOGE | UP | 0.55 | 0.63 | 0.45 |
| 10-25 23:02 | +10 stop | HYPE | UP | 0.55 | 0.39 | -1.95 |
| 10-25 23:02 | +20 | HYPE | UP | 0.55 | open |  |
| 10-25 23:02 | +15 | HYPE | UP | 0.55 | open |  |
| 10-25 23:02 | +10 | HYPE | UP | 0.55 | open |  |
| 10-25 23:02 | +5 | HYPE | UP | 0.55 | open |  |
