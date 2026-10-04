# Range-Scalp Bot

*Updated Sun Oct 04 18:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2603 | 2238 | 365 (3) | 2 | $-902.52 | -5.5% |
| **+10¢** | 2034 | 1624 | 410 (4) | 4 | $-739.66 | -5.8% |
| **+15¢** | 1708 | 1279 | 429 (5) | 4 | $-603.12 | -5.6% |
| **+20¢** | 1519 | 1068 | 451 (9) | 4 | $-525.32 | -5.5% |
| **+10¢ (15¢ stop)** | 3240 | 3239 | 1 (1) | 0 | $-1219.26 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 18:09 | +10 stop | NEAR | UP | 0.69 | 0.80 | 0.83 |
| 10-04 18:08 | +10 stop | HYPE | UP | 0.50 | 0.60 | 0.65 |
| 10-04 18:08 | +10 stop | DOGE | UP | 0.45 | 0.55 | 0.64 |
| 10-04 18:08 | +5 | BTC | DOWN | 0.47 | 0.59 | 0.85 |
| 10-04 18:07 | +5 | BTC | UP | 0.52 | 0.65 | 0.96 |
| 10-04 18:07 | +10 stop | HYPE | DOWN | 0.56 | 0.35 | -2.44 |
| 10-04 18:06 | +10 stop | XRP | DOWN | 0.58 | 0.71 | 0.97 |
| 10-04 18:06 | +5 | XRP | DOWN | 0.58 | 0.66 | 0.46 |
| 10-04 18:06 | +10 stop | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 10-04 18:06 | +5 | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 10-04 18:06 | +10 stop | BTC | UP | 0.57 | 0.40 | -2.05 |
| 10-04 18:06 | +20 | BTC | UP | 0.57 | open |  |
| 10-04 18:06 | +10 | BTC | UP | 0.57 | open |  |
| 10-04 18:06 | +5 | BTC | UP | 0.57 | 0.65 | 0.46 |
| 10-04 18:06 | +10 stop | DOGE | UP | 0.70 | 0.55 | -1.87 |
| 10-04 18:05 | +10 stop | HYPE | UP | 0.70 | 0.82 | 0.93 |
| 10-04 18:04 | +10 stop | ETH | DOWN | 0.65 | 0.43 | -2.54 |
| 10-04 18:04 | +15 | ETH | DOWN | 0.65 | 0.83 | 1.54 |
| 10-04 18:04 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-04 18:04 | +5 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-04 18:04 | +10 stop | DOGE | DOWN | 0.51 | 0.32 | -2.23 |
| 10-04 18:04 | +10 stop | BNB | UP | 0.58 | 0.68 | 0.66 |
| 10-04 18:04 | +5 | BNB | UP | 0.58 | 0.68 | 0.66 |
| 10-04 18:03 | +5 | ZEC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-04 18:03 | +5 | BTC | UP | 0.66 | 0.74 | 0.50 |
| 10-04 18:03 | +5 | ETH | DOWN | 0.64 | 0.72 | 0.44 |
| 10-04 18:02 | +10 stop | BTC | UP | 0.63 | 0.74 | 0.79 |
| 10-04 18:02 | +15 | BTC | UP | 0.63 | open |  |
| 10-04 18:02 | +10 | BTC | UP | 0.63 | 0.74 | 0.79 |
| 10-04 18:02 | +5 | BTC | UP | 0.63 | 0.68 | 0.17 |
| 10-04 18:02 | +10 stop | XRP | DOWN | 0.70 | 0.50 | -2.33 |
| 10-04 18:02 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.90 |
| 10-04 18:02 | +15 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 10-04 18:02 | +10 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 10-04 18:02 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 10-04 18:02 | +5 | BNB | UP | 0.53 | 0.67 | 1.06 |
| 10-04 18:01 | +10 stop | ZEC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-04 18:01 | +20 | ZEC | DOWN | 0.59 | 0.80 | 1.81 |
| 10-04 18:01 | +15 | ZEC | DOWN | 0.59 | 0.80 | 1.81 |
| 10-04 18:01 | +10 | ZEC | DOWN | 0.59 | 0.70 | 0.78 |
