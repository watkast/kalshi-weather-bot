# Range-Scalp Bot

*Updated Sun Nov 01 04:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43184 | 37642 | 5542 (62) | 2 | $-12283.15 | -4.5% |
| **+10¢** | 32202 | 25798 | 6404 (84) | 3 | $-11007.57 | -5.4% |
| **+15¢** | 26943 | 20042 | 6901 (112) | 3 | $-10066.17 | -6.0% |
| **+20¢** | 23927 | 16697 | 7230 (146) | 3 | $-8896.20 | -5.9% |
| **+10¢ (15¢ stop)** | 52658 | 52575 | 83 (48) | 0 | $-19917.04 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 04:07 | +10 stop | HYPE | UP | 0.62 | 0.74 | 0.85 |
| 11-01 04:07 | +5 | HYPE | UP | 0.68 | 0.74 | 0.30 |
| 11-01 04:06 | +10 stop | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 11-01 04:05 | +10 stop | HYPE | DOWN | 0.49 | 0.34 | -1.84 |
| 11-01 04:05 | +10 | HYPE | DOWN | 0.49 | open |  |
| 11-01 04:05 | +5 | HYPE | DOWN | 0.49 | 0.56 | 0.34 |
| 11-01 04:05 | +5 | DOGE | UP | 0.64 | open |  |
| 11-01 04:05 | +10 stop | HYPE | UP | 0.20 | 0.55 | 3.20 |
| 11-01 04:05 | +10 stop | DOGE | UP | 0.59 | 0.40 | -2.24 |
| 11-01 04:05 | +5 | DOGE | UP | 0.59 | 0.66 | 0.37 |
| 11-01 04:04 | +10 stop | NEAR | DOWN | 0.62 | 0.75 | 1.01 |
| 11-01 04:04 | +10 | NEAR | DOWN | 0.62 | 0.75 | 1.01 |
| 11-01 04:04 | +5 | NEAR | DOWN | 0.62 | 0.69 | 0.39 |
| 11-01 04:03 | +10 stop | BNB | DOWN | 0.58 | 0.72 | 1.07 |
| 11-01 04:02 | +10 stop | DOGE | DOWN | 0.57 | 0.29 | -3.13 |
| 11-01 04:02 | +5 | HYPE | DOWN | 0.68 | 0.75 | 0.40 |
| 11-01 04:01 | +10 stop | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 11-01 04:01 | +20 | NEAR | DOWN | 0.59 | 0.80 | 1.81 |
| 11-01 04:01 | +15 | NEAR | DOWN | 0.59 | 0.75 | 1.29 |
| 11-01 04:01 | +10 | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 11-01 04:01 | +5 | NEAR | DOWN | 0.59 | 0.65 | 0.27 |
| 11-01 04:01 | +10 stop | BTC | DOWN | 0.60 | 0.74 | 1.09 |
| 11-01 04:01 | +20 | BTC | DOWN | 0.60 | 0.80 | 1.71 |
| 11-01 04:01 | +15 | BTC | DOWN | 0.60 | 0.80 | 1.71 |
| 11-01 04:01 | +10 | BTC | DOWN | 0.60 | 0.74 | 1.09 |
| 11-01 04:01 | +5 | BTC | DOWN | 0.60 | 0.68 | 0.47 |
| 11-01 04:01 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-01 04:01 | +20 | XRP | DOWN | 0.71 | 0.92 | 1.91 |
| 11-01 04:01 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 11-01 04:01 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-01 04:01 | +5 | XRP | DOWN | 0.71 | 0.77 | 0.32 |
| 11-01 04:01 | +10 stop | DOGE | UP | 0.62 | 0.44 | -2.15 |
| 11-01 04:01 | +20 | DOGE | UP | 0.62 | open |  |
| 11-01 04:01 | +15 | DOGE | UP | 0.62 | open |  |
| 11-01 04:01 | +10 | DOGE | UP | 0.62 | open |  |
| 11-01 04:01 | +5 | DOGE | UP | 0.62 | 0.69 | 0.38 |
| 11-01 04:00 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-01 04:00 | +20 | SOL | DOWN | 0.69 | 0.90 | 1.92 |
| 11-01 04:00 | +15 | SOL | DOWN | 0.68 | 0.90 | 2.01 |
| 11-01 04:00 | +10 | SOL | DOWN | 0.68 | 0.79 | 0.82 |
