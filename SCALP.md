# Range-Scalp Bot

*Updated Wed Nov 18 03:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63528 | 55405 | 8123 (118) | 0 | $-17374.85 | -4.3% |
| **+10¢** | 47459 | 37952 | 9507 (159) | 0 | $-16293.32 | -5.5% |
| **+15¢** | 39796 | 29545 | 10251 (203) | 0 | $-14773.71 | -5.9% |
| **+20¢** | 35452 | 24694 | 10758 (258) | 0 | $-13033.09 | -5.9% |
| **+10¢ (15¢ stop)** | 77304 | 77146 | 158 (93) | 0 | $-28428.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 03:32 | +10 stop | BNB | UP | 0.71 | 0.85 | 1.16 |
| 11-18 03:32 | +20 | BNB | UP | 0.71 | 0.92 | 1.85 |
| 11-18 03:32 | +15 | BNB | UP | 0.71 | 0.86 | 1.26 |
| 11-18 03:32 | +10 | BNB | UP | 0.71 | 0.85 | 1.16 |
| 11-18 03:32 | +5 | BNB | UP | 0.71 | 0.80 | 0.63 |
| 11-18 03:26 | +10 stop | SOL | DOWN | 0.68 | 0.49 | -2.24 |
| 11-18 03:26 | +20 | SOL | DOWN | 0.68 | 0.98 | 2.81 |
| 11-18 03:26 | +15 | SOL | DOWN | 0.68 | 0.84 | 1.34 |
| 11-18 03:26 | +10 | SOL | DOWN | 0.68 | 0.84 | 1.34 |
| 11-18 03:26 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 11-18 03:20 | +5 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-18 03:19 | +5 | ZEC | DOWN | 0.63 | 0.69 | 0.28 |
| 11-18 03:19 | +5 | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-18 03:18 | +10 stop | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-18 03:18 | +20 | DOGE | DOWN | 0.63 | 0.87 | 2.15 |
| 11-18 03:18 | +15 | DOGE | DOWN | 0.63 | 0.78 | 1.20 |
| 11-18 03:18 | +10 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-18 03:18 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 11-18 03:18 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-18 03:18 | +20 | BTC | DOWN | 0.61 | 0.81 | 1.72 |
| 11-18 03:18 | +15 | BTC | DOWN | 0.61 | 0.81 | 1.72 |
| 11-18 03:18 | +10 | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-18 03:18 | +5 | BTC | DOWN | 0.61 | 0.68 | 0.37 |
| 11-18 03:18 | +5 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-18 03:18 | +5 | ZEC | DOWN | 0.60 | 0.65 | 0.17 |
| 11-18 03:18 | +10 stop | BNB | DOWN | 0.60 | 0.72 | 0.88 |
| 11-18 03:18 | +20 | BNB | DOWN | 0.60 | 0.81 | 1.82 |
| 11-18 03:18 | +15 | BNB | DOWN | 0.60 | 0.79 | 1.61 |
| 11-18 03:18 | +10 | BNB | DOWN | 0.60 | 0.72 | 0.88 |
| 11-18 03:18 | +5 | BNB | DOWN | 0.60 | 0.65 | 0.17 |
| 11-18 03:17 | +10 stop | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-18 03:17 | +10 stop | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 11-18 03:17 | +20 | NEAR | DOWN | 0.69 | 0.92 | 2.05 |
| 11-18 03:17 | +15 | NEAR | DOWN | 0.69 | 0.86 | 1.46 |
| 11-18 03:17 | +10 | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 11-18 03:17 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.42 |
| 11-18 03:17 | +10 stop | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 11-18 03:17 | +20 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 11-18 03:17 | +15 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 11-18 03:17 | +10 | SOL | DOWN | 0.69 | 0.80 | 0.83 |
