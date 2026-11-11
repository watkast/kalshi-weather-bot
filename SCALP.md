# Range-Scalp Bot

*Updated Wed Nov 11 04:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55390 | 48304 | 7086 (94) | 0 | $-15142.88 | -4.3% |
| **+10¢** | 41377 | 33109 | 8268 (124) | 0 | $-14097.18 | -5.4% |
| **+15¢** | 34691 | 25778 | 8913 (158) | 1 | $-12855.45 | -5.9% |
| **+20¢** | 30891 | 21542 | 9349 (207) | 1 | $-11246.05 | -5.8% |
| **+10¢ (15¢ stop)** | 67454 | 67336 | 118 (73) | 0 | $-24864.39 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 04:16 | +10 stop | HYPE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-11 04:16 | +20 | HYPE | DOWN | 0.71 | open |  |
| 11-11 04:16 | +15 | HYPE | DOWN | 0.71 | open |  |
| 11-11 04:16 | +10 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-11 04:16 | +5 | HYPE | DOWN | 0.71 | 0.79 | 0.53 |
| 11-11 04:13 | +10 stop | HYPE | UP | 0.57 | 0.17 | -4.28 |
| 11-11 04:10 | +10 stop | XRP | UP | 0.69 | 0.51 | -2.13 |
| 11-11 04:10 | +20 | XRP | UP | 0.69 | no | -7.05 |
| 11-11 04:10 | +15 | XRP | UP | 0.69 | no | -7.05 |
| 11-11 04:10 | +10 | XRP | UP | 0.69 | no | -7.05 |
| 11-11 04:10 | +10 stop | HYPE | UP | 0.71 | 0.31 | -4.30 |
| 11-11 04:10 | +20 | HYPE | UP | 0.71 | no | -7.25 |
| 11-11 04:10 | +15 | HYPE | UP | 0.71 | no | -7.25 |
| 11-11 04:10 | +10 | HYPE | UP | 0.71 | no | -7.25 |
| 11-11 04:10 | +5 | HYPE | UP | 0.71 | no | -7.25 |
| 11-11 04:10 | +10 stop | SOL | UP | 0.54 | 0.66 | 0.86 |
| 11-11 04:08 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 11-11 04:07 | +10 stop | XRP | UP | 0.55 | 0.65 | 0.66 |
| 11-11 04:07 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 11-11 04:07 | +20 | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 11-11 04:07 | +15 | ZEC | DOWN | 0.65 | 0.82 | 1.43 |
| 11-11 04:07 | +10 | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 11-11 04:07 | +5 | ZEC | DOWN | 0.65 | 0.70 | 0.19 |
| 11-11 04:06 | +10 stop | SOL | UP | 0.59 | 0.74 | 1.19 |
| 11-11 04:05 | +10 stop | XRP | UP | 0.58 | 0.42 | -1.96 |
| 11-11 04:05 | +20 | XRP | UP | 0.58 | 0.81 | 2.01 |
| 11-11 04:05 | +15 | XRP | UP | 0.58 | 0.75 | 1.38 |
| 11-11 04:05 | +10 | XRP | UP | 0.58 | 0.71 | 0.97 |
| 11-11 04:05 | +10 stop | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 11-11 04:05 | +10 stop | ZEC | UP | 0.53 | 0.28 | -2.83 |
| 11-11 04:04 | +5 | ZEC | UP | 0.54 | 0.67 | 0.96 |
| 11-11 04:04 | +10 stop | SOL | UP | 0.64 | 0.75 | 0.79 |
| 11-11 04:02 | +10 stop | ZEC | UP | 0.57 | 0.67 | 0.66 |
| 11-11 04:02 | +5 | ZEC | UP | 0.57 | 0.65 | 0.46 |
| 11-11 04:02 | +10 stop | HYPE | UP | 0.70 | 0.85 | 1.26 |
| 11-11 04:02 | +5 | HYPE | UP | 0.69 | 0.85 | 1.32 |
| 11-11 04:02 | +10 stop | SOL | UP | 0.59 | 0.69 | 0.68 |
| 11-11 04:02 | +10 stop | XRP | DOWN | 0.59 | 0.32 | -3.03 |
| 11-11 04:02 | +5 | BTC | UP | 0.69 | 0.77 | 0.52 |
| 11-11 04:02 | +5 | NEAR | DOWN | 0.57 | 0.72 | 1.17 |
