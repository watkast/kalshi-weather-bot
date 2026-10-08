# Range-Scalp Bot

*Updated Thu Oct 08 22:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8056 | 6976 | 1080 (13) | 2 | $-2569.34 | -5.1% |
| **+10¢** | 6099 | 4819 | 1280 (25) | 2 | $-2539.95 | -6.6% |
| **+15¢** | 5134 | 3788 | 1346 (37) | 2 | $-2054.69 | -6.4% |
| **+20¢** | 4584 | 3188 | 1396 (45) | 2 | $-1635.84 | -5.7% |
| **+10¢ (15¢ stop)** | 9778 | 9748 | 30 (19) | 0 | $-3596.78 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 21:58 | +10 stop | NEAR | DOWN | 0.50 | 0.60 | 0.65 |
| 10-08 21:58 | +5 | NEAR | DOWN | 0.50 | 0.60 | 0.65 |
| 10-08 21:58 | +10 stop | HYPE | DOWN | 0.60 | 0.93 | 3.09 |
| 10-08 21:58 | +20 | HYPE | DOWN | 0.60 | 0.93 | 3.09 |
| 10-08 21:58 | +15 | HYPE | DOWN | 0.60 | 0.93 | 3.09 |
| 10-08 21:58 | +10 | HYPE | DOWN | 0.59 | 0.93 | 3.19 |
| 10-08 21:58 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.27 |
| 10-08 21:58 | +10 stop | BTC | DOWN | 0.68 | 0.87 | 1.66 |
| 10-08 21:58 | +10 | BTC | DOWN | 0.68 | 0.87 | 1.66 |
| 10-08 21:58 | +5 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 10-08 21:58 | +10 stop | XRP | UP | 0.69 | 0.80 | 0.83 |
| 10-08 21:58 | +20 | XRP | UP | 0.70 | 0.92 | 2.01 |
| 10-08 21:58 | +15 | XRP | UP | 0.70 | 0.88 | 1.57 |
| 10-08 21:58 | +10 | XRP | UP | 0.70 | 0.80 | 0.73 |
| 10-08 21:58 | +5 | XRP | UP | 0.70 | 0.80 | 0.73 |
| 10-08 21:55 | +10 stop | BTC | UP | 0.71 | 0.81 | 0.74 |
| 10-08 21:55 | +15 | BTC | UP | 0.71 | no | -7.25 |
| 10-08 21:55 | +10 | BTC | UP | 0.71 | 0.81 | 0.74 |
| 10-08 21:55 | +5 | BTC | UP | 0.71 | 0.77 | 0.32 |
| 10-08 21:53 | +10 stop | BNB | UP | 0.70 | 0.91 | 1.91 |
| 10-08 21:53 | +5 | BNB | UP | 0.70 | 0.78 | 0.52 |
| 10-08 21:53 | +10 stop | ETH | UP | 0.70 | 0.55 | -1.83 |
| 10-08 21:53 | +15 | ETH | UP | 0.70 | 0.86 | 1.36 |
| 10-08 21:53 | +10 | ETH | UP | 0.70 | 0.84 | 1.15 |
| 10-08 21:53 | +5 | ETH | UP | 0.70 | 0.84 | 1.15 |
| 10-08 21:52 | +10 stop | DOGE | DOWN | 0.50 | 0.33 | -2.04 |
| 10-08 21:52 | +20 | DOGE | DOWN | 0.51 | yes | -5.28 |
| 10-08 21:52 | +15 | DOGE | DOWN | 0.51 | yes | -5.23 |
| 10-08 21:52 | +10 | DOGE | DOWN | 0.50 | yes | -5.18 |
| 10-08 21:52 | +5 | DOGE | DOWN | 0.50 | yes | -5.18 |
| 10-08 21:52 | +10 stop | HYPE | UP | 0.63 | 0.80 | 1.41 |
| 10-08 21:52 | +20 | HYPE | UP | 0.63 | 0.86 | 2.04 |
| 10-08 21:52 | +15 | HYPE | UP | 0.63 | 0.80 | 1.41 |
| 10-08 21:52 | +10 | HYPE | UP | 0.63 | 0.80 | 1.41 |
| 10-08 21:52 | +5 | HYPE | UP | 0.63 | 0.69 | 0.28 |
| 10-08 21:52 | +10 stop | BNB | UP | 0.59 | 0.70 | 0.78 |
| 10-08 21:52 | +5 | BNB | UP | 0.59 | 0.64 | 0.16 |
| 10-08 21:51 | +5 | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 10-08 21:51 | +10 stop | NEAR | DOWN | 0.59 | 0.35 | -2.73 |
| 10-08 21:51 | +15 | NEAR | DOWN | 0.59 | 0.87 | 2.55 |
