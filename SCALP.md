# Range-Scalp Bot

*Updated Tue Nov 03 03:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45512 | 39627 | 5885 (69) | 1 | $-13146.69 | -4.6% |
| **+10¢** | 33973 | 27155 | 6818 (91) | 1 | $-12023.42 | -5.6% |
| **+15¢** | 28421 | 21084 | 7337 (119) | 4 | $-11049.78 | -6.2% |
| **+20¢** | 25240 | 17556 | 7684 (154) | 6 | $-9809.48 | -6.2% |
| **+10¢ (15¢ stop)** | 55532 | 55443 | 89 (53) | 1 | $-20936.77 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 03:19 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 11-03 03:19 | +5 | ZEC | UP | 0.67 | 0.77 | 0.71 |
| 11-03 03:19 | +10 stop | HYPE | UP | 0.65 | 0.80 | 1.22 |
| 11-03 03:19 | +20 | HYPE | UP | 0.65 | open |  |
| 11-03 03:19 | +15 | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 11-03 03:19 | +10 | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 11-03 03:19 | +5 | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 11-03 03:19 | +10 stop | DOGE | UP | 0.64 | 0.78 | 1.10 |
| 11-03 03:18 | +10 stop | BTC | DOWN | 0.50 | open |  |
| 11-03 03:18 | +5 | BTC | DOWN | 0.51 | open |  |
| 11-03 03:17 | +10 stop | ZEC | UP | 0.57 | 0.67 | 0.66 |
| 11-03 03:17 | +20 | ZEC | UP | 0.57 | 0.77 | 1.69 |
| 11-03 03:17 | +15 | ZEC | UP | 0.57 | 0.77 | 1.69 |
| 11-03 03:17 | +10 | ZEC | UP | 0.58 | 0.70 | 0.90 |
| 11-03 03:17 | +5 | ZEC | UP | 0.58 | 0.63 | 0.18 |
| 11-03 03:17 | +10 stop | DOGE | UP | 0.68 | 0.53 | -1.84 |
| 11-03 03:17 | +20 | DOGE | UP | 0.68 | open |  |
| 11-03 03:17 | +15 | DOGE | UP | 0.68 | 0.85 | 1.45 |
| 11-03 03:17 | +10 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 11-03 03:17 | +5 | DOGE | UP | 0.70 | 0.78 | 0.52 |
| 11-03 03:17 | +10 stop | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 11-03 03:17 | +20 | NEAR | UP | 0.69 | open |  |
| 11-03 03:17 | +15 | NEAR | UP | 0.69 | open |  |
| 11-03 03:17 | +10 | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 11-03 03:17 | +5 | NEAR | UP | 0.69 | 0.74 | 0.21 |
| 11-03 03:17 | +10 stop | XRP | UP | 0.65 | 0.75 | 0.70 |
| 11-03 03:17 | +20 | XRP | UP | 0.65 | 0.90 | 2.31 |
| 11-03 03:17 | +15 | XRP | UP | 0.65 | 0.82 | 1.43 |
| 11-03 03:17 | +10 | XRP | UP | 0.65 | 0.75 | 0.70 |
| 11-03 03:17 | +5 | XRP | UP | 0.65 | 0.75 | 0.70 |
| 11-03 03:17 | +5 | ETH | UP | 0.66 | 0.73 | 0.40 |
| 11-03 03:16 | +10 stop | BTC | UP | 0.59 | 0.44 | -1.85 |
| 11-03 03:16 | +20 | BTC | UP | 0.59 | open |  |
| 11-03 03:16 | +15 | BTC | UP | 0.59 | open |  |
| 11-03 03:16 | +10 | BTC | UP | 0.59 | open |  |
| 11-03 03:16 | +5 | BTC | UP | 0.59 | 0.64 | 0.16 |
| 11-03 03:16 | +10 stop | ETH | UP | 0.62 | 0.73 | 0.79 |
| 11-03 03:16 | +20 | ETH | UP | 0.62 | open |  |
| 11-03 03:16 | +15 | ETH | UP | 0.62 | open |  |
| 11-03 03:16 | +10 | ETH | UP | 0.61 | 0.73 | 0.89 |
