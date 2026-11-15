# Range-Scalp Bot

*Updated Sun Nov 15 00:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60110 | 52436 | 7674 (107) | 6 | $-16345.05 | -4.3% |
| **+10¢** | 44907 | 35914 | 8993 (143) | 8 | $-15437.66 | -5.5% |
| **+15¢** | 37621 | 27924 | 9697 (181) | 9 | $-14084.83 | -6.0% |
| **+20¢** | 33520 | 23346 | 10174 (233) | 9 | $-12426.19 | -5.9% |
| **+10¢ (15¢ stop)** | 73189 | 73046 | 143 (82) | 0 | $-26931.94 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 00:47 | +10 stop | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-15 00:47 | +10 stop | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 11-15 00:47 | +10 stop | NEAR | DOWN | 0.63 | 0.77 | 1.10 |
| 11-15 00:47 | +10 stop | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-15 00:47 | +10 stop | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-15 00:47 | +10 stop | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 11-15 00:47 | +5 | BNB | DOWN | 0.66 | 0.73 | 0.40 |
| 11-15 00:46 | +10 stop | DOGE | DOWN | 0.66 | 0.79 | 1.07 |
| 11-15 00:46 | +10 stop | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 11-15 00:46 | +10 | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 11-15 00:46 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 11-15 00:46 | +5 | HYPE | DOWN | 0.68 | 0.82 | 1.13 |
| 11-15 00:46 | +10 stop | XRP | UP | 0.47 | 0.60 | 0.95 |
| 11-15 00:46 | +20 | XRP | UP | 0.47 | open |  |
| 11-15 00:46 | +15 | XRP | UP | 0.48 | open |  |
| 11-15 00:46 | +10 | XRP | UP | 0.48 | 0.60 | 0.85 |
| 11-15 00:46 | +5 | XRP | UP | 0.48 | 0.60 | 0.85 |
| 11-15 00:46 | +10 stop | BNB | UP | 0.56 | 0.39 | -2.05 |
| 11-15 00:46 | +20 | BNB | UP | 0.56 | open |  |
| 11-15 00:46 | +15 | BNB | UP | 0.56 | open |  |
| 11-15 00:46 | +10 | BNB | UP | 0.56 | open |  |
| 11-15 00:46 | +5 | BNB | UP | 0.56 | 0.61 | 0.15 |
| 11-15 00:46 | +10 stop | DOGE | UP | 0.56 | 0.40 | -1.95 |
| 11-15 00:46 | +20 | DOGE | UP | 0.56 | open |  |
| 11-15 00:46 | +15 | DOGE | UP | 0.56 | open |  |
| 11-15 00:46 | +10 | DOGE | UP | 0.56 | open |  |
| 11-15 00:46 | +5 | DOGE | UP | 0.56 | open |  |
| 11-15 00:46 | +10 stop | ZEC | UP | 0.55 | 0.35 | -2.34 |
| 11-15 00:46 | +20 | ZEC | UP | 0.55 | open |  |
| 11-15 00:46 | +15 | ZEC | UP | 0.57 | open |  |
| 11-15 00:46 | +10 | ZEC | UP | 0.57 | open |  |
| 11-15 00:46 | +5 | ZEC | UP | 0.57 | open |  |
| 11-15 00:46 | +10 stop | NEAR | UP | 0.54 | 0.37 | -2.05 |
| 11-15 00:46 | +20 | NEAR | UP | 0.54 | open |  |
| 11-15 00:46 | +15 | NEAR | UP | 0.55 | open |  |
| 11-15 00:46 | +10 | NEAR | UP | 0.55 | open |  |
| 11-15 00:46 | +5 | NEAR | UP | 0.55 | open |  |
| 11-15 00:46 | +10 stop | BTC | UP | 0.59 | 0.36 | -2.64 |
| 11-15 00:46 | +20 | BTC | UP | 0.60 | open |  |
| 11-15 00:46 | +15 | BTC | UP | 0.60 | open |  |
