# Range-Scalp Bot

*Updated Wed Nov 04 01:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46624 | 40602 | 6022 (72) | 0 | $-13388.82 | -4.6% |
| **+10¢** | 34824 | 27845 | 6979 (96) | 0 | $-12198.83 | -5.6% |
| **+15¢** | 29162 | 21653 | 7509 (124) | 0 | $-11154.53 | -6.1% |
| **+20¢** | 25905 | 18039 | 7866 (164) | 0 | $-9824.88 | -6.0% |
| **+10¢ (15¢ stop)** | 56841 | 56748 | 93 (56) | 0 | $-21246.45 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 01:42 | +10 stop | XRP | DOWN | 0.59 | 0.41 | -2.14 |
| 11-04 01:42 | +15 | XRP | DOWN | 0.58 | 0.78 | 1.69 |
| 11-04 01:42 | +10 | XRP | DOWN | 0.58 | 0.78 | 1.69 |
| 11-04 01:42 | +5 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 11-04 01:42 | +10 stop | BTC | UP | 0.51 | 0.82 | 2.81 |
| 11-04 01:42 | +15 | BTC | UP | 0.51 | 0.82 | 2.81 |
| 11-04 01:42 | +10 | BTC | UP | 0.51 | 0.82 | 2.81 |
| 11-04 01:42 | +5 | BTC | UP | 0.51 | 0.59 | 0.45 |
| 11-04 01:42 | +10 stop | ETH | DOWN | 0.59 | 0.22 | -4.00 |
| 11-04 01:42 | +20 | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 11-04 01:42 | +15 | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 11-04 01:42 | +10 | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 11-04 01:42 | +5 | ETH | DOWN | 0.56 | 0.66 | 0.66 |
| 11-04 01:41 | +10 stop | XRP | DOWN | 0.50 | 0.65 | 1.16 |
| 11-04 01:41 | +20 | XRP | DOWN | 0.50 | 0.78 | 2.49 |
| 11-04 01:41 | +15 | XRP | DOWN | 0.50 | 0.65 | 1.16 |
| 11-04 01:41 | +10 | XRP | DOWN | 0.50 | 0.65 | 1.16 |
| 11-04 01:41 | +5 | XRP | DOWN | 0.50 | 0.56 | 0.24 |
| 11-04 01:40 | +10 stop | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 11-04 01:40 | +15 | SOL | DOWN | 0.69 | 0.93 | 2.20 |
| 11-04 01:38 | +10 stop | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 11-04 01:38 | +10 | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 11-04 01:38 | +5 | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 11-04 01:38 | +5 | BTC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-04 01:36 | +5 | XRP | DOWN | 0.60 | 0.66 | 0.22 |
| 11-04 01:35 | +10 stop | ETH | DOWN | 0.58 | 0.73 | 1.18 |
| 11-04 01:35 | +10 stop | NEAR | DOWN | 0.70 | 0.83 | 1.05 |
| 11-04 01:35 | +10 stop | SOL | UP | 0.61 | 0.46 | -1.85 |
| 11-04 01:35 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-04 01:35 | +20 | DOGE | DOWN | 0.68 | 0.95 | 2.47 |
| 11-04 01:35 | +10 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-04 01:35 | +5 | DOGE | DOWN | 0.67 | 0.75 | 0.50 |
| 11-04 01:34 | +5 | XRP | DOWN | 0.55 | 0.60 | 0.15 |
| 11-04 01:34 | +10 stop | BTC | DOWN | 0.53 | 0.67 | 1.06 |
| 11-04 01:34 | +10 | BTC | DOWN | 0.53 | 0.67 | 1.06 |
| 11-04 01:34 | +5 | BTC | DOWN | 0.54 | 0.61 | 0.35 |
| 11-04 01:34 | +10 stop | NEAR | DOWN | 0.71 | 0.55 | -1.93 |
| 11-04 01:34 | +20 | NEAR | DOWN | 0.71 | 0.94 | 2.13 |
| 11-04 01:34 | +15 | NEAR | DOWN | 0.71 | 0.86 | 1.26 |
| 11-04 01:34 | +10 | NEAR | DOWN | 0.71 | 0.83 | 0.95 |
