# Range-Scalp Bot

*Updated Thu Oct 29 14:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39302 | 34302 | 5000 (50) | 0 | $-10986.32 | -4.4% |
| **+10¢** | 29303 | 23526 | 5777 (73) | 0 | $-9734.53 | -5.3% |
| **+15¢** | 24501 | 18293 | 6208 (100) | 0 | $-8708.43 | -5.7% |
| **+20¢** | 21737 | 15233 | 6504 (129) | 0 | $-7609.35 | -5.6% |
| **+10¢ (15¢ stop)** | 48024 | 47954 | 70 (37) | 0 | $-18226.65 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 14:13 | +10 stop | DOGE | UP | 0.42 | 0.59 | 1.35 |
| 10-29 14:13 | +20 | DOGE | UP | 0.44 | 0.70 | 2.27 |
| 10-29 14:13 | +15 | DOGE | UP | 0.46 | 0.70 | 2.07 |
| 10-29 14:13 | +10 | DOGE | UP | 0.48 | 0.59 | 0.75 |
| 10-29 14:13 | +5 | DOGE | UP | 0.38 | 0.59 | 1.76 |
| 10-29 14:13 | +10 stop | ETH | UP | 0.22 | 0.64 | 3.90 |
| 10-29 14:13 | +20 | ETH | UP | 0.22 | 0.64 | 3.90 |
| 10-29 14:13 | +15 | ETH | UP | 0.22 | 0.64 | 3.90 |
| 10-29 14:13 | +10 | ETH | UP | 0.24 | 0.64 | 3.70 |
| 10-29 14:13 | +5 | ETH | UP | 0.26 | 0.64 | 3.54 |
| 10-29 14:12 | +10 stop | BTC | UP | 0.68 | 0.49 | -2.24 |
| 10-29 14:12 | +15 | BTC | UP | 0.68 | 0.96 | 2.61 |
| 10-29 14:12 | +10 | BTC | UP | 0.69 | 0.96 | 2.52 |
| 10-29 14:12 | +5 | BTC | UP | 0.69 | 0.96 | 2.52 |
| 10-29 14:09 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-29 14:09 | +5 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-29 14:08 | +10 stop | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 10-29 14:08 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-29 14:08 | +20 | SOL | DOWN | 0.70 | 0.92 | 1.97 |
| 10-29 14:08 | +15 | SOL | DOWN | 0.70 | 0.89 | 1.68 |
| 10-29 14:08 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-29 14:08 | +5 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-29 14:08 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 10-29 14:08 | +15 | ETH | DOWN | 0.70 | 0.87 | 1.47 |
| 10-29 14:08 | +10 | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 10-29 14:08 | +5 | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 10-29 14:08 | +10 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-29 14:08 | +5 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-29 14:08 | +5 | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-29 14:08 | +20 | HYPE | DOWN | 0.66 | 0.88 | 1.92 |
| 10-29 14:08 | +15 | HYPE | DOWN | 0.66 | 0.83 | 1.40 |
| 10-29 14:08 | +5 | HYPE | DOWN | 0.66 | 0.75 | 0.56 |
| 10-29 14:07 | +10 stop | HYPE | DOWN | 0.69 | 0.83 | 1.11 |
| 10-29 14:07 | +10 | HYPE | DOWN | 0.69 | 0.83 | 1.11 |
| 10-29 14:07 | +5 | HYPE | DOWN | 0.69 | 0.76 | 0.38 |
| 10-29 14:06 | +10 stop | BTC | DOWN | 0.67 | 0.49 | -2.14 |
| 10-29 14:06 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-29 14:06 | +10 | SOL | DOWN | 0.66 | 0.76 | 0.72 |
| 10-29 14:06 | +5 | SOL | DOWN | 0.66 | 0.73 | 0.41 |
| 10-29 14:06 | +10 stop | DOGE | DOWN | 0.70 | 0.88 | 1.57 |
