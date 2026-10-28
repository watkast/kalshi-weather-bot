# Range-Scalp Bot

*Updated Wed Oct 28 13:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38146 | 33285 | 4861 (46) | 4 | $-10740.89 | -4.5% |
| **+10¢** | 28454 | 22833 | 5621 (68) | 4 | $-9576.36 | -5.3% |
| **+15¢** | 23805 | 17770 | 6035 (93) | 4 | $-8523.62 | -5.7% |
| **+20¢** | 21115 | 14794 | 6321 (118) | 4 | $-7494.55 | -5.7% |
| **+10¢ (15¢ stop)** | 46704 | 46637 | 67 (35) | 0 | $-17760.59 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 13:11 | +10 stop | NEAR | UP | 0.71 | 0.85 | 1.16 |
| 10-28 13:11 | +20 | NEAR | UP | 0.71 | 0.93 | 2.04 |
| 10-28 13:11 | +10 | NEAR | UP | 0.71 | 0.85 | 1.16 |
| 10-28 13:11 | +5 | NEAR | UP | 0.71 | 0.85 | 1.16 |
| 10-28 13:10 | +5 | BTC | DOWN | 0.71 | 0.78 | 0.42 |
| 10-28 13:09 | +10 stop | XRP | UP | 0.41 | 0.59 | 1.46 |
| 10-28 13:09 | +10 stop | DOGE | UP | 0.44 | 0.61 | 1.35 |
| 10-28 13:09 | +10 stop | ZEC | UP | 0.50 | 0.24 | -2.91 |
| 10-28 13:09 | +5 | BTC | DOWN | 0.53 | 0.67 | 1.06 |
| 10-28 13:09 | +10 stop | XRP | DOWN | 0.53 | 0.38 | -1.85 |
| 10-28 13:09 | +10 stop | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-28 13:09 | +10 stop | DOGE | DOWN | 0.63 | 0.41 | -2.54 |
| 10-28 13:09 | +10 stop | ZEC | DOWN | 0.60 | 0.39 | -2.44 |
| 10-28 13:08 | +10 stop | XRP | UP | 0.37 | 0.61 | 2.06 |
| 10-28 13:08 | +10 stop | BNB | DOWN | 0.64 | 0.42 | -2.55 |
| 10-28 13:08 | +20 | BNB | DOWN | 0.65 | 0.88 | 2.06 |
| 10-28 13:08 | +15 | BNB | DOWN | 0.65 | 0.80 | 1.22 |
| 10-28 13:08 | +10 | BNB | DOWN | 0.64 | 0.76 | 0.86 |
| 10-28 13:08 | +5 | BNB | DOWN | 0.64 | 0.76 | 0.86 |
| 10-28 13:08 | +10 stop | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 10-28 13:08 | +10 stop | BTC | DOWN | 0.63 | 0.48 | -1.85 |
| 10-28 13:08 | +10 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-28 13:08 | +5 | BTC | DOWN | 0.61 | 0.67 | 0.27 |
| 10-28 13:07 | +10 stop | ZEC | DOWN | 0.61 | 0.43 | -2.13 |
| 10-28 13:07 | +10 stop | XRP | DOWN | 0.62 | 0.43 | -2.23 |
| 10-28 13:07 | +10 stop | DOGE | DOWN | 0.71 | 0.54 | -2.03 |
| 10-28 13:07 | +10 stop | NEAR | UP | 0.58 | 0.71 | 0.97 |
| 10-28 13:07 | +20 | NEAR | UP | 0.58 | 0.83 | 2.22 |
| 10-28 13:07 | +10 | NEAR | UP | 0.57 | 0.71 | 1.07 |
| 10-28 13:07 | +5 | NEAR | UP | 0.56 | 0.71 | 1.17 |
| 10-28 13:06 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-28 13:05 | +10 stop | ETH | DOWN | 0.52 | 0.72 | 1.67 |
| 10-28 13:05 | +5 | BNB | DOWN | 0.60 | 0.72 | 0.92 |
| 10-28 13:05 | +10 stop | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-28 13:05 | +20 | ZEC | UP | 0.59 | 0.80 | 1.81 |
| 10-28 13:04 | +5 | XRP | UP | 0.69 | open |  |
| 10-28 13:04 | +5 | DOGE | UP | 0.64 | open |  |
| 10-28 13:04 | +10 stop | ZEC | UP | 0.64 | 0.49 | -1.85 |
| 10-28 13:04 | +15 | ZEC | UP | 0.64 | 0.80 | 1.31 |
| 10-28 13:04 | +10 | ZEC | UP | 0.64 | 0.80 | 1.31 |
