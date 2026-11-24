# Range-Scalp Bot

*Updated Tue Nov 24 23:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71259 | 62198 | 9061 (156) | 0 | $-18987.80 | -4.2% |
| **+10¢** | 53153 | 42570 | 10583 (202) | 0 | $-17585.98 | -5.3% |
| **+15¢** | 44519 | 33126 | 11393 (259) | 0 | $-15622.48 | -5.6% |
| **+20¢** | 39639 | 27643 | 11996 (325) | 0 | $-14003.55 | -5.6% |
| **+10¢ (15¢ stop)** | 86764 | 86563 | 201 (121) | 0 | $-31904.28 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 23:31 | +10 stop | ZEC | DOWN | 0.68 | 0.81 | 1.03 |
| 11-24 23:31 | +20 | ZEC | DOWN | 0.67 | 0.87 | 1.76 |
| 11-24 23:31 | +15 | ZEC | DOWN | 0.67 | 0.83 | 1.34 |
| 11-24 23:31 | +10 | ZEC | DOWN | 0.67 | 0.81 | 1.13 |
| 11-24 23:31 | +5 | ZEC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-24 23:31 | +10 stop | BTC | DOWN | 0.64 | 0.81 | 1.42 |
| 11-24 23:31 | +20 | BTC | DOWN | 0.64 | 0.85 | 1.84 |
| 11-24 23:31 | +15 | BTC | DOWN | 0.64 | 0.81 | 1.42 |
| 11-24 23:31 | +10 | BTC | DOWN | 0.64 | 0.81 | 1.42 |
| 11-24 23:31 | +5 | BTC | DOWN | 0.64 | 0.72 | 0.48 |
| 11-24 23:31 | +10 stop | SOL | DOWN | 0.70 | 0.81 | 0.82 |
| 11-24 23:31 | +20 | SOL | DOWN | 0.70 | 0.91 | 1.91 |
| 11-24 23:31 | +15 | SOL | DOWN | 0.70 | 0.86 | 1.34 |
| 11-24 23:31 | +10 | SOL | DOWN | 0.70 | 0.81 | 0.82 |
| 11-24 23:31 | +5 | SOL | DOWN | 0.70 | 0.80 | 0.71 |
| 11-24 23:31 | +10 stop | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-24 23:31 | +20 | DOGE | DOWN | 0.68 | 0.89 | 1.87 |
| 11-24 23:31 | +15 | DOGE | DOWN | 0.68 | 0.84 | 1.34 |
| 11-24 23:31 | +10 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-24 23:31 | +5 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-24 23:27 | +10 stop | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-24 23:27 | +15 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-24 23:27 | +10 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-24 23:27 | +5 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-24 23:26 | +10 stop | ZEC | UP | 0.35 | 0.66 | 2.80 |
| 11-24 23:25 | +10 stop | XRP | DOWN | 0.65 | 0.85 | 1.76 |
| 11-24 23:24 | +10 stop | XRP | UP | 0.51 | 0.34 | -2.04 |
| 11-24 23:24 | +15 | BNB | UP | 0.63 | 0.81 | 1.52 |
| 11-24 23:24 | +15 | XRP | UP | 0.52 | no | -5.38 |
| 11-24 23:24 | +5 | XRP | UP | 0.52 | no | -5.38 |
| 11-24 23:24 | +10 stop | BNB | UP | 0.60 | 0.73 | 0.99 |
| 11-24 23:24 | +10 stop | HYPE | DOWN | 0.66 | 0.47 | -2.24 |
| 11-24 23:24 | +10 | HYPE | DOWN | 0.67 | 0.92 | 2.23 |
| 11-24 23:24 | +5 | HYPE | DOWN | 0.67 | 0.92 | 2.23 |
| 11-24 23:24 | +10 stop | ZEC | DOWN | 0.62 | 0.34 | -3.13 |
| 11-24 23:24 | +20 | ZEC | DOWN | 0.62 | 0.83 | 1.83 |
| 11-24 23:24 | +15 | ZEC | DOWN | 0.60 | 0.76 | 1.30 |
| 11-24 23:24 | +10 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-24 23:24 | +5 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-24 23:23 | +10 stop | SOL | UP | 0.58 | 0.82 | 2.11 |
