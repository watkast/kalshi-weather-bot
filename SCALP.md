# Range-Scalp Bot

*Updated Fri Oct 09 04:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8559 | 7404 | 1155 (13) | 0 | $-2801.78 | -5.2% |
| **+10¢** | 6478 | 5118 | 1360 (25) | 1 | $-2721.64 | -6.7% |
| **+15¢** | 5467 | 4037 | 1430 (37) | 1 | $-2186.21 | -6.4% |
| **+20¢** | 4864 | 3379 | 1485 (45) | 2 | $-1810.26 | -5.9% |
| **+10¢ (15¢ stop)** | 10413 | 10383 | 30 (19) | 0 | $-3853.76 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 04:50 | +5 | HYPE | DOWN | 0.65 | 0.72 | 0.35 |
| 10-09 04:49 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 10-09 04:47 | +5 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 10-09 04:47 | +10 stop | HYPE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-09 04:47 | +20 | HYPE | DOWN | 0.56 | open |  |
| 10-09 04:47 | +15 | HYPE | DOWN | 0.56 | 0.72 | 1.27 |
| 10-09 04:47 | +10 | HYPE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-09 04:47 | +5 | HYPE | DOWN | 0.56 | 0.61 | 0.15 |
| 10-09 04:47 | +10 stop | DOGE | DOWN | 0.51 | 0.62 | 0.75 |
| 10-09 04:47 | +20 | DOGE | DOWN | 0.52 | 0.82 | 2.71 |
| 10-09 04:47 | +15 | DOGE | DOWN | 0.56 | 0.82 | 2.31 |
| 10-09 04:47 | +10 | DOGE | DOWN | 0.56 | 0.69 | 0.97 |
| 10-09 04:47 | +5 | DOGE | DOWN | 0.56 | 0.62 | 0.25 |
| 10-09 04:47 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 10-09 04:47 | +20 | BNB | DOWN | 0.61 | 0.81 | 1.72 |
| 10-09 04:47 | +15 | BNB | DOWN | 0.61 | 0.77 | 1.30 |
| 10-09 04:47 | +10 | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 10-09 04:47 | +5 | BNB | DOWN | 0.61 | 0.69 | 0.48 |
| 10-09 04:47 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-09 04:47 | +20 | XRP | DOWN | 0.66 | 0.89 | 2.07 |
| 10-09 04:47 | +15 | XRP | DOWN | 0.66 | 0.81 | 1.27 |
| 10-09 04:47 | +10 | XRP | DOWN | 0.65 | 0.76 | 0.79 |
| 10-09 04:47 | +5 | XRP | DOWN | 0.65 | 0.76 | 0.79 |
| 10-09 04:47 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-09 04:47 | +20 | BTC | DOWN | 0.66 | 0.89 | 2.07 |
| 10-09 04:47 | +15 | BTC | DOWN | 0.65 | 0.84 | 1.64 |
| 10-09 04:47 | +10 | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-09 04:47 | +5 | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-09 04:46 | +10 stop | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-09 04:46 | +20 | ETH | DOWN | 0.66 | 0.88 | 1.96 |
| 10-09 04:46 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 10-09 04:46 | +10 | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-09 04:46 | +5 | ETH | DOWN | 0.66 | 0.74 | 0.50 |
| 10-09 04:46 | +10 stop | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-09 04:46 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-09 04:46 | +15 | ZEC | DOWN | 0.69 | 0.85 | 1.36 |
| 10-09 04:46 | +10 | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-09 04:46 | +5 | ZEC | DOWN | 0.69 | 0.76 | 0.42 |
| 10-09 04:46 | +5 | NEAR | DOWN | 0.67 | 0.73 | 0.30 |
| 10-09 04:45 | +10 stop | NEAR | UP | 0.49 | 0.33 | -1.94 |
