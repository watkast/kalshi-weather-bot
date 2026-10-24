# Range-Scalp Bot

*Updated Sat Oct 24 00:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31177 | 27171 | 4006 (40) | 3 | $-8996.92 | -4.6% |
| **+10¢** | 23323 | 18693 | 4630 (58) | 3 | $-8004.33 | -5.5% |
| **+15¢** | 19513 | 14532 | 4981 (81) | 3 | $-7206.29 | -5.9% |
| **+20¢** | 17284 | 12067 | 5217 (103) | 3 | $-6450.94 | -5.9% |
| **+10¢ (15¢ stop)** | 38245 | 38186 | 59 (32) | 0 | $-14580.42 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 00:38 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-24 00:38 | +20 | HYPE | DOWN | 0.70 | 0.90 | 1.82 |
| 10-24 00:38 | +15 | HYPE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-24 00:38 | +10 | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-24 00:38 | +5 | HYPE | DOWN | 0.70 | 0.75 | 0.21 |
| 10-24 00:38 | +10 stop | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-24 00:35 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-24 00:34 | +10 stop | SOL | DOWN | 0.69 | 0.80 | 0.87 |
| 10-24 00:34 | +10 stop | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 00:34 | +10 stop | XRP | DOWN | 0.57 | 0.75 | 1.48 |
| 10-24 00:34 | +5 | XRP | DOWN | 0.57 | 0.64 | 0.35 |
| 10-24 00:34 | +10 stop | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-24 00:34 | +10 stop | XRP | DOWN | 0.56 | 0.66 | 0.66 |
| 10-24 00:34 | +20 | XRP | DOWN | 0.56 | 0.76 | 1.69 |
| 10-24 00:34 | +15 | XRP | DOWN | 0.58 | 0.75 | 1.38 |
| 10-24 00:34 | +10 | XRP | DOWN | 0.58 | 0.75 | 1.38 |
| 10-24 00:34 | +5 | XRP | DOWN | 0.58 | 0.66 | 0.46 |
| 10-24 00:33 | +10 stop | DOGE | DOWN | 0.71 | 0.56 | -1.83 |
| 10-24 00:33 | +10 stop | BTC | DOWN | 0.67 | 0.51 | -1.94 |
| 10-24 00:33 | +20 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 10-24 00:33 | +15 | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 10-24 00:33 | +10 | BTC | DOWN | 0.67 | 0.81 | 1.13 |
| 10-24 00:33 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-24 00:32 | +5 | NEAR | DOWN | 0.62 | 0.75 | 0.99 |
| 10-24 00:32 | +10 stop | HYPE | DOWN | 0.61 | 0.82 | 1.82 |
| 10-24 00:32 | +20 | HYPE | DOWN | 0.61 | 0.82 | 1.82 |
| 10-24 00:32 | +15 | HYPE | DOWN | 0.61 | 0.82 | 1.82 |
| 10-24 00:32 | +10 | HYPE | DOWN | 0.61 | 0.82 | 1.82 |
| 10-24 00:32 | +5 | HYPE | DOWN | 0.61 | 0.82 | 1.82 |
| 10-24 00:32 | +10 stop | NEAR | DOWN | 0.58 | 0.75 | 1.38 |
| 10-24 00:32 | +20 | NEAR | DOWN | 0.58 | 0.83 | 2.22 |
| 10-24 00:32 | +15 | NEAR | DOWN | 0.58 | 0.75 | 1.38 |
| 10-24 00:32 | +10 | NEAR | DOWN | 0.58 | 0.75 | 1.38 |
| 10-24 00:32 | +5 | NEAR | DOWN | 0.58 | 0.64 | 0.25 |
| 10-24 00:32 | +10 stop | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 10-24 00:31 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-24 00:31 | +20 | ZEC | DOWN | 0.70 | 0.91 | 1.89 |
| 10-24 00:31 | +15 | ZEC | DOWN | 0.70 | 0.86 | 1.36 |
| 10-24 00:31 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-24 00:31 | +5 | ZEC | DOWN | 0.70 | 0.77 | 0.42 |
