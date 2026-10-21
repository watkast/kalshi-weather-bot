# Range-Scalp Bot

*Updated Wed Oct 21 21:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27735 | 24158 | 3577 (39) | 2 | $-8030.44 | -4.6% |
| **+10¢** | 20842 | 16713 | 4129 (55) | 3 | $-7066.07 | -5.4% |
| **+15¢** | 17456 | 13012 | 4444 (78) | 5 | $-6310.38 | -5.8% |
| **+20¢** | 15453 | 10795 | 4658 (98) | 5 | $-5656.37 | -5.8% |
| **+10¢ (15¢ stop)** | 34036 | 33977 | 59 (32) | 1 | $-12651.55 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 21:12 | +10 stop | DOGE | DOWN | 0.60 | open |  |
| 10-21 21:12 | +15 | DOGE | DOWN | 0.60 | open |  |
| 10-21 21:12 | +10 | DOGE | DOWN | 0.55 | 0.65 | 0.66 |
| 10-21 21:12 | +5 | DOGE | DOWN | 0.55 | 0.65 | 0.66 |
| 10-21 21:12 | +10 stop | BNB | DOWN | 0.48 | 0.24 | -2.71 |
| 10-21 21:11 | +10 stop | BTC | UP | 0.71 | 0.82 | 0.84 |
| 10-21 21:10 | +10 stop | DOGE | DOWN | 0.61 | 0.79 | 1.52 |
| 10-21 21:10 | +10 stop | NEAR | DOWN | 0.70 | 0.85 | 1.26 |
| 10-21 21:10 | +10 stop | ETH | DOWN | 0.55 | 0.74 | 1.62 |
| 10-21 21:10 | +10 stop | SOL | DOWN | 0.64 | 0.81 | 1.42 |
| 10-21 21:10 | +10 stop | NEAR | UP | 0.41 | 0.53 | 0.85 |
| 10-21 21:10 | +10 stop | HYPE | DOWN | 0.62 | 0.85 | 2.00 |
| 10-21 21:10 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-21 21:10 | +20 | XRP | DOWN | 0.63 | 0.89 | 2.36 |
| 10-21 21:10 | +15 | XRP | DOWN | 0.63 | 0.89 | 2.36 |
| 10-21 21:10 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-21 21:10 | +5 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-21 21:09 | +10 stop | DOGE | DOWN | 0.71 | 0.51 | -2.33 |
| 10-21 21:09 | +10 stop | SOL | DOWN | 0.70 | 0.55 | -1.83 |
| 10-21 21:09 | +10 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 10-21 21:09 | +5 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 10-21 21:09 | +10 stop | BNB | DOWN | 0.55 | 0.75 | 1.68 |
| 10-21 21:09 | +5 | SOL | DOWN | 0.65 | 0.81 | 1.33 |
| 10-21 21:09 | +5 | SOL | UP | 0.42 | 0.61 | 1.55 |
| 10-21 21:08 | +10 stop | SOL | UP | 0.63 | 0.39 | -2.74 |
| 10-21 21:08 | +10 stop | BTC | UP | 0.68 | 0.80 | 0.92 |
| 10-21 21:08 | +10 stop | SOL | DOWN | 0.47 | 0.57 | 0.64 |
| 10-21 21:07 | +10 stop | NEAR | DOWN | 0.62 | 0.41 | -2.44 |
| 10-21 21:07 | +10 stop | BNB | DOWN | 0.68 | 0.46 | -2.54 |
| 10-21 21:06 | +10 stop | ETH | DOWN | 0.61 | 0.45 | -1.95 |
| 10-21 21:06 | +10 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-21 21:06 | +5 | XRP | DOWN | 0.62 | 0.68 | 0.27 |
| 10-21 21:06 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-21 21:06 | +10 stop | BTC | DOWN | 0.59 | 0.42 | -2.05 |
| 10-21 21:05 | +10 stop | HYPE | DOWN | 0.62 | 0.75 | 0.95 |
| 10-21 21:05 | +10 stop | DOGE | DOWN | 0.59 | 0.73 | 1.04 |
| 10-21 21:05 | +10 stop | ETH | DOWN | 0.55 | 0.65 | 0.66 |
| 10-21 21:04 | +10 stop | SOL | UP | 0.52 | 0.35 | -2.04 |
| 10-21 21:04 | +5 | SOL | UP | 0.52 | 0.60 | 0.45 |
| 10-21 21:04 | +5 | BNB | UP | 0.57 | 0.72 | 1.17 |
