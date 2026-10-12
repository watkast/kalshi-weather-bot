# Range-Scalp Bot

*Updated Mon Oct 12 08:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13265 | 11463 | 1802 (25) | 0 | $-4326.45 | -5.2% |
| **+10¢** | 10051 | 7964 | 2087 (37) | 1 | $-4038.32 | -6.4% |
| **+15¢** | 8455 | 6225 | 2230 (55) | 1 | $-3556.05 | -6.7% |
| **+20¢** | 7530 | 5205 | 2325 (70) | 1 | $-3024.37 | -6.4% |
| **+10¢ (15¢ stop)** | 16340 | 16299 | 41 (25) | 0 | $-6408.22 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 08:02 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.42 |
| 10-12 08:01 | +10 stop | NEAR | UP | 0.47 | 0.29 | -2.17 |
| 10-12 08:01 | +20 | NEAR | UP | 0.48 | open |  |
| 10-12 08:01 | +15 | NEAR | UP | 0.48 | open |  |
| 10-12 08:01 | +10 | NEAR | UP | 0.48 | open |  |
| 10-12 08:01 | +5 | NEAR | UP | 0.48 | 0.54 | 0.24 |
| 10-12 08:01 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-12 08:01 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.94 |
| 10-12 08:01 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 10-12 08:01 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-12 08:01 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 10-12 08:01 | +10 stop | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-12 08:01 | +20 | ZEC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-12 08:01 | +15 | ZEC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-12 08:01 | +10 | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-12 08:01 | +5 | ZEC | DOWN | 0.63 | 0.74 | 0.78 |
| 10-12 08:01 | +10 stop | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-12 08:01 | +20 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 10-12 08:01 | +15 | SOL | DOWN | 0.68 | 0.83 | 1.24 |
| 10-12 08:01 | +10 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-12 08:01 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 10-12 07:57 | +10 stop | XRP | DOWN | 0.59 | 0.82 | 2.02 |
| 10-12 07:57 | +10 stop | BNB | DOWN | 0.63 | 0.86 | 2.01 |
| 10-12 07:57 | +15 | BNB | DOWN | 0.63 | 0.86 | 2.01 |
| 10-12 07:57 | +10 stop | XRP | UP | 0.62 | 0.44 | -2.15 |
| 10-12 07:56 | +10 stop | SOL | UP | 0.49 | 0.28 | -2.43 |
| 10-12 07:56 | +5 | BNB | UP | 0.61 | no | -6.27 |
| 10-12 07:56 | +10 stop | NEAR | UP | 0.55 | 0.39 | -1.95 |
| 10-12 07:56 | +10 stop | ETH | DOWN | 0.62 | 0.81 | 1.62 |
| 10-12 07:55 | +20 | ETH | DOWN | 0.62 | 0.86 | 2.14 |
| 10-12 07:55 | +5 | ETH | DOWN | 0.62 | 0.70 | 0.48 |
| 10-12 07:55 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 10-12 07:55 | +10 stop | NEAR | DOWN | 0.54 | 0.33 | -2.44 |
| 10-12 07:55 | +10 | NEAR | DOWN | 0.54 | 0.65 | 0.76 |
| 10-12 07:55 | +5 | NEAR | DOWN | 0.54 | 0.59 | 0.15 |
| 10-12 07:55 | +10 stop | XRP | UP | 0.64 | 0.84 | 1.73 |
| 10-12 07:55 | +10 stop | BNB | UP | 0.55 | 0.31 | -2.73 |
| 10-12 07:55 | +5 | BNB | UP | 0.55 | 0.64 | 0.55 |
| 10-12 07:54 | +10 stop | XRP | UP | 0.60 | 0.71 | 0.78 |
| 10-12 07:54 | +10 stop | BNB | UP | 0.51 | 0.61 | 0.65 |
