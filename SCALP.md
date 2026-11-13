# Range-Scalp Bot

*Updated Fri Nov 13 03:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57724 | 50349 | 7375 (101) | 0 | $-15704.90 | -4.3% |
| **+10¢** | 43136 | 34524 | 8612 (133) | 0 | $-14632.98 | -5.4% |
| **+15¢** | 36165 | 26897 | 9268 (167) | 0 | $-13165.80 | -5.8% |
| **+20¢** | 32217 | 22491 | 9726 (217) | 0 | $-11534.81 | -5.7% |
| **+10¢ (15¢ stop)** | 70365 | 70237 | 128 (78) | 0 | $-25936.42 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 03:07 | +10 stop | HYPE | DOWN | 0.61 | 0.73 | 0.84 |
| 11-13 03:07 | +10 stop | SOL | DOWN | 0.59 | 0.74 | 1.19 |
| 11-13 03:06 | +5 | XRP | DOWN | 0.71 | 0.79 | 0.53 |
| 11-13 03:06 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-13 03:06 | +10 stop | ETH | DOWN | 0.57 | 0.74 | 1.38 |
| 11-13 03:06 | +10 stop | HYPE | DOWN | 0.52 | 0.65 | 0.96 |
| 11-13 03:05 | +10 stop | SOL | UP | 0.49 | 0.59 | 0.65 |
| 11-13 03:05 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-13 03:05 | +10 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-13 03:05 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-13 03:05 | +10 stop | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 11-13 03:05 | +10 | XRP | DOWN | 0.59 | 0.72 | 0.98 |
| 11-13 03:05 | +5 | XRP | DOWN | 0.59 | 0.66 | 0.37 |
| 11-13 03:04 | +10 stop | SOL | DOWN | 0.66 | 0.51 | -1.84 |
| 11-13 03:04 | +10 | SOL | DOWN | 0.66 | 0.79 | 1.02 |
| 11-13 03:04 | +10 stop | BTC | DOWN | 0.67 | 0.50 | -2.04 |
| 11-13 03:04 | +20 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-13 03:04 | +15 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-13 03:04 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-13 03:04 | +5 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-13 03:04 | +10 stop | ETH | DOWN | 0.70 | 0.53 | -2.03 |
| 11-13 03:04 | +15 | ETH | DOWN | 0.71 | 0.87 | 1.37 |
| 11-13 03:04 | +10 | ETH | DOWN | 0.71 | 0.85 | 1.16 |
| 11-13 03:04 | +5 | ETH | DOWN | 0.71 | 0.85 | 1.16 |
| 11-13 03:03 | +10 stop | ZEC | DOWN | 0.69 | 0.53 | -1.93 |
| 11-13 03:03 | +5 | ZEC | DOWN | 0.69 | 0.75 | 0.31 |
| 11-13 03:03 | +10 stop | HYPE | DOWN | 0.66 | 0.46 | -2.34 |
| 11-13 03:03 | +5 | HYPE | DOWN | 0.66 | 0.73 | 0.40 |
| 11-13 03:03 | +5 | XRP | DOWN | 0.64 | 0.72 | 0.48 |
| 11-13 03:03 | +10 stop | BNB | DOWN | 0.71 | 0.55 | -1.92 |
| 11-13 03:03 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.32 |
| 11-13 03:03 | +10 stop | ETH | DOWN | 0.62 | 0.73 | 0.79 |
| 11-13 03:03 | +10 stop | NEAR | DOWN | 0.64 | 0.78 | 1.10 |
| 11-13 03:03 | +10 | NEAR | DOWN | 0.64 | 0.78 | 1.10 |
| 11-13 03:03 | +5 | NEAR | DOWN | 0.64 | 0.71 | 0.38 |
| 11-13 03:02 | +5 | DOGE | DOWN | 0.59 | 0.72 | 0.98 |
| 11-13 03:02 | +10 stop | XRP | DOWN | 0.55 | 0.72 | 1.37 |
| 11-13 03:02 | +10 | XRP | DOWN | 0.55 | 0.72 | 1.37 |
| 11-13 03:02 | +5 | XRP | DOWN | 0.55 | 0.60 | 0.15 |
| 11-13 03:02 | +15 | ETH | DOWN | 0.55 | 0.73 | 1.48 |
