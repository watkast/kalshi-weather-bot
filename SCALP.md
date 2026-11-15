# Range-Scalp Bot

*Updated Sun Nov 15 13:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60829 | 53070 | 7759 (112) | 2 | $-16458.81 | -4.3% |
| **+10¢** | 45446 | 36349 | 9097 (150) | 4 | $-15525.04 | -5.4% |
| **+15¢** | 38063 | 28251 | 9812 (188) | 4 | $-14198.00 | -5.9% |
| **+20¢** | 33921 | 23629 | 10292 (240) | 4 | $-12486.55 | -5.9% |
| **+10¢ (15¢ stop)** | 74026 | 73875 | 151 (89) | 1 | $-27203.14 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 13:21 | +10 stop | BNB | UP | 0.63 | open |  |
| 11-15 13:21 | +10 stop | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-15 13:21 | +10 | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-15 13:21 | +5 | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-15 13:20 | +10 stop | BNB | DOWN | 0.53 | 0.34 | -2.24 |
| 11-15 13:20 | +20 | BNB | DOWN | 0.54 | open |  |
| 11-15 13:20 | +15 | BNB | DOWN | 0.54 | open |  |
| 11-15 13:20 | +10 | BNB | DOWN | 0.55 | open |  |
| 11-15 13:20 | +5 | BNB | DOWN | 0.55 | open |  |
| 11-15 13:20 | +5 | NEAR | DOWN | 0.46 | 0.55 | 0.54 |
| 11-15 13:19 | +10 | BTC | UP | 0.63 | 0.73 | 0.69 |
| 11-15 13:19 | +10 stop | NEAR | DOWN | 0.53 | 0.33 | -2.34 |
| 11-15 13:19 | +10 | NEAR | DOWN | 0.53 | open |  |
| 11-15 13:19 | +5 | NEAR | DOWN | 0.53 | 0.58 | 0.14 |
| 11-15 13:19 | +10 stop | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 11-15 13:19 | +10 | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 11-15 13:19 | +10 stop | HYPE | UP | 0.63 | 0.86 | 2.04 |
| 11-15 13:19 | +20 | HYPE | UP | 0.62 | 0.86 | 2.14 |
| 11-15 13:19 | +15 | HYPE | UP | 0.62 | 0.86 | 2.14 |
| 11-15 13:19 | +10 | HYPE | UP | 0.62 | 0.72 | 0.68 |
| 11-15 13:19 | +5 | HYPE | UP | 0.62 | 0.72 | 0.68 |
| 11-15 13:18 | +5 | BNB | DOWN | 0.69 | 0.75 | 0.31 |
| 11-15 13:18 | +10 stop | NEAR | UP | 0.45 | 0.55 | 0.64 |
| 11-15 13:18 | +20 | NEAR | UP | 0.45 | 0.66 | 1.76 |
| 11-15 13:18 | +15 | NEAR | UP | 0.45 | 0.66 | 1.76 |
| 11-15 13:18 | +10 | NEAR | UP | 0.45 | 0.55 | 0.64 |
| 11-15 13:18 | +5 | NEAR | UP | 0.45 | 0.55 | 0.64 |
| 11-15 13:18 | +5 | ETH | DOWN | 0.66 | open |  |
| 11-15 13:17 | +10 stop | DOGE | UP | 0.58 | 0.74 | 1.28 |
| 11-15 13:17 | +20 | DOGE | UP | 0.58 | 0.86 | 2.53 |
| 11-15 13:17 | +15 | DOGE | UP | 0.58 | 0.74 | 1.28 |
| 11-15 13:17 | +10 | DOGE | UP | 0.58 | 0.74 | 1.28 |
| 11-15 13:17 | +5 | DOGE | UP | 0.58 | 0.67 | 0.56 |
| 11-15 13:17 | +5 | XRP | UP | 0.70 | 0.77 | 0.42 |
| 11-15 13:17 | +10 stop | BNB | DOWN | 0.58 | 0.69 | 0.77 |
| 11-15 13:17 | +20 | BNB | DOWN | 0.58 | 0.80 | 1.90 |
| 11-15 13:17 | +15 | BNB | DOWN | 0.58 | 0.75 | 1.38 |
| 11-15 13:17 | +10 | BNB | DOWN | 0.58 | 0.69 | 0.77 |
| 11-15 13:17 | +5 | BNB | DOWN | 0.58 | 0.63 | 0.15 |
| 11-15 13:17 | +10 stop | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
