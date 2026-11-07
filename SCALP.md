# Range-Scalp Bot

*Updated Sat Nov 07 03:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50395 | 43928 | 6467 (76) | 0 | $-14170.91 | -4.5% |
| **+10¢** | 37611 | 30081 | 7530 (102) | 0 | $-13102.60 | -5.5% |
| **+15¢** | 31496 | 23381 | 8115 (131) | 1 | $-12027.86 | -6.1% |
| **+20¢** | 28002 | 19495 | 8507 (173) | 1 | $-10626.88 | -6.1% |
| **+10¢ (15¢ stop)** | 61361 | 61262 | 99 (58) | 0 | $-22715.48 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 03:26 | +10 stop | HYPE | DOWN | 0.53 | 0.75 | 1.89 |
| 11-07 03:25 | +10 stop | HYPE | UP | 0.65 | 0.44 | -2.44 |
| 11-07 03:25 | +10 | HYPE | UP | 0.65 | 0.91 | 2.35 |
| 11-07 03:25 | +5 | HYPE | UP | 0.65 | 0.91 | 2.35 |
| 11-07 03:25 | +10 stop | ETH | DOWN | 0.55 | 0.77 | 1.89 |
| 11-07 03:25 | +20 | ETH | DOWN | 0.55 | 0.77 | 1.89 |
| 11-07 03:25 | +15 | ETH | DOWN | 0.55 | 0.77 | 1.89 |
| 11-07 03:25 | +10 | ETH | DOWN | 0.55 | 0.77 | 1.89 |
| 11-07 03:25 | +5 | ETH | DOWN | 0.55 | 0.61 | 0.25 |
| 11-07 03:22 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-07 03:22 | +20 | HYPE | DOWN | 0.71 | 1.00 | 2.72 |
| 11-07 03:22 | +15 | HYPE | DOWN | 0.71 | 0.87 | 1.37 |
| 11-07 03:22 | +10 | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-07 03:22 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.22 |
| 11-07 03:17 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-07 03:17 | +10 | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-07 03:17 | +5 | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-07 03:16 | +10 stop | ZEC | UP | 0.41 | 0.55 | 1.05 |
| 11-07 03:16 | +20 | ZEC | UP | 0.41 | open |  |
| 11-07 03:16 | +15 | ZEC | UP | 0.41 | open |  |
| 11-07 03:16 | +10 | ZEC | UP | 0.41 | 0.55 | 1.05 |
| 11-07 03:16 | +5 | ZEC | UP | 0.41 | 0.55 | 1.05 |
| 11-07 03:16 | +10 stop | ETH | UP | 0.39 | 0.60 | 1.76 |
| 11-07 03:16 | +20 | ETH | UP | 0.39 | 0.60 | 1.76 |
| 11-07 03:16 | +15 | ETH | UP | 0.39 | 0.60 | 1.76 |
| 11-07 03:16 | +10 | ETH | UP | 0.39 | 0.60 | 1.76 |
| 11-07 03:16 | +5 | ETH | UP | 0.39 | 0.60 | 1.76 |
| 11-07 03:16 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-07 03:16 | +20 | BTC | DOWN | 0.69 | 0.92 | 2.04 |
| 11-07 03:16 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-07 03:16 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-07 03:16 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 11-07 03:16 | +10 stop | HYPE | UP | 0.34 | 0.55 | 1.76 |
| 11-07 03:16 | +20 | HYPE | UP | 0.34 | 0.55 | 1.76 |
| 11-07 03:16 | +15 | HYPE | UP | 0.34 | 0.55 | 1.76 |
| 11-07 03:16 | +10 | HYPE | UP | 0.34 | 0.55 | 1.76 |
| 11-07 03:16 | +5 | HYPE | UP | 0.34 | 0.55 | 1.76 |
| 11-07 03:13 | +10 stop | HYPE | DOWN | 0.38 | 0.60 | 1.86 |
| 11-07 03:13 | +20 | HYPE | DOWN | 0.38 | 0.60 | 1.86 |
| 11-07 03:13 | +15 | HYPE | DOWN | 0.38 | 0.60 | 1.86 |
