# Range-Scalp Bot

*Updated Tue Nov 17 04:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62551 | 54570 | 7981 (117) | 3 | $-16950.83 | -4.3% |
| **+10¢** | 46716 | 37378 | 9338 (159) | 4 | $-15815.28 | -5.4% |
| **+15¢** | 39157 | 29085 | 10072 (201) | 5 | $-14362.34 | -5.8% |
| **+20¢** | 34902 | 24340 | 10562 (256) | 6 | $-12527.74 | -5.7% |
| **+10¢ (15¢ stop)** | 76133 | 75977 | 156 (92) | 2 | $-28047.48 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 04:22 | +5 | SOL | DOWN | 0.60 | 0.75 | 1.19 |
| 11-17 04:22 | +10 stop | BNB | UP | 0.70 | 0.46 | -2.73 |
| 11-17 04:22 | +10 stop | HYPE | DOWN | 0.67 | open |  |
| 11-17 04:22 | +10 | HYPE | DOWN | 0.67 | open |  |
| 11-17 04:22 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-17 04:22 | +10 stop | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 11-17 04:21 | +10 stop | DOGE | DOWN | 0.71 | 0.56 | -1.83 |
| 11-17 04:21 | +5 | XRP | DOWN | 0.68 | 0.73 | 0.20 |
| 11-17 04:20 | +10 stop | BTC | UP | 0.61 | open |  |
| 11-17 04:20 | +10 stop | BNB | UP | 0.71 | 0.49 | -2.53 |
| 11-17 04:20 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 11-17 04:20 | +5 | BNB | UP | 0.70 | open |  |
| 11-17 04:19 | +10 stop | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 11-17 04:19 | +20 | NEAR | DOWN | 0.64 | 0.86 | 1.94 |
| 11-17 04:19 | +15 | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 11-17 04:19 | +10 | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 11-17 04:19 | +5 | NEAR | DOWN | 0.64 | 0.73 | 0.59 |
| 11-17 04:19 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 11-17 04:19 | +10 stop | HYPE | UP | 0.53 | 0.30 | -2.63 |
| 11-17 04:19 | +5 | XRP | DOWN | 0.57 | 0.62 | 0.15 |
| 11-17 04:19 | +10 stop | DOGE | DOWN | 0.50 | 0.63 | 0.95 |
| 11-17 04:19 | +5 | XRP | DOWN | 0.56 | 0.63 | 0.35 |
| 11-17 04:19 | +5 | BNB | DOWN | 0.56 | 0.63 | 0.35 |
| 11-17 04:19 | +10 stop | HYPE | DOWN | 0.47 | 0.57 | 0.64 |
| 11-17 04:18 | +10 stop | XRP | DOWN | 0.59 | 0.73 | 1.09 |
| 11-17 04:18 | +20 | XRP | DOWN | 0.59 | 0.81 | 1.92 |
| 11-17 04:18 | +15 | XRP | DOWN | 0.59 | 0.81 | 1.92 |
| 11-17 04:18 | +10 | XRP | DOWN | 0.59 | 0.73 | 1.09 |
| 11-17 04:18 | +5 | XRP | DOWN | 0.59 | 0.64 | 0.16 |
| 11-17 04:18 | +10 stop | SOL | UP | 0.55 | 0.35 | -2.34 |
| 11-17 04:17 | +10 stop | DOGE | UP | 0.54 | 0.39 | -1.85 |
| 11-17 04:17 | +20 | DOGE | UP | 0.54 | open |  |
| 11-17 04:17 | +15 | DOGE | UP | 0.54 | open |  |
| 11-17 04:17 | +10 | DOGE | UP | 0.54 | open |  |
| 11-17 04:17 | +5 | DOGE | UP | 0.54 | open |  |
| 11-17 04:17 | +10 stop | ZEC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-17 04:17 | +20 | ZEC | DOWN | 0.67 | 0.90 | 2.11 |
| 11-17 04:17 | +15 | ZEC | DOWN | 0.67 | 0.86 | 1.65 |
| 11-17 04:17 | +10 | ZEC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-17 04:17 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
