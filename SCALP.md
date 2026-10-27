# Range-Scalp Bot

*Updated Tue Oct 27 13:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36634 | 31992 | 4642 (43) | 0 | $-10125.25 | -4.4% |
| **+10¢** | 27371 | 22001 | 5370 (65) | 0 | $-8941.48 | -5.2% |
| **+15¢** | 22900 | 17137 | 5763 (89) | 0 | $-7858.79 | -5.5% |
| **+20¢** | 20295 | 14260 | 6035 (113) | 1 | $-6859.92 | -5.4% |
| **+10¢ (15¢ stop)** | 44882 | 44819 | 63 (33) | 0 | $-17108.94 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 13:49 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.19 |
| 10-27 13:49 | +5 | XRP | DOWN | 0.65 | 0.73 | 0.50 |
| 10-27 13:48 | +10 stop | BTC | DOWN | 0.53 | 0.65 | 0.86 |
| 10-27 13:48 | +10 | BTC | DOWN | 0.53 | 0.65 | 0.86 |
| 10-27 13:48 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 10-27 13:47 | +10 stop | HYPE | DOWN | 0.66 | 0.80 | 1.08 |
| 10-27 13:47 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-27 13:47 | +5 | BTC | DOWN | 0.68 | 0.76 | 0.51 |
| 10-27 13:47 | +10 stop | DOGE | DOWN | 0.66 | 0.49 | -2.03 |
| 10-27 13:47 | +10 | DOGE | DOWN | 0.66 | 0.76 | 0.72 |
| 10-27 13:47 | +5 | DOGE | DOWN | 0.66 | 0.76 | 0.72 |
| 10-27 13:46 | +10 stop | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 10-27 13:46 | +20 | NEAR | DOWN | 0.64 | 0.89 | 2.26 |
| 10-27 13:46 | +15 | NEAR | DOWN | 0.64 | 0.80 | 1.31 |
| 10-27 13:46 | +10 | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 10-27 13:46 | +5 | NEAR | DOWN | 0.64 | 0.71 | 0.38 |
| 10-27 13:46 | +10 stop | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 10-27 13:46 | +20 | XRP | DOWN | 0.69 | 0.90 | 1.89 |
| 10-27 13:46 | +15 | XRP | DOWN | 0.69 | 0.90 | 1.89 |
| 10-27 13:46 | +10 | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 10-27 13:46 | +5 | XRP | DOWN | 0.69 | 0.75 | 0.31 |
| 10-27 13:46 | +10 stop | BNB | DOWN | 0.66 | 0.84 | 1.54 |
| 10-27 13:46 | +20 | BNB | DOWN | 0.66 | 0.87 | 1.86 |
| 10-27 13:46 | +15 | BNB | DOWN | 0.66 | 0.84 | 1.54 |
| 10-27 13:46 | +10 | BNB | DOWN | 0.66 | 0.84 | 1.54 |
| 10-27 13:46 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.19 |
| 10-27 13:46 | +10 stop | ETH | DOWN | 0.68 | 0.53 | -1.84 |
| 10-27 13:46 | +20 | ETH | DOWN | 0.68 | open |  |
| 10-27 13:46 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-27 13:46 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-27 13:46 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.20 |
| 10-27 13:46 | +10 stop | BTC | DOWN | 0.57 | 0.68 | 0.76 |
| 10-27 13:46 | +20 | BTC | DOWN | 0.57 | 0.84 | 2.42 |
| 10-27 13:46 | +15 | BTC | DOWN | 0.57 | 0.76 | 1.59 |
| 10-27 13:46 | +10 | BTC | DOWN | 0.57 | 0.68 | 0.76 |
| 10-27 13:46 | +5 | BTC | DOWN | 0.57 | 0.66 | 0.56 |
| 10-27 13:46 | +10 stop | ZEC | DOWN | 0.58 | 0.72 | 1.07 |
| 10-27 13:46 | +20 | ZEC | DOWN | 0.58 | 0.89 | 2.85 |
| 10-27 13:46 | +15 | ZEC | DOWN | 0.58 | 0.73 | 1.18 |
| 10-27 13:46 | +10 | ZEC | DOWN | 0.58 | 0.72 | 1.07 |
