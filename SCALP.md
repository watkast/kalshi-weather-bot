# Range-Scalp Bot

*Updated Mon Oct 05 19:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4184 | 3597 | 587 (4) | 2 | $-1508.35 | -5.7% |
| **+10¢** | 3230 | 2557 | 673 (5) | 3 | $-1358.22 | -6.7% |
| **+15¢** | 2709 | 2000 | 709 (8) | 3 | $-1172.22 | -6.9% |
| **+20¢** | 2418 | 1680 | 738 (13) | 4 | $-999.68 | -6.6% |
| **+10¢ (15¢ stop)** | 5157 | 5152 | 5 (2) | 0 | $-1882.65 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 19:27 | +10 stop | ETH | UP | 0.64 | 0.83 | 1.63 |
| 10-05 19:27 | +10 | ETH | UP | 0.64 | 0.83 | 1.63 |
| 10-05 19:27 | +5 | ETH | UP | 0.64 | 0.69 | 0.18 |
| 10-05 19:25 | +5 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-05 19:24 | +10 stop | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-05 19:24 | +10 | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-05 19:24 | +5 | ZEC | DOWN | 0.65 | 0.73 | 0.50 |
| 10-05 19:24 | +5 | ETH | UP | 0.60 | 0.74 | 1.09 |
| 10-05 19:24 | +10 stop | SOL | DOWN | 0.70 | 0.88 | 1.57 |
| 10-05 19:24 | +10 | SOL | DOWN | 0.70 | 0.88 | 1.57 |
| 10-05 19:24 | +5 | SOL | DOWN | 0.70 | 0.75 | 0.21 |
| 10-05 19:24 | +5 | ETH | UP | 0.54 | 0.66 | 0.86 |
| 10-05 19:23 | +5 | ZEC | DOWN | 0.58 | 0.70 | 0.87 |
| 10-05 19:23 | +10 stop | ZEC | DOWN | 0.56 | 0.70 | 1.07 |
| 10-05 19:23 | +10 | ZEC | DOWN | 0.56 | 0.70 | 1.07 |
| 10-05 19:23 | +5 | ZEC | DOWN | 0.56 | 0.63 | 0.35 |
| 10-05 19:22 | +5 | ETH | UP | 0.63 | 0.69 | 0.28 |
| 10-05 19:22 | +10 | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 10-05 19:22 | +5 | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 10-05 19:22 | +10 stop | BNB | DOWN | 0.71 | 0.83 | 0.95 |
| 10-05 19:21 | +10 stop | SOL | DOWN | 0.70 | 0.51 | -2.23 |
| 10-05 19:21 | +10 stop | BNB | UP | 0.62 | 0.42 | -2.35 |
| 10-05 19:20 | +10 stop | ETH | UP | 0.64 | 0.74 | 0.69 |
| 10-05 19:20 | +20 | ETH | UP | 0.64 | open |  |
| 10-05 19:20 | +15 | ETH | UP | 0.64 | 0.83 | 1.63 |
| 10-05 19:20 | +10 | ETH | UP | 0.64 | 0.74 | 0.69 |
| 10-05 19:20 | +5 | ETH | UP | 0.64 | 0.72 | 0.48 |
| 10-05 19:20 | +10 stop | ZEC | DOWN | 0.66 | 0.78 | 0.92 |
| 10-05 19:19 | +10 stop | SOL | UP | 0.71 | 0.54 | -2.03 |
| 10-05 19:18 | +10 stop | BNB | UP | 0.55 | 0.40 | -1.85 |
| 10-05 19:18 | +10 stop | SOL | DOWN | 0.36 | 0.54 | 1.45 |
| 10-05 19:18 | +10 stop | ZEC | DOWN | 0.65 | 0.50 | -1.84 |
| 10-05 19:18 | +20 | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-05 19:18 | +15 | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-05 19:18 | +10 | ZEC | DOWN | 0.65 | 0.78 | 1.01 |
| 10-05 19:18 | +5 | ZEC | DOWN | 0.65 | 0.78 | 1.01 |
| 10-05 19:18 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.26 |
| 10-05 19:17 | +5 | NEAR | UP | 0.58 | 0.66 | 0.46 |
| 10-05 19:17 | +10 stop | BTC | DOWN | 0.71 | 0.51 | -2.33 |
| 10-05 19:17 | +20 | BTC | DOWN | 0.71 | open |  |
