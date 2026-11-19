# Range-Scalp Bot

*Updated Thu Nov 19 16:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65179 | 56896 | 8283 (124) | 1 | $-17451.14 | -4.3% |
| **+10¢** | 48672 | 38982 | 9690 (165) | 3 | $-16247.61 | -5.3% |
| **+15¢** | 40811 | 30357 | 10454 (211) | 2 | $-14651.39 | -5.7% |
| **+20¢** | 36341 | 25360 | 10981 (266) | 4 | $-12970.19 | -5.7% |
| **+10¢ (15¢ stop)** | 79342 | 79178 | 164 (98) | 0 | $-29202.49 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 16:28 | +15 | NEAR | DOWN | 0.68 | 0.99 | 2.97 |
| 11-19 16:28 | +10 | NEAR | DOWN | 0.68 | 0.81 | 1.03 |
| 11-19 16:28 | +5 | NEAR | DOWN | 0.65 | 0.73 | 0.50 |
| 11-19 16:28 | +10 stop | HYPE | DOWN | 0.43 | 0.60 | 1.35 |
| 11-19 16:28 | +10 | HYPE | DOWN | 0.43 | 0.60 | 1.35 |
| 11-19 16:28 | +5 | HYPE | DOWN | 0.43 | 0.60 | 1.35 |
| 11-19 16:28 | +10 stop | XRP | DOWN | 0.48 | 0.64 | 1.26 |
| 11-19 16:27 | +5 | ZEC | DOWN | 0.69 | 0.75 | 0.31 |
| 11-19 16:26 | +10 stop | ZEC | DOWN | 0.70 | 0.47 | -2.62 |
| 11-19 16:26 | +10 stop | DOGE | DOWN | 0.54 | 0.75 | 1.78 |
| 11-19 16:26 | +10 | DOGE | DOWN | 0.54 | 0.75 | 1.78 |
| 11-19 16:26 | +5 | DOGE | DOWN | 0.54 | 0.61 | 0.35 |
| 11-19 16:26 | +10 stop | HYPE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-19 16:26 | +10 stop | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-19 16:26 | +5 | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-19 16:25 | +10 stop | BNB | UP | 0.37 | 0.52 | 1.15 |
| 11-19 16:25 | +15 | BNB | UP | 0.37 | 0.52 | 1.15 |
| 11-19 16:25 | +10 | BNB | UP | 0.37 | 0.52 | 1.15 |
| 11-19 16:25 | +5 | BNB | UP | 0.35 | 0.52 | 1.36 |
| 11-19 16:25 | +5 | BTC | UP | 0.60 | 0.66 | 0.27 |
| 11-19 16:25 | +10 stop | HYPE | UP | 0.59 | 0.33 | -2.93 |
| 11-19 16:24 | +10 stop | XRP | UP | 0.68 | 0.38 | -3.33 |
| 11-19 16:24 | +15 | XRP | UP | 0.68 | open |  |
| 11-19 16:24 | +5 | XRP | UP | 0.68 | 0.75 | 0.40 |
| 11-19 16:24 | +10 stop | SOL | DOWN | 0.59 | 0.85 | 2.34 |
| 11-19 16:24 | +20 | SOL | DOWN | 0.59 | 0.85 | 2.34 |
| 11-19 16:24 | +10 stop | ZEC | UP | 0.69 | 0.48 | -2.43 |
| 11-19 16:24 | +10 | BTC | UP | 0.60 | open |  |
| 11-19 16:24 | +5 | BTC | UP | 0.60 | 0.66 | 0.27 |
| 11-19 16:24 | +10 stop | NEAR | UP | 0.51 | 0.36 | -1.90 |
| 11-19 16:23 | +10 stop | ETH | DOWN | 0.37 | 0.58 | 1.75 |
| 11-19 16:23 | +10 stop | NEAR | UP | 0.44 | 0.56 | 0.84 |
| 11-19 16:23 | +10 stop | ZEC | UP | 0.54 | 0.68 | 1.06 |
| 11-19 16:22 | +10 stop | NEAR | DOWN | 0.60 | 0.37 | -2.64 |
| 11-19 16:22 | +10 | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 11-19 16:22 | +5 | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 11-19 16:22 | +5 | BNB | UP | 0.69 | 0.75 | 0.31 |
| 11-19 16:22 | +10 stop | DOGE | UP | 0.60 | 0.76 | 1.30 |
| 11-19 16:22 | +5 | DOGE | UP | 0.59 | 0.76 | 1.40 |
| 11-19 16:22 | +10 stop | BTC | UP | 0.61 | 0.37 | -2.74 |
