# Range-Scalp Bot

*Updated Fri Nov 06 01:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48942 | 42641 | 6301 (75) | 0 | $-13942.01 | -4.5% |
| **+10¢** | 36538 | 29213 | 7325 (101) | 0 | $-12814.85 | -5.6% |
| **+15¢** | 30608 | 22720 | 7888 (130) | 1 | $-11694.66 | -6.1% |
| **+20¢** | 27200 | 18933 | 8267 (170) | 1 | $-10356.24 | -6.1% |
| **+10¢ (15¢ stop)** | 59675 | 59580 | 95 (57) | 0 | $-22107.01 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 00:54 | +10 stop | BTC | DOWN | 0.61 | 0.81 | 1.72 |
| 11-06 00:53 | +10 stop | BTC | DOWN | 0.51 | 0.65 | 1.06 |
| 11-06 00:52 | +5 | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 11-06 00:52 | +10 stop | BTC | DOWN | 0.70 | 0.54 | -1.93 |
| 11-06 00:52 | +20 | BTC | DOWN | 0.70 | 0.90 | 1.81 |
| 11-06 00:52 | +15 | BTC | DOWN | 0.70 | 0.85 | 1.26 |
| 11-06 00:52 | +10 | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-06 00:52 | +5 | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-06 00:51 | +10 stop | ZEC | UP | 0.62 | 0.74 | 0.89 |
| 11-06 00:50 | +15 | ZEC | DOWN | 0.50 | open |  |
| 11-06 00:50 | +10 stop | ZEC | DOWN | 0.60 | 0.44 | -1.95 |
| 11-06 00:48 | +5 | ZEC | UP | 0.62 | 0.67 | 0.17 |
| 11-06 00:47 | +10 stop | ZEC | UP | 0.62 | 0.42 | -2.35 |
| 11-06 00:47 | +10 | ZEC | UP | 0.63 | 0.74 | 0.79 |
| 11-06 00:47 | +5 | ZEC | UP | 0.63 | 0.69 | 0.28 |
| 11-06 00:47 | +10 stop | ZEC | DOWN | 0.43 | 0.54 | 0.74 |
| 11-06 00:47 | +20 | ZEC | DOWN | 0.43 | open |  |
| 11-06 00:47 | +15 | ZEC | DOWN | 0.43 | 0.59 | 1.25 |
| 11-06 00:47 | +10 | ZEC | DOWN | 0.43 | 0.54 | 0.74 |
| 11-06 00:47 | +5 | ZEC | DOWN | 0.43 | 0.54 | 0.74 |
| 11-06 00:47 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 11-06 00:47 | +20 | BNB | DOWN | 0.70 | 0.92 | 2.04 |
| 11-06 00:47 | +15 | BNB | DOWN | 0.70 | 0.86 | 1.36 |
| 11-06 00:47 | +10 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 11-06 00:47 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 11-06 00:46 | +10 stop | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-06 00:46 | +20 | BTC | DOWN | 0.59 | 0.79 | 1.71 |
| 11-06 00:46 | +15 | BTC | DOWN | 0.59 | 0.75 | 1.29 |
| 11-06 00:46 | +10 | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 11-06 00:46 | +5 | BTC | DOWN | 0.60 | 0.69 | 0.58 |
| 11-06 00:46 | +10 stop | XRP | DOWN | 0.70 | 0.88 | 1.57 |
| 11-06 00:46 | +20 | XRP | DOWN | 0.70 | 0.95 | 2.29 |
| 11-06 00:46 | +15 | XRP | DOWN | 0.71 | 0.88 | 1.48 |
| 11-06 00:46 | +10 | XRP | DOWN | 0.71 | 0.88 | 1.47 |
| 11-06 00:46 | +10 stop | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 11-06 00:46 | +20 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-06 00:46 | +15 | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 11-06 00:46 | +10 | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 11-06 00:46 | +5 | DOGE | DOWN | 0.64 | 0.73 | 0.59 |
| 11-06 00:46 | +10 stop | SOL | DOWN | 0.65 | 0.84 | 1.64 |
