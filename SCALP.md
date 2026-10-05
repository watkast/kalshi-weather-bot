# Range-Scalp Bot

*Updated Mon Oct 05 11:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3725 | 3205 | 520 (3) | 0 | $-1302.25 | -5.5% |
| **+10¢** | 2883 | 2285 | 598 (4) | 0 | $-1177.13 | -6.5% |
| **+15¢** | 2421 | 1792 | 629 (7) | 0 | $-1011.37 | -6.7% |
| **+20¢** | 2162 | 1507 | 655 (12) | 0 | $-843.40 | -6.2% |
| **+10¢ (15¢ stop)** | 4613 | 4612 | 1 (1) | 0 | $-1744.58 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 11:13 | +10 stop | ZEC | UP | 0.69 | 0.85 | 1.37 |
| 10-05 11:13 | +20 | ZEC | UP | 0.69 | 0.94 | 2.30 |
| 10-05 11:13 | +15 | ZEC | UP | 0.69 | 0.85 | 1.40 |
| 10-05 11:13 | +10 | ZEC | UP | 0.64 | 0.85 | 1.85 |
| 10-05 11:13 | +5 | ZEC | UP | 0.64 | 0.69 | 0.19 |
| 10-05 11:12 | +10 stop | BNB | UP | 0.59 | 0.82 | 2.03 |
| 10-05 11:09 | +10 stop | HYPE | DOWN | 0.68 | 0.50 | -2.18 |
| 10-05 11:08 | +10 stop | HYPE | UP | 0.52 | 0.35 | -2.04 |
| 10-05 11:08 | +10 | HYPE | UP | 0.54 | 0.77 | 1.99 |
| 10-05 11:08 | +5 | HYPE | UP | 0.54 | 0.62 | 0.45 |
| 10-05 11:07 | +10 stop | BNB | UP | 0.65 | 0.50 | -1.84 |
| 10-05 11:07 | +5 | BNB | UP | 0.65 | 0.82 | 1.43 |
| 10-05 11:05 | +10 stop | BNB | DOWN | 0.56 | 0.32 | -2.74 |
| 10-05 11:05 | +15 | BNB | DOWN | 0.56 | 0.86 | 2.73 |
| 10-05 11:05 | +10 | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 10-05 11:04 | +10 stop | HYPE | UP | 0.70 | 0.81 | 0.84 |
| 10-05 11:04 | +20 | HYPE | UP | 0.70 | 0.91 | 1.87 |
| 10-05 11:04 | +15 | HYPE | UP | 0.71 | 0.91 | 1.78 |
| 10-05 11:04 | +10 | HYPE | UP | 0.71 | 0.81 | 0.75 |
| 10-05 11:04 | +5 | HYPE | UP | 0.70 | 0.81 | 0.80 |
| 10-05 11:02 | +10 stop | BNB | UP | 0.49 | 0.32 | -2.04 |
| 10-05 11:02 | +5 | NEAR | DOWN | 0.63 | 0.69 | 0.28 |
| 10-05 11:01 | +10 stop | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
| 10-05 11:01 | +20 | NEAR | DOWN | 0.55 | 0.78 | 1.99 |
| 10-05 11:01 | +15 | NEAR | DOWN | 0.55 | 0.71 | 1.27 |
| 10-05 11:01 | +10 | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
| 10-05 11:01 | +5 | NEAR | DOWN | 0.53 | 0.61 | 0.45 |
| 10-05 11:01 | +10 stop | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 10-05 11:01 | +20 | XRP | DOWN | 0.62 | 0.82 | 1.72 |
| 10-05 11:01 | +15 | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 10-05 11:01 | +10 | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 10-05 11:01 | +5 | XRP | DOWN | 0.62 | 0.71 | 0.58 |
| 10-05 11:01 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-05 11:01 | +20 | BTC | DOWN | 0.67 | 0.87 | 1.76 |
| 10-05 11:01 | +15 | BTC | DOWN | 0.67 | 0.85 | 1.55 |
| 10-05 11:01 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-05 11:01 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-05 11:01 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-05 11:01 | +20 | ZEC | DOWN | 0.58 | 0.80 | 1.90 |
| 10-05 11:01 | +15 | ZEC | DOWN | 0.58 | 0.75 | 1.38 |
