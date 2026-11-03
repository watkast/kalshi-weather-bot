# Range-Scalp Bot

*Updated Tue Nov 03 01:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45409 | 39532 | 5877 (67) | 6 | $-13176.69 | -4.6% |
| **+10¢** | 33895 | 27087 | 6808 (89) | 6 | $-12045.96 | -5.7% |
| **+15¢** | 28352 | 21028 | 7324 (116) | 6 | $-11083.20 | -6.2% |
| **+20¢** | 25178 | 17507 | 7671 (151) | 7 | $-9858.91 | -6.2% |
| **+10¢ (15¢ stop)** | 55426 | 55339 | 87 (51) | 1 | $-20938.08 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 01:26 | +10 stop | NEAR | UP | 0.63 | 0.81 | 1.52 |
| 11-03 01:24 | +10 stop | SOL | UP | 0.63 | open |  |
| 11-03 01:24 | +10 | SOL | UP | 0.63 | open |  |
| 11-03 01:24 | +10 stop | NEAR | DOWN | 0.67 | 0.46 | -2.44 |
| 11-03 01:24 | +5 | SOL | UP | 0.70 | open |  |
| 11-03 01:23 | +10 stop | SOL | UP | 0.59 | 0.69 | 0.68 |
| 11-03 01:23 | +15 | SOL | UP | 0.59 | open |  |
| 11-03 01:23 | +10 | SOL | UP | 0.57 | 0.69 | 0.87 |
| 11-03 01:23 | +5 | SOL | UP | 0.57 | 0.63 | 0.25 |
| 11-03 01:22 | +10 stop | BTC | UP | 0.70 | 0.82 | 0.94 |
| 11-03 01:21 | +10 stop | NEAR | DOWN | 0.59 | 0.74 | 1.19 |
| 11-03 01:21 | +10 stop | ZEC | UP | 0.66 | 0.83 | 1.44 |
| 11-03 01:20 | +10 stop | SOL | UP | 0.58 | 0.72 | 1.07 |
| 11-03 01:20 | +15 | SOL | UP | 0.58 | 0.74 | 1.28 |
| 11-03 01:20 | +10 | SOL | UP | 0.58 | 0.72 | 1.07 |
| 11-03 01:20 | +5 | SOL | UP | 0.58 | 0.72 | 1.07 |
| 11-03 01:20 | +5 | NEAR | UP | 0.60 | 0.67 | 0.37 |
| 11-03 01:18 | +10 stop | BTC | UP | 0.59 | 0.69 | 0.68 |
| 11-03 01:18 | +10 stop | ZEC | UP | 0.69 | 0.52 | -2.03 |
| 11-03 01:18 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.88 |
| 11-03 01:17 | +10 stop | ETH | UP | 0.62 | 0.79 | 1.41 |
| 11-03 01:17 | +20 | ETH | UP | 0.62 | 0.83 | 1.83 |
| 11-03 01:17 | +15 | ETH | UP | 0.62 | 0.79 | 1.41 |
| 11-03 01:17 | +10 | ETH | UP | 0.62 | 0.79 | 1.41 |
| 11-03 01:17 | +5 | ETH | UP | 0.62 | 0.70 | 0.48 |
| 11-03 01:17 | +10 stop | BNB | UP | 0.71 | 0.83 | 0.95 |
| 11-03 01:16 | +10 stop | NEAR | UP | 0.66 | 0.45 | -2.44 |
| 11-03 01:16 | +20 | NEAR | UP | 0.66 | open |  |
| 11-03 01:16 | +15 | NEAR | UP | 0.66 | 0.81 | 1.23 |
| 11-03 01:16 | +10 | NEAR | UP | 0.66 | 0.81 | 1.23 |
| 11-03 01:16 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 11-03 01:16 | +10 stop | DOGE | UP | 0.66 | 0.77 | 0.81 |
| 11-03 01:16 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 11-03 01:16 | +20 | SOL | UP | 0.64 | open |  |
| 11-03 01:16 | +15 | SOL | UP | 0.64 | 0.82 | 1.52 |
| 11-03 01:16 | +10 | SOL | UP | 0.64 | 0.76 | 0.90 |
| 11-03 01:16 | +5 | SOL | UP | 0.64 | 0.72 | 0.48 |
| 11-03 01:16 | +10 stop | HYPE | UP | 0.66 | 0.77 | 0.81 |
| 11-03 01:16 | +20 | HYPE | UP | 0.66 | 0.89 | 2.07 |
| 11-03 01:16 | +15 | HYPE | UP | 0.66 | 0.81 | 1.23 |
