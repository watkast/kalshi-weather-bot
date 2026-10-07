# Range-Scalp Bot

*Updated Wed Oct 07 04:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5948 | 5156 | 792 (9) | 1 | $-1832.18 | -4.9% |
| **+10¢** | 4536 | 3602 | 934 (16) | 0 | $-1736.41 | -6.1% |
| **+15¢** | 3810 | 2820 | 990 (20) | 0 | $-1507.88 | -6.3% |
| **+20¢** | 3403 | 2369 | 1034 (27) | 1 | $-1254.50 | -5.9% |
| **+10¢ (15¢ stop)** | 7229 | 7214 | 15 (9) | 0 | $-2541.35 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 04:24 | +10 stop | XRP | DOWN | 0.65 | 0.30 | -3.81 |
| 10-07 04:24 | +5 | XRP | DOWN | 0.71 | open |  |
| 10-07 04:24 | +10 stop | XRP | UP | 0.52 | 0.33 | -2.24 |
| 10-07 04:24 | +20 | XRP | UP | 0.52 | 0.72 | 1.67 |
| 10-07 04:24 | +15 | XRP | UP | 0.52 | 0.69 | 1.37 |
| 10-07 04:24 | +10 | XRP | UP | 0.52 | 0.69 | 1.37 |
| 10-07 04:24 | +5 | XRP | UP | 0.52 | 0.58 | 0.24 |
| 10-07 04:16 | +10 stop | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 10-07 04:16 | +20 | BNB | DOWN | 0.60 | 0.85 | 2.24 |
| 10-07 04:16 | +15 | BNB | DOWN | 0.60 | 0.85 | 2.24 |
| 10-07 04:16 | +10 | BNB | DOWN | 0.60 | 0.71 | 0.78 |
| 10-07 04:16 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.27 |
| 10-07 04:16 | +10 stop | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 10-07 04:16 | +20 | HYPE | DOWN | 0.64 | 0.90 | 2.37 |
| 10-07 04:16 | +15 | HYPE | DOWN | 0.64 | 0.90 | 2.37 |
| 10-07 04:16 | +10 | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 10-07 04:16 | +5 | HYPE | DOWN | 0.64 | 0.69 | 0.18 |
| 10-07 04:16 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-07 04:16 | +20 | BTC | DOWN | 0.69 | open |  |
| 10-07 04:16 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-07 04:16 | +10 | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-07 04:16 | +5 | BTC | DOWN | 0.69 | 0.77 | 0.52 |
| 10-07 04:16 | +10 stop | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 10-07 04:16 | +20 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 10-07 04:16 | +15 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 10-07 04:16 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.85 |
| 10-07 04:16 | +5 | ETH | DOWN | 0.71 | 0.79 | 0.53 |
| 10-07 04:16 | +10 stop | ZEC | DOWN | 0.71 | 0.88 | 1.47 |
| 10-07 04:16 | +20 | ZEC | DOWN | 0.71 | 0.91 | 1.80 |
| 10-07 04:16 | +15 | ZEC | DOWN | 0.71 | 0.88 | 1.47 |
| 10-07 04:16 | +10 | ZEC | DOWN | 0.71 | 0.88 | 1.47 |
| 10-07 04:16 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-07 04:16 | +10 stop | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 10-07 04:16 | +20 | XRP | DOWN | 0.69 | 0.89 | 1.78 |
| 10-07 04:16 | +15 | XRP | DOWN | 0.69 | 0.84 | 1.25 |
| 10-07 04:16 | +10 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 10-07 04:16 | +5 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 10-07 04:16 | +10 stop | DOGE | DOWN | 0.68 | 0.82 | 1.13 |
| 10-07 04:16 | +20 | DOGE | DOWN | 0.70 | 0.94 | 2.24 |
| 10-07 04:16 | +15 | DOGE | DOWN | 0.70 | 0.89 | 1.68 |
