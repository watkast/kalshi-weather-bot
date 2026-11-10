# Range-Scalp Bot

*Updated Tue Nov 10 16:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54724 | 47738 | 6986 (91) | 7 | $-14877.06 | -4.3% |
| **+10¢** | 40888 | 32736 | 8152 (121) | 7 | $-13801.85 | -5.4% |
| **+15¢** | 34274 | 25488 | 8786 (155) | 8 | $-12542.13 | -5.8% |
| **+20¢** | 30513 | 21294 | 9219 (204) | 9 | $-10966.53 | -5.7% |
| **+10¢ (15¢ stop)** | 66672 | 66558 | 114 (70) | 2 | $-24665.00 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 16:25 | +10 | BTC | UP | 0.67 | open |  |
| 11-10 16:25 | +10 stop | BTC | UP | 0.67 | open |  |
| 11-10 16:25 | +5 | BTC | UP | 0.67 | open |  |
| 11-10 16:25 | +10 stop | SOL | UP | 0.71 | open |  |
| 11-10 16:24 | +10 stop | SOL | UP | 0.50 | 0.60 | 0.65 |
| 11-10 16:24 | +10 stop | XRP | DOWN | 0.68 | 0.51 | -2.04 |
| 11-10 16:24 | +10 stop | NEAR | UP | 0.53 | 0.72 | 1.57 |
| 11-10 16:24 | +20 | NEAR | UP | 0.53 | open |  |
| 11-10 16:24 | +15 | NEAR | UP | 0.53 | 0.72 | 1.57 |
| 11-10 16:24 | +10 | NEAR | UP | 0.53 | 0.72 | 1.57 |
| 11-10 16:24 | +5 | NEAR | UP | 0.51 | 0.56 | 0.14 |
| 11-10 16:24 | +10 stop | ETH | DOWN | 0.61 | 0.45 | -1.95 |
| 11-10 16:23 | +10 stop | SOL | DOWN | 0.65 | 0.43 | -2.54 |
| 11-10 16:23 | +10 stop | XRP | UP | 0.69 | 0.49 | -2.33 |
| 11-10 16:23 | +15 | XRP | UP | 0.68 | open |  |
| 11-10 16:23 | +10 | XRP | UP | 0.68 | open |  |
| 11-10 16:23 | +5 | XRP | UP | 0.68 | open |  |
| 11-10 16:22 | +10 stop | BTC | UP | 0.45 | 0.23 | -2.51 |
| 11-10 16:22 | +10 | BTC | UP | 0.45 | 0.59 | 1.05 |
| 11-10 16:22 | +5 | BTC | UP | 0.45 | 0.54 | 0.54 |
| 11-10 16:22 | +10 stop | SOL | UP | 0.63 | 0.42 | -2.45 |
| 11-10 16:22 | +10 stop | ETH | UP | 0.60 | 0.31 | -3.22 |
| 11-10 16:22 | +20 | ETH | UP | 0.61 | open |  |
| 11-10 16:22 | +15 | ETH | UP | 0.62 | open |  |
| 11-10 16:22 | +10 | ETH | UP | 0.63 | open |  |
| 11-10 16:22 | +5 | ETH | UP | 0.65 | open |  |
| 11-10 16:21 | +10 stop | DOGE | UP | 0.43 | 0.56 | 0.94 |
| 11-10 16:21 | +15 | DOGE | UP | 0.43 | open |  |
| 11-10 16:21 | +10 | DOGE | UP | 0.43 | 0.56 | 0.94 |
| 11-10 16:21 | +5 | DOGE | UP | 0.43 | 0.56 | 0.94 |
| 11-10 16:21 | +10 stop | SOL | UP | 0.63 | 0.44 | -2.25 |
| 11-10 16:21 | +15 | SOL | UP | 0.63 | open |  |
| 11-10 16:21 | +10 | SOL | UP | 0.63 | open |  |
| 11-10 16:21 | +5 | SOL | UP | 0.63 | open |  |
| 11-10 16:20 | +5 | BNB | UP | 0.68 | open |  |
| 11-10 16:18 | +10 stop | HYPE | DOWN | 0.46 | 0.58 | 0.84 |
| 11-10 16:18 | +5 | XRP | UP | 0.64 | 0.71 | 0.38 |
| 11-10 16:17 | +10 stop | XRP | UP | 0.63 | 0.79 | 1.32 |
| 11-10 16:17 | +20 | XRP | UP | 0.63 | open |  |
| 11-10 16:17 | +15 | XRP | UP | 0.63 | 0.79 | 1.32 |
