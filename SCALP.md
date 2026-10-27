# Range-Scalp Bot

*Updated Tue Oct 27 02:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35870 | 31308 | 4562 (43) | 1 | $-10017.19 | -4.4% |
| **+10¢** | 26817 | 21542 | 5275 (65) | 1 | $-8838.75 | -5.2% |
| **+15¢** | 22441 | 16774 | 5667 (89) | 1 | $-7848.36 | -5.6% |
| **+20¢** | 19891 | 13954 | 5937 (112) | 1 | $-6890.14 | -5.5% |
| **+10¢ (15¢ stop)** | 43973 | 43910 | 63 (33) | 0 | $-16707.57 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 02:43 | +10 stop | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 10-27 02:43 | +10 stop | BTC | UP | 0.26 | 0.69 | 4.01 |
| 10-27 02:41 | +10 stop | HYPE | UP | 0.71 | 0.89 | 1.58 |
| 10-27 02:41 | +15 | HYPE | UP | 0.71 | 0.89 | 1.58 |
| 10-27 02:41 | +5 | HYPE | UP | 0.71 | 0.78 | 0.42 |
| 10-27 02:40 | +10 stop | XRP | UP | 0.51 | 0.65 | 1.06 |
| 10-27 02:40 | +10 stop | NEAR | DOWN | 0.62 | 0.40 | -2.54 |
| 10-27 02:40 | +20 | NEAR | DOWN | 0.62 | open |  |
| 10-27 02:40 | +10 | NEAR | DOWN | 0.62 | open |  |
| 10-27 02:40 | +5 | NEAR | DOWN | 0.62 | open |  |
| 10-27 02:40 | +10 stop | HYPE | UP | 0.61 | 0.76 | 1.20 |
| 10-27 02:40 | +5 | DOGE | UP | 0.57 | 0.72 | 1.17 |
| 10-27 02:39 | +10 stop | ETH | DOWN | 0.52 | 0.29 | -2.63 |
| 10-27 02:39 | +10 stop | ZEC | DOWN | 0.44 | 0.16 | -3.08 |
| 10-27 02:39 | +10 stop | HYPE | DOWN | 0.57 | 0.37 | -2.39 |
| 10-27 02:39 | +10 stop | DOGE | UP | 0.53 | 0.72 | 1.57 |
| 10-27 02:39 | +15 | DOGE | UP | 0.54 | 0.72 | 1.47 |
| 10-27 02:39 | +10 | DOGE | UP | 0.50 | 0.60 | 0.65 |
| 10-27 02:39 | +5 | DOGE | UP | 0.49 | 0.58 | 0.54 |
| 10-27 02:38 | +10 stop | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-27 02:38 | +15 | NEAR | DOWN | 0.69 | open |  |
| 10-27 02:38 | +5 | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-27 02:37 | +10 stop | XRP | DOWN | 0.57 | 0.38 | -2.25 |
| 10-27 02:37 | +10 stop | HYPE | DOWN | 0.55 | 0.69 | 1.03 |
| 10-27 02:36 | +10 stop | HYPE | UP | 0.59 | 0.41 | -2.14 |
| 10-27 02:36 | +10 stop | ZEC | UP | 0.60 | 0.43 | -2.05 |
| 10-27 02:36 | +10 stop | XRP | UP | 0.58 | 0.43 | -1.86 |
| 10-27 02:36 | +5 | XRP | UP | 0.58 | 0.65 | 0.36 |
| 10-27 02:36 | +10 stop | ETH | UP | 0.63 | 0.39 | -2.74 |
| 10-27 02:36 | +10 stop | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 10-27 02:36 | +20 | NEAR | DOWN | 0.53 | 0.79 | 2.30 |
| 10-27 02:36 | +15 | NEAR | DOWN | 0.53 | 0.68 | 1.16 |
| 10-27 02:36 | +5 | NEAR | DOWN | 0.53 | 0.59 | 0.25 |
| 10-27 02:36 | +5 | DOGE | UP | 0.68 | 0.76 | 0.51 |
| 10-27 02:35 | +10 stop | ETH | DOWN | 0.45 | 0.56 | 0.74 |
| 10-27 02:35 | +10 stop | XRP | DOWN | 0.64 | 0.40 | -2.74 |
| 10-27 02:34 | +10 stop | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 10-27 02:34 | +10 stop | HYPE | DOWN | 0.63 | 0.47 | -1.99 |
| 10-27 02:34 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 10-27 02:34 | +10 | NEAR | DOWN | 0.66 | 0.79 | 1.02 |
