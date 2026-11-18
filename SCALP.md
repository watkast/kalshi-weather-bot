# Range-Scalp Bot

*Updated Wed Nov 18 00:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63355 | 55261 | 8094 (118) | 2 | $-17275.85 | -4.3% |
| **+10¢** | 47322 | 37851 | 9471 (159) | 5 | $-16172.35 | -5.4% |
| **+15¢** | 39673 | 29459 | 10214 (203) | 5 | $-14664.70 | -5.9% |
| **+20¢** | 35348 | 24630 | 10718 (258) | 6 | $-12903.21 | -5.8% |
| **+10¢ (15¢ stop)** | 77098 | 76940 | 158 (93) | 0 | $-28401.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 00:43 | +10 stop | SOL | UP | 0.46 | 0.57 | 0.74 |
| 11-18 00:43 | +20 | SOL | UP | 0.47 | 0.69 | 1.87 |
| 11-18 00:43 | +15 | SOL | UP | 0.47 | 0.69 | 1.87 |
| 11-18 00:43 | +10 | SOL | UP | 0.48 | 0.69 | 1.77 |
| 11-18 00:43 | +5 | SOL | UP | 0.48 | 0.57 | 0.54 |
| 11-18 00:43 | +10 stop | ZEC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-18 00:43 | +20 | ZEC | DOWN | 0.66 | open |  |
| 11-18 00:43 | +15 | ZEC | DOWN | 0.65 | 0.82 | 1.43 |
| 11-18 00:43 | +10 | ZEC | DOWN | 0.65 | 0.82 | 1.43 |
| 11-18 00:43 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-18 00:42 | +10 stop | ETH | UP | 0.70 | 0.44 | -2.91 |
| 11-18 00:42 | +20 | ETH | UP | 0.68 | open |  |
| 11-18 00:42 | +15 | ETH | UP | 0.68 | open |  |
| 11-18 00:42 | +10 | ETH | UP | 0.68 | open |  |
| 11-18 00:42 | +5 | ETH | UP | 0.68 | 0.73 | 0.20 |
| 11-18 00:42 | +10 stop | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 11-18 00:42 | +5 | XRP | DOWN | 0.58 | 0.74 | 1.28 |
| 11-18 00:41 | +10 stop | XRP | UP | 0.59 | 0.42 | -2.05 |
| 11-18 00:41 | +20 | XRP | UP | 0.59 | open |  |
| 11-18 00:41 | +15 | XRP | UP | 0.59 | open |  |
| 11-18 00:41 | +10 | XRP | UP | 0.59 | open |  |
| 11-18 00:41 | +5 | XRP | UP | 0.59 | 0.68 | 0.57 |
| 11-18 00:41 | +10 | SOL | UP | 0.47 | 0.57 | 0.64 |
| 11-18 00:41 | +5 | SOL | UP | 0.47 | 0.54 | 0.34 |
| 11-18 00:40 | +20 | SOL | UP | 0.53 | 0.73 | 1.68 |
| 11-18 00:40 | +10 | SOL | UP | 0.52 | 0.63 | 0.75 |
| 11-18 00:40 | +5 | SOL | UP | 0.52 | 0.63 | 0.77 |
| 11-18 00:40 | +10 stop | DOGE | DOWN | 0.70 | 0.87 | 1.47 |
| 11-18 00:40 | +5 | DOGE | DOWN | 0.68 | 0.75 | 0.41 |
| 11-18 00:40 | +10 stop | NEAR | DOWN | 0.63 | 0.78 | 1.19 |
| 11-18 00:39 | +10 stop | NEAR | UP | 0.56 | 0.39 | -2.05 |
| 11-18 00:39 | +20 | NEAR | UP | 0.56 | open |  |
| 11-18 00:39 | +15 | NEAR | UP | 0.56 | open |  |
| 11-18 00:39 | +10 | NEAR | UP | 0.56 | open |  |
| 11-18 00:39 | +5 | NEAR | UP | 0.57 | open |  |
| 11-18 00:39 | +10 stop | HYPE | UP | 0.60 | 0.41 | -2.24 |
| 11-18 00:39 | +10 | HYPE | UP | 0.61 | open |  |
| 11-18 00:39 | +5 | HYPE | UP | 0.61 | open |  |
| 11-18 00:37 | +10 stop | DOGE | UP | 0.57 | 0.70 | 0.97 |
| 11-18 00:36 | +10 stop | XRP | UP | 0.68 | 0.81 | 1.03 |
