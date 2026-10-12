# Range-Scalp Bot

*Updated Mon Oct 12 06:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13175 | 11384 | 1791 (25) | 0 | $-4297.01 | -5.2% |
| **+10¢** | 9988 | 7916 | 2072 (37) | 1 | $-3999.22 | -6.4% |
| **+15¢** | 8400 | 6185 | 2215 (55) | 1 | $-3526.05 | -6.7% |
| **+20¢** | 7481 | 5171 | 2310 (70) | 0 | $-3003.61 | -6.4% |
| **+10¢ (15¢ stop)** | 16224 | 16183 | 41 (25) | 0 | $-6362.03 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 06:35 | +15 | NEAR | UP | 0.70 | open |  |
| 10-12 06:35 | +10 | NEAR | UP | 0.70 | open |  |
| 10-12 06:33 | +10 stop | NEAR | UP | 0.68 | 0.79 | 0.83 |
| 10-12 06:33 | +5 | NEAR | UP | 0.68 | 0.73 | 0.21 |
| 10-12 06:31 | +5 | NEAR | UP | 0.41 | 0.59 | 1.46 |
| 10-12 06:31 | +10 stop | HYPE | UP | 0.60 | 0.71 | 0.78 |
| 10-12 06:31 | +20 | HYPE | UP | 0.60 | 0.83 | 2.03 |
| 10-12 06:31 | +15 | HYPE | UP | 0.60 | 0.79 | 1.57 |
| 10-12 06:31 | +10 | HYPE | UP | 0.60 | 0.71 | 0.74 |
| 10-12 06:31 | +5 | HYPE | UP | 0.60 | 0.68 | 0.43 |
| 10-12 06:30 | +10 stop | NEAR | UP | 0.57 | 0.37 | -2.35 |
| 10-12 06:30 | +20 | NEAR | UP | 0.57 | 0.79 | 1.90 |
| 10-12 06:30 | +15 | NEAR | UP | 0.57 | 0.72 | 1.17 |
| 10-12 06:30 | +10 | NEAR | UP | 0.57 | 0.72 | 1.17 |
| 10-12 06:30 | +5 | NEAR | UP | 0.57 | 0.65 | 0.46 |
| 10-12 06:30 | +10 stop | DOGE | UP | 0.65 | 0.78 | 1.01 |
| 10-12 06:30 | +20 | DOGE | UP | 0.65 | 0.85 | 1.75 |
| 10-12 06:30 | +15 | DOGE | UP | 0.65 | 0.83 | 1.54 |
| 10-12 06:30 | +10 | DOGE | UP | 0.65 | 0.78 | 1.01 |
| 10-12 06:30 | +5 | DOGE | UP | 0.65 | 0.78 | 1.01 |
| 10-12 06:24 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-12 06:24 | +10 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-12 06:24 | +5 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-12 06:22 | +5 | ZEC | DOWN | 0.59 | 0.68 | 0.57 |
| 10-12 06:22 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-12 06:22 | +20 | ZEC | DOWN | 0.58 | 0.82 | 2.11 |
| 10-12 06:22 | +15 | ZEC | DOWN | 0.58 | 0.74 | 1.28 |
| 10-12 06:22 | +10 | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-12 06:22 | +5 | ZEC | DOWN | 0.58 | 0.65 | 0.36 |
| 10-12 06:16 | +10 stop | ZEC | DOWN | 0.58 | 0.76 | 1.49 |
| 10-12 06:16 | +20 | ZEC | DOWN | 0.58 | 0.78 | 1.70 |
| 10-12 06:16 | +15 | ZEC | DOWN | 0.58 | 0.76 | 1.49 |
| 10-12 06:16 | +10 | ZEC | DOWN | 0.58 | 0.76 | 1.50 |
| 10-12 06:16 | +5 | ZEC | DOWN | 0.58 | 0.65 | 0.36 |
| 10-12 06:16 | +10 stop | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-12 06:16 | +20 | ETH | DOWN | 0.66 | 0.86 | 1.75 |
| 10-12 06:16 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 10-12 06:16 | +10 | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-12 06:16 | +5 | ETH | DOWN | 0.66 | 0.75 | 0.60 |
| 10-12 06:16 | +10 stop | XRP | DOWN | 0.64 | 0.75 | 0.79 |
