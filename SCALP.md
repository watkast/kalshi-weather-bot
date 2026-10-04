# Range-Scalp Bot

*Updated Sun Oct 04 05:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1809 | 1557 | 252 (3) | 5 | $-624.64 | -5.4% |
| **+10¢** | 1408 | 1128 | 280 (4) | 4 | $-462.04 | -5.2% |
| **+15¢** | 1184 | 889 | 295 (5) | 6 | $-391.03 | -5.3% |
| **+20¢** | 1041 | 727 | 314 (7) | 7 | $-394.35 | -6.0% |
| **+10¢ (15¢ stop)** | 2282 | 2281 | 1 (1) | 3 | $-955.41 | -6.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 05:19 | +5 | HYPE | UP | 0.68 | open |  |
| 10-04 05:19 | +10 stop | DOGE | UP | 0.68 | open |  |
| 10-04 05:18 | +5 | HYPE | UP | 0.58 | 0.65 | 0.36 |
| 10-04 05:18 | +5 | NEAR | DOWN | 0.67 | open |  |
| 10-04 05:18 | +10 stop | XRP | UP | 0.62 | 0.73 | 0.79 |
| 10-04 05:18 | +20 | XRP | UP | 0.62 | open |  |
| 10-04 05:18 | +15 | XRP | UP | 0.62 | 0.77 | 1.20 |
| 10-04 05:18 | +10 | XRP | UP | 0.62 | 0.73 | 0.79 |
| 10-04 05:18 | +5 | XRP | UP | 0.62 | 0.68 | 0.27 |
| 10-04 05:18 | +10 stop | DOGE | DOWN | 0.60 | 0.43 | -2.05 |
| 10-04 05:18 | +20 | DOGE | DOWN | 0.60 | open |  |
| 10-04 05:18 | +15 | DOGE | DOWN | 0.60 | open |  |
| 10-04 05:18 | +10 | DOGE | DOWN | 0.60 | open |  |
| 10-04 05:18 | +5 | DOGE | DOWN | 0.60 | open |  |
| 10-04 05:17 | +10 stop | HYPE | UP | 0.55 | 0.66 | 0.72 |
| 10-04 05:17 | +20 | HYPE | UP | 0.55 | open |  |
| 10-04 05:17 | +15 | HYPE | UP | 0.55 | open |  |
| 10-04 05:17 | +10 | HYPE | UP | 0.55 | 0.66 | 0.72 |
| 10-04 05:17 | +5 | HYPE | UP | 0.55 | 0.62 | 0.31 |
| 10-04 05:17 | +10 stop | NEAR | DOWN | 0.62 | open |  |
| 10-04 05:17 | +20 | NEAR | DOWN | 0.62 | open |  |
| 10-04 05:17 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-04 05:17 | +10 | NEAR | DOWN | 0.62 | open |  |
| 10-04 05:17 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
| 10-04 05:16 | +10 stop | ETH | UP | 0.61 | 0.77 | 1.30 |
| 10-04 05:16 | +20 | ETH | UP | 0.61 | 0.84 | 2.03 |
| 10-04 05:16 | +15 | ETH | UP | 0.61 | 0.77 | 1.30 |
| 10-04 05:16 | +10 | ETH | UP | 0.61 | 0.77 | 1.30 |
| 10-04 05:16 | +5 | ETH | UP | 0.61 | 0.77 | 1.30 |
| 10-04 05:16 | +10 stop | ZEC | DOWN | 0.66 | open |  |
| 10-04 05:16 | +20 | ZEC | DOWN | 0.66 | open |  |
| 10-04 05:16 | +15 | ZEC | DOWN | 0.66 | open |  |
| 10-04 05:16 | +10 | ZEC | DOWN | 0.66 | open |  |
| 10-04 05:16 | +5 | ZEC | DOWN | 0.65 | open |  |
| 10-04 05:16 | +10 stop | BTC | DOWN | 0.58 | 0.40 | -2.15 |
| 10-04 05:16 | +20 | BTC | DOWN | 0.58 | open |  |
| 10-04 05:16 | +15 | BTC | DOWN | 0.58 | open |  |
| 10-04 05:16 | +10 | BTC | DOWN | 0.58 | open |  |
| 10-04 05:16 | +5 | BTC | DOWN | 0.58 | open |  |
| 10-04 05:16 | +10 stop | SOL | UP | 0.71 | 0.82 | 0.84 |
