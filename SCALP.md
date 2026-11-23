# Range-Scalp Bot

*Updated Mon Nov 23 00:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69266 | 60435 | 8831 (146) | 0 | $-18667.88 | -4.3% |
| **+10¢** | 51691 | 41381 | 10310 (189) | 2 | $-17311.16 | -5.3% |
| **+15¢** | 43325 | 32210 | 11115 (244) | 1 | $-15514.72 | -5.7% |
| **+20¢** | 38585 | 26901 | 11684 (305) | 1 | $-13806.73 | -5.7% |
| **+10¢ (15¢ stop)** | 84349 | 84159 | 190 (118) | 0 | $-31036.50 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 00:12 | +10 stop | DOGE | UP | 0.63 | 0.20 | -4.59 |
| 11-23 00:12 | +15 | DOGE | UP | 0.63 | 0.96 | 3.11 |
| 11-23 00:12 | +10 | DOGE | UP | 0.63 | 0.96 | 3.11 |
| 11-23 00:12 | +5 | DOGE | UP | 0.63 | 0.70 | 0.38 |
| 11-23 00:12 | +10 stop | NEAR | UP | 0.59 | 0.75 | 1.29 |
| 11-23 00:10 | +10 stop | BNB | UP | 0.62 | 0.74 | 0.89 |
| 11-23 00:10 | +20 | BNB | UP | 0.62 | 0.88 | 2.35 |
| 11-23 00:10 | +15 | BNB | UP | 0.62 | 0.88 | 2.35 |
| 11-23 00:10 | +10 | BNB | UP | 0.62 | 0.74 | 0.89 |
| 11-23 00:10 | +5 | BNB | UP | 0.62 | 0.74 | 0.89 |
| 11-23 00:09 | +5 | ETH | UP | 0.69 | 0.89 | 1.78 |
| 11-23 00:09 | +10 stop | NEAR | UP | 0.54 | 0.35 | -2.24 |
| 11-23 00:09 | +10 stop | BTC | DOWN | 0.49 | 0.59 | 0.65 |
| 11-23 00:09 | +5 | BTC | DOWN | 0.50 | 0.59 | 0.55 |
| 11-23 00:09 | +10 stop | DOGE | DOWN | 0.58 | 0.82 | 2.11 |
| 11-23 00:08 | +5 | SOL | DOWN | 0.64 | 0.70 | 0.28 |
| 11-23 00:08 | +10 | BTC | DOWN | 0.69 | open |  |
| 11-23 00:06 | +10 stop | DOGE | DOWN | 0.61 | 0.74 | 1.01 |
| 11-23 00:06 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 11-23 00:05 | +5 | BTC | DOWN | 0.56 | 0.64 | 0.45 |
| 11-23 00:05 | +10 stop | NEAR | UP | 0.63 | 0.38 | -2.84 |
| 11-23 00:05 | +20 | NEAR | UP | 0.63 | 0.85 | 1.94 |
| 11-23 00:05 | +15 | NEAR | UP | 0.63 | 0.85 | 1.94 |
| 11-23 00:05 | +10 | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-23 00:05 | +5 | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-23 00:05 | +10 stop | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-23 00:05 | +20 | HYPE | DOWN | 0.67 | 0.92 | 2.28 |
| 11-23 00:05 | +15 | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-23 00:05 | +10 | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-23 00:05 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-23 00:04 | +5 | BNB | UP | 0.68 | 0.74 | 0.30 |
| 11-23 00:04 | +5 | ETH | UP | 0.57 | 0.64 | 0.35 |
| 11-23 00:03 | +5 | BTC | DOWN | 0.55 | 0.62 | 0.35 |
| 11-23 00:03 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-23 00:03 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 11-23 00:03 | +5 | ETH | UP | 0.59 | 0.64 | 0.16 |
| 11-23 00:02 | +10 stop | SOL | DOWN | 0.62 | 0.35 | -3.03 |
| 11-23 00:02 | +20 | SOL | DOWN | 0.62 | open |  |
| 11-23 00:02 | +15 | SOL | DOWN | 0.62 | open |  |
| 11-23 00:02 | +10 | SOL | DOWN | 0.62 | open |  |
