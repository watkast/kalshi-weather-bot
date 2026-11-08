# Range-Scalp Bot

*Updated Sun Nov 08 23:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52978 | 46193 | 6785 (85) | 1 | $-14644.97 | -4.4% |
| **+10¢** | 39549 | 31639 | 7910 (110) | 1 | $-13623.89 | -5.5% |
| **+15¢** | 33137 | 24614 | 8523 (141) | 1 | $-12443.61 | -6.0% |
| **+20¢** | 29477 | 20543 | 8934 (186) | 1 | $-10935.73 | -5.9% |
| **+10¢ (15¢ stop)** | 64516 | 64410 | 106 (63) | 0 | $-23896.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 23:34 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-08 23:34 | +10 | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 11-08 23:34 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 11-08 23:34 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.80 |
| 11-08 23:34 | +10 | XRP | DOWN | 0.70 | 0.81 | 0.80 |
| 11-08 23:34 | +10 stop | ZEC | DOWN | 0.69 | 0.85 | 1.37 |
| 11-08 23:34 | +5 | ZEC | DOWN | 0.68 | 0.77 | 0.61 |
| 11-08 23:33 | +5 | ETH | DOWN | 0.69 | 0.76 | 0.42 |
| 11-08 23:33 | +10 stop | BNB | UP | 0.49 | 0.32 | -2.04 |
| 11-08 23:33 | +10 stop | HYPE | UP | 0.52 | 0.35 | -2.04 |
| 11-08 23:33 | +10 stop | ZEC | UP | 0.59 | 0.36 | -2.61 |
| 11-08 23:32 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-08 23:32 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.20 |
| 11-08 23:31 | +5 | DOGE | DOWN | 0.68 | 0.74 | 0.30 |
| 11-08 23:31 | +10 stop | ZEC | DOWN | 0.60 | 0.42 | -2.15 |
| 11-08 23:31 | +20 | ZEC | DOWN | 0.59 | 0.85 | 2.34 |
| 11-08 23:31 | +15 | ZEC | DOWN | 0.56 | 0.77 | 1.79 |
| 11-08 23:31 | +10 | ZEC | DOWN | 0.56 | 0.66 | 0.66 |
| 11-08 23:31 | +5 | ZEC | DOWN | 0.56 | 0.62 | 0.25 |
| 11-08 23:31 | +5 | XRP | DOWN | 0.70 | 0.77 | 0.42 |
| 11-08 23:31 | +10 stop | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 11-08 23:31 | +20 | ETH | DOWN | 0.58 | 0.78 | 1.69 |
| 11-08 23:31 | +15 | ETH | DOWN | 0.58 | 0.76 | 1.49 |
| 11-08 23:31 | +10 | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 11-08 23:31 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.25 |
| 11-08 23:31 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.71 |
| 11-08 23:31 | +20 | NEAR | DOWN | 0.61 | 0.82 | 1.85 |
| 11-08 23:31 | +15 | NEAR | DOWN | 0.61 | 0.78 | 1.43 |
| 11-08 23:31 | +10 | NEAR | DOWN | 0.61 | 0.71 | 0.71 |
| 11-08 23:31 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.21 |
| 11-08 23:31 | +10 stop | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-08 23:31 | +20 | BTC | DOWN | 0.60 | 0.82 | 1.92 |
| 11-08 23:31 | +15 | BTC | DOWN | 0.60 | 0.77 | 1.40 |
| 11-08 23:31 | +10 | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-08 23:31 | +5 | BTC | DOWN | 0.60 | 0.66 | 0.27 |
| 11-08 23:31 | +10 stop | BNB | DOWN | 0.61 | 0.39 | -2.54 |
| 11-08 23:31 | +20 | BNB | DOWN | 0.61 | 0.83 | 1.93 |
| 11-08 23:31 | +15 | BNB | DOWN | 0.62 | 0.79 | 1.41 |
| 11-08 23:31 | +10 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-08 23:31 | +5 | BNB | DOWN | 0.62 | 0.69 | 0.38 |
