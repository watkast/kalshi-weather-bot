# Range-Scalp Bot

*Updated Mon Nov 16 11:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62011 | 54105 | 7906 (115) | 0 | $-16749.43 | -4.3% |
| **+10¢** | 46312 | 37058 | 9254 (157) | 0 | $-15631.10 | -5.4% |
| **+15¢** | 38809 | 28829 | 9980 (196) | 0 | $-14225.67 | -5.8% |
| **+20¢** | 34596 | 24132 | 10464 (249) | 0 | $-12405.64 | -5.7% |
| **+10¢ (15¢ stop)** | 75464 | 75310 | 154 (90) | 0 | $-27822.87 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 11:42 | +10 stop | NEAR | UP | 0.68 | 0.96 | 2.64 |
| 11-16 11:42 | +5 | NEAR | UP | 0.67 | 0.75 | 0.50 |
| 11-16 11:41 | +10 stop | NEAR | DOWN | 0.48 | 0.61 | 0.95 |
| 11-16 11:41 | +5 | NEAR | DOWN | 0.48 | 0.61 | 0.95 |
| 11-16 11:40 | +10 stop | DOGE | DOWN | 0.71 | 0.50 | -2.43 |
| 11-16 11:40 | +10 stop | XRP | DOWN | 0.48 | 0.30 | -2.13 |
| 11-16 11:40 | +5 | DOGE | DOWN | 0.71 | yes | -7.25 |
| 11-16 11:40 | +10 stop | SOL | DOWN | 0.55 | 0.28 | -3.03 |
| 11-16 11:40 | +5 | DOGE | UP | 0.42 | 0.54 | 0.84 |
| 11-16 11:40 | +10 stop | ZEC | DOWN | 0.67 | 0.85 | 1.55 |
| 11-16 11:39 | +10 stop | SOL | DOWN | 0.46 | 0.57 | 0.74 |
| 11-16 11:39 | +10 stop | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-16 11:39 | +10 stop | SOL | UP | 0.62 | 0.45 | -2.05 |
| 11-16 11:39 | +5 | SOL | UP | 0.63 | 0.69 | 0.28 |
| 11-16 11:38 | +10 stop | BTC | DOWN | 0.71 | 0.50 | -2.43 |
| 11-16 11:38 | +10 stop | DOGE | UP | 0.63 | 0.33 | -3.33 |
| 11-16 11:38 | +15 | DOGE | UP | 0.63 | 0.86 | 2.04 |
| 11-16 11:38 | +10 | DOGE | UP | 0.63 | 0.86 | 2.04 |
| 11-16 11:38 | +5 | DOGE | UP | 0.63 | 0.70 | 0.38 |
| 11-16 11:37 | +10 stop | NEAR | DOWN | 0.63 | 0.80 | 1.41 |
| 11-16 11:37 | +10 stop | ZEC | UP | 0.64 | 0.46 | -2.15 |
| 11-16 11:37 | +10 | ZEC | UP | 0.64 | no | -6.57 |
| 11-16 11:37 | +5 | ZEC | UP | 0.64 | no | -6.57 |
| 11-16 11:37 | +5 | ETH | UP | 0.68 | no | -6.96 |
| 11-16 11:37 | +5 | BTC | UP | 0.69 | no | -7.05 |
| 11-16 11:37 | +10 | ETH | UP | 0.65 | no | -6.66 |
| 11-16 11:37 | +10 stop | BTC | UP | 0.68 | 0.52 | -1.94 |
| 11-16 11:37 | +15 | BTC | UP | 0.68 | no | -6.96 |
| 11-16 11:37 | +10 | BTC | UP | 0.68 | no | -6.96 |
| 11-16 11:36 | +5 | ETH | UP | 0.58 | 0.67 | 0.56 |
| 11-16 11:36 | +5 | BTC | UP | 0.64 | 0.69 | 0.18 |
| 11-16 11:36 | +10 stop | XRP | UP | 0.69 | 0.52 | -2.03 |
| 11-16 11:36 | +20 | XRP | UP | 0.69 | 0.91 | 1.99 |
| 11-16 11:36 | +10 | XRP | UP | 0.69 | 0.88 | 1.67 |
| 11-16 11:36 | +5 | XRP | UP | 0.69 | 0.75 | 0.31 |
| 11-16 11:35 | +5 | BTC | UP | 0.54 | 0.60 | 0.25 |
| 11-16 11:35 | +10 stop | BTC | UP | 0.54 | 0.69 | 1.17 |
| 11-16 11:35 | +10 stop | ETH | DOWN | 0.45 | 0.60 | 1.15 |
| 11-16 11:35 | +5 | DOGE | UP | 0.67 | 0.73 | 0.30 |
| 11-16 11:34 | +10 stop | DOGE | UP | 0.58 | 0.73 | 1.18 |
