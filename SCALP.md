# Range-Scalp Bot

*Updated Wed Oct 14 20:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16469 | 14269 | 2200 (28) | 2 | $-5200.74 | -5.0% |
| **+10¢** | 12460 | 9911 | 2549 (40) | 4 | $-4770.58 | -6.1% |
| **+15¢** | 10471 | 7736 | 2735 (59) | 4 | $-4263.52 | -6.5% |
| **+20¢** | 9309 | 6441 | 2868 (76) | 5 | $-3782.47 | -6.5% |
| **+10¢ (15¢ stop)** | 20292 | 20242 | 50 (29) | 0 | $-7837.11 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 20:26 | +5 | NEAR | DOWN | 0.51 | 0.65 | 1.11 |
| 10-14 20:26 | +10 stop | NEAR | UP | 0.53 | 0.31 | -2.53 |
| 10-14 20:26 | +20 | NEAR | UP | 0.53 | open |  |
| 10-14 20:26 | +10 | NEAR | UP | 0.53 | open |  |
| 10-14 20:26 | +5 | NEAR | UP | 0.53 | 0.62 | 0.55 |
| 10-14 20:25 | +10 stop | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 10-14 20:25 | +5 | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 10-14 20:24 | +10 stop | HYPE | DOWN | 0.66 | 0.81 | 1.19 |
| 10-14 20:23 | +10 stop | ZEC | DOWN | 0.66 | 0.79 | 1.04 |
| 10-14 20:23 | +10 stop | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 10-14 20:23 | +15 | ETH | UP | 0.63 | open |  |
| 10-14 20:23 | +5 | ETH | UP | 0.63 | 0.69 | 0.28 |
| 10-14 20:23 | +10 stop | NEAR | UP | 0.68 | 0.80 | 0.92 |
| 10-14 20:23 | +15 | NEAR | UP | 0.68 | open |  |
| 10-14 20:23 | +10 | NEAR | UP | 0.68 | 0.80 | 0.92 |
| 10-14 20:23 | +5 | NEAR | UP | 0.68 | 0.73 | 0.20 |
| 10-14 20:21 | +10 | ZEC | UP | 0.71 | open |  |
| 10-14 20:21 | +5 | ZEC | UP | 0.71 | open |  |
| 10-14 20:21 | +10 stop | ETH | UP | 0.65 | 0.35 | -3.32 |
| 10-14 20:21 | +10 | ETH | UP | 0.65 | open |  |
| 10-14 20:21 | +10 stop | XRP | DOWN | 0.44 | 0.57 | 0.94 |
| 10-14 20:20 | +5 | ETH | UP | 0.65 | 0.72 | 0.39 |
| 10-14 20:20 | +10 stop | BNB | UP | 0.55 | 0.77 | 1.90 |
| 10-14 20:20 | +5 | BTC | UP | 0.65 | 0.76 | 0.81 |
| 10-14 20:20 | +10 stop | HYPE | DOWN | 0.58 | 0.71 | 0.93 |
| 10-14 20:19 | +10 stop | ZEC | UP | 0.68 | 0.45 | -2.64 |
| 10-14 20:19 | +5 | DOGE | UP | 0.60 | 0.66 | 0.27 |
| 10-14 20:19 | +10 stop | BTC | UP | 0.63 | 0.76 | 1.00 |
| 10-14 20:19 | +10 | BTC | UP | 0.63 | 0.76 | 1.00 |
| 10-14 20:19 | +10 stop | ETH | UP | 0.55 | 0.68 | 0.96 |
| 10-14 20:19 | +20 | ETH | UP | 0.55 | open |  |
| 10-14 20:19 | +15 | ETH | UP | 0.55 | 0.72 | 1.37 |
| 10-14 20:19 | +10 | ETH | UP | 0.55 | 0.68 | 0.96 |
| 10-14 20:19 | +5 | ETH | UP | 0.55 | 0.61 | 0.25 |
| 10-14 20:18 | +10 stop | NEAR | UP | 0.60 | 0.72 | 0.88 |
| 10-14 20:18 | +20 | NEAR | UP | 0.60 | 0.80 | 1.71 |
| 10-14 20:18 | +15 | NEAR | UP | 0.61 | 0.77 | 1.30 |
| 10-14 20:18 | +10 | NEAR | UP | 0.61 | 0.72 | 0.78 |
| 10-14 20:18 | +5 | NEAR | UP | 0.62 | 0.67 | 0.19 |
| 10-14 20:18 | +10 stop | SOL | UP | 0.63 | 0.80 | 1.41 |
