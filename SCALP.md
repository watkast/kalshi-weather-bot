# Range-Scalp Bot

*Updated Tue Nov 17 06:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62708 | 54701 | 8007 (117) | 2 | $-17048.21 | -4.3% |
| **+10¢** | 46826 | 37453 | 9373 (159) | 2 | $-15964.29 | -5.4% |
| **+15¢** | 39245 | 29136 | 10109 (201) | 2 | $-14522.42 | -5.9% |
| **+20¢** | 34980 | 24380 | 10600 (256) | 2 | $-12693.07 | -5.8% |
| **+10¢ (15¢ stop)** | 76302 | 76146 | 156 (92) | 0 | $-28125.85 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 06:25 | +10 stop | DOGE | DOWN | 0.66 | 0.46 | -2.34 |
| 11-17 06:25 | +20 | DOGE | DOWN | 0.65 | open |  |
| 11-17 06:25 | +15 | DOGE | DOWN | 0.65 | open |  |
| 11-17 06:25 | +10 | DOGE | DOWN | 0.63 | open |  |
| 11-17 06:25 | +5 | DOGE | DOWN | 0.62 | open |  |
| 11-17 06:24 | +10 stop | HYPE | DOWN | 0.58 | 0.36 | -2.55 |
| 11-17 06:24 | +15 | HYPE | DOWN | 0.58 | open |  |
| 11-17 06:24 | +10 | HYPE | DOWN | 0.58 | open |  |
| 11-17 06:24 | +5 | HYPE | DOWN | 0.57 | open |  |
| 11-17 06:21 | +10 stop | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-17 06:21 | +10 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-17 06:21 | +5 | HYPE | DOWN | 0.66 | 0.73 | 0.40 |
| 11-17 06:18 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
| 11-17 06:18 | +10 stop | DOGE | DOWN | 0.64 | 0.82 | 1.52 |
| 11-17 06:18 | +10 | DOGE | DOWN | 0.64 | 0.82 | 1.52 |
| 11-17 06:18 | +5 | DOGE | DOWN | 0.60 | 0.65 | 0.17 |
| 11-17 06:17 | +10 stop | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 11-17 06:17 | +20 | ZEC | DOWN | 0.68 | 0.94 | 2.36 |
| 11-17 06:17 | +15 | ZEC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-17 06:17 | +10 | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 11-17 06:17 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-17 06:17 | +10 stop | SOL | DOWN | 0.66 | 0.84 | 1.54 |
| 11-17 06:17 | +20 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 11-17 06:17 | +15 | SOL | DOWN | 0.66 | 0.84 | 1.54 |
| 11-17 06:17 | +10 | SOL | DOWN | 0.66 | 0.84 | 1.54 |
| 11-17 06:17 | +5 | SOL | DOWN | 0.66 | 0.84 | 1.54 |
| 11-17 06:17 | +10 stop | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-17 06:17 | +20 | BTC | DOWN | 0.67 | 0.92 | 2.32 |
| 11-17 06:17 | +15 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 11-17 06:17 | +10 | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-17 06:17 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-17 06:16 | +10 stop | DOGE | DOWN | 0.60 | 0.70 | 0.68 |
| 11-17 06:16 | +20 | DOGE | DOWN | 0.60 | 0.82 | 1.92 |
| 11-17 06:16 | +15 | DOGE | DOWN | 0.60 | 0.82 | 1.92 |
| 11-17 06:16 | +10 | DOGE | DOWN | 0.60 | 0.70 | 0.68 |
| 11-17 06:16 | +5 | DOGE | DOWN | 0.60 | 0.65 | 0.17 |
| 11-17 06:16 | +10 stop | NEAR | DOWN | 0.70 | 0.83 | 1.06 |
| 11-17 06:16 | +20 | NEAR | DOWN | 0.70 | 0.95 | 2.32 |
| 11-17 06:16 | +15 | NEAR | DOWN | 0.69 | 0.84 | 1.25 |
| 11-17 06:16 | +10 | NEAR | DOWN | 0.69 | 0.83 | 1.15 |
