# Range-Scalp Bot

*Updated Sat Oct 31 19:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42661 | 37195 | 5466 (61) | 1 | $-12085.76 | -4.5% |
| **+10¢** | 31816 | 25491 | 6325 (83) | 0 | $-10869.79 | -5.4% |
| **+15¢** | 26614 | 19792 | 6822 (111) | 0 | $-9985.49 | -6.0% |
| **+20¢** | 23638 | 16489 | 7149 (143) | 0 | $-8859.72 | -6.0% |
| **+10¢ (15¢ stop)** | 52058 | 51975 | 83 (48) | 0 | $-19706.28 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 19:55 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 10-31 19:54 | +10 stop | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-31 19:54 | +20 | HYPE | DOWN | 0.63 | 0.86 | 2.04 |
| 10-31 19:54 | +15 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-31 19:54 | +10 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-31 19:54 | +5 | HYPE | DOWN | 0.63 | 0.71 | 0.48 |
| 10-31 19:53 | +10 stop | NEAR | UP | 0.59 | 0.34 | -2.87 |
| 10-31 19:53 | +5 | NEAR | UP | 0.62 | open |  |
| 10-31 19:52 | +10 stop | NEAR | DOWN | 0.57 | 0.41 | -1.95 |
| 10-31 19:52 | +20 | NEAR | DOWN | 0.57 | 0.78 | 1.79 |
| 10-31 19:52 | +15 | NEAR | DOWN | 0.57 | 0.78 | 1.79 |
| 10-31 19:52 | +10 | NEAR | DOWN | 0.57 | 0.67 | 0.66 |
| 10-31 19:52 | +5 | NEAR | DOWN | 0.57 | 0.62 | 0.15 |
| 10-31 19:42 | +10 stop | BNB | UP | 0.71 | 0.90 | 1.69 |
| 10-31 19:41 | +10 | SOL | DOWN | 0.69 | 1.00 | 2.90 |
| 10-31 19:41 | +5 | SOL | DOWN | 0.69 | 1.00 | 2.90 |
| 10-31 19:41 | +10 stop | SOL | DOWN | 0.70 | 0.30 | -4.30 |
| 10-31 19:41 | +15 | SOL | DOWN | 0.70 | 1.00 | 2.80 |
| 10-31 19:38 | +10 stop | HYPE | UP | 0.66 | 0.86 | 1.71 |
| 10-31 19:38 | +10 stop | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 10-31 19:38 | +10 stop | BNB | UP | 0.62 | 0.73 | 0.75 |
| 10-31 19:38 | +5 | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 10-31 19:36 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-31 19:36 | +10 stop | XRP | DOWN | 0.62 | 0.74 | 0.87 |
| 10-31 19:35 | +10 stop | BNB | UP | 0.67 | 0.49 | -2.14 |
| 10-31 19:35 | +10 stop | SOL | UP | 0.58 | 0.28 | -3.33 |
| 10-31 19:35 | +10 stop | BTC | UP | 0.70 | 0.80 | 0.73 |
| 10-31 19:35 | +10 | BTC | UP | 0.70 | 0.80 | 0.73 |
| 10-31 19:34 | +5 | BTC | UP | 0.67 | 0.73 | 0.30 |
| 10-31 19:34 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-31 19:34 | +10 stop | HYPE | UP | 0.68 | 0.49 | -2.24 |
| 10-31 19:34 | +10 stop | ZEC | UP | 0.56 | 0.35 | -2.43 |
| 10-31 19:34 | +10 stop | SOL | UP | 0.66 | 0.50 | -1.94 |
| 10-31 19:33 | +10 stop | XRP | UP | 0.65 | 0.38 | -3.03 |
| 10-31 19:33 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-31 19:33 | +15 | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 10-31 19:33 | +10 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-31 19:33 | +5 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-31 19:33 | +10 stop | ZEC | DOWN | 0.71 | 0.53 | -2.13 |
| 10-31 19:33 | +20 | ZEC | DOWN | 0.71 | 0.93 | 1.95 |
