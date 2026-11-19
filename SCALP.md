# Range-Scalp Bot

*Updated Thu Nov 19 00:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64471 | 56237 | 8234 (124) | 0 | $-17553.82 | -4.3% |
| **+10¢** | 48164 | 38534 | 9630 (165) | 0 | $-16366.11 | -5.4% |
| **+15¢** | 40386 | 30006 | 10380 (210) | 0 | $-14785.22 | -5.8% |
| **+20¢** | 35963 | 25066 | 10897 (265) | 0 | $-13081.50 | -5.8% |
| **+10¢ (15¢ stop)** | 78430 | 78266 | 164 (98) | 0 | $-28849.97 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 00:07 | +10 stop | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 11-19 00:07 | +20 | NEAR | DOWN | 0.71 | 0.94 | 2.06 |
| 11-19 00:07 | +15 | NEAR | DOWN | 0.71 | 0.94 | 2.06 |
| 11-19 00:07 | +10 | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 11-19 00:07 | +5 | NEAR | DOWN | 0.71 | 0.80 | 0.63 |
| 11-19 00:05 | +5 | DOGE | DOWN | 0.71 | 0.80 | 0.63 |
| 11-19 00:04 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 11-19 00:04 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 11-19 00:04 | +20 | ETH | DOWN | 0.71 | 0.93 | 2.03 |
| 11-19 00:04 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 11-19 00:04 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 11-19 00:04 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-19 00:04 | +20 | ZEC | DOWN | 0.71 | 0.92 | 1.91 |
| 11-19 00:04 | +15 | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 11-19 00:04 | +10 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-19 00:04 | +5 | ZEC | DOWN | 0.71 | 0.79 | 0.53 |
| 11-19 00:03 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-19 00:03 | +20 | HYPE | DOWN | 0.69 | 0.90 | 1.88 |
| 11-19 00:03 | +15 | HYPE | DOWN | 0.70 | 0.86 | 1.36 |
| 11-19 00:03 | +10 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-19 00:03 | +5 | HYPE | DOWN | 0.69 | 0.78 | 0.62 |
| 11-18 23:56 | +10 stop | SOL | DOWN | 0.52 | 0.64 | 0.86 |
| 11-18 23:55 | +10 stop | BNB | DOWN | 0.69 | 0.81 | 0.94 |
| 11-18 23:54 | +10 stop | DOGE | DOWN | 0.56 | 0.74 | 1.48 |
| 11-18 23:54 | +10 stop | SOL | UP | 0.71 | 0.41 | -3.32 |
| 11-18 23:53 | +10 stop | SOL | UP | 0.71 | 0.55 | -1.93 |
| 11-18 23:53 | +10 stop | BNB | DOWN | 0.71 | 0.49 | -2.53 |
| 11-18 23:53 | +10 stop | DOGE | UP | 0.56 | 0.41 | -1.85 |
| 11-18 23:53 | +10 | DOGE | UP | 0.56 | no | -5.78 |
| 11-18 23:53 | +5 | DOGE | UP | 0.56 | no | -5.78 |
| 11-18 23:53 | +10 stop | ETH | UP | 0.54 | 0.24 | -3.31 |
| 11-18 23:53 | +10 stop | ZEC | UP | 0.54 | 0.27 | -3.02 |
| 11-18 23:53 | +20 | ZEC | UP | 0.54 | no | -5.58 |
| 11-18 23:53 | +15 | ZEC | UP | 0.55 | no | -5.68 |
| 11-18 23:53 | +10 | ZEC | UP | 0.56 | no | -5.78 |
| 11-18 23:53 | +5 | ZEC | UP | 0.56 | no | -5.78 |
| 11-18 23:52 | +10 stop | HYPE | UP | 0.52 | 0.64 | 0.85 |
| 11-18 23:52 | +10 stop | XRP | UP | 0.58 | 0.37 | -2.45 |
| 11-18 23:52 | +10 stop | HYPE | UP | 0.59 | 0.69 | 0.70 |
| 11-18 23:52 | +10 stop | DOGE | UP | 0.54 | 0.65 | 0.76 |
