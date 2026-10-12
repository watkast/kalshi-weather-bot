# Range-Scalp Bot

*Updated Mon Oct 12 02:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12904 | 11137 | 1767 (25) | 0 | $-4277.98 | -5.3% |
| **+10¢** | 9781 | 7740 | 2041 (37) | 1 | $-3996.03 | -6.5% |
| **+15¢** | 8227 | 6051 | 2176 (55) | 3 | $-3490.04 | -6.8% |
| **+20¢** | 7328 | 5062 | 2266 (69) | 3 | $-2969.55 | -6.5% |
| **+10¢ (15¢ stop)** | 15906 | 15865 | 41 (25) | 1 | $-6261.94 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 02:15 | +10 stop | NEAR | UP | 0.65 | 0.75 | 0.70 |
| 10-12 02:15 | +20 | NEAR | UP | 0.65 | open |  |
| 10-12 02:15 | +15 | NEAR | UP | 0.65 | open |  |
| 10-12 02:15 | +10 | NEAR | UP | 0.65 | 0.75 | 0.70 |
| 10-12 02:15 | +5 | NEAR | UP | 0.65 | 0.75 | 0.70 |
| 10-12 02:15 | +10 stop | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 10-12 02:15 | +20 | ZEC | UP | 0.71 | open |  |
| 10-12 02:15 | +15 | ZEC | UP | 0.71 | open |  |
| 10-12 02:15 | +10 | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 10-12 02:15 | +5 | ZEC | UP | 0.71 | 0.80 | 0.63 |
| 10-12 02:15 | +10 stop | HYPE | UP | 0.69 | open |  |
| 10-12 02:15 | +20 | HYPE | UP | 0.69 | open |  |
| 10-12 02:15 | +15 | HYPE | UP | 0.69 | open |  |
| 10-12 02:15 | +10 | HYPE | UP | 0.69 | open |  |
| 10-12 02:15 | +5 | HYPE | UP | 0.69 | 0.77 | 0.48 |
| 10-12 02:11 | +10 stop | HYPE | UP | 0.69 | 0.86 | 1.46 |
| 10-12 02:11 | +20 | HYPE | UP | 0.69 | 0.96 | 2.57 |
| 10-12 02:11 | +15 | HYPE | UP | 0.69 | 0.86 | 1.46 |
| 10-12 02:11 | +10 | HYPE | UP | 0.69 | 0.86 | 1.46 |
| 10-12 02:11 | +5 | HYPE | UP | 0.69 | 0.74 | 0.21 |
| 10-12 02:10 | +10 stop | XRP | UP | 0.62 | 0.73 | 0.79 |
| 10-12 02:09 | +10 stop | NEAR | UP | 0.62 | 0.47 | -1.85 |
| 10-12 02:09 | +20 | NEAR | UP | 0.62 | no | -6.37 |
| 10-12 02:09 | +15 | NEAR | UP | 0.62 | no | -6.37 |
| 10-12 02:09 | +10 | NEAR | UP | 0.62 | no | -6.37 |
| 10-12 02:09 | +5 | NEAR | UP | 0.62 | no | -6.37 |
| 10-12 02:09 | +10 stop | BTC | UP | 0.66 | 0.83 | 1.44 |
| 10-12 02:09 | +20 | BTC | UP | 0.66 | 0.91 | 2.32 |
| 10-12 02:09 | +15 | BTC | UP | 0.67 | 0.83 | 1.34 |
| 10-12 02:09 | +10 | BTC | UP | 0.67 | 0.83 | 1.34 |
| 10-12 02:08 | +10 stop | HYPE | DOWN | 0.70 | 0.34 | -3.91 |
| 10-12 02:07 | +15 | SOL | UP | 0.57 | 0.97 | 3.77 |
| 10-12 02:07 | +5 | SOL | UP | 0.57 | 0.65 | 0.42 |
| 10-12 02:06 | +10 stop | HYPE | UP | 0.59 | 0.42 | -2.05 |
| 10-12 02:06 | +10 | HYPE | UP | 0.59 | 0.72 | 0.98 |
| 10-12 02:06 | +5 | HYPE | UP | 0.59 | 0.65 | 0.27 |
| 10-12 02:05 | +10 | SOL | UP | 0.65 | 0.97 | 3.03 |
| 10-12 02:05 | +5 | SOL | UP | 0.65 | 0.72 | 0.39 |
| 10-12 02:05 | +10 stop | XRP | UP | 0.64 | 0.47 | -2.05 |
| 10-12 02:05 | +10 stop | SOL | UP | 0.65 | 0.32 | -3.62 |
