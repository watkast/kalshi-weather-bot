# Range-Scalp Bot

*Updated Mon Oct 12 06:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13170 | 11379 | 1791 (25) | 0 | $-4300.58 | -5.2% |
| **+10¢** | 9985 | 7913 | 2072 (37) | 0 | $-4002.14 | -6.4% |
| **+15¢** | 8397 | 6182 | 2215 (55) | 0 | $-3530.33 | -6.7% |
| **+20¢** | 7478 | 5168 | 2310 (70) | 0 | $-3009.29 | -6.4% |
| **+10¢ (15¢ stop)** | 16220 | 16179 | 41 (25) | 0 | $-6362.30 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
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
| 10-12 06:16 | +20 | XRP | DOWN | 0.64 | 0.84 | 1.73 |
| 10-12 06:16 | +15 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-12 06:16 | +10 | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 10-12 06:16 | +5 | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 10-12 06:16 | +10 stop | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-12 06:16 | +20 | DOGE | DOWN | 0.58 | 0.78 | 1.69 |
| 10-12 06:16 | +15 | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-12 06:16 | +10 | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-12 06:16 | +5 | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-12 06:16 | +10 stop | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-12 06:16 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-12 06:16 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-12 06:16 | +10 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-12 06:16 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 10-12 06:16 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-12 06:16 | +20 | HYPE | DOWN | 0.69 | 0.89 | 1.78 |
| 10-12 06:16 | +15 | HYPE | DOWN | 0.69 | 0.85 | 1.36 |
| 10-12 06:16 | +10 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-12 06:16 | +5 | HYPE | DOWN | 0.69 | 0.77 | 0.52 |
| 10-12 06:16 | +10 stop | SOL | DOWN | 0.58 | 0.72 | 1.07 |
