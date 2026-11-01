# Range-Scalp Bot

*Updated Sun Nov 01 11:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43559 | 37953 | 5606 (63) | 2 | $-12464.26 | -4.5% |
| **+10¢** | 32497 | 26023 | 6474 (85) | 1 | $-11175.91 | -5.5% |
| **+15¢** | 27201 | 20230 | 6971 (112) | 2 | $-10196.90 | -6.0% |
| **+20¢** | 24153 | 16851 | 7302 (146) | 2 | $-9011.50 | -5.9% |
| **+10¢ (15¢ stop)** | 53142 | 53057 | 85 (50) | 0 | $-20095.95 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 11:36 | +10 stop | HYPE | UP | 0.60 | 0.70 | 0.68 |
| 11-01 11:36 | +10 | HYPE | UP | 0.60 | 0.70 | 0.68 |
| 11-01 11:36 | +5 | HYPE | UP | 0.60 | 0.70 | 0.68 |
| 11-01 11:36 | +10 stop | DOGE | DOWN | 0.68 | 0.53 | -1.84 |
| 11-01 11:36 | +15 | DOGE | DOWN | 0.68 | open |  |
| 11-01 11:36 | +10 | DOGE | DOWN | 0.68 | open |  |
| 11-01 11:36 | +5 | DOGE | DOWN | 0.68 | open |  |
| 11-01 11:35 | +5 | ZEC | DOWN | 0.62 | open |  |
| 11-01 11:35 | +10 stop | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 11-01 11:35 | +10 | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 11-01 11:35 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-01 11:34 | +5 | NEAR | DOWN | 0.66 | 0.79 | 1.02 |
| 11-01 11:34 | +10 stop | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 11-01 11:34 | +15 | SOL | DOWN | 0.54 | 0.70 | 1.27 |
| 11-01 11:34 | +10 | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 11-01 11:34 | +5 | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 11-01 11:34 | +10 stop | ZEC | UP | 0.53 | 0.38 | -1.85 |
| 11-01 11:34 | +20 | ZEC | UP | 0.53 | 0.75 | 1.88 |
| 11-01 11:34 | +15 | ZEC | UP | 0.53 | 0.71 | 1.47 |
| 11-01 11:34 | +10 | ZEC | UP | 0.53 | 0.65 | 0.86 |
| 11-01 11:34 | +5 | ZEC | UP | 0.53 | 0.59 | 0.25 |
| 11-01 11:33 | +5 | NEAR | DOWN | 0.59 | 0.65 | 0.27 |
| 11-01 11:33 | +10 stop | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 11-01 11:33 | +20 | HYPE | DOWN | 0.62 | open |  |
| 11-01 11:33 | +15 | HYPE | DOWN | 0.61 | open |  |
| 11-01 11:33 | +10 | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 11-01 11:33 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.37 |
| 11-01 11:33 | +10 stop | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-01 11:33 | +15 | DOGE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-01 11:33 | +10 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-01 11:33 | +5 | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 11-01 11:33 | +10 stop | NEAR | DOWN | 0.56 | 0.79 | 2.00 |
| 11-01 11:33 | +15 | NEAR | DOWN | 0.56 | 0.79 | 2.00 |
| 11-01 11:33 | +10 | NEAR | DOWN | 0.56 | 0.79 | 2.00 |
| 11-01 11:33 | +5 | NEAR | DOWN | 0.56 | 0.64 | 0.45 |
| 11-01 11:31 | +10 stop | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 11-01 11:31 | +20 | ETH | DOWN | 0.69 | 0.89 | 1.78 |
| 11-01 11:31 | +15 | ETH | DOWN | 0.69 | 0.89 | 1.74 |
| 11-01 11:31 | +10 | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 11-01 11:31 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
