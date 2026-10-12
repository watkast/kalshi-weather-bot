# Range-Scalp Bot

*Updated Mon Oct 12 05:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13127 | 11339 | 1788 (25) | 0 | $-4303.81 | -5.2% |
| **+10¢** | 9947 | 7879 | 2068 (37) | 0 | $-4015.50 | -6.4% |
| **+15¢** | 8363 | 6152 | 2211 (55) | 0 | $-3548.37 | -6.8% |
| **+20¢** | 7447 | 5141 | 2306 (70) | 1 | $-3039.79 | -6.5% |
| **+10¢ (15¢ stop)** | 16177 | 16136 | 41 (25) | 0 | $-6374.16 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 05:31 | +10 stop | ZEC | DOWN | 0.69 | 0.83 | 1.15 |
| 10-12 05:31 | +20 | ZEC | DOWN | 0.69 | open |  |
| 10-12 05:31 | +15 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-12 05:31 | +10 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-12 05:31 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-12 05:23 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.77 |
| 10-12 05:23 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.77 |
| 10-12 05:23 | +5 | HYPE | DOWN | 0.68 | 0.78 | 0.67 |
| 10-12 05:22 | +5 | DOGE | DOWN | 0.71 | 0.79 | 0.53 |
| 10-12 05:19 | +10 stop | HYPE | DOWN | 0.65 | 0.46 | -2.24 |
| 10-12 05:18 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 10-12 05:18 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-12 05:18 | +10 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-12 05:18 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 10-12 05:18 | +10 stop | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-12 05:18 | +15 | DOGE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-12 05:18 | +10 | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-12 05:18 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.50 |
| 10-12 05:17 | +5 | SOL | DOWN | 0.57 | 0.64 | 0.35 |
| 10-12 05:17 | +5 | ZEC | DOWN | 0.63 | 0.69 | 0.28 |
| 10-12 05:17 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-12 05:17 | +10 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-12 05:17 | +5 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-12 05:17 | +10 stop | HYPE | UP | 0.67 | 0.49 | -2.18 |
| 10-12 05:17 | +20 | HYPE | UP | 0.67 | no | -6.90 |
| 10-12 05:17 | +15 | HYPE | UP | 0.67 | no | -6.90 |
| 10-12 05:17 | +10 | HYPE | UP | 0.67 | 0.79 | 0.88 |
| 10-12 05:17 | +5 | HYPE | UP | 0.67 | 0.79 | 0.88 |
| 10-12 05:17 | +5 | ETH | DOWN | 0.64 | 0.72 | 0.48 |
| 10-12 05:17 | +5 | BTC | DOWN | 0.56 | 0.64 | 0.45 |
| 10-12 05:16 | +10 stop | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 10-12 05:16 | +20 | BNB | DOWN | 0.64 | 0.84 | 1.73 |
| 10-12 05:16 | +15 | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-12 05:16 | +10 | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 10-12 05:16 | +5 | BNB | DOWN | 0.64 | 0.71 | 0.38 |
| 10-12 05:16 | +5 | XRP | DOWN | 0.63 | 0.71 | 0.48 |
| 10-12 05:16 | +10 stop | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-12 05:16 | +20 | SOL | DOWN | 0.59 | 0.80 | 1.81 |
| 10-12 05:16 | +15 | SOL | DOWN | 0.59 | 0.78 | 1.60 |
| 10-12 05:16 | +10 | SOL | DOWN | 0.59 | 0.72 | 0.98 |
