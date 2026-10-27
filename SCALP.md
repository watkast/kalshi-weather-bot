# Range-Scalp Bot

*Updated Tue Oct 27 11:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36463 | 31839 | 4624 (43) | 0 | $-10096.31 | -4.4% |
| **+10¢** | 27248 | 21901 | 5347 (65) | 0 | $-8904.00 | -5.2% |
| **+15¢** | 22798 | 17059 | 5739 (89) | 0 | $-7834.25 | -5.5% |
| **+20¢** | 20201 | 14188 | 6013 (113) | 0 | $-6871.07 | -5.4% |
| **+10¢ (15¢ stop)** | 44691 | 44628 | 63 (33) | 0 | $-17054.32 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 11:24 | +10 stop | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-27 11:23 | +10 stop | XRP | DOWN | 0.71 | 0.89 | 1.58 |
| 10-27 11:23 | +10 stop | ETH | UP | 0.64 | 0.37 | -3.04 |
| 10-27 11:21 | +10 stop | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-27 11:21 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-27 11:21 | +15 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-27 11:21 | +10 | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-27 11:21 | +5 | ZEC | DOWN | 0.69 | 0.75 | 0.31 |
| 10-27 11:21 | +10 stop | ETH | DOWN | 0.57 | 0.41 | -1.95 |
| 10-27 11:21 | +10 stop | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-27 11:21 | +10 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-27 11:21 | +5 | BTC | DOWN | 0.64 | 0.73 | 0.59 |
| 10-27 11:20 | +10 stop | XRP | UP | 0.67 | 0.51 | -1.94 |
| 10-27 11:20 | +10 stop | HYPE | DOWN | 0.68 | 0.81 | 1.06 |
| 10-27 11:20 | +20 | HYPE | DOWN | 0.68 | 0.92 | 2.19 |
| 10-27 11:20 | +15 | HYPE | DOWN | 0.68 | 0.86 | 1.55 |
| 10-27 11:20 | +10 | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-27 11:20 | +5 | HYPE | DOWN | 0.69 | 0.76 | 0.42 |
| 10-27 11:20 | +10 stop | BTC | DOWN | 0.57 | 0.68 | 0.76 |
| 10-27 11:20 | +20 | BTC | DOWN | 0.57 | 0.79 | 1.90 |
| 10-27 11:20 | +15 | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 10-27 11:20 | +10 | BTC | DOWN | 0.56 | 0.68 | 0.86 |
| 10-27 11:20 | +5 | BTC | DOWN | 0.56 | 0.68 | 0.86 |
| 10-27 11:20 | +5 | SOL | DOWN | 0.65 | 0.74 | 0.60 |
| 10-27 11:19 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.49 |
| 10-27 11:18 | +10 stop | ETH | DOWN | 0.68 | 0.47 | -2.44 |
| 10-27 11:18 | +20 | ETH | DOWN | 0.68 | 0.89 | 1.85 |
| 10-27 11:18 | +15 | ETH | DOWN | 0.69 | 0.89 | 1.78 |
| 10-27 11:18 | +10 | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-27 11:18 | +5 | ETH | DOWN | 0.68 | 0.75 | 0.40 |
| 10-27 11:17 | +10 stop | BNB | DOWN | 0.62 | 0.76 | 1.10 |
| 10-27 11:17 | +20 | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 10-27 11:17 | +15 | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 10-27 11:17 | +10 | BNB | DOWN | 0.62 | 0.76 | 1.10 |
| 10-27 11:17 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 10-27 11:17 | +5 | XRP | DOWN | 0.61 | 0.68 | 0.37 |
| 10-27 11:17 | +10 stop | SOL | DOWN | 0.69 | 0.83 | 1.15 |
| 10-27 11:17 | +20 | SOL | DOWN | 0.70 | 0.91 | 1.88 |
| 10-27 11:17 | +15 | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 10-27 11:17 | +10 | SOL | DOWN | 0.70 | 0.83 | 1.05 |
