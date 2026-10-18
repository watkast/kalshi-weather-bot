# Range-Scalp Bot

*Updated Sun Oct 18 07:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22182 | 19309 | 2873 (29) | 0 | $-6466.50 | -4.6% |
| **+10¢** | 16701 | 13384 | 3317 (42) | 0 | $-5732.67 | -5.5% |
| **+15¢** | 13988 | 10411 | 3577 (62) | 0 | $-5215.77 | -5.9% |
| **+20¢** | 12379 | 8630 | 3749 (80) | 0 | $-4682.34 | -6.0% |
| **+10¢ (15¢ stop)** | 27285 | 27235 | 50 (29) | 0 | $-10421.07 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 06:53 | +10 stop | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 10-18 06:51 | +10 stop | DOGE | DOWN | 0.57 | 0.67 | 0.67 |
| 10-18 06:50 | +10 stop | SOL | DOWN | 0.60 | 0.71 | 0.82 |
| 10-18 06:49 | +10 stop | XRP | DOWN | 0.58 | 0.68 | 0.68 |
| 10-18 06:48 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 10-18 06:48 | +10 stop | SOL | DOWN | 0.57 | 0.70 | 0.96 |
| 10-18 06:48 | +10 stop | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-18 06:48 | +20 | ZEC | DOWN | 0.65 | 0.86 | 1.85 |
| 10-18 06:48 | +15 | ZEC | DOWN | 0.65 | 0.81 | 1.33 |
| 10-18 06:48 | +10 | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-18 06:48 | +5 | ZEC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-18 06:47 | +10 stop | DOGE | DOWN | 0.67 | 0.45 | -2.54 |
| 10-18 06:47 | +10 stop | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 10-18 06:47 | +20 | NEAR | DOWN | 0.62 | 0.83 | 1.83 |
| 10-18 06:47 | +15 | NEAR | DOWN | 0.62 | 0.78 | 1.30 |
| 10-18 06:47 | +10 | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 10-18 06:47 | +5 | NEAR | DOWN | 0.62 | 0.71 | 0.58 |
| 10-18 06:47 | +5 | BNB | DOWN | 0.70 | 0.76 | 0.32 |
| 10-18 06:46 | +10 stop | HYPE | DOWN | 0.63 | 0.74 | 0.75 |
| 10-18 06:46 | +20 | HYPE | DOWN | 0.66 | 0.87 | 1.82 |
| 10-18 06:46 | +15 | HYPE | DOWN | 0.66 | 0.82 | 1.29 |
| 10-18 06:46 | +10 | HYPE | DOWN | 0.66 | 0.78 | 0.87 |
| 10-18 06:46 | +5 | HYPE | DOWN | 0.66 | 0.74 | 0.46 |
| 10-18 06:46 | +10 stop | SOL | UP | 0.55 | 0.36 | -2.25 |
| 10-18 06:46 | +20 | SOL | UP | 0.55 | no | -5.68 |
| 10-18 06:46 | +15 | SOL | UP | 0.55 | 0.73 | 1.48 |
| 10-18 06:46 | +10 | SOL | UP | 0.55 | 0.73 | 1.48 |
| 10-18 06:46 | +5 | SOL | UP | 0.55 | 0.73 | 1.48 |
| 10-18 06:46 | +5 | DOGE | UP | 0.55 | 0.95 | 3.79 |
| 10-18 06:46 | +10 stop | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 10-18 06:46 | +20 | BNB | DOWN | 0.64 | 0.84 | 1.73 |
| 10-18 06:46 | +15 | BNB | DOWN | 0.64 | 0.84 | 1.73 |
| 10-18 06:46 | +10 | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 10-18 06:46 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.18 |
| 10-18 06:45 | +10 stop | XRP | UP | 0.52 | 0.27 | -2.82 |
| 10-18 06:45 | +20 | XRP | UP | 0.52 | no | -5.38 |
| 10-18 06:45 | +15 | XRP | UP | 0.52 | no | -5.38 |
| 10-18 06:45 | +10 | XRP | UP | 0.52 | no | -5.38 |
| 10-18 06:45 | +5 | XRP | UP | 0.52 | no | -5.38 |
| 10-18 06:45 | +10 stop | DOGE | UP | 0.59 | 0.42 | -2.05 |
