# Range-Scalp Bot

*Updated Sun Oct 11 09:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11736 | 10120 | 1616 (24) | 3 | $-3963.26 | -5.4% |
| **+10¢** | 8893 | 7018 | 1875 (37) | 3 | $-3755.88 | -6.7% |
| **+15¢** | 7487 | 5500 | 1987 (53) | 5 | $-3212.88 | -6.8% |
| **+20¢** | 6669 | 4603 | 2066 (67) | 5 | $-2684.94 | -6.4% |
| **+10¢ (15¢ stop)** | 14439 | 14398 | 41 (25) | 2 | $-5703.97 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 09:42 | +5 | XRP | UP | 0.65 | open |  |
| 10-11 09:42 | +10 stop | BTC | UP | 0.52 | 0.62 | 0.65 |
| 10-11 09:42 | +5 | BTC | UP | 0.52 | 0.62 | 0.65 |
| 10-11 09:42 | +10 stop | DOGE | DOWN | 0.59 | open |  |
| 10-11 09:42 | +10 | DOGE | DOWN | 0.59 | open |  |
| 10-11 09:42 | +5 | DOGE | DOWN | 0.59 | open |  |
| 10-11 09:41 | +10 stop | NEAR | UP | 0.70 | 0.82 | 0.94 |
| 10-11 09:41 | +20 | NEAR | UP | 0.70 | open |  |
| 10-11 09:41 | +15 | NEAR | UP | 0.70 | open |  |
| 10-11 09:41 | +10 | NEAR | UP | 0.70 | 0.82 | 0.94 |
| 10-11 09:41 | +5 | NEAR | UP | 0.70 | 0.82 | 0.94 |
| 10-11 09:41 | +10 stop | XRP | UP | 0.53 | 0.64 | 0.76 |
| 10-11 09:41 | +10 | XRP | UP | 0.53 | 0.64 | 0.76 |
| 10-11 09:41 | +5 | XRP | UP | 0.53 | 0.58 | 0.15 |
| 10-11 09:41 | +10 stop | SOL | UP | 0.50 | open |  |
| 10-11 09:41 | +15 | SOL | UP | 0.48 | open |  |
| 10-11 09:41 | +10 | SOL | UP | 0.49 | open |  |
| 10-11 09:41 | +5 | SOL | UP | 0.50 | open |  |
| 10-11 09:41 | +5 | BTC | DOWN | 0.36 | 0.55 | 1.55 |
| 10-11 09:41 | +10 stop | BTC | DOWN | 0.64 | 0.36 | -3.14 |
| 10-11 09:41 | +10 stop | DOGE | UP | 0.58 | 0.68 | 0.67 |
| 10-11 09:41 | +20 | DOGE | UP | 0.58 | open |  |
| 10-11 09:41 | +15 | DOGE | UP | 0.58 | open |  |
| 10-11 09:41 | +10 | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 10-11 09:41 | +5 | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 10-11 09:38 | +10 stop | XRP | UP | 0.68 | 0.79 | 0.81 |
| 10-11 09:38 | +20 | XRP | UP | 0.68 | open |  |
| 10-11 09:38 | +15 | XRP | UP | 0.68 | open |  |
| 10-11 09:38 | +10 | XRP | UP | 0.68 | 0.79 | 0.81 |
| 10-11 09:38 | +5 | XRP | UP | 0.68 | 0.79 | 0.81 |
| 10-11 09:37 | +10 stop | NEAR | UP | 0.67 | 0.81 | 1.13 |
| 10-11 09:37 | +20 | NEAR | UP | 0.67 | 0.88 | 1.86 |
| 10-11 09:37 | +15 | NEAR | UP | 0.67 | 0.84 | 1.44 |
| 10-11 09:37 | +10 | NEAR | UP | 0.67 | 0.81 | 1.13 |
| 10-11 09:37 | +5 | NEAR | UP | 0.67 | 0.72 | 0.19 |
| 10-11 09:37 | +20 | SOL | UP | 0.69 | open |  |
| 10-11 09:37 | +15 | SOL | UP | 0.69 | 0.84 | 1.25 |
| 10-11 09:37 | +10 | SOL | UP | 0.69 | 0.81 | 0.94 |
| 10-11 09:37 | +5 | SOL | UP | 0.69 | 0.74 | 0.21 |
| 10-11 09:36 | +10 stop | BTC | UP | 0.71 | 0.43 | -3.13 |
