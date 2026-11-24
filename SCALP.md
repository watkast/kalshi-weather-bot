# Range-Scalp Bot

*Updated Tue Nov 24 00:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70320 | 61374 | 8946 (147) | 1 | $-18840.83 | -4.3% |
| **+10¢** | 52464 | 42015 | 10449 (190) | 0 | $-17480.68 | -5.3% |
| **+15¢** | 43950 | 32695 | 11255 (246) | 0 | $-15581.31 | -5.7% |
| **+20¢** | 39132 | 27286 | 11846 (311) | 0 | $-13952.48 | -5.7% |
| **+10¢ (15¢ stop)** | 85635 | 85439 | 196 (118) | 0 | $-31487.81 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 00:08 | +15 | DOGE | DOWN | 0.68 | 0.86 | 1.55 |
| 11-24 00:08 | +10 stop | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-24 00:08 | +10 | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-24 00:08 | +5 | DOGE | DOWN | 0.67 | 0.74 | 0.40 |
| 11-24 00:07 | +10 stop | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 11-24 00:07 | +10 | BTC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-24 00:07 | +5 | BTC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-24 00:07 | +10 stop | DOGE | DOWN | 0.43 | 0.55 | 0.84 |
| 11-24 00:07 | +20 | DOGE | DOWN | 0.43 | 0.66 | 1.96 |
| 11-24 00:07 | +15 | DOGE | DOWN | 0.43 | 0.58 | 1.14 |
| 11-24 00:07 | +10 | DOGE | DOWN | 0.43 | 0.55 | 0.84 |
| 11-24 00:07 | +5 | DOGE | DOWN | 0.44 | 0.55 | 0.74 |
| 11-24 00:04 | +10 stop | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-24 00:03 | +5 | DOGE | DOWN | 0.61 | 0.68 | 0.37 |
| 11-24 00:03 | +10 stop | HYPE | UP | 0.56 | 0.37 | -2.25 |
| 11-24 00:03 | +5 | HYPE | UP | 0.56 | open |  |
| 11-24 00:02 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-24 00:02 | +20 | XRP | DOWN | 0.70 | 0.94 | 2.22 |
| 11-24 00:02 | +15 | XRP | DOWN | 0.70 | 0.87 | 1.47 |
| 11-24 00:02 | +10 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-24 00:02 | +5 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-24 00:02 | +5 | BTC | DOWN | 0.63 | 0.69 | 0.28 |
| 11-24 00:02 | +10 | ZEC | DOWN | 0.50 | 0.67 | 1.36 |
| 11-24 00:02 | +5 | ZEC | DOWN | 0.50 | 0.57 | 0.34 |
| 11-24 00:02 | +10 stop | DOGE | DOWN | 0.53 | 0.68 | 1.16 |
| 11-24 00:02 | +15 | DOGE | DOWN | 0.53 | 0.68 | 1.16 |
| 11-24 00:02 | +10 | DOGE | DOWN | 0.54 | 0.68 | 1.06 |
| 11-24 00:02 | +5 | DOGE | DOWN | 0.55 | 0.62 | 0.35 |
| 11-24 00:02 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 11-24 00:01 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 11-24 00:01 | +20 | NEAR | DOWN | 0.62 | 0.82 | 1.72 |
| 11-24 00:01 | +15 | NEAR | DOWN | 0.62 | 0.77 | 1.20 |
| 11-24 00:01 | +10 | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 11-24 00:01 | +5 | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 11-24 00:01 | +5 | HYPE | DOWN | 0.58 | 0.65 | 0.36 |
| 11-24 00:01 | +10 stop | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 11-24 00:01 | +20 | ETH | DOWN | 0.66 | 0.87 | 1.86 |
| 11-24 00:01 | +15 | ETH | DOWN | 0.66 | 0.87 | 1.86 |
| 11-24 00:01 | +10 | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 11-24 00:01 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
