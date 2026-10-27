# Range-Scalp Bot

*Updated Tue Oct 27 00:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35660 | 31118 | 4542 (43) | 1 | $-10006.50 | -4.5% |
| **+10¢** | 26659 | 21407 | 5252 (65) | 3 | $-8841.65 | -5.3% |
| **+15¢** | 22316 | 16669 | 5647 (89) | 3 | $-7896.06 | -5.6% |
| **+20¢** | 19783 | 13866 | 5917 (112) | 3 | $-6948.65 | -5.6% |
| **+10¢ (15¢ stop)** | 43710 | 43648 | 62 (33) | 1 | $-16649.65 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 00:23 | +10 stop | ETH | UP | 0.59 | 0.36 | -2.64 |
| 10-27 00:23 | +10 stop | BTC | DOWN | 0.65 | open |  |
| 10-27 00:23 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-27 00:22 | +10 stop | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 10-27 00:21 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 10-27 00:20 | +10 stop | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-27 00:20 | +15 | BTC | DOWN | 0.63 | open |  |
| 10-27 00:20 | +5 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-27 00:20 | +5 | XRP | UP | 0.52 | 0.57 | 0.14 |
| 10-27 00:20 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-27 00:20 | +5 | NEAR | DOWN | 0.66 | 0.87 | 1.86 |
| 10-27 00:20 | +10 stop | ETH | DOWN | 0.58 | 0.34 | -2.74 |
| 10-27 00:19 | +10 | BTC | DOWN | 0.67 | open |  |
| 10-27 00:19 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-27 00:18 | +10 stop | XRP | UP | 0.51 | 0.35 | -1.94 |
| 10-27 00:18 | +10 | XRP | UP | 0.51 | open |  |
| 10-27 00:18 | +5 | XRP | UP | 0.52 | 0.58 | 0.24 |
| 10-27 00:18 | +10 stop | ETH | UP | 0.61 | 0.43 | -2.15 |
| 10-27 00:18 | +5 | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-27 00:17 | +5 | XRP | UP | 0.59 | 0.64 | 0.16 |
| 10-27 00:17 | +5 | NEAR | DOWN | 0.60 | 0.67 | 0.37 |
| 10-27 00:17 | +10 stop | ZEC | DOWN | 0.68 | 0.85 | 1.45 |
| 10-27 00:17 | +15 | ZEC | DOWN | 0.68 | 0.85 | 1.45 |
| 10-27 00:17 | +10 | ZEC | DOWN | 0.68 | 0.85 | 1.45 |
| 10-27 00:17 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-27 00:17 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-27 00:17 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-27 00:17 | +5 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-27 00:17 | +10 stop | XRP | UP | 0.53 | 0.64 | 0.75 |
| 10-27 00:17 | +20 | XRP | UP | 0.53 | open |  |
| 10-27 00:17 | +15 | XRP | UP | 0.54 | open |  |
| 10-27 00:17 | +10 | XRP | UP | 0.54 | 0.64 | 0.65 |
| 10-27 00:17 | +5 | XRP | UP | 0.54 | 0.59 | 0.15 |
| 10-27 00:17 | +10 stop | BNB | DOWN | 0.59 | 0.69 | 0.68 |
| 10-27 00:17 | +20 | BNB | DOWN | 0.59 | 0.79 | 1.71 |
| 10-27 00:17 | +15 | BNB | DOWN | 0.59 | 0.76 | 1.40 |
| 10-27 00:17 | +10 | BNB | DOWN | 0.59 | 0.69 | 0.68 |
| 10-27 00:17 | +5 | BNB | DOWN | 0.59 | 0.69 | 0.68 |
| 10-27 00:17 | +10 stop | DOGE | DOWN | 0.64 | 0.76 | 0.87 |
| 10-27 00:17 | +20 | DOGE | DOWN | 0.64 | 0.85 | 1.81 |
