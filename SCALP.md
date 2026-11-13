# Range-Scalp Bot

*Updated Fri Nov 13 17:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58411 | 50968 | 7443 (105) | 0 | $-15740.35 | -4.3% |
| **+10¢** | 43643 | 34940 | 8703 (139) | 0 | $-14695.22 | -5.4% |
| **+15¢** | 36583 | 27210 | 9373 (174) | 0 | $-13266.16 | -5.8% |
| **+20¢** | 32590 | 22748 | 9842 (225) | 0 | $-11657.78 | -5.7% |
| **+10¢ (15¢ stop)** | 71135 | 71001 | 134 (82) | 0 | $-26167.29 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 17:53 | +10 stop | ETH | DOWN | 0.70 | 0.89 | 1.68 |
| 11-13 17:51 | +10 stop | ETH | UP | 0.55 | 0.32 | -2.64 |
| 11-13 17:51 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-13 17:51 | +10 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-13 17:51 | +5 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-13 17:48 | +10 stop | ETH | DOWN | 0.62 | 0.43 | -2.25 |
| 11-13 17:48 | +20 | ETH | DOWN | 0.63 | 0.89 | 2.36 |
| 11-13 17:48 | +15 | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 11-13 17:48 | +10 | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 11-13 17:48 | +5 | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 11-13 17:48 | +10 stop | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 11-13 17:48 | +20 | HYPE | DOWN | 0.66 | 0.86 | 1.75 |
| 11-13 17:48 | +5 | HYPE | DOWN | 0.66 | 0.73 | 0.40 |
| 11-13 17:48 | +10 stop | DOGE | DOWN | 0.63 | 0.78 | 1.20 |
| 11-13 17:48 | +20 | DOGE | DOWN | 0.63 | 0.87 | 2.15 |
| 11-13 17:48 | +15 | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-13 17:48 | +10 | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-13 17:48 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-13 17:48 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-13 17:48 | +20 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-13 17:48 | +15 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-13 17:48 | +10 | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-13 17:48 | +5 | BTC | DOWN | 0.68 | 0.76 | 0.51 |
| 11-13 17:48 | +10 stop | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-13 17:48 | +20 | SOL | DOWN | 0.70 | 0.91 | 1.90 |
| 11-13 17:48 | +15 | SOL | DOWN | 0.70 | 0.89 | 1.68 |
| 11-13 17:48 | +10 | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-13 17:48 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 11-13 17:48 | +10 stop | BNB | DOWN | 0.64 | 0.80 | 1.31 |
| 11-13 17:48 | +20 | BNB | DOWN | 0.64 | 0.86 | 1.94 |
| 11-13 17:48 | +15 | BNB | DOWN | 0.64 | 0.80 | 1.31 |
| 11-13 17:48 | +10 | BNB | DOWN | 0.64 | 0.80 | 1.31 |
| 11-13 17:48 | +5 | BNB | DOWN | 0.65 | 0.72 | 0.39 |
| 11-13 17:48 | +15 | HYPE | DOWN | 0.71 | 0.86 | 1.26 |
| 11-13 17:48 | +10 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-13 17:36 | +20 | XRP | UP | 0.71 | 0.93 | 1.96 |
| 11-13 17:36 | +15 | XRP | UP | 0.71 | 0.88 | 1.48 |
| 11-13 17:36 | +10 | XRP | UP | 0.71 | 0.84 | 1.06 |
| 11-13 17:36 | +5 | XRP | UP | 0.71 | 0.76 | 0.23 |
| 11-13 17:35 | +10 stop | ZEC | UP | 0.63 | 0.76 | 1.00 |
