# Range-Scalp Bot

*Updated Sun Nov 22 18:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68936 | 60157 | 8779 (145) | 4 | $-18508.88 | -4.3% |
| **+10¢** | 51441 | 41189 | 10252 (188) | 5 | $-17155.46 | -5.3% |
| **+15¢** | 43110 | 32055 | 11055 (240) | 5 | $-15419.10 | -5.7% |
| **+20¢** | 38384 | 26767 | 11617 (299) | 6 | $-13724.38 | -5.7% |
| **+10¢ (15¢ stop)** | 83940 | 83751 | 189 (117) | 0 | $-30916.64 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 18:25 | +10 stop | BTC | DOWN | 0.70 | 0.53 | -2.03 |
| 11-22 18:24 | +10 stop | BNB | UP | 0.62 | 0.73 | 0.79 |
| 11-22 18:23 | +5 | BNB | UP | 0.61 | 0.73 | 0.89 |
| 11-22 18:23 | +10 stop | BNB | UP | 0.71 | 0.54 | -2.03 |
| 11-22 18:23 | +10 stop | NEAR | DOWN | 0.63 | 0.78 | 1.20 |
| 11-22 18:23 | +20 | NEAR | DOWN | 0.63 | open |  |
| 11-22 18:23 | +15 | NEAR | DOWN | 0.63 | 0.78 | 1.20 |
| 11-22 18:23 | +10 | NEAR | DOWN | 0.63 | 0.78 | 1.20 |
| 11-22 18:23 | +5 | NEAR | DOWN | 0.63 | 0.70 | 0.38 |
| 11-22 18:23 | +10 stop | BTC | DOWN | 0.53 | 0.64 | 0.75 |
| 11-22 18:20 | +10 stop | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 11-22 18:20 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 11-22 18:20 | +10 stop | DOGE | DOWN | 0.71 | 0.85 | 1.17 |
| 11-22 18:20 | +10 stop | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 11-22 18:20 | +10 stop | BNB | UP | 0.64 | 0.44 | -2.35 |
| 11-22 18:20 | +15 | BNB | UP | 0.64 | 0.83 | 1.63 |
| 11-22 18:20 | +10 | BNB | UP | 0.65 | 0.83 | 1.54 |
| 11-22 18:20 | +5 | BNB | UP | 0.64 | 0.69 | 0.18 |
| 11-22 18:19 | +5 | ZEC | DOWN | 0.70 | 0.81 | 0.85 |
| 11-22 18:19 | +10 stop | HYPE | UP | 0.50 | 0.34 | -1.94 |
| 11-22 18:19 | +10 stop | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 11-22 18:19 | +10 | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 11-22 18:19 | +5 | XRP | DOWN | 0.62 | 0.67 | 0.17 |
| 11-22 18:18 | +5 | BTC | UP | 0.71 | open |  |
| 11-22 18:17 | +10 stop | NEAR | DOWN | 0.55 | 0.71 | 1.27 |
| 11-22 18:17 | +10 stop | NEAR | UP | 0.39 | 0.55 | 1.25 |
| 11-22 18:17 | +10 stop | HYPE | UP | 0.61 | 0.46 | -1.85 |
| 11-22 18:17 | +20 | HYPE | UP | 0.61 | open |  |
| 11-22 18:17 | +15 | HYPE | UP | 0.60 | open |  |
| 11-22 18:17 | +10 | HYPE | UP | 0.61 | open |  |
| 11-22 18:17 | +5 | HYPE | UP | 0.60 | open |  |
| 11-22 18:17 | +10 stop | DOGE | UP | 0.65 | 0.47 | -2.14 |
| 11-22 18:17 | +20 | DOGE | UP | 0.65 | open |  |
| 11-22 18:17 | +15 | DOGE | UP | 0.65 | open |  |
| 11-22 18:17 | +10 | DOGE | UP | 0.65 | open |  |
| 11-22 18:17 | +5 | DOGE | UP | 0.65 | open |  |
| 11-22 18:16 | +10 stop | BNB | UP | 0.65 | 0.78 | 1.01 |
| 11-22 18:16 | +20 | BNB | UP | 0.64 | 0.85 | 1.84 |
| 11-22 18:16 | +15 | BNB | UP | 0.64 | 0.79 | 1.21 |
| 11-22 18:16 | +10 | BNB | UP | 0.65 | 0.78 | 1.01 |
