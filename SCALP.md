# Range-Scalp Bot

*Updated Sun Nov 15 00:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60074 | 52404 | 7670 (107) | 1 | $-16340.80 | -4.3% |
| **+10¢** | 44879 | 35892 | 8987 (143) | 5 | $-15426.14 | -5.5% |
| **+15¢** | 37607 | 27915 | 9692 (181) | 3 | $-14067.33 | -6.0% |
| **+20¢** | 33505 | 23337 | 10168 (233) | 6 | $-12404.92 | -5.9% |
| **+10¢ (15¢ stop)** | 73133 | 72990 | 143 (82) | 2 | $-26896.85 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 00:21 | +10 | HYPE | DOWN | 0.70 | open |  |
| 11-15 00:21 | +5 | HYPE | DOWN | 0.70 | 0.78 | 0.53 |
| 11-15 00:21 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 11-15 00:21 | +10 stop | DOGE | DOWN | 0.69 | open |  |
| 11-15 00:21 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.51 |
| 11-15 00:21 | +10 stop | NEAR | DOWN | 0.54 | 0.65 | 0.76 |
| 11-15 00:21 | +5 | NEAR | DOWN | 0.54 | 0.65 | 0.76 |
| 11-15 00:21 | +10 stop | XRP | UP | 0.60 | 0.42 | -2.15 |
| 11-15 00:20 | +5 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-15 00:19 | +10 stop | ZEC | DOWN | 0.66 | 0.83 | 1.44 |
| 11-15 00:19 | +10 stop | DOGE | UP | 0.49 | 0.30 | -2.23 |
| 11-15 00:18 | +10 stop | HYPE | DOWN | 0.62 | 0.72 | 0.72 |
| 11-15 00:18 | +20 | HYPE | DOWN | 0.60 | open |  |
| 11-15 00:18 | +15 | HYPE | DOWN | 0.60 | 0.78 | 1.50 |
| 11-15 00:18 | +10 | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 11-15 00:18 | +5 | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 11-15 00:18 | +5 | BTC | DOWN | 0.51 | 0.56 | 0.14 |
| 11-15 00:18 | +5 | DOGE | DOWN | 0.60 | 0.68 | 0.47 |
| 11-15 00:18 | +10 stop | NEAR | UP | 0.63 | 0.33 | -3.33 |
| 11-15 00:18 | +10 stop | BNB | DOWN | 0.49 | 0.62 | 0.95 |
| 11-15 00:18 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.19 |
| 11-15 00:18 | +10 stop | SOL | DOWN | 0.57 | 0.41 | -1.95 |
| 11-15 00:18 | +20 | SOL | DOWN | 0.57 | 0.79 | 1.90 |
| 11-15 00:18 | +15 | SOL | DOWN | 0.57 | 0.72 | 1.17 |
| 11-15 00:18 | +10 stop | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 11-15 00:18 | +10 | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 11-15 00:18 | +5 | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 11-15 00:18 | +10 stop | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 11-15 00:18 | +5 | BTC | DOWN | 0.54 | 0.60 | 0.25 |
| 11-15 00:17 | +10 stop | DOGE | DOWN | 0.69 | 0.53 | -1.93 |
| 11-15 00:17 | +10 stop | ZEC | DOWN | 0.70 | 0.50 | -2.33 |
| 11-15 00:17 | +10 stop | NEAR | UP | 0.44 | 0.54 | 0.64 |
| 11-15 00:17 | +5 | SOL | DOWN | 0.69 | 0.76 | 0.42 |
| 11-15 00:17 | +10 stop | XRP | UP | 0.61 | 0.74 | 0.99 |
| 11-15 00:17 | +5 | BTC | UP | 0.46 | 0.54 | 0.44 |
| 11-15 00:17 | +10 stop | NEAR | UP | 0.56 | 0.66 | 0.66 |
| 11-15 00:17 | +10 stop | BNB | UP | 0.60 | 0.45 | -1.85 |
| 11-15 00:17 | +20 | BNB | UP | 0.60 | open |  |
| 11-15 00:17 | +15 | BNB | UP | 0.60 | open |  |
| 11-15 00:17 | +10 | BNB | UP | 0.61 | open |  |
