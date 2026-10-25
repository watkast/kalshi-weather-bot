# Range-Scalp Bot

*Updated Sun Oct 25 23:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33908 | 29607 | 4301 (43) | 1 | $-9361.10 | -4.4% |
| **+10¢** | 25381 | 20408 | 4973 (65) | 1 | $-8187.09 | -5.1% |
| **+15¢** | 21231 | 15878 | 5353 (89) | 1 | $-7305.43 | -5.5% |
| **+20¢** | 18813 | 13208 | 5605 (111) | 1 | $-6382.46 | -5.4% |
| **+10¢ (15¢ stop)** | 41532 | 41470 | 62 (33) | 0 | $-15778.61 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 23:23 | +10 stop | HYPE | DOWN | 0.71 | 0.56 | -1.83 |
| 10-25 23:23 | +10 | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-25 23:23 | +5 | HYPE | DOWN | 0.70 | 0.88 | 1.54 |
| 10-25 23:22 | +10 stop | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 10-25 23:22 | +10 | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 10-25 23:22 | +5 | SOL | DOWN | 0.71 | 0.80 | 0.63 |
| 10-25 23:22 | +10 stop | HYPE | DOWN | 0.52 | 0.68 | 1.26 |
| 10-25 23:22 | +15 | HYPE | DOWN | 0.54 | 0.70 | 1.27 |
| 10-25 23:22 | +10 | HYPE | DOWN | 0.54 | 0.68 | 1.06 |
| 10-25 23:22 | +5 | HYPE | DOWN | 0.54 | 0.68 | 1.06 |
| 10-25 23:20 | +10 stop | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 10-25 23:20 | +15 | SOL | DOWN | 0.69 | 0.94 | 2.25 |
| 10-25 23:20 | +10 | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 10-25 23:20 | +5 | SOL | DOWN | 0.69 | 0.76 | 0.42 |
| 10-25 23:17 | +10 stop | BTC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-25 23:17 | +20 | BTC | DOWN | 0.71 | 0.92 | 1.87 |
| 10-25 23:17 | +15 | BTC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-25 23:17 | +10 | BTC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-25 23:17 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-25 23:17 | +10 stop | BNB | DOWN | 0.65 | 0.83 | 1.54 |
| 10-25 23:17 | +20 | BNB | DOWN | 0.65 | 0.87 | 1.96 |
| 10-25 23:17 | +15 | BNB | DOWN | 0.65 | 0.83 | 1.54 |
| 10-25 23:17 | +10 | BNB | DOWN | 0.65 | 0.83 | 1.54 |
| 10-25 23:17 | +5 | BNB | DOWN | 0.65 | 0.72 | 0.39 |
| 10-25 23:16 | +10 stop | DOGE | DOWN | 0.68 | 0.82 | 1.13 |
| 10-25 23:16 | +10 stop | ETH | DOWN | 0.66 | 0.85 | 1.65 |
| 10-25 23:16 | +10 | ETH | DOWN | 0.66 | 0.85 | 1.65 |
| 10-25 23:16 | +5 | ETH | DOWN | 0.66 | 0.74 | 0.50 |
| 10-25 23:16 | +10 stop | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 10-25 23:16 | +20 | ZEC | DOWN | 0.63 | 0.84 | 1.83 |
| 10-25 23:16 | +15 | ZEC | DOWN | 0.64 | 0.84 | 1.73 |
| 10-25 23:16 | +10 | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-25 23:16 | +5 | ZEC | DOWN | 0.64 | 0.69 | 0.18 |
| 10-25 23:16 | +10 stop | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 10-25 23:16 | +20 | XRP | DOWN | 0.64 | 0.85 | 1.84 |
| 10-25 23:16 | +15 | XRP | DOWN | 0.64 | 0.85 | 1.84 |
| 10-25 23:16 | +10 | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 10-25 23:16 | +5 | XRP | DOWN | 0.64 | 0.70 | 0.28 |
| 10-25 23:16 | +10 stop | SOL | DOWN | 0.64 | 0.78 | 1.15 |
| 10-25 23:16 | +20 | SOL | DOWN | 0.63 | 0.83 | 1.73 |
