# Range-Scalp Bot

*Updated Tue Nov 17 06:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62698 | 54691 | 8007 (117) | 0 | $-17053.25 | -4.3% |
| **+10¢** | 46817 | 37444 | 9373 (159) | 0 | $-15974.41 | -5.4% |
| **+15¢** | 39238 | 29129 | 10109 (201) | 0 | $-14532.29 | -5.9% |
| **+20¢** | 34974 | 24374 | 10600 (256) | 0 | $-12706.06 | -5.8% |
| **+10¢ (15¢ stop)** | 76291 | 76135 | 156 (92) | 0 | $-28130.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 06:13 | +10 stop | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 11-17 06:13 | +10 | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 11-17 06:13 | +5 | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 11-17 06:12 | +10 stop | XRP | DOWN | 0.63 | 0.86 | 2.06 |
| 11-17 06:12 | +10 | XRP | DOWN | 0.63 | 0.86 | 2.05 |
| 11-17 06:12 | +5 | XRP | DOWN | 0.61 | 0.86 | 2.24 |
| 11-17 06:11 | +10 stop | XRP | DOWN | 0.50 | 0.71 | 1.77 |
| 11-17 06:11 | +10 stop | ZEC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-17 06:11 | +10 | ZEC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-17 06:11 | +5 | ZEC | DOWN | 0.58 | 0.70 | 0.87 |
| 11-17 06:10 | +10 stop | HYPE | UP | 0.52 | 0.26 | -2.92 |
| 11-17 06:10 | +10 stop | XRP | UP | 0.68 | 0.37 | -3.43 |
| 11-17 06:10 | +10 stop | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-17 06:10 | +20 | SOL | DOWN | 0.66 | 0.86 | 1.75 |
| 11-17 06:10 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-17 06:10 | +10 | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 11-17 06:10 | +5 | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 11-17 06:10 | +5 | ETH | DOWN | 0.52 | 0.65 | 0.96 |
| 11-17 06:09 | +15 | HYPE | DOWN | 0.60 | 0.79 | 1.61 |
| 11-17 06:09 | +10 | HYPE | DOWN | 0.60 | 0.71 | 0.78 |
| 11-17 06:09 | +5 | HYPE | DOWN | 0.60 | 0.71 | 0.78 |
| 11-17 06:09 | +10 stop | XRP | DOWN | 0.63 | 0.40 | -2.64 |
| 11-17 06:09 | +10 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 11-17 06:09 | +5 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 11-17 06:09 | +10 stop | ETH | DOWN | 0.65 | 0.50 | -1.84 |
| 11-17 06:08 | +5 | HYPE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-17 06:08 | +10 stop | HYPE | DOWN | 0.64 | 0.43 | -2.45 |
| 11-17 06:07 | +10 stop | ETH | UP | 0.51 | 0.36 | -1.85 |
| 11-17 06:07 | +5 | SOL | DOWN | 0.70 | 0.75 | 0.21 |
| 11-17 06:06 | +10 stop | BNB | DOWN | 0.60 | 0.80 | 1.71 |
| 11-17 06:06 | +5 | SOL | DOWN | 0.61 | 0.66 | 0.17 |
| 11-17 06:06 | +5 | BNB | DOWN | 0.68 | 0.80 | 0.92 |
| 11-17 06:06 | +10 stop | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 11-17 06:06 | +10 | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 11-17 06:06 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 11-17 06:06 | +10 stop | ZEC | UP | 0.57 | 0.67 | 0.66 |
| 11-17 06:06 | +10 stop | HYPE | UP | 0.60 | 0.44 | -1.95 |
| 11-17 06:06 | +10 stop | BTC | DOWN | 0.71 | 0.84 | 1.05 |
| 11-17 06:06 | +10 stop | NEAR | DOWN | 0.66 | 0.80 | 1.12 |
| 11-17 06:05 | +10 stop | BNB | UP | 0.50 | 0.33 | -2.04 |
