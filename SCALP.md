# Range-Scalp Bot

*Updated Fri Nov 06 03:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49106 | 42787 | 6319 (75) | 5 | $-13944.36 | -4.5% |
| **+10¢** | 36664 | 29318 | 7346 (101) | 4 | $-12812.53 | -5.6% |
| **+15¢** | 30708 | 22798 | 7910 (130) | 5 | $-11693.60 | -6.1% |
| **+20¢** | 27294 | 19004 | 8290 (170) | 5 | $-10345.98 | -6.0% |
| **+10¢ (15¢ stop)** | 59895 | 59800 | 95 (57) | 2 | $-22202.15 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 03:22 | +10 stop | NEAR | UP | 0.53 | open |  |
| 11-06 03:22 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 11-06 03:22 | +10 stop | DOGE | UP | 0.48 | 0.58 | 0.64 |
| 11-06 03:22 | +5 | SOL | DOWN | 0.65 | open |  |
| 11-06 03:22 | +10 stop | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 11-06 03:22 | +20 | SOL | DOWN | 0.58 | open |  |
| 11-06 03:22 | +15 | SOL | DOWN | 0.58 | open |  |
| 11-06 03:22 | +10 | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 11-06 03:22 | +5 | SOL | DOWN | 0.58 | 0.66 | 0.46 |
| 11-06 03:21 | +5 | ZEC | DOWN | 0.61 | open |  |
| 11-06 03:20 | +10 stop | NEAR | DOWN | 0.64 | 0.44 | -2.35 |
| 11-06 03:20 | +10 | NEAR | DOWN | 0.64 | open |  |
| 11-06 03:20 | +5 | NEAR | DOWN | 0.64 | open |  |
| 11-06 03:19 | +5 | ZEC | DOWN | 0.65 | 0.71 | 0.29 |
| 11-06 03:18 | +10 stop | DOGE | DOWN | 0.70 | 0.51 | -2.23 |
| 11-06 03:18 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-06 03:18 | +15 | DOGE | DOWN | 0.70 | open |  |
| 11-06 03:18 | +10 | DOGE | DOWN | 0.70 | open |  |
| 11-06 03:18 | +5 | DOGE | DOWN | 0.70 | open |  |
| 11-06 03:18 | +10 stop | ZEC | DOWN | 0.70 | 0.55 | -1.83 |
| 11-06 03:18 | +10 | ZEC | DOWN | 0.70 | open |  |
| 11-06 03:17 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.19 |
| 11-06 03:17 | +10 stop | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 11-06 03:17 | +20 | NEAR | DOWN | 0.65 | open |  |
| 11-06 03:17 | +15 | NEAR | DOWN | 0.65 | open |  |
| 11-06 03:17 | +10 | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 11-06 03:17 | +5 | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 11-06 03:17 | +10 stop | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-06 03:17 | +10 stop | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-06 03:17 | +20 | BNB | DOWN | 0.68 | 0.88 | 1.76 |
| 11-06 03:17 | +15 | BNB | DOWN | 0.68 | 0.85 | 1.45 |
| 11-06 03:17 | +10 | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-06 03:17 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.51 |
| 11-06 03:16 | +5 | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 11-06 03:16 | +10 stop | XRP | DOWN | 0.64 | 0.76 | 0.90 |
| 11-06 03:16 | +20 | XRP | DOWN | 0.64 | 0.84 | 1.73 |
| 11-06 03:16 | +15 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 11-06 03:16 | +10 | XRP | DOWN | 0.64 | 0.76 | 0.90 |
| 11-06 03:16 | +5 | XRP | DOWN | 0.64 | 0.70 | 0.28 |
| 11-06 03:16 | +10 stop | BTC | DOWN | 0.62 | 0.77 | 1.20 |
