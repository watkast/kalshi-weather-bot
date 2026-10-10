# Range-Scalp Bot

*Updated Sat Oct 10 05:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9987 | 8618 | 1369 (18) | 7 | $-3379.84 | -5.4% |
| **+10¢** | 7544 | 5949 | 1595 (30) | 7 | $-3246.13 | -6.8% |
| **+15¢** | 6370 | 4688 | 1682 (43) | 7 | $-2680.59 | -6.7% |
| **+20¢** | 5659 | 3912 | 1747 (55) | 7 | $-2243.09 | -6.3% |
| **+10¢ (15¢ stop)** | 12273 | 12238 | 35 (22) | 4 | $-4827.60 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 05:09 | +10 stop | SOL | UP | 0.63 | open |  |
| 10-10 05:08 | +10 stop | ETH | DOWN | 0.60 | open |  |
| 10-10 05:08 | +5 | ETH | DOWN | 0.60 | open |  |
| 10-10 05:08 | +10 stop | DOGE | UP | 0.67 | 0.79 | 0.88 |
| 10-10 05:08 | +10 stop | BTC | DOWN | 0.51 | open |  |
| 10-10 05:08 | +15 | BTC | DOWN | 0.51 | open |  |
| 10-10 05:08 | +10 stop | HYPE | UP | 0.70 | open |  |
| 10-10 05:07 | +10 stop | SOL | DOWN | 0.54 | 0.39 | -1.85 |
| 10-10 05:07 | +15 | SOL | DOWN | 0.54 | open |  |
| 10-10 05:07 | +10 | SOL | DOWN | 0.55 | open |  |
| 10-10 05:07 | +5 | SOL | DOWN | 0.54 | open |  |
| 10-10 05:07 | +10 stop | BNB | DOWN | 0.38 | 0.57 | 1.55 |
| 10-10 05:07 | +15 | BNB | DOWN | 0.38 | 0.57 | 1.55 |
| 10-10 05:07 | +10 | BNB | DOWN | 0.38 | 0.57 | 1.55 |
| 10-10 05:07 | +5 | BNB | DOWN | 0.38 | 0.57 | 1.55 |
| 10-10 05:06 | +10 stop | BTC | DOWN | 0.71 | 0.52 | -2.23 |
| 10-10 05:06 | +10 | BTC | DOWN | 0.71 | open |  |
| 10-10 05:06 | +5 | BTC | DOWN | 0.71 | open |  |
| 10-10 05:06 | +10 stop | ETH | DOWN | 0.69 | 0.52 | -2.03 |
| 10-10 05:06 | +10 | ETH | DOWN | 0.69 | open |  |
| 10-10 05:06 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 10-10 05:06 | +10 stop | DOGE | DOWN | 0.60 | 0.36 | -2.74 |
| 10-10 05:06 | +10 | DOGE | DOWN | 0.58 | open |  |
| 10-10 05:05 | +10 stop | XRP | DOWN | 0.66 | 0.51 | -1.84 |
| 10-10 05:05 | +15 | XRP | DOWN | 0.66 | open |  |
| 10-10 05:05 | +10 | XRP | DOWN | 0.69 | open |  |
| 10-10 05:05 | +5 | XRP | DOWN | 0.69 | open |  |
| 10-10 05:05 | +5 | DOGE | DOWN | 0.67 | open |  |
| 10-10 05:03 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-10 05:03 | +5 | SOL | DOWN | 0.62 | 0.70 | 0.48 |
| 10-10 05:03 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-10 05:03 | +5 | XRP | DOWN | 0.60 | 0.68 | 0.47 |
| 10-10 05:02 | +10 stop | SOL | UP | 0.62 | 0.35 | -3.03 |
| 10-10 05:02 | +5 | ETH | DOWN | 0.61 | 0.68 | 0.37 |
| 10-10 05:02 | +5 | ETH | DOWN | 0.59 | 0.66 | 0.37 |
| 10-10 05:02 | +10 stop | HYPE | DOWN | 0.56 | 0.36 | -2.39 |
| 10-10 05:02 | +20 | HYPE | DOWN | 0.56 | open |  |
| 10-10 05:02 | +15 | HYPE | DOWN | 0.56 | open |  |
| 10-10 05:02 | +10 | HYPE | DOWN | 0.56 | open |  |
| 10-10 05:02 | +5 | HYPE | DOWN | 0.56 | open |  |
