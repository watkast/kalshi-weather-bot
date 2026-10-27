# Range-Scalp Bot

*Updated Tue Oct 27 04:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35970 | 31402 | 4568 (43) | 1 | $-9999.33 | -4.4% |
| **+10¢** | 26891 | 21605 | 5286 (65) | 2 | $-8843.67 | -5.2% |
| **+15¢** | 22500 | 16818 | 5682 (89) | 2 | $-7870.15 | -5.6% |
| **+20¢** | 19943 | 13990 | 5953 (112) | 2 | $-6912.91 | -5.5% |
| **+10¢ (15¢ stop)** | 44097 | 44034 | 63 (33) | 0 | $-16785.67 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 04:13 | +10 stop | ZEC | DOWN | 0.45 | 0.63 | 1.45 |
| 10-27 04:13 | +15 | ZEC | DOWN | 0.44 | 0.63 | 1.55 |
| 10-27 04:13 | +10 | ZEC | DOWN | 0.44 | 0.63 | 1.55 |
| 10-27 04:13 | +5 | ZEC | DOWN | 0.45 | 0.63 | 1.45 |
| 10-27 04:12 | +10 stop | HYPE | DOWN | 0.60 | 0.39 | -2.44 |
| 10-27 04:11 | +5 | BTC | UP | 0.63 | 0.70 | 0.38 |
| 10-27 04:11 | +10 stop | DOGE | UP | 0.52 | 0.34 | -2.14 |
| 10-27 04:11 | +10 stop | BNB | DOWN | 0.70 | 0.86 | 1.36 |
| 10-27 04:10 | +10 stop | DOGE | DOWN | 0.59 | 0.42 | -2.05 |
| 10-27 04:09 | +10 stop | HYPE | UP | 0.64 | 0.38 | -2.94 |
| 10-27 04:09 | +10 stop | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 10-27 04:08 | +10 stop | SOL | DOWN | 0.56 | 0.67 | 0.76 |
| 10-27 04:08 | +15 | BTC | UP | 0.62 | 0.96 | 3.25 |
| 10-27 04:08 | +5 | BTC | UP | 0.62 | 0.67 | 0.17 |
| 10-27 04:07 | +10 stop | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 10-27 04:07 | +10 | ETH | UP | 0.62 | 0.72 | 0.68 |
| 10-27 04:07 | +10 stop | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-27 04:07 | +5 | ZEC | DOWN | 0.57 | 0.67 | 0.66 |
| 10-27 04:07 | +10 stop | ETH | UP | 0.62 | 0.45 | -2.05 |
| 10-27 04:06 | +10 | ZEC | DOWN | 0.57 | 0.67 | 0.66 |
| 10-27 04:06 | +5 | ZEC | DOWN | 0.57 | 0.62 | 0.15 |
| 10-27 04:06 | +10 stop | NEAR | DOWN | 0.54 | 0.64 | 0.65 |
| 10-27 04:06 | +5 | ETH | UP | 0.64 | 0.72 | 0.48 |
| 10-27 04:06 | +10 stop | HYPE | DOWN | 0.60 | 0.42 | -2.16 |
| 10-27 04:06 | +10 stop | DOGE | UP | 0.68 | 0.46 | -2.54 |
| 10-27 04:06 | +5 | DOGE | UP | 0.68 | 0.87 | 1.66 |
| 10-27 04:06 | +10 stop | ETH | UP | 0.51 | 0.61 | 0.65 |
| 10-27 04:06 | +5 | ETH | UP | 0.51 | 0.58 | 0.34 |
| 10-27 04:06 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-27 04:05 | +10 stop | BTC | UP | 0.69 | 0.38 | -3.42 |
| 10-27 04:05 | +10 | BTC | UP | 0.69 | 0.96 | 2.57 |
| 10-27 04:05 | +5 | BTC | UP | 0.69 | 0.74 | 0.21 |
| 10-27 04:05 | +10 stop | ETH | DOWN | 0.56 | 0.39 | -2.05 |
| 10-27 04:04 | +10 stop | SOL | UP | 0.58 | 0.41 | -2.05 |
| 10-27 04:04 | +10 stop | BNB | UP | 0.53 | 0.36 | -2.05 |
| 10-27 04:04 | +5 | BTC | UP | 0.61 | 0.69 | 0.48 |
| 10-27 04:04 | +5 | DOGE | DOWN | 0.53 | 0.61 | 0.45 |
| 10-27 04:03 | +5 | DOGE | DOWN | 0.60 | 0.68 | 0.47 |
| 10-27 04:03 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 10-27 04:03 | +10 stop | XRP | DOWN | 0.63 | 0.47 | -1.95 |
