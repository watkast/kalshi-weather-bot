# Range-Scalp Bot

*Updated Mon Oct 26 20:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35342 | 30849 | 4493 (43) | 0 | $-9860.83 | -4.4% |
| **+10¢** | 26440 | 21244 | 5196 (65) | 0 | $-8675.73 | -5.2% |
| **+15¢** | 22127 | 16534 | 5593 (89) | 0 | $-7769.21 | -5.6% |
| **+20¢** | 19624 | 13763 | 5861 (112) | 0 | $-6808.64 | -5.5% |
| **+10¢ (15¢ stop)** | 43337 | 43275 | 62 (33) | 0 | $-16486.41 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 20:07 | +10 stop | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-26 20:07 | +20 | HYPE | DOWN | 0.64 | 0.92 | 2.52 |
| 10-26 20:07 | +15 | HYPE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-26 20:07 | +10 | HYPE | DOWN | 0.65 | 0.79 | 1.12 |
| 10-26 20:07 | +5 | HYPE | DOWN | 0.65 | 0.70 | 0.19 |
| 10-26 20:07 | +10 stop | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 10-26 20:07 | +20 | XRP | DOWN | 0.67 | 0.88 | 1.86 |
| 10-26 20:07 | +15 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 10-26 20:07 | +10 | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 10-26 20:07 | +5 | XRP | DOWN | 0.70 | 0.79 | 0.63 |
| 10-26 20:07 | +5 | DOGE | DOWN | 0.62 | 0.71 | 0.58 |
| 10-26 20:06 | +10 stop | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-26 20:06 | +10 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-26 20:06 | +5 | DOGE | DOWN | 0.64 | 0.70 | 0.28 |
| 10-26 20:03 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 10-26 20:03 | +10 stop | ZEC | DOWN | 0.65 | 0.77 | 0.89 |
| 10-26 20:03 | +10 | ZEC | DOWN | 0.65 | 0.75 | 0.72 |
| 10-26 20:03 | +5 | ZEC | DOWN | 0.65 | 0.75 | 0.73 |
| 10-26 20:02 | +5 | BNB | DOWN | 0.67 | 0.73 | 0.30 |
| 10-26 20:01 | +10 stop | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-26 20:01 | +20 | DOGE | DOWN | 0.67 | 0.92 | 2.23 |
| 10-26 20:01 | +15 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-26 20:01 | +10 | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-26 20:01 | +5 | DOGE | DOWN | 0.67 | 0.75 | 0.50 |
| 10-26 20:01 | +10 stop | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-26 20:01 | +20 | BNB | DOWN | 0.66 | 0.89 | 2.07 |
| 10-26 20:01 | +15 | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 10-26 20:01 | +10 | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-26 20:01 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.29 |
| 10-26 20:01 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-26 20:01 | +20 | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-26 20:01 | +15 | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-26 20:01 | +10 | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-26 20:01 | +5 | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-26 20:01 | +10 stop | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 10-26 20:01 | +20 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 10-26 20:01 | +15 | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 10-26 20:01 | +10 | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 10-26 20:01 | +5 | NEAR | DOWN | 0.65 | 0.72 | 0.39 |
| 10-26 20:01 | +10 stop | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
