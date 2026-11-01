# Range-Scalp Bot

*Updated Sun Nov 01 02:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43098 | 37567 | 5531 (62) | 2 | $-12250.11 | -4.5% |
| **+10¢** | 32139 | 25748 | 6391 (84) | 2 | $-10977.44 | -5.4% |
| **+15¢** | 26886 | 19998 | 6888 (112) | 2 | $-10054.64 | -6.0% |
| **+20¢** | 23877 | 16663 | 7214 (146) | 3 | $-8866.69 | -5.9% |
| **+10¢ (15¢ stop)** | 52564 | 52481 | 83 (48) | 0 | $-19910.97 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 02:41 | +10 stop | ETH | UP | 0.59 | 0.43 | -1.95 |
| 11-01 02:41 | +10 stop | BNB | DOWN | 0.70 | 0.54 | -1.90 |
| 11-01 02:40 | +15 | ETH | UP | 0.60 | open |  |
| 11-01 02:40 | +10 | ETH | UP | 0.60 | open |  |
| 11-01 02:40 | +5 | ETH | UP | 0.60 | open |  |
| 11-01 02:39 | +10 stop | HYPE | DOWN | 0.56 | 0.70 | 1.07 |
| 11-01 02:39 | +15 | HYPE | DOWN | 0.56 | 0.72 | 1.27 |
| 11-01 02:39 | +10 | HYPE | DOWN | 0.56 | 0.70 | 1.07 |
| 11-01 02:39 | +5 | HYPE | DOWN | 0.56 | 0.70 | 1.07 |
| 11-01 02:39 | +10 stop | BTC | DOWN | 0.68 | 0.81 | 1.03 |
| 11-01 02:39 | +20 | BTC | DOWN | 0.68 | 0.92 | 2.15 |
| 11-01 02:39 | +15 | BTC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-01 02:39 | +10 | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-01 02:39 | +5 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-01 02:39 | +10 stop | ETH | UP | 0.66 | 0.44 | -2.54 |
| 11-01 02:39 | +10 stop | BNB | DOWN | 0.61 | 0.74 | 0.99 |
| 11-01 02:37 | +10 stop | BTC | DOWN | 0.71 | 0.87 | 1.37 |
| 11-01 02:37 | +10 | BTC | DOWN | 0.71 | 0.87 | 1.37 |
| 11-01 02:37 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 11-01 02:36 | +10 stop | ZEC | UP | 0.50 | 0.25 | -2.82 |
| 11-01 02:35 | +10 stop | ETH | DOWN | 0.63 | 0.42 | -2.45 |
| 11-01 02:35 | +10 stop | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-01 02:35 | +20 | BTC | DOWN | 0.62 | 0.87 | 2.25 |
| 11-01 02:35 | +15 | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-01 02:35 | +10 | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-01 02:35 | +5 | BTC | DOWN | 0.63 | 0.70 | 0.38 |
| 11-01 02:34 | +10 stop | ZEC | UP | 0.63 | 0.45 | -2.15 |
| 11-01 02:34 | +10 stop | HYPE | DOWN | 0.67 | 0.82 | 1.24 |
| 11-01 02:34 | +20 | HYPE | DOWN | 0.67 | 0.92 | 2.33 |
| 11-01 02:34 | +15 | HYPE | DOWN | 0.67 | 0.82 | 1.24 |
| 11-01 02:34 | +10 | HYPE | DOWN | 0.67 | 0.82 | 1.24 |
| 11-01 02:34 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.31 |
| 11-01 02:34 | +5 | BNB | UP | 0.61 | 0.74 | 0.99 |
| 11-01 02:34 | +5 | SOL | DOWN | 0.65 | 0.72 | 0.39 |
| 11-01 02:33 | +10 stop | ZEC | DOWN | 0.59 | 0.41 | -2.14 |
| 11-01 02:31 | +10 stop | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 11-01 02:31 | +20 | NEAR | DOWN | 0.69 | 0.89 | 1.78 |
| 11-01 02:31 | +15 | NEAR | DOWN | 0.69 | 0.84 | 1.25 |
| 11-01 02:31 | +10 | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 11-01 02:31 | +5 | NEAR | DOWN | 0.69 | 0.78 | 0.62 |
