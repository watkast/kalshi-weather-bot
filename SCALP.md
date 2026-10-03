# Range-Scalp Bot

*Updated Sat Oct 03 04:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 173 | 147 | 26 (1) | 0 | $-69.77 | -6.3% |
| **+10¢** | 146 | 120 | 26 (1) | 0 | $-25.20 | -2.7% |
| **+15¢** | 120 | 93 | 27 (1) | 0 | $-20.32 | -2.7% |
| **+20¢** | 325 | 231 | 94 (2) | 0 | $-84.01 | -4.1% |
| **+10¢ (15¢ stop)** | 239 | 239 | 0 (0) | 0 | $-105.28 | -7.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 04:24 | +10 stop | XRP | DOWN | 0.61 | 0.45 | -1.95 |
| 10-03 04:24 | +15 | XRP | DOWN | 0.61 | 0.79 | 1.51 |
| 10-03 04:24 | +10 | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 10-03 04:24 | +5 | XRP | DOWN | 0.61 | 0.70 | 0.58 |
| 10-03 04:19 | +10 stop | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 10-03 04:19 | +20 | XRP | DOWN | 0.71 | 0.95 | 2.19 |
| 10-03 04:19 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-03 04:19 | +10 | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 10-03 04:19 | +5 | XRP | DOWN | 0.71 | 0.79 | 0.53 |
| 10-03 04:18 | +10 stop | SOL | DOWN | 0.64 | 0.78 | 1.10 |
| 10-03 04:18 | +20 | SOL | DOWN | 0.64 | 0.89 | 2.26 |
| 10-03 04:18 | +15 | SOL | DOWN | 0.64 | 0.80 | 1.31 |
| 10-03 04:18 | +10 | SOL | DOWN | 0.64 | 0.78 | 1.10 |
| 10-03 04:18 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 10-03 04:18 | +10 stop | ZEC | DOWN | 0.56 | 0.76 | 1.69 |
| 10-03 04:18 | +20 | ZEC | DOWN | 0.56 | 0.76 | 1.69 |
| 10-03 04:18 | +15 | ZEC | DOWN | 0.56 | 0.76 | 1.69 |
| 10-03 04:18 | +10 | ZEC | DOWN | 0.56 | 0.76 | 1.69 |
| 10-03 04:18 | +5 | ZEC | DOWN | 0.56 | 0.63 | 0.35 |
| 10-03 04:17 | +15 | HYPE | DOWN | 0.61 | 0.82 | 1.77 |
| 10-03 04:16 | +10 stop | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 10-03 04:16 | +10 | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 10-03 04:16 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.37 |
| 10-03 04:16 | +10 stop | HYPE | DOWN | 0.48 | 0.62 | 1.05 |
| 10-03 04:16 | +20 | HYPE | DOWN | 0.48 | 0.68 | 1.66 |
| 10-03 04:16 | +15 | HYPE | DOWN | 0.48 | 0.65 | 1.36 |
| 10-03 04:16 | +10 | HYPE | DOWN | 0.48 | 0.62 | 1.05 |
| 10-03 04:16 | +5 | HYPE | DOWN | 0.48 | 0.62 | 1.05 |
| 10-03 04:11 | +10 stop | BNB | DOWN | 0.71 | 0.18 | -5.56 |
| 10-03 04:11 | +15 | BNB | DOWN | 0.71 | yes | -7.25 |
| 10-03 04:11 | +10 | BNB | DOWN | 0.71 | yes | -7.25 |
| 10-03 04:11 | +5 | BNB | DOWN | 0.71 | yes | -7.25 |
| 10-03 04:09 | +10 stop | BNB | DOWN | 0.59 | 0.78 | 1.60 |
| 10-03 04:08 | +10 stop | BNB | UP | 0.64 | 0.42 | -2.54 |
| 10-03 04:08 | +10 stop | BTC | UP | 0.62 | 0.35 | -3.03 |
| 10-03 04:07 | +10 stop | BTC | UP | 0.59 | 0.69 | 0.68 |
| 10-03 04:06 | +10 stop | XRP | DOWN | 0.57 | 0.71 | 1.08 |
| 10-03 04:06 | +5 | SOL | UP | 0.66 | 0.83 | 1.44 |
| 10-03 04:06 | +10 stop | SOL | UP | 0.66 | 0.83 | 1.44 |
| 10-03 04:05 | +10 stop | BTC | UP | 0.69 | 0.54 | -1.83 |
