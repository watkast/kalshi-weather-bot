# Range-Scalp Bot

*Updated Sun Oct 04 21:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2850 | 2449 | 401 (3) | 3 | $-997.98 | -5.5% |
| **+10¢** | 2229 | 1779 | 450 (4) | 4 | $-816.99 | -5.8% |
| **+15¢** | 1874 | 1397 | 477 (5) | 5 | $-706.04 | -6.0% |
| **+20¢** | 1669 | 1171 | 498 (9) | 6 | $-597.47 | -5.7% |
| **+10¢ (15¢ stop)** | 3552 | 3551 | 1 (1) | 4 | $-1402.49 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 21:51 | +10 stop | BTC | DOWN | 0.60 | open |  |
| 10-04 21:51 | +10 stop | NEAR | UP | 0.58 | open |  |
| 10-04 21:50 | +5 | SOL | UP | 0.67 | 0.73 | 0.30 |
| 10-04 21:50 | +10 stop | ETH | DOWN | 0.48 | open |  |
| 10-04 21:49 | +10 stop | XRP | DOWN | 0.59 | 0.44 | -1.85 |
| 10-04 21:49 | +10 stop | BTC | DOWN | 0.68 | 0.53 | -1.84 |
| 10-04 21:49 | +10 stop | NEAR | DOWN | 0.68 | 0.43 | -2.84 |
| 10-04 21:48 | +5 | SOL | UP | 0.64 | 0.72 | 0.48 |
| 10-04 21:48 | +10 stop | DOGE | UP | 0.69 | 0.80 | 0.79 |
| 10-04 21:48 | +20 | DOGE | UP | 0.69 | 0.91 | 2.03 |
| 10-04 21:48 | +15 | DOGE | UP | 0.69 | 0.84 | 1.25 |
| 10-04 21:48 | +10 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-04 21:48 | +5 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-04 21:47 | +10 stop | XRP | UP | 0.62 | 0.40 | -2.54 |
| 10-04 21:47 | +10 | XRP | UP | 0.62 | 0.72 | 0.68 |
| 10-04 21:47 | +5 | XRP | UP | 0.62 | 0.72 | 0.68 |
| 10-04 21:47 | +10 stop | NEAR | UP | 0.55 | 0.36 | -2.25 |
| 10-04 21:47 | +20 | NEAR | UP | 0.55 | open |  |
| 10-04 21:47 | +15 | NEAR | UP | 0.55 | open |  |
| 10-04 21:47 | +10 | NEAR | UP | 0.55 | open |  |
| 10-04 21:47 | +5 | NEAR | UP | 0.55 | open |  |
| 10-04 21:46 | +10 stop | XRP | UP | 0.62 | 0.74 | 0.89 |
| 10-04 21:46 | +20 | XRP | UP | 0.62 | open |  |
| 10-04 21:46 | +15 | XRP | UP | 0.62 | open |  |
| 10-04 21:46 | +10 | XRP | UP | 0.62 | 0.74 | 0.89 |
| 10-04 21:46 | +5 | XRP | UP | 0.62 | 0.68 | 0.27 |
| 10-04 21:46 | +10 stop | ETH | UP | 0.67 | 0.52 | -1.84 |
| 10-04 21:46 | +20 | ETH | UP | 0.67 | open |  |
| 10-04 21:46 | +15 | ETH | UP | 0.67 | open |  |
| 10-04 21:46 | +10 | ETH | UP | 0.67 | open |  |
| 10-04 21:46 | +5 | ETH | UP | 0.67 | open |  |
| 10-04 21:46 | +10 stop | BNB | UP | 0.65 | 0.76 | 0.78 |
| 10-04 21:46 | +20 | BNB | UP | 0.65 | open |  |
| 10-04 21:46 | +15 | BNB | UP | 0.65 | 0.82 | 1.40 |
| 10-04 21:46 | +10 | BNB | UP | 0.65 | 0.76 | 0.78 |
| 10-04 21:46 | +5 | BNB | UP | 0.65 | 0.74 | 0.57 |
| 10-04 21:46 | +10 stop | BTC | UP | 0.70 | 0.54 | -1.93 |
| 10-04 21:46 | +20 | BTC | UP | 0.70 | open |  |
| 10-04 21:46 | +15 | BTC | UP | 0.70 | open |  |
| 10-04 21:46 | +10 | BTC | UP | 0.70 | open |  |
