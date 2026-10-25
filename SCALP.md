# Range-Scalp Bot

*Updated Sun Oct 25 04:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32552 | 28385 | 4167 (42) | 3 | $-9264.84 | -4.5% |
| **+10¢** | 24367 | 19541 | 4826 (60) | 3 | $-8298.02 | -5.4% |
| **+15¢** | 20399 | 15207 | 5192 (83) | 3 | $-7451.77 | -5.8% |
| **+20¢** | 18069 | 12636 | 5433 (105) | 4 | $-6592.09 | -5.8% |
| **+10¢ (15¢ stop)** | 39998 | 39938 | 60 (32) | 0 | $-15264.74 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 04:13 | +10 stop | BTC | UP | 0.20 | 0.58 | 3.50 |
| 10-25 04:13 | +10 stop | XRP | DOWN | 0.53 | 0.90 | 3.46 |
| 10-25 04:13 | +20 | XRP | DOWN | 0.53 | 0.90 | 3.47 |
| 10-25 04:13 | +15 | XRP | DOWN | 0.54 | 0.90 | 3.42 |
| 10-25 04:13 | +10 | XRP | DOWN | 0.50 | 0.90 | 3.77 |
| 10-25 04:13 | +5 | XRP | DOWN | 0.50 | 0.59 | 0.55 |
| 10-25 04:13 | +10 stop | BTC | DOWN | 0.30 | 0.58 | 2.46 |
| 10-25 04:09 | +10 stop | BTC | UP | 0.63 | 0.76 | 1.00 |
| 10-25 04:09 | +10 stop | NEAR | UP | 0.64 | 0.81 | 1.42 |
| 10-25 04:09 | +15 | NEAR | UP | 0.64 | 0.81 | 1.42 |
| 10-25 04:09 | +10 | NEAR | UP | 0.64 | 0.81 | 1.42 |
| 10-25 04:09 | +5 | NEAR | UP | 0.64 | 0.69 | 0.18 |
| 10-25 04:08 | +10 stop | DOGE | UP | 0.57 | 0.67 | 0.66 |
| 10-25 04:07 | +10 stop | BTC | DOWN | 0.66 | 0.51 | -1.84 |
| 10-25 04:07 | +20 | BTC | DOWN | 0.66 | 0.99 | 3.10 |
| 10-25 04:07 | +15 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 10-25 04:07 | +10 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 10-25 04:07 | +5 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 10-25 04:07 | +10 stop | ETH | UP | 0.69 | 0.82 | 1.04 |
| 10-25 04:06 | +10 stop | SOL | UP | 0.64 | 0.76 | 0.90 |
| 10-25 04:05 | +10 stop | ZEC | DOWN | 0.47 | 0.64 | 1.35 |
| 10-25 04:05 | +15 | ZEC | DOWN | 0.47 | 0.64 | 1.35 |
| 10-25 04:05 | +10 | ZEC | DOWN | 0.47 | 0.64 | 1.35 |
| 10-25 04:05 | +5 | ZEC | DOWN | 0.47 | 0.64 | 1.35 |
| 10-25 04:05 | +10 stop | ETH | UP | 0.56 | 0.66 | 0.66 |
| 10-25 04:05 | +10 stop | DOGE | DOWN | 0.60 | 0.45 | -1.85 |
| 10-25 04:04 | +10 stop | NEAR | UP | 0.64 | 0.74 | 0.70 |
| 10-25 04:04 | +10 | NEAR | UP | 0.64 | 0.74 | 0.70 |
| 10-25 04:04 | +5 | NEAR | UP | 0.64 | 0.69 | 0.19 |
| 10-25 04:03 | +10 stop | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 10-25 04:03 | +15 | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 10-25 04:03 | +10 | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 10-25 04:03 | +10 stop | SOL | DOWN | 0.66 | 0.45 | -2.44 |
| 10-25 04:03 | +10 | SOL | DOWN | 0.66 | open |  |
| 10-25 04:03 | +5 | SOL | DOWN | 0.66 | open |  |
| 10-25 04:03 | +5 | NEAR | UP | 0.56 | 0.76 | 1.69 |
| 10-25 04:03 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.30 |
| 10-25 04:02 | +10 stop | ETH | DOWN | 0.63 | 0.43 | -2.35 |
| 10-25 04:02 | +20 | ETH | DOWN | 0.63 | open |  |
| 10-25 04:02 | +15 | ETH | DOWN | 0.63 | open |  |
