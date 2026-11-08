# Range-Scalp Bot

*Updated Sun Nov 08 20:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52794 | 46029 | 6765 (83) | 4 | $-14615.24 | -4.4% |
| **+10¢** | 39413 | 31530 | 7883 (108) | 7 | $-13592.84 | -5.5% |
| **+15¢** | 33020 | 24528 | 8492 (139) | 7 | $-12411.35 | -6.0% |
| **+20¢** | 29371 | 20469 | 8902 (184) | 7 | $-10910.08 | -5.9% |
| **+10¢ (15¢ stop)** | 64296 | 64190 | 106 (63) | 0 | $-23799.98 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 20:37 | +10 stop | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 11-08 20:35 | +10 stop | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 11-08 20:35 | +10 stop | DOGE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-08 20:35 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-08 20:34 | +10 stop | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-08 20:33 | +10 stop | DOGE | UP | 0.50 | 0.30 | -2.33 |
| 11-08 20:33 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-08 20:33 | +10 stop | NEAR | DOWN | 0.66 | 0.80 | 1.15 |
| 11-08 20:33 | +5 | NEAR | DOWN | 0.66 | 0.75 | 0.63 |
| 11-08 20:33 | +10 stop | ETH | DOWN | 0.45 | 0.62 | 1.35 |
| 11-08 20:32 | +5 | BTC | DOWN | 0.70 | 0.77 | 0.42 |
| 11-08 20:32 | +10 stop | BNB | DOWN | 0.55 | 0.66 | 0.76 |
| 11-08 20:32 | +5 | NEAR | DOWN | 0.58 | 0.65 | 0.36 |
| 11-08 20:32 | +10 stop | SOL | UP | 0.66 | 0.37 | -3.23 |
| 11-08 20:32 | +20 | SOL | UP | 0.66 | open |  |
| 11-08 20:32 | +15 | SOL | UP | 0.66 | open |  |
| 11-08 20:32 | +10 | SOL | UP | 0.66 | open |  |
| 11-08 20:32 | +5 | SOL | UP | 0.65 | open |  |
| 11-08 20:32 | +10 stop | ZEC | DOWN | 0.59 | 0.78 | 1.60 |
| 11-08 20:32 | +20 | ZEC | DOWN | 0.59 | 0.79 | 1.71 |
| 11-08 20:32 | +15 | ZEC | DOWN | 0.59 | 0.78 | 1.60 |
| 11-08 20:32 | +10 | ZEC | DOWN | 0.59 | 0.78 | 1.60 |
| 11-08 20:32 | +5 | ZEC | DOWN | 0.59 | 0.78 | 1.60 |
| 11-08 20:32 | +5 | XRP | DOWN | 0.60 | 0.67 | 0.37 |
| 11-08 20:31 | +10 stop | HYPE | DOWN | 0.63 | 0.48 | -1.85 |
| 11-08 20:31 | +20 | HYPE | DOWN | 0.63 | 0.87 | 2.15 |
| 11-08 20:31 | +15 | HYPE | DOWN | 0.63 | 0.81 | 1.52 |
| 11-08 20:31 | +10 | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-08 20:31 | +5 | HYPE | DOWN | 0.63 | 0.70 | 0.38 |
| 11-08 20:31 | +10 stop | DOGE | UP | 0.59 | 0.44 | -1.85 |
| 11-08 20:31 | +20 | DOGE | UP | 0.59 | open |  |
| 11-08 20:31 | +15 | DOGE | UP | 0.59 | open |  |
| 11-08 20:31 | +10 | DOGE | UP | 0.59 | open |  |
| 11-08 20:31 | +5 | DOGE | UP | 0.59 | open |  |
| 11-08 20:31 | +10 stop | NEAR | UP | 0.51 | 0.34 | -2.04 |
| 11-08 20:31 | +20 | NEAR | UP | 0.51 | open |  |
| 11-08 20:31 | +15 | NEAR | UP | 0.51 | open |  |
| 11-08 20:31 | +10 | NEAR | UP | 0.51 | open |  |
| 11-08 20:31 | +5 | NEAR | UP | 0.51 | 0.58 | 0.34 |
| 11-08 20:31 | +10 stop | BTC | UP | 0.47 | 0.31 | -1.93 |
