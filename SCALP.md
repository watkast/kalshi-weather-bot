# Range-Scalp Bot

*Updated Tue Nov 10 23:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55025 | 47986 | 7039 (94) | 0 | $-15049.43 | -4.3% |
| **+10¢** | 41119 | 32911 | 8208 (124) | 0 | $-13942.94 | -5.4% |
| **+15¢** | 34474 | 25630 | 8844 (158) | 0 | $-12658.29 | -5.9% |
| **+20¢** | 30688 | 21409 | 9279 (207) | 0 | $-11077.16 | -5.8% |
| **+10¢ (15¢ stop)** | 67042 | 66924 | 118 (73) | 0 | $-24784.11 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 23:11 | +10 stop | HYPE | UP | 0.70 | 0.82 | 0.94 |
| 11-10 23:10 | +10 stop | HYPE | DOWN | 0.42 | 0.58 | 1.19 |
| 11-10 23:09 | +10 stop | HYPE | UP | 0.65 | 0.34 | -3.42 |
| 11-10 23:09 | +10 stop | ZEC | DOWN | 0.55 | 0.67 | 0.86 |
| 11-10 23:08 | +10 | ZEC | DOWN | 0.60 | 0.84 | 2.13 |
| 11-10 23:08 | +10 stop | HYPE | DOWN | 0.58 | 0.36 | -2.59 |
| 11-10 23:07 | +5 | ZEC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-10 23:07 | +10 stop | ZEC | DOWN | 0.68 | 0.53 | -1.84 |
| 11-10 23:06 | +10 stop | HYPE | UP | 0.61 | 0.40 | -2.44 |
| 11-10 23:06 | +10 | HYPE | UP | 0.61 | 0.72 | 0.74 |
| 11-10 23:06 | +5 | HYPE | UP | 0.60 | 0.72 | 0.87 |
| 11-10 23:05 | +10 stop | ZEC | UP | 0.57 | 0.35 | -2.54 |
| 11-10 23:05 | +10 stop | HYPE | UP | 0.56 | 0.66 | 0.66 |
| 11-10 23:05 | +15 | HYPE | UP | 0.56 | 0.72 | 1.27 |
| 11-10 23:05 | +10 | HYPE | UP | 0.56 | 0.66 | 0.66 |
| 11-10 23:05 | +5 | HYPE | UP | 0.56 | 0.66 | 0.66 |
| 11-10 23:04 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-10 23:04 | +20 | DOGE | DOWN | 0.66 | 0.89 | 2.07 |
| 11-10 23:04 | +15 | DOGE | DOWN | 0.66 | 0.89 | 2.07 |
| 11-10 23:04 | +10 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-10 23:04 | +5 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-10 23:04 | +5 | NEAR | UP | 0.66 | no | -6.76 |
| 11-10 23:03 | +10 stop | ZEC | DOWN | 0.61 | 0.42 | -2.25 |
| 11-10 23:03 | +20 | ZEC | DOWN | 0.62 | 0.84 | 1.93 |
| 11-10 23:03 | +15 | ZEC | DOWN | 0.61 | 0.84 | 2.03 |
| 11-10 23:03 | +10 | ZEC | DOWN | 0.59 | 0.71 | 0.88 |
| 11-10 23:03 | +5 | ZEC | DOWN | 0.59 | 0.64 | 0.16 |
| 11-10 23:03 | +5 | SOL | DOWN | 0.63 | 0.71 | 0.48 |
| 11-10 23:03 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-10 23:03 | +20 | XRP | DOWN | 0.71 | 0.94 | 2.11 |
| 11-10 23:03 | +15 | XRP | DOWN | 0.71 | 0.88 | 1.47 |
| 11-10 23:03 | +5 | XRP | DOWN | 0.71 | 0.78 | 0.42 |
| 11-10 23:03 | +5 | ETH | DOWN | 0.69 | 0.80 | 0.86 |
| 11-10 23:02 | +10 stop | HYPE | UP | 0.51 | 0.67 | 1.26 |
| 11-10 23:02 | +20 | HYPE | UP | 0.51 | 0.72 | 1.77 |
| 11-10 23:02 | +15 | HYPE | UP | 0.51 | 0.67 | 1.26 |
| 11-10 23:02 | +10 | HYPE | UP | 0.51 | 0.67 | 1.26 |
| 11-10 23:02 | +5 | HYPE | UP | 0.51 | 0.60 | 0.55 |
| 11-10 23:02 | +10 stop | NEAR | UP | 0.58 | 0.40 | -2.15 |
| 11-10 23:02 | +20 | NEAR | UP | 0.58 | no | -5.98 |
