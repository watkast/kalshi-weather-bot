# Range-Scalp Bot

*Updated Sun Oct 25 21:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33771 | 29481 | 4290 (43) | 0 | $-9372.43 | -4.4% |
| **+10¢** | 25275 | 20313 | 4962 (65) | 0 | $-8235.33 | -5.2% |
| **+15¢** | 21141 | 15800 | 5341 (89) | 0 | $-7358.26 | -5.5% |
| **+20¢** | 18733 | 13140 | 5593 (111) | 0 | $-6450.71 | -5.5% |
| **+10¢ (15¢ stop)** | 41379 | 41317 | 62 (33) | 0 | $-15758.21 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 21:10 | +10 stop | XRP | DOWN | 0.50 | 0.73 | 1.98 |
| 10-25 21:10 | +20 | XRP | DOWN | 0.50 | 0.73 | 1.98 |
| 10-25 21:10 | +10 stop | SOL | DOWN | 0.59 | 0.86 | 2.44 |
| 10-25 21:09 | +10 stop | SOL | UP | 0.42 | 0.56 | 1.04 |
| 10-25 21:09 | +10 stop | BNB | UP | 0.52 | 0.37 | -1.85 |
| 10-25 21:09 | +10 stop | NEAR | DOWN | 0.67 | 0.86 | 1.65 |
| 10-25 21:09 | +20 | NEAR | DOWN | 0.67 | 0.90 | 2.07 |
| 10-25 21:09 | +10 | NEAR | DOWN | 0.67 | 0.86 | 1.65 |
| 10-25 21:09 | +5 | NEAR | DOWN | 0.67 | 0.72 | 0.19 |
| 10-25 21:08 | +10 stop | ETH | DOWN | 0.67 | 0.80 | 0.97 |
| 10-25 21:08 | +5 | ETH | DOWN | 0.68 | 0.74 | 0.30 |
| 10-25 21:08 | +10 stop | SOL | DOWN | 0.57 | 0.42 | -1.86 |
| 10-25 21:07 | +10 stop | BNB | DOWN | 0.64 | 0.49 | -1.85 |
| 10-25 21:07 | +15 | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-25 21:07 | +10 | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-25 21:07 | +5 | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-25 21:07 | +10 stop | BTC | UP | 0.66 | 0.76 | 0.71 |
| 10-25 21:07 | +10 | BTC | UP | 0.66 | 0.76 | 0.71 |
| 10-25 21:07 | +5 | BTC | UP | 0.66 | 0.72 | 0.29 |
| 10-25 21:07 | +15 | HYPE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-25 21:07 | +10 | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-25 21:07 | +5 | HYPE | DOWN | 0.71 | 0.77 | 0.32 |
| 10-25 21:07 | +10 stop | SOL | UP | 0.65 | 0.40 | -2.83 |
| 10-25 21:07 | +10 stop | DOGE | UP | 0.46 | 0.17 | -3.22 |
| 10-25 21:06 | +10 stop | XRP | UP | 0.65 | 0.45 | -2.34 |
| 10-25 21:06 | +10 stop | DOGE | DOWN | 0.44 | 0.56 | 0.84 |
| 10-25 21:06 | +10 stop | ETH | DOWN | 0.68 | 0.53 | -1.84 |
| 10-25 21:06 | +15 | ETH | DOWN | 0.69 | 0.93 | 2.24 |
| 10-25 21:06 | +10 | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-25 21:06 | +5 | ETH | DOWN | 0.65 | 0.72 | 0.39 |
| 10-25 21:05 | +10 stop | BTC | UP | 0.60 | 0.70 | 0.68 |
| 10-25 21:05 | +10 stop | SOL | UP | 0.53 | 0.65 | 0.86 |
| 10-25 21:05 | +10 stop | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 10-25 21:05 | +15 | NEAR | DOWN | 0.71 | 0.86 | 1.26 |
| 10-25 21:05 | +10 | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 10-25 21:05 | +5 | NEAR | DOWN | 0.71 | 0.80 | 0.63 |
| 10-25 21:05 | +10 stop | DOGE | DOWN | 0.65 | 0.49 | -1.94 |
| 10-25 21:05 | +10 | DOGE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-25 21:05 | +5 | DOGE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-25 21:04 | +10 stop | SOL | DOWN | 0.68 | 0.45 | -2.64 |
