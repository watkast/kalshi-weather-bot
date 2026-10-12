# Range-Scalp Bot

*Updated Mon Oct 12 10:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13438 | 11626 | 1812 (25) | 0 | $-4281.94 | -5.1% |
| **+10¢** | 10174 | 8073 | 2101 (37) | 0 | $-3996.20 | -6.2% |
| **+15¢** | 8563 | 6317 | 2246 (55) | 0 | $-3511.03 | -6.5% |
| **+20¢** | 7621 | 5278 | 2343 (70) | 1 | $-2987.27 | -6.2% |
| **+10¢ (15¢ stop)** | 16534 | 16493 | 41 (25) | 0 | $-6458.77 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 10:27 | +10 stop | BTC | UP | 0.62 | 0.45 | -2.05 |
| 10-12 10:27 | +10 stop | DOGE | DOWN | 0.68 | 0.87 | 1.66 |
| 10-12 10:27 | +5 | DOGE | DOWN | 0.68 | 0.77 | 0.61 |
| 10-12 10:26 | +10 stop | HYPE | UP | 0.51 | 0.34 | -2.04 |
| 10-12 10:26 | +10 stop | SOL | DOWN | 0.45 | 0.62 | 1.34 |
| 10-12 10:26 | +15 | SOL | DOWN | 0.45 | 0.62 | 1.33 |
| 10-12 10:26 | +10 | SOL | DOWN | 0.45 | 0.62 | 1.33 |
| 10-12 10:26 | +5 | SOL | DOWN | 0.45 | 0.62 | 1.31 |
| 10-12 10:26 | +5 | DOGE | DOWN | 0.33 | 0.53 | 1.66 |
| 10-12 10:25 | +10 stop | HYPE | DOWN | 0.63 | 0.46 | -2.05 |
| 10-12 10:24 | +10 stop | DOGE | DOWN | 0.71 | 0.53 | -2.13 |
| 10-12 10:24 | +20 | DOGE | DOWN | 0.71 | open |  |
| 10-12 10:24 | +15 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-12 10:24 | +10 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-12 10:24 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-12 10:24 | +10 stop | BTC | UP | 0.56 | 0.68 | 0.86 |
| 10-12 10:24 | +10 stop | NEAR | UP | 0.55 | 0.32 | -2.64 |
| 10-12 10:24 | +10 stop | ETH | UP | 0.55 | 0.75 | 1.68 |
| 10-12 10:23 | +10 stop | BNB | UP | 0.64 | 0.44 | -2.35 |
| 10-12 10:23 | +10 stop | SOL | DOWN | 0.58 | 0.70 | 0.87 |
| 10-12 10:23 | +20 | SOL | DOWN | 0.58 | 0.82 | 2.11 |
| 10-12 10:23 | +15 | SOL | DOWN | 0.58 | 0.73 | 1.18 |
| 10-12 10:23 | +10 | SOL | DOWN | 0.58 | 0.70 | 0.87 |
| 10-12 10:23 | +5 | SOL | DOWN | 0.58 | 0.70 | 0.87 |
| 10-12 10:22 | +5 | BTC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-12 10:22 | +10 stop | HYPE | UP | 0.57 | 0.41 | -1.95 |
| 10-12 10:21 | +10 stop | BNB | DOWN | 0.60 | 0.36 | -2.74 |
| 10-12 10:21 | +10 stop | ETH | DOWN | 0.64 | 0.49 | -1.85 |
| 10-12 10:21 | +5 | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 10-12 10:20 | +10 stop | BNB | UP | 0.50 | 0.62 | 0.85 |
| 10-12 10:20 | +10 stop | BTC | DOWN | 0.69 | 0.52 | -2.03 |
| 10-12 10:20 | +20 | BTC | DOWN | 0.69 | 0.91 | 1.96 |
| 10-12 10:20 | +15 | BTC | DOWN | 0.69 | 0.91 | 1.96 |
| 10-12 10:20 | +10 | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-12 10:20 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-12 10:20 | +5 | ETH | DOWN | 0.50 | 0.67 | 1.36 |
| 10-12 10:19 | +10 stop | ETH | DOWN | 0.66 | 0.50 | -1.94 |
| 10-12 10:18 | +10 stop | NEAR | UP | 0.45 | 0.57 | 0.84 |
| 10-12 10:18 | +10 stop | BNB | DOWN | 0.70 | 0.43 | -3.03 |
| 10-12 10:18 | +20 | BNB | DOWN | 0.70 | 0.95 | 2.33 |
