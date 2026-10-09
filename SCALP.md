# Range-Scalp Bot

*Updated Fri Oct 09 00:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8219 | 7109 | 1110 (13) | 0 | $-2690.15 | -5.2% |
| **+10¢** | 6224 | 4911 | 1313 (25) | 0 | $-2658.80 | -6.8% |
| **+15¢** | 5246 | 3864 | 1382 (37) | 0 | $-2169.68 | -6.6% |
| **+20¢** | 4677 | 3242 | 1435 (45) | 0 | $-1778.75 | -6.1% |
| **+10¢ (15¢ stop)** | 9980 | 9950 | 30 (19) | 0 | $-3692.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 00:16 | +10 stop | BNB | DOWN | 0.66 | 0.78 | 0.91 |
| 10-09 00:16 | +20 | BNB | DOWN | 0.66 | 0.86 | 1.75 |
| 10-09 00:16 | +15 | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 10-09 00:16 | +10 | BNB | DOWN | 0.66 | 0.78 | 0.91 |
| 10-09 00:16 | +5 | BNB | DOWN | 0.66 | 0.75 | 0.60 |
| 10-09 00:16 | +10 stop | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-09 00:16 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-09 00:16 | +15 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 10-09 00:16 | +10 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-09 00:16 | +5 | BTC | DOWN | 0.69 | 0.76 | 0.42 |
| 10-09 00:16 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 10-09 00:16 | +20 | ETH | DOWN | 0.69 | 0.89 | 1.78 |
| 10-09 00:16 | +15 | ETH | DOWN | 0.68 | 0.89 | 1.87 |
| 10-09 00:16 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-09 00:16 | +5 | ETH | DOWN | 0.68 | 0.75 | 0.40 |
| 10-09 00:09 | +10 stop | BNB | UP | 0.66 | 0.81 | 1.23 |
| 10-09 00:08 | +10 stop | ZEC | UP | 0.68 | 0.82 | 1.10 |
| 10-09 00:08 | +5 | ZEC | UP | 0.69 | 0.76 | 0.43 |
| 10-09 00:08 | +10 stop | HYPE | UP | 0.57 | 0.74 | 1.38 |
| 10-09 00:07 | +10 stop | BTC | UP | 0.68 | 0.83 | 1.24 |
| 10-09 00:07 | +15 | BTC | UP | 0.68 | 0.83 | 1.24 |
| 10-09 00:07 | +10 | BTC | UP | 0.68 | 0.83 | 1.24 |
| 10-09 00:07 | +5 | BTC | UP | 0.66 | 0.73 | 0.40 |
| 10-09 00:07 | +10 stop | BNB | DOWN | 0.64 | 0.42 | -2.55 |
| 10-09 00:07 | +20 | BNB | DOWN | 0.64 | yes | -6.57 |
| 10-09 00:07 | +15 | BNB | DOWN | 0.64 | yes | -6.57 |
| 10-09 00:07 | +10 | BNB | DOWN | 0.64 | yes | -6.57 |
| 10-09 00:07 | +5 | BNB | DOWN | 0.64 | yes | -6.57 |
| 10-09 00:06 | +5 | ZEC | UP | 0.57 | 0.64 | 0.37 |
| 10-09 00:06 | +10 stop | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 10-09 00:06 | +15 | SOL | DOWN | 0.60 | 0.75 | 1.19 |
| 10-09 00:06 | +10 | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 10-09 00:06 | +5 | SOL | DOWN | 0.60 | 0.69 | 0.58 |
| 10-09 00:05 | +10 stop | HYPE | UP | 0.62 | 0.33 | -3.23 |
| 10-09 00:05 | +10 stop | ZEC | UP | 0.71 | 0.48 | -2.63 |
| 10-09 00:05 | +10 | ZEC | UP | 0.71 | 0.82 | 0.84 |
| 10-09 00:05 | +5 | ZEC | UP | 0.71 | 0.76 | 0.22 |
| 10-09 00:04 | +10 stop | HYPE | DOWN | 0.64 | 0.43 | -2.45 |
| 10-09 00:04 | +20 | HYPE | DOWN | 0.64 | yes | -6.57 |
| 10-09 00:04 | +15 | HYPE | DOWN | 0.64 | yes | -6.57 |
