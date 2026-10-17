# Range-Scalp Bot

*Updated Sat Oct 17 05:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20448 | 17789 | 2659 (29) | 6 | $-6026.47 | -4.7% |
| **+10¢** | 15401 | 12334 | 3067 (41) | 6 | $-5359.67 | -5.5% |
| **+15¢** | 12881 | 9583 | 3298 (60) | 7 | $-4820.29 | -6.0% |
| **+20¢** | 11419 | 7964 | 3455 (79) | 8 | $-4268.05 | -6.0% |
| **+10¢ (15¢ stop)** | 25124 | 25074 | 50 (29) | 3 | $-9492.83 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 05:39 | +5 | DOGE | DOWN | 0.56 | open |  |
| 10-17 05:38 | +10 stop | ETH | DOWN | 0.69 | 0.48 | -2.43 |
| 10-17 05:38 | +10 stop | BTC | DOWN | 0.60 | open |  |
| 10-17 05:38 | +20 | BTC | DOWN | 0.60 | open |  |
| 10-17 05:38 | +15 | BTC | DOWN | 0.60 | open |  |
| 10-17 05:38 | +10 | BTC | DOWN | 0.60 | open |  |
| 10-17 05:38 | +5 | BTC | DOWN | 0.60 | open |  |
| 10-17 05:38 | +10 stop | XRP | UP | 0.52 | 0.66 | 1.06 |
| 10-17 05:38 | +5 | ETH | DOWN | 0.66 | open |  |
| 10-17 05:38 | +5 | DOGE | DOWN | 0.57 | 0.62 | 0.15 |
| 10-17 05:37 | +5 | NEAR | UP | 0.69 | 0.76 | 0.42 |
| 10-17 05:37 | +10 stop | HYPE | DOWN | 0.70 | 0.50 | -2.37 |
| 10-17 05:37 | +10 stop | DOGE | DOWN | 0.62 | open |  |
| 10-17 05:37 | +15 | DOGE | DOWN | 0.62 | open |  |
| 10-17 05:37 | +10 | DOGE | DOWN | 0.63 | open |  |
| 10-17 05:37 | +5 | DOGE | DOWN | 0.63 | 0.68 | 0.17 |
| 10-17 05:37 | +10 stop | ZEC | DOWN | 0.67 | open |  |
| 10-17 05:37 | +10 stop | XRP | DOWN | 0.63 | 0.44 | -2.25 |
| 10-17 05:37 | +20 | XRP | DOWN | 0.63 | open |  |
| 10-17 05:37 | +15 | XRP | DOWN | 0.63 | open |  |
| 10-17 05:37 | +10 | XRP | DOWN | 0.63 | open |  |
| 10-17 05:37 | +5 | XRP | DOWN | 0.63 | open |  |
| 10-17 05:37 | +10 stop | ETH | DOWN | 0.70 | 0.55 | -1.83 |
| 10-17 05:37 | +20 | ETH | DOWN | 0.70 | open |  |
| 10-17 05:37 | +15 | ETH | DOWN | 0.70 | open |  |
| 10-17 05:37 | +10 | ETH | DOWN | 0.70 | open |  |
| 10-17 05:37 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 10-17 05:36 | +10 stop | DOGE | DOWN | 0.50 | 0.67 | 1.36 |
| 10-17 05:36 | +15 | DOGE | DOWN | 0.50 | 0.67 | 1.36 |
| 10-17 05:36 | +10 | DOGE | DOWN | 0.50 | 0.67 | 1.36 |
| 10-17 05:36 | +5 | DOGE | DOWN | 0.50 | 0.67 | 1.36 |
| 10-17 05:36 | +10 stop | NEAR | UP | 0.63 | 0.76 | 1.00 |
| 10-17 05:36 | +20 | NEAR | UP | 0.63 | open |  |
| 10-17 05:36 | +15 | NEAR | UP | 0.63 | 0.79 | 1.31 |
| 10-17 05:36 | +10 | NEAR | UP | 0.63 | 0.76 | 1.00 |
| 10-17 05:36 | +5 | NEAR | UP | 0.63 | 0.72 | 0.58 |
| 10-17 05:36 | +10 stop | SOL | UP | 0.65 | 0.85 | 1.75 |
| 10-17 05:36 | +20 | SOL | UP | 0.65 | 0.85 | 1.75 |
| 10-17 05:36 | +15 | SOL | UP | 0.65 | 0.85 | 1.75 |
| 10-17 05:36 | +10 | SOL | UP | 0.65 | 0.85 | 1.75 |
