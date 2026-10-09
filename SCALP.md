# Range-Scalp Bot

*Updated Fri Oct 09 16:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9183 | 7925 | 1258 (16) | 0 | $-3119.51 | -5.4% |
| **+10¢** | 6943 | 5468 | 1475 (28) | 0 | $-3025.88 | -6.9% |
| **+15¢** | 5856 | 4303 | 1553 (41) | 0 | $-2492.60 | -6.8% |
| **+20¢** | 5211 | 3598 | 1613 (52) | 0 | $-2080.38 | -6.4% |
| **+10¢ (15¢ stop)** | 11229 | 11197 | 32 (20) | 0 | $-4300.20 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 16:43 | +10 stop | SOL | UP | 0.54 | 0.66 | 0.86 |
| 10-09 16:43 | +5 | SOL | UP | 0.54 | 0.66 | 0.86 |
| 10-09 16:42 | +10 stop | SOL | UP | 0.58 | 0.31 | -3.03 |
| 10-09 16:42 | +10 stop | BTC | UP | 0.64 | 0.47 | -2.05 |
| 10-09 16:42 | +20 | BTC | UP | 0.61 | no | -6.27 |
| 10-09 16:42 | +15 | BTC | UP | 0.61 | no | -6.27 |
| 10-09 16:42 | +10 | BTC | UP | 0.61 | no | -6.27 |
| 10-09 16:42 | +5 | BTC | UP | 0.61 | no | -6.27 |
| 10-09 16:42 | +10 stop | DOGE | DOWN | 0.70 | 0.85 | 1.26 |
| 10-09 16:42 | +5 | DOGE | DOWN | 0.70 | 0.85 | 1.26 |
| 10-09 16:41 | +10 stop | BTC | UP | 0.71 | 0.82 | 0.84 |
| 10-09 16:41 | +10 | BTC | UP | 0.71 | 0.82 | 0.84 |
| 10-09 16:41 | +5 | BTC | UP | 0.71 | 0.82 | 0.84 |
| 10-09 16:41 | +5 | DOGE | DOWN | 0.57 | 0.64 | 0.35 |
| 10-09 16:40 | +10 stop | SOL | UP | 0.60 | 0.76 | 1.30 |
| 10-09 16:40 | +10 stop | BNB | DOWN | 0.68 | 0.43 | -2.83 |
| 10-09 16:40 | +5 | DOGE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-09 16:39 | +5 | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 10-09 16:39 | +10 stop | XRP | DOWN | 0.64 | 0.47 | -2.05 |
| 10-09 16:39 | +10 stop | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 10-09 16:39 | +10 stop | DOGE | DOWN | 0.69 | 0.51 | -2.13 |
| 10-09 16:39 | +10 stop | HYPE | UP | 0.71 | 0.84 | 1.05 |
| 10-09 16:39 | +5 | DOGE | DOWN | 0.67 | 0.73 | 0.30 |
| 10-09 16:38 | +10 stop | SOL | UP | 0.48 | 0.65 | 1.40 |
| 10-09 16:38 | +10 stop | BTC | UP | 0.51 | 0.65 | 1.06 |
| 10-09 16:38 | +20 | BTC | UP | 0.51 | 0.82 | 2.81 |
| 10-09 16:38 | +15 | BTC | UP | 0.51 | 0.68 | 1.36 |
| 10-09 16:38 | +10 | BTC | UP | 0.51 | 0.65 | 1.06 |
| 10-09 16:38 | +5 | BTC | UP | 0.51 | 0.65 | 1.06 |
| 10-09 16:38 | +5 | DOGE | UP | 0.51 | 0.57 | 0.24 |
| 10-09 16:38 | +10 stop | XRP | UP | 0.57 | 0.39 | -2.12 |
| 10-09 16:38 | +10 stop | ETH | DOWN | 0.63 | 0.76 | 1.00 |
| 10-09 16:38 | +5 | ETH | DOWN | 0.62 | 0.76 | 1.09 |
| 10-09 16:38 | +10 stop | BNB | UP | 0.66 | 0.44 | -2.52 |
| 10-09 16:38 | +15 | BNB | UP | 0.66 | no | -6.74 |
| 10-09 16:38 | +10 | BNB | UP | 0.66 | no | -6.74 |
| 10-09 16:38 | +5 | BNB | UP | 0.66 | no | -6.74 |
| 10-09 16:37 | +5 | DOGE | UP | 0.56 | 0.61 | 0.15 |
| 10-09 16:37 | +10 stop | ETH | UP | 0.58 | 0.42 | -1.96 |
| 10-09 16:37 | +15 | ETH | UP | 0.58 | no | -5.98 |
