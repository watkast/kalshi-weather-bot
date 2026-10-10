# Range-Scalp Bot

*Updated Sat Oct 10 16:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10574 | 9123 | 1451 (22) | 6 | $-3551.37 | -5.3% |
| **+10¢** | 8008 | 6316 | 1692 (36) | 7 | $-3379.65 | -6.7% |
| **+15¢** | 6757 | 4966 | 1791 (52) | 7 | $-2835.98 | -6.7% |
| **+20¢** | 6005 | 4136 | 1869 (66) | 7 | $-2427.87 | -6.4% |
| **+10¢ (15¢ stop)** | 12984 | 12943 | 41 (25) | 0 | $-5104.91 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 16:28 | +5 | BTC | UP | 0.64 | open |  |
| 10-10 16:27 | +10 stop | ZEC | DOWN | 0.65 | 0.49 | -1.94 |
| 10-10 16:27 | +10 stop | DOGE | DOWN | 0.69 | 0.93 | 2.21 |
| 10-10 16:26 | +5 | BTC | UP | 0.57 | 0.64 | 0.35 |
| 10-10 16:25 | +10 stop | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-10 16:25 | +10 stop | DOGE | DOWN | 0.55 | 0.68 | 0.96 |
| 10-10 16:24 | +10 stop | XRP | DOWN | 0.66 | 0.77 | 0.81 |
| 10-10 16:24 | +5 | ZEC | UP | 0.59 | 0.64 | 0.16 |
| 10-10 16:23 | +5 | DOGE | UP | 0.60 | open |  |
| 10-10 16:22 | +10 stop | SOL | DOWN | 0.63 | 0.77 | 1.10 |
| 10-10 16:22 | +20 | SOL | DOWN | 0.63 | 0.83 | 1.73 |
| 10-10 16:22 | +15 | SOL | DOWN | 0.63 | 0.78 | 1.20 |
| 10-10 16:22 | +10 | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 10-10 16:22 | +5 | SOL | DOWN | 0.67 | 0.77 | 0.73 |
| 10-10 16:22 | +10 stop | BTC | UP | 0.63 | 0.26 | -4.01 |
| 10-10 16:22 | +20 | BTC | UP | 0.63 | open |  |
| 10-10 16:22 | +15 | BTC | UP | 0.63 | open |  |
| 10-10 16:22 | +10 | BTC | UP | 0.63 | open |  |
| 10-10 16:22 | +5 | BTC | UP | 0.63 | 0.70 | 0.38 |
| 10-10 16:22 | +10 stop | DOGE | UP | 0.53 | 0.29 | -2.73 |
| 10-10 16:22 | +15 | DOGE | UP | 0.53 | open |  |
| 10-10 16:22 | +10 | DOGE | UP | 0.53 | open |  |
| 10-10 16:22 | +5 | DOGE | UP | 0.53 | 0.58 | 0.14 |
| 10-10 16:22 | +10 stop | BNB | DOWN | 0.59 | 0.72 | 0.98 |
| 10-10 16:22 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.74 |
| 10-10 16:22 | +10 stop | XRP | UP | 0.58 | 0.39 | -2.25 |
| 10-10 16:22 | +15 | XRP | UP | 0.59 | open |  |
| 10-10 16:22 | +10 | XRP | UP | 0.59 | open |  |
| 10-10 16:22 | +5 | XRP | UP | 0.59 | open |  |
| 10-10 16:21 | +5 | ZEC | UP | 0.65 | 0.72 | 0.39 |
| 10-10 16:20 | +5 | BNB | UP | 0.70 | open |  |
| 10-10 16:20 | +5 | HYPE | UP | 0.71 | open |  |
| 10-10 16:17 | +10 stop | ZEC | UP | 0.70 | 0.49 | -2.46 |
| 10-10 16:17 | +20 | ZEC | UP | 0.70 | open |  |
| 10-10 16:17 | +15 | ZEC | UP | 0.70 | open |  |
| 10-10 16:17 | +10 | ZEC | UP | 0.70 | open |  |
| 10-10 16:17 | +5 | ZEC | UP | 0.71 | 0.76 | 0.26 |
| 10-10 16:17 | +10 stop | BNB | UP | 0.64 | 0.49 | -1.85 |
| 10-10 16:17 | +20 | BNB | UP | 0.64 | open |  |
| 10-10 16:17 | +15 | BNB | UP | 0.64 | open |  |
