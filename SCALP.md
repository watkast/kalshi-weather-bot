# Range-Scalp Bot

*Updated Sun Nov 01 01:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43038 | 37519 | 5519 (62) | 0 | $-12194.95 | -4.5% |
| **+10¢** | 32096 | 25717 | 6379 (84) | 0 | $-10934.96 | -5.4% |
| **+15¢** | 26846 | 19968 | 6878 (112) | 0 | $-10032.82 | -6.0% |
| **+20¢** | 23846 | 16642 | 7204 (145) | 1 | $-8852.85 | -5.9% |
| **+10¢ (15¢ stop)** | 52489 | 52406 | 83 (48) | 0 | $-19876.42 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 01:49 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-01 01:49 | +10 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-01 01:49 | +5 | NEAR | DOWN | 0.68 | 0.73 | 0.20 |
| 11-01 01:47 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.80 |
| 11-01 01:47 | +20 | HYPE | DOWN | 0.70 | open |  |
| 11-01 01:47 | +15 | HYPE | DOWN | 0.70 | 0.86 | 1.31 |
| 11-01 01:47 | +10 | HYPE | DOWN | 0.70 | 0.81 | 0.79 |
| 11-01 01:47 | +5 | HYPE | DOWN | 0.70 | 0.81 | 0.79 |
| 11-01 01:47 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 11-01 01:46 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 11-01 01:46 | +20 | NEAR | DOWN | 0.61 | 0.83 | 1.93 |
| 11-01 01:46 | +15 | NEAR | DOWN | 0.61 | 0.77 | 1.30 |
| 11-01 01:46 | +10 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 11-01 01:46 | +5 | NEAR | DOWN | 0.61 | 0.66 | 0.17 |
| 11-01 01:41 | +10 stop | BNB | DOWN | 0.54 | 0.65 | 0.72 |
| 11-01 01:40 | +10 stop | BNB | UP | 0.63 | 0.35 | -3.13 |
| 11-01 01:40 | +20 | BNB | UP | 0.63 | 0.90 | 2.46 |
| 11-01 01:40 | +15 | BNB | UP | 0.63 | 0.79 | 1.31 |
| 11-01 01:40 | +10 | BNB | UP | 0.63 | 0.79 | 1.31 |
| 11-01 01:40 | +5 | BNB | UP | 0.62 | 0.79 | 1.41 |
| 11-01 01:33 | +5 | XRP | UP | 0.66 | 0.76 | 0.71 |
| 11-01 01:33 | +5 | HYPE | UP | 0.55 | 0.63 | 0.45 |
| 11-01 01:32 | +10 stop | ZEC | UP | 0.59 | 0.72 | 0.98 |
| 11-01 01:32 | +5 | ZEC | UP | 0.63 | 0.72 | 0.58 |
| 11-01 01:32 | +10 | BNB | UP | 0.71 | 0.81 | 0.74 |
| 11-01 01:32 | +5 | BNB | UP | 0.71 | 0.80 | 0.63 |
| 11-01 01:31 | +10 stop | XRP | UP | 0.65 | 0.76 | 0.81 |
| 11-01 01:31 | +20 | XRP | UP | 0.65 | 0.88 | 2.06 |
| 11-01 01:31 | +15 | XRP | UP | 0.65 | 0.88 | 2.06 |
| 11-01 01:31 | +10 | XRP | UP | 0.65 | 0.76 | 0.81 |
| 11-01 01:31 | +5 | XRP | UP | 0.65 | 0.72 | 0.39 |
| 11-01 01:31 | +10 stop | ZEC | DOWN | 0.53 | 0.33 | -2.34 |
| 11-01 01:31 | +20 | ZEC | DOWN | 0.53 | yes | -5.48 |
| 11-01 01:31 | +15 | ZEC | DOWN | 0.53 | yes | -5.48 |
| 11-01 01:31 | +10 | ZEC | DOWN | 0.53 | yes | -5.48 |
| 11-01 01:31 | +5 | ZEC | DOWN | 0.54 | 0.59 | 0.15 |
| 11-01 01:31 | +10 stop | SOL | UP | 0.66 | 0.78 | 0.91 |
| 11-01 01:31 | +20 | SOL | UP | 0.66 | 0.90 | 2.19 |
| 11-01 01:31 | +15 | SOL | UP | 0.66 | 0.81 | 1.23 |
| 11-01 01:31 | +10 | SOL | UP | 0.66 | 0.78 | 0.91 |
