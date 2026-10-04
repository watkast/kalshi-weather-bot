# Range-Scalp Bot

*Updated Sun Oct 04 08:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1973 | 1704 | 269 (3) | 1 | $-642.40 | -5.1% |
| **+10¢** | 1536 | 1237 | 299 (4) | 1 | $-460.06 | -4.7% |
| **+15¢** | 1293 | 976 | 317 (5) | 1 | $-384.85 | -4.7% |
| **+20¢** | 1144 | 809 | 335 (7) | 1 | $-355.15 | -4.9% |
| **+10¢ (15¢ stop)** | 2466 | 2465 | 1 (1) | 0 | $-965.83 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 07:56 | +10 stop | NEAR | UP | 0.57 | 0.67 | 0.66 |
| 10-04 07:56 | +20 | NEAR | UP | 0.59 | 0.89 | 2.76 |
| 10-04 07:56 | +15 | NEAR | UP | 0.59 | 0.89 | 2.76 |
| 10-04 07:56 | +10 | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 10-04 07:56 | +5 | NEAR | UP | 0.59 | 0.67 | 0.48 |
| 10-04 07:55 | +10 stop | HYPE | DOWN | 0.68 | 0.22 | -4.89 |
| 10-04 07:55 | +10 stop | SOL | DOWN | 0.66 | 0.49 | -2.03 |
| 10-04 07:52 | +10 stop | NEAR | UP | 0.60 | 0.80 | 1.75 |
| 10-04 07:52 | +20 | NEAR | UP | 0.59 | 0.80 | 1.76 |
| 10-04 07:52 | +15 | NEAR | UP | 0.59 | 0.80 | 1.76 |
| 10-04 07:52 | +10 | NEAR | UP | 0.60 | 0.80 | 1.75 |
| 10-04 07:52 | +5 | NEAR | UP | 0.60 | 0.80 | 1.75 |
| 10-04 07:52 | +10 stop | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-04 07:52 | +15 | ZEC | DOWN | 0.64 | 0.79 | 1.21 |
| 10-04 07:52 | +10 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-04 07:52 | +5 | ZEC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-04 07:50 | +10 stop | SOL | UP | 0.64 | 0.43 | -2.45 |
| 10-04 07:50 | +10 stop | HYPE | UP | 0.48 | 0.28 | -2.33 |
| 10-04 07:50 | +10 stop | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-04 07:50 | +10 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-04 07:50 | +5 | ZEC | DOWN | 0.71 | 0.83 | 0.97 |
| 10-04 07:49 | +10 stop | NEAR | UP | 0.63 | 0.81 | 1.49 |
| 10-04 07:49 | +15 | NEAR | UP | 0.64 | 0.81 | 1.41 |
| 10-04 07:49 | +10 | NEAR | UP | 0.66 | 0.81 | 1.23 |
| 10-04 07:49 | +5 | NEAR | UP | 0.66 | 0.81 | 1.23 |
| 10-04 07:48 | +10 stop | SOL | DOWN | 0.60 | 0.44 | -1.95 |
| 10-04 07:48 | +10 | SOL | DOWN | 0.60 | 0.81 | 1.82 |
| 10-04 07:48 | +5 | SOL | DOWN | 0.60 | 0.81 | 1.82 |
| 10-04 07:48 | +5 | HYPE | DOWN | 0.68 | open |  |
| 10-04 07:48 | +10 stop | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-04 07:47 | +5 | NEAR | UP | 0.66 | 0.71 | 0.24 |
| 10-04 07:46 | +10 stop | HYPE | DOWN | 0.66 | 0.47 | -2.24 |
| 10-04 07:46 | +20 | HYPE | DOWN | 0.66 | open |  |
| 10-04 07:46 | +15 | HYPE | DOWN | 0.66 | open |  |
| 10-04 07:46 | +10 | HYPE | DOWN | 0.66 | open |  |
| 10-04 07:46 | +5 | HYPE | DOWN | 0.66 | 0.72 | 0.29 |
| 10-04 07:46 | +10 stop | ZEC | DOWN | 0.66 | 0.44 | -2.54 |
| 10-04 07:46 | +20 | ZEC | DOWN | 0.66 | 0.90 | 2.18 |
| 10-04 07:46 | +15 | ZEC | DOWN | 0.66 | 0.83 | 1.44 |
| 10-04 07:46 | +10 | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
