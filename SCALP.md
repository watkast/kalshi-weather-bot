# Range-Scalp Bot

*Updated Wed Oct 07 19:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6698 | 5815 | 883 (10) | 5 | $-2027.84 | -4.8% |
| **+10¢** | 5088 | 4053 | 1035 (17) | 5 | $-1904.06 | -5.9% |
| **+15¢** | 4262 | 3171 | 1091 (21) | 5 | $-1598.07 | -6.0% |
| **+20¢** | 3807 | 2670 | 1137 (28) | 5 | $-1274.99 | -5.3% |
| **+10¢ (15¢ stop)** | 8151 | 8134 | 17 (10) | 0 | $-2904.50 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 19:11 | +10 stop | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 10-07 19:11 | +10 stop | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-07 19:11 | +10 stop | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 10-07 19:10 | +10 stop | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 10-07 19:09 | +10 stop | SOL | UP | 0.50 | 0.25 | -2.82 |
| 10-07 19:09 | +10 stop | ETH | UP | 0.62 | 0.43 | -2.25 |
| 10-07 19:09 | +10 | ETH | UP | 0.62 | open |  |
| 10-07 19:09 | +5 | ETH | UP | 0.62 | open |  |
| 10-07 19:09 | +10 stop | BTC | UP | 0.63 | 0.31 | -3.52 |
| 10-07 19:08 | +10 stop | ETH | DOWN | 0.40 | 0.58 | 1.45 |
| 10-07 19:07 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-07 19:07 | +10 stop | HYPE | DOWN | 0.62 | 0.17 | -4.77 |
| 10-07 19:06 | +10 stop | BTC | DOWN | 0.57 | 0.69 | 0.87 |
| 10-07 19:06 | +10 stop | SOL | DOWN | 0.66 | 0.80 | 1.12 |
| 10-07 19:06 | +5 | HYPE | UP | 0.65 | 0.82 | 1.43 |
| 10-07 19:05 | +10 stop | XRP | DOWN | 0.56 | 0.38 | -2.15 |
| 10-07 19:05 | +10 stop | ETH | UP | 0.57 | 0.32 | -2.84 |
| 10-07 19:05 | +10 stop | BNB | DOWN | 0.60 | 0.74 | 1.09 |
| 10-07 19:04 | +10 stop | SOL | DOWN | 0.58 | 0.42 | -1.96 |
| 10-07 19:04 | +10 stop | HYPE | UP | 0.64 | 0.47 | -2.08 |
| 10-07 19:04 | +10 | HYPE | UP | 0.64 | 0.82 | 1.49 |
| 10-07 19:04 | +5 | HYPE | UP | 0.64 | 0.73 | 0.56 |
| 10-07 19:04 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-07 19:03 | +10 stop | XRP | UP | 0.65 | 0.46 | -2.26 |
| 10-07 19:03 | +10 | XRP | UP | 0.65 | 0.80 | 1.25 |
| 10-07 19:03 | +5 | XRP | UP | 0.64 | 0.73 | 0.59 |
| 10-07 19:03 | +10 stop | DOGE | UP | 0.67 | 0.41 | -2.93 |
| 10-07 19:03 | +20 | DOGE | UP | 0.67 | open |  |
| 10-07 19:03 | +15 | DOGE | UP | 0.67 | open |  |
| 10-07 19:03 | +10 | DOGE | UP | 0.67 | open |  |
| 10-07 19:03 | +5 | DOGE | UP | 0.67 | open |  |
| 10-07 19:03 | +10 stop | BTC | UP | 0.66 | 0.51 | -1.84 |
| 10-07 19:03 | +20 | BTC | UP | 0.66 | open |  |
| 10-07 19:03 | +15 | BTC | UP | 0.66 | open |  |
| 10-07 19:03 | +10 | BTC | UP | 0.66 | open |  |
| 10-07 19:03 | +5 | BTC | UP | 0.66 | open |  |
| 10-07 19:03 | +10 stop | SOL | UP | 0.70 | 0.50 | -2.33 |
| 10-07 19:03 | +20 | SOL | UP | 0.70 | open |  |
| 10-07 19:03 | +15 | SOL | UP | 0.70 | open |  |
| 10-07 19:03 | +10 | SOL | UP | 0.70 | open |  |
