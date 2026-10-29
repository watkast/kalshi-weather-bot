# Range-Scalp Bot

*Updated Thu Oct 29 00:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38744 | 33810 | 4934 (49) | 1 | $-10879.11 | -4.5% |
| **+10¢** | 28897 | 23199 | 5698 (71) | 1 | $-9643.62 | -5.3% |
| **+15¢** | 24173 | 18051 | 6122 (97) | 0 | $-8598.13 | -5.7% |
| **+20¢** | 21447 | 15036 | 6411 (125) | 1 | $-7497.14 | -5.6% |
| **+10¢ (15¢ stop)** | 47381 | 47314 | 67 (35) | 1 | $-17980.41 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 00:53 | +10 stop | BTC | DOWN | 0.71 | open |  |
| 10-29 00:53 | +10 | BTC | DOWN | 0.71 | open |  |
| 10-29 00:53 | +5 | BTC | DOWN | 0.71 | open |  |
| 10-29 00:51 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-29 00:51 | +15 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-29 00:51 | +10 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-29 00:51 | +5 | ZEC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-29 00:51 | +10 stop | XRP | DOWN | 0.69 | 0.84 | 1.25 |
| 10-29 00:51 | +15 | XRP | DOWN | 0.69 | 0.84 | 1.25 |
| 10-29 00:51 | +10 | XRP | DOWN | 0.69 | 0.84 | 1.25 |
| 10-29 00:51 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.30 |
| 10-29 00:50 | +5 | BTC | DOWN | 0.63 | 0.69 | 0.28 |
| 10-29 00:49 | +5 | ZEC | DOWN | 0.64 | 0.72 | 0.48 |
| 10-29 00:49 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-29 00:49 | +10 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-29 00:49 | +5 | SOL | DOWN | 0.63 | 0.70 | 0.38 |
| 10-29 00:48 | +5 | SOL | DOWN | 0.58 | 0.70 | 0.87 |
| 10-29 00:48 | +5 | XRP | DOWN | 0.57 | 0.71 | 1.07 |
| 10-29 00:47 | +10 stop | ETH | DOWN | 0.59 | 0.73 | 1.09 |
| 10-29 00:47 | +10 stop | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 10-29 00:47 | +20 | SOL | DOWN | 0.60 | 0.82 | 1.92 |
| 10-29 00:47 | +15 | SOL | DOWN | 0.60 | 0.75 | 1.19 |
| 10-29 00:47 | +10 | SOL | DOWN | 0.59 | 0.70 | 0.78 |
| 10-29 00:47 | +5 | SOL | DOWN | 0.60 | 0.65 | 0.17 |
| 10-29 00:46 | +10 stop | HYPE | DOWN | 0.66 | 0.80 | 1.12 |
| 10-29 00:46 | +20 | HYPE | DOWN | 0.66 | 0.86 | 1.75 |
| 10-29 00:46 | +15 | HYPE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-29 00:46 | +10 | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 10-29 00:46 | +5 | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 10-29 00:46 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-29 00:46 | +20 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 10-29 00:46 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-29 00:46 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-29 00:46 | +5 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-29 00:46 | +10 stop | NEAR | DOWN | 0.55 | 0.79 | 2.10 |
| 10-29 00:46 | +20 | NEAR | DOWN | 0.55 | 0.79 | 2.10 |
| 10-29 00:46 | +15 | NEAR | DOWN | 0.55 | 0.79 | 2.10 |
| 10-29 00:46 | +10 | NEAR | DOWN | 0.55 | 0.79 | 2.10 |
| 10-29 00:46 | +5 | NEAR | DOWN | 0.55 | 0.79 | 2.10 |
| 10-29 00:46 | +10 stop | BTC | DOWN | 0.59 | 0.69 | 0.68 |
