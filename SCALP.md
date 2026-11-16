# Range-Scalp Bot

*Updated Mon Nov 16 19:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62132 | 54215 | 7917 (117) | 4 | $-16740.20 | -4.3% |
| **+10¢** | 46397 | 37133 | 9264 (159) | 5 | $-15601.01 | -5.3% |
| **+15¢** | 38877 | 28883 | 9994 (200) | 4 | $-14196.96 | -5.8% |
| **+20¢** | 34654 | 24175 | 10479 (255) | 6 | $-12359.20 | -5.7% |
| **+10¢ (15¢ stop)** | 75635 | 75479 | 156 (92) | 0 | $-27925.36 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 19:28 | +10 stop | XRP | DOWN | 0.35 | 0.55 | 1.66 |
| 11-16 19:28 | +10 stop | SOL | DOWN | 0.47 | 0.65 | 1.46 |
| 11-16 19:28 | +20 | SOL | DOWN | 0.48 | open |  |
| 11-16 19:28 | +15 | SOL | DOWN | 0.48 | 0.65 | 1.38 |
| 11-16 19:28 | +10 | SOL | DOWN | 0.48 | 0.65 | 1.38 |
| 11-16 19:28 | +5 | SOL | DOWN | 0.43 | 0.65 | 1.86 |
| 11-16 19:26 | +10 stop | BTC | UP | 0.40 | 0.58 | 1.45 |
| 11-16 19:25 | +10 stop | BNB | UP | 0.69 | 0.83 | 1.15 |
| 11-16 19:25 | +5 | BNB | UP | 0.70 | 0.83 | 1.05 |
| 11-16 19:25 | +10 stop | ZEC | UP | 0.62 | 0.42 | -2.35 |
| 11-16 19:24 | +10 stop | BTC | DOWN | 0.59 | 0.41 | -2.14 |
| 11-16 19:24 | +10 stop | SOL | UP | 0.70 | 0.83 | 1.05 |
| 11-16 19:24 | +10 stop | DOGE | UP | 0.70 | 0.83 | 1.05 |
| 11-16 19:24 | +10 stop | ZEC | DOWN | 0.59 | 0.43 | -1.95 |
| 11-16 19:24 | +5 | ZEC | DOWN | 0.58 | 0.83 | 2.18 |
| 11-16 19:24 | +5 | SOL | UP | 0.70 | 0.76 | 0.32 |
| 11-16 19:23 | +10 stop | ETH | UP | 0.51 | 0.61 | 0.65 |
| 11-16 19:23 | +10 stop | XRP | UP | 0.64 | 0.78 | 1.10 |
| 11-16 19:23 | +10 stop | ETH | DOWN | 0.50 | 0.34 | -1.94 |
| 11-16 19:23 | +10 stop | DOGE | DOWN | 0.45 | 0.25 | -2.32 |
| 11-16 19:23 | +10 stop | ZEC | DOWN | 0.61 | 0.43 | -2.15 |
| 11-16 19:23 | +15 | ZEC | DOWN | 0.61 | 0.83 | 1.93 |
| 11-16 19:23 | +10 | ZEC | DOWN | 0.61 | 0.83 | 1.93 |
| 11-16 19:23 | +5 | ZEC | DOWN | 0.61 | 0.68 | 0.37 |
| 11-16 19:23 | +10 stop | SOL | DOWN | 0.43 | 0.56 | 0.95 |
| 11-16 19:22 | +15 | NEAR | DOWN | 0.60 | open |  |
| 11-16 19:22 | +10 | NEAR | DOWN | 0.60 | open |  |
| 11-16 19:22 | +5 | NEAR | DOWN | 0.60 | open |  |
| 11-16 19:22 | +10 | XRP | DOWN | 0.65 | open |  |
| 11-16 19:22 | +5 | XRP | DOWN | 0.65 | open |  |
| 11-16 19:22 | +10 | BTC | DOWN | 0.69 | open |  |
| 11-16 19:22 | +5 | BTC | DOWN | 0.68 | 0.76 | 0.51 |
| 11-16 19:21 | +10 stop | BNB | DOWN | 0.64 | 0.40 | -2.74 |
| 11-16 19:21 | +10 stop | DOGE | DOWN | 0.69 | 0.48 | -2.40 |
| 11-16 19:21 | +5 | DOGE | DOWN | 0.68 | open |  |
| 11-16 19:21 | +10 stop | ETH | DOWN | 0.62 | 0.45 | -2.05 |
| 11-16 19:21 | +10 | ETH | DOWN | 0.62 | open |  |
| 11-16 19:21 | +5 | ETH | DOWN | 0.62 | open |  |
| 11-16 19:21 | +5 | BTC | DOWN | 0.58 | 0.65 | 0.36 |
| 11-16 19:21 | +10 stop | BNB | DOWN | 0.50 | 0.60 | 0.65 |
