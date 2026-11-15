# Range-Scalp Bot

*Updated Sun Nov 15 03:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60237 | 52539 | 7698 (107) | 0 | $-16434.06 | -4.3% |
| **+10¢** | 45014 | 35994 | 9020 (143) | 1 | $-15517.67 | -5.5% |
| **+15¢** | 37713 | 27987 | 9726 (181) | 3 | $-14162.08 | -6.0% |
| **+20¢** | 33610 | 23407 | 10203 (233) | 5 | $-12475.39 | -5.9% |
| **+10¢ (15¢ stop)** | 73351 | 73208 | 143 (82) | 1 | $-27005.13 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 03:03 | +10 stop | NEAR | UP | 0.55 | open |  |
| 11-15 03:03 | +10 | NEAR | UP | 0.55 | open |  |
| 11-15 03:03 | +5 | NEAR | UP | 0.55 | 0.60 | 0.15 |
| 11-15 03:01 | +10 stop | ETH | UP | 0.66 | 0.79 | 1.02 |
| 11-15 03:01 | +20 | ETH | UP | 0.66 | open |  |
| 11-15 03:01 | +15 | ETH | UP | 0.67 | 0.82 | 1.23 |
| 11-15 03:01 | +10 | ETH | UP | 0.67 | 0.79 | 0.92 |
| 11-15 03:01 | +5 | ETH | UP | 0.66 | 0.79 | 1.02 |
| 11-15 03:01 | +10 stop | SOL | UP | 0.70 | 0.84 | 1.15 |
| 11-15 03:01 | +20 | SOL | UP | 0.70 | open |  |
| 11-15 03:01 | +15 | SOL | UP | 0.71 | open |  |
| 11-15 03:01 | +10 | SOL | UP | 0.71 | 0.84 | 1.05 |
| 11-15 03:01 | +10 stop | BNB | UP | 0.71 | 0.84 | 1.09 |
| 11-15 03:01 | +20 | BNB | UP | 0.69 | open |  |
| 11-15 03:01 | +15 | BNB | UP | 0.71 | open |  |
| 11-15 03:01 | +10 | BNB | UP | 0.71 | 0.84 | 1.09 |
| 11-15 03:01 | +5 | BNB | UP | 0.69 | 0.84 | 1.25 |
| 11-15 03:01 | +10 stop | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 11-15 03:01 | +20 | NEAR | UP | 0.68 | open |  |
| 11-15 03:01 | +15 | NEAR | UP | 0.68 | open |  |
| 11-15 03:01 | +10 | NEAR | UP | 0.67 | 0.79 | 0.92 |
| 11-15 03:01 | +5 | NEAR | UP | 0.67 | 0.79 | 0.92 |
| 11-15 03:01 | +10 stop | BTC | UP | 0.69 | 0.81 | 0.94 |
| 11-15 03:01 | +20 | BTC | UP | 0.69 | open |  |
| 11-15 03:01 | +15 | BTC | UP | 0.69 | 0.85 | 1.36 |
| 11-15 03:01 | +10 | BTC | UP | 0.70 | 0.81 | 0.84 |
| 11-15 03:01 | +5 | BTC | UP | 0.70 | 0.81 | 0.84 |
| 11-15 02:56 | +10 | SOL | UP | 0.66 | 0.83 | 1.44 |
| 11-15 02:56 | +5 | SOL | UP | 0.66 | 0.83 | 1.44 |
| 11-15 02:55 | +10 stop | ZEC | UP | 0.63 | 0.48 | -1.85 |
| 11-15 02:55 | +10 stop | NEAR | DOWN | 0.67 | 0.40 | -3.03 |
| 11-15 02:55 | +10 stop | SOL | UP | 0.71 | 0.83 | 0.95 |
| 11-15 02:54 | +10 stop | ETH | UP | 0.71 | 0.83 | 0.99 |
| 11-15 02:54 | +5 | ETH | UP | 0.71 | 0.79 | 0.57 |
| 11-15 02:53 | +20 | XRP | UP | 0.71 | 0.92 | 1.90 |
| 11-15 02:53 | +5 | ETH | UP | 0.60 | 0.66 | 0.27 |
| 11-15 02:53 | +10 stop | ZEC | DOWN | 0.61 | 0.45 | -1.93 |
| 11-15 02:53 | +20 | ZEC | DOWN | 0.60 | yes | -6.17 |
| 11-15 02:53 | +15 | ZEC | DOWN | 0.60 | yes | -6.17 |
| 11-15 02:53 | +10 | ZEC | DOWN | 0.60 | yes | -6.17 |
