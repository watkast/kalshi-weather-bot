# Range-Scalp Bot

*Updated Sun Oct 18 13:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22607 | 19678 | 2929 (29) | 0 | $-6610.32 | -4.6% |
| **+10¢** | 17004 | 13622 | 3382 (43) | 1 | $-5879.66 | -5.5% |
| **+15¢** | 14239 | 10589 | 3650 (64) | 1 | $-5373.41 | -6.0% |
| **+20¢** | 12605 | 8784 | 3821 (82) | 1 | $-4783.34 | -6.0% |
| **+10¢ (15¢ stop)** | 27795 | 27745 | 50 (29) | 0 | $-10631.80 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 13:09 | +5 | XRP | DOWN | 0.45 | 0.65 | 1.66 |
| 10-18 13:09 | +5 | XRP | DOWN | 0.58 | 0.63 | 0.15 |
| 10-18 13:08 | +10 stop | XRP | DOWN | 0.64 | 0.44 | -2.35 |
| 10-18 13:07 | +10 stop | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-18 13:07 | +20 | HYPE | DOWN | 0.65 | 0.85 | 1.75 |
| 10-18 13:07 | +15 | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-18 13:07 | +10 | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-18 13:07 | +5 | HYPE | DOWN | 0.65 | 0.71 | 0.29 |
| 10-18 13:07 | +10 stop | BNB | DOWN | 0.61 | 0.75 | 1.09 |
| 10-18 13:07 | +10 stop | BTC | DOWN | 0.59 | 0.76 | 1.40 |
| 10-18 13:05 | +10 stop | BTC | DOWN | 0.64 | 0.45 | -2.25 |
| 10-18 13:05 | +10 stop | DOGE | DOWN | 0.67 | 0.52 | -1.84 |
| 10-18 13:05 | +10 stop | BNB | DOWN | 0.68 | 0.53 | -1.84 |
| 10-18 13:05 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 10-18 13:04 | +10 stop | DOGE | DOWN | 0.71 | 0.55 | -1.93 |
| 10-18 13:04 | +20 | DOGE | DOWN | 0.71 | 0.92 | 1.84 |
| 10-18 13:04 | +15 | DOGE | DOWN | 0.71 | 0.92 | 1.84 |
| 10-18 13:04 | +10 | DOGE | DOWN | 0.71 | 0.92 | 1.84 |
| 10-18 13:04 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-18 13:04 | +10 stop | BTC | DOWN | 0.66 | 0.49 | -2.04 |
| 10-18 13:04 | +10 | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-18 13:04 | +5 | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-18 13:04 | +5 | XRP | DOWN | 0.68 | 0.73 | 0.20 |
| 10-18 13:01 | +10 stop | BNB | DOWN | 0.68 | 0.53 | -1.84 |
| 10-18 13:01 | +20 | BNB | DOWN | 0.68 | 0.94 | 2.38 |
| 10-18 13:01 | +15 | BNB | DOWN | 0.68 | 0.87 | 1.66 |
| 10-18 13:01 | +10 | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 10-18 13:01 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.51 |
| 10-18 13:01 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-18 13:01 | +20 | BTC | DOWN | 0.64 | 0.85 | 1.84 |
| 10-18 13:01 | +15 | BTC | DOWN | 0.64 | 0.82 | 1.52 |
| 10-18 13:01 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-18 13:01 | +5 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-18 13:01 | +10 stop | XRP | DOWN | 0.71 | 0.45 | -2.93 |
| 10-18 13:01 | +20 | XRP | DOWN | 0.71 | open |  |
| 10-18 13:01 | +15 | XRP | DOWN | 0.71 | open |  |
| 10-18 13:01 | +10 | XRP | DOWN | 0.71 | open |  |
| 10-18 13:01 | +5 | XRP | DOWN | 0.71 | 0.79 | 0.53 |
| 10-18 13:01 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.87 |
| 10-18 13:01 | +20 | ZEC | DOWN | 0.71 | 0.92 | 1.92 |
