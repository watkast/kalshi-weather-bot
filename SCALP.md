# Range-Scalp Bot

*Updated Wed Nov 11 06:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55497 | 48398 | 7099 (94) | 4 | $-15172.13 | -4.3% |
| **+10¢** | 41464 | 33180 | 8284 (124) | 4 | $-14125.61 | -5.4% |
| **+15¢** | 34768 | 25836 | 8932 (158) | 4 | $-12885.86 | -5.9% |
| **+20¢** | 30962 | 21594 | 9368 (207) | 5 | $-11260.45 | -5.8% |
| **+10¢ (15¢ stop)** | 67594 | 67476 | 118 (73) | 0 | $-24877.75 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 06:07 | +10 stop | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-11 06:07 | +10 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-11 06:07 | +5 | BTC | DOWN | 0.66 | 0.75 | 0.60 |
| 11-11 06:07 | +10 stop | BNB | DOWN | 0.66 | 0.80 | 1.12 |
| 11-11 06:06 | +10 stop | XRP | DOWN | 0.64 | 0.49 | -1.85 |
| 11-11 06:04 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-11 06:04 | +20 | BTC | DOWN | 0.71 | open |  |
| 11-11 06:04 | +15 | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 11-11 06:04 | +10 | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-11 06:04 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-11 06:04 | +10 stop | XRP | UP | 0.50 | 0.31 | -2.23 |
| 11-11 06:03 | +10 stop | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 11-11 06:02 | +10 stop | DOGE | DOWN | 0.57 | 0.80 | 2.00 |
| 11-11 06:02 | +10 stop | NEAR | DOWN | 0.64 | 0.83 | 1.63 |
| 11-11 06:02 | +10 stop | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 11-11 06:02 | +20 | SOL | DOWN | 0.70 | 0.93 | 2.10 |
| 11-11 06:02 | +15 | SOL | DOWN | 0.70 | 0.85 | 1.26 |
| 11-11 06:02 | +10 | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 11-11 06:02 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 11-11 06:01 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-11 06:01 | +20 | ZEC | DOWN | 0.70 | 0.90 | 1.79 |
| 11-11 06:01 | +15 | ZEC | DOWN | 0.70 | 0.87 | 1.47 |
| 11-11 06:01 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-11 06:01 | +5 | ZEC | DOWN | 0.70 | 0.79 | 0.63 |
| 11-11 06:01 | +10 stop | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-11 06:01 | +20 | HYPE | DOWN | 0.66 | 0.87 | 1.86 |
| 11-11 06:01 | +15 | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-11 06:01 | +10 | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-11 06:01 | +5 | HYPE | DOWN | 0.66 | 0.75 | 0.60 |
| 11-11 06:01 | +10 stop | XRP | UP | 0.65 | 0.45 | -2.34 |
| 11-11 06:01 | +20 | XRP | UP | 0.65 | open |  |
| 11-11 06:01 | +15 | XRP | UP | 0.65 | open |  |
| 11-11 06:01 | +10 | XRP | UP | 0.66 | open |  |
| 11-11 06:01 | +5 | XRP | UP | 0.65 | open |  |
| 11-11 06:01 | +10 stop | DOGE | UP | 0.62 | 0.45 | -2.05 |
| 11-11 06:01 | +20 | DOGE | UP | 0.62 | open |  |
| 11-11 06:01 | +15 | DOGE | UP | 0.61 | open |  |
| 11-11 06:01 | +10 | DOGE | UP | 0.61 | open |  |
| 11-11 06:01 | +5 | DOGE | UP | 0.61 | open |  |
| 11-11 06:01 | +10 stop | NEAR | UP | 0.60 | 0.45 | -1.85 |
