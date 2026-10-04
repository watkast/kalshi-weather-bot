# Range-Scalp Bot

*Updated Sun Oct 04 04:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1788 | 1540 | 248 (3) | 2 | $-609.63 | -5.4% |
| **+10¢** | 1391 | 1116 | 275 (4) | 2 | $-443.30 | -5.0% |
| **+15¢** | 1171 | 882 | 289 (5) | 2 | $-363.62 | -4.9% |
| **+20¢** | 1028 | 720 | 308 (7) | 3 | $-371.25 | -5.7% |
| **+10¢ (15¢ stop)** | 2262 | 2261 | 1 (1) | 0 | $-945.80 | -6.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 04:57 | +5 | BNB | UP | 0.66 | 0.78 | 0.91 |
| 10-04 04:56 | +10 stop | BNB | UP | 0.56 | 0.78 | 1.89 |
| 10-04 04:56 | +10 | BNB | UP | 0.56 | 0.78 | 1.89 |
| 10-04 04:56 | +5 | BNB | UP | 0.56 | 0.61 | 0.15 |
| 10-04 04:54 | +10 stop | BTC | DOWN | 0.62 | 0.77 | 1.20 |
| 10-04 04:54 | +10 stop | ZEC | DOWN | 0.66 | 0.84 | 1.53 |
| 10-04 04:54 | +10 stop | DOGE | UP | 0.66 | 0.78 | 0.91 |
| 10-04 04:54 | +20 | DOGE | UP | 0.67 | 0.90 | 2.12 |
| 10-04 04:54 | +15 | DOGE | UP | 0.67 | 0.90 | 2.12 |
| 10-04 04:54 | +10 | DOGE | UP | 0.67 | 0.78 | 0.86 |
| 10-04 04:54 | +5 | DOGE | UP | 0.67 | 0.78 | 0.86 |
| 10-04 04:53 | +10 stop | ZEC | UP | 0.59 | 0.40 | -2.24 |
| 10-04 04:53 | +10 | ZEC | UP | 0.59 | 0.74 | 1.19 |
| 10-04 04:53 | +5 | ZEC | UP | 0.59 | 0.68 | 0.57 |
| 10-04 04:53 | +10 stop | ETH | DOWN | 0.59 | 0.76 | 1.40 |
| 10-04 04:53 | +15 | ETH | DOWN | 0.59 | 0.76 | 1.40 |
| 10-04 04:53 | +10 | ETH | DOWN | 0.59 | 0.76 | 1.40 |
| 10-04 04:53 | +5 | ETH | DOWN | 0.59 | 0.68 | 0.57 |
| 10-04 04:52 | +10 stop | XRP | UP | 0.60 | 0.44 | -1.92 |
| 10-04 04:52 | +10 stop | HYPE | UP | 0.70 | 0.52 | -2.13 |
| 10-04 04:52 | +20 | HYPE | UP | 0.70 | open |  |
| 10-04 04:52 | +15 | HYPE | UP | 0.70 | open |  |
| 10-04 04:52 | +10 | HYPE | UP | 0.69 | open |  |
| 10-04 04:52 | +5 | HYPE | UP | 0.69 | open |  |
| 10-04 04:51 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.74 |
| 10-04 04:51 | +15 | SOL | UP | 0.71 | 0.86 | 1.26 |
| 10-04 04:51 | +10 | SOL | UP | 0.71 | 0.81 | 0.74 |
| 10-04 04:51 | +5 | SOL | UP | 0.71 | 0.81 | 0.74 |
| 10-04 04:50 | +10 stop | XRP | UP | 0.67 | 0.48 | -2.24 |
| 10-04 04:50 | +10 stop | NEAR | DOWN | 0.57 | 0.68 | 0.76 |
| 10-04 04:50 | +15 | NEAR | DOWN | 0.57 | 0.75 | 1.48 |
| 10-04 04:50 | +10 | NEAR | DOWN | 0.57 | 0.68 | 0.76 |
| 10-04 04:50 | +5 | NEAR | DOWN | 0.57 | 0.68 | 0.76 |
| 10-04 04:50 | +10 stop | BNB | UP | 0.64 | 0.74 | 0.70 |
| 10-04 04:49 | +10 stop | ETH | DOWN | 0.55 | 0.71 | 1.27 |
| 10-04 04:49 | +20 | ETH | DOWN | 0.55 | 0.76 | 1.79 |
| 10-04 04:49 | +15 | ETH | DOWN | 0.55 | 0.71 | 1.27 |
| 10-04 04:49 | +10 | ETH | DOWN | 0.55 | 0.71 | 1.27 |
| 10-04 04:49 | +5 | ETH | DOWN | 0.55 | 0.71 | 1.27 |
| 10-04 04:49 | +10 stop | XRP | UP | 0.62 | 0.73 | 0.79 |
