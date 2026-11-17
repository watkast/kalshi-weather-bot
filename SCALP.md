# Range-Scalp Bot

*Updated Tue Nov 17 14:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62880 | 54849 | 8031 (117) | 1 | $-17117.68 | -4.3% |
| **+10¢** | 46963 | 37566 | 9397 (159) | 1 | $-15992.07 | -5.4% |
| **+15¢** | 39363 | 29228 | 10135 (201) | 1 | $-14537.12 | -5.9% |
| **+20¢** | 35076 | 24448 | 10628 (256) | 3 | $-12716.78 | -5.8% |
| **+10¢ (15¢ stop)** | 76523 | 76367 | 156 (92) | 0 | $-28209.39 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 14:23 | +10 stop | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-17 14:23 | +5 | BNB | DOWN | 0.65 | 0.71 | 0.29 |
| 11-17 14:22 | +10 | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 11-17 14:22 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 11-17 14:22 | +10 stop | BNB | DOWN | 0.63 | 0.79 | 1.31 |
| 11-17 14:22 | +10 | BNB | DOWN | 0.63 | 0.79 | 1.31 |
| 11-17 14:22 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 11-17 14:22 | +10 stop | NEAR | DOWN | 0.63 | 0.74 | 0.80 |
| 11-17 14:22 | +10 stop | HYPE | UP | 0.47 | 0.32 | -1.84 |
| 11-17 14:21 | +10 | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-17 14:21 | +10 stop | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-17 14:21 | +10 stop | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-17 14:21 | +5 | SOL | DOWN | 0.70 | 0.75 | 0.21 |
| 11-17 14:21 | +5 | ZEC | UP | 0.69 | 0.76 | 0.42 |
| 11-17 14:21 | +15 | HYPE | UP | 0.49 | open |  |
| 11-17 14:20 | +10 stop | NEAR | UP | 0.67 | 0.50 | -2.04 |
| 11-17 14:20 | +10 stop | XRP | UP | 0.58 | 0.29 | -3.20 |
| 11-17 14:20 | +10 stop | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 11-17 14:20 | +10 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 11-17 14:20 | +10 stop | SOL | UP | 0.63 | 0.36 | -3.04 |
| 11-17 14:20 | +10 stop | XRP | DOWN | 0.48 | 0.59 | 0.78 |
| 11-17 14:19 | +10 stop | NEAR | UP | 0.57 | 0.68 | 0.76 |
| 11-17 14:19 | +10 stop | HYPE | UP | 0.70 | 0.48 | -2.53 |
| 11-17 14:19 | +10 | HYPE | UP | 0.71 | open |  |
| 11-17 14:19 | +10 stop | BTC | UP | 0.57 | 0.36 | -2.45 |
| 11-17 14:18 | +10 stop | BNB | UP | 0.50 | 0.31 | -2.23 |
| 11-17 14:18 | +5 | BNB | UP | 0.50 | 0.56 | 0.24 |
| 11-17 14:18 | +10 stop | XRP | UP | 0.60 | 0.43 | -2.05 |
| 11-17 14:18 | +5 | HYPE | UP | 0.69 | open |  |
| 11-17 14:18 | +10 stop | SOL | UP | 0.70 | 0.54 | -1.93 |
| 11-17 14:17 | +5 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-17 14:17 | +10 stop | NEAR | DOWN | 0.56 | 0.40 | -1.95 |
| 11-17 14:17 | +20 | NEAR | DOWN | 0.56 | 0.77 | 1.79 |
| 11-17 14:17 | +15 | NEAR | DOWN | 0.56 | 0.74 | 1.48 |
| 11-17 14:17 | +10 | NEAR | DOWN | 0.56 | 0.69 | 0.97 |
| 11-17 14:17 | +5 | NEAR | DOWN | 0.56 | 0.63 | 0.35 |
| 11-17 14:17 | +5 | ETH | DOWN | 0.70 | 0.77 | 0.42 |
| 11-17 14:17 | +10 stop | XRP | DOWN | 0.68 | 0.40 | -3.10 |
| 11-17 14:17 | +20 | XRP | DOWN | 0.68 | open |  |
| 11-17 14:17 | +15 | XRP | DOWN | 0.68 | 0.83 | 1.27 |
