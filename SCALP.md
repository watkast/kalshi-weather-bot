# Range-Scalp Bot

*Updated Fri Nov 13 02:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57658 | 50287 | 7371 (101) | 1 | $-15712.29 | -4.3% |
| **+10¢** | 43090 | 34483 | 8607 (133) | 3 | $-14642.93 | -5.4% |
| **+15¢** | 36127 | 26863 | 9264 (167) | 4 | $-13193.19 | -5.8% |
| **+20¢** | 32183 | 22463 | 9720 (217) | 6 | $-11550.03 | -5.7% |
| **+10¢ (15¢ stop)** | 70295 | 70167 | 128 (78) | 0 | $-25896.33 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 02:23 | +10 stop | HYPE | UP | 0.51 | 0.61 | 0.65 |
| 11-13 02:23 | +10 | HYPE | UP | 0.50 | 0.61 | 0.75 |
| 11-13 02:23 | +5 | HYPE | UP | 0.50 | 0.61 | 0.75 |
| 11-13 02:22 | +5 | NEAR | UP | 0.70 | 0.79 | 0.63 |
| 11-13 02:22 | +10 stop | BTC | UP | 0.62 | 0.75 | 0.99 |
| 11-13 02:22 | +10 stop | DOGE | UP | 0.70 | 0.42 | -3.13 |
| 11-13 02:22 | +10 | BTC | UP | 0.63 | 0.75 | 0.89 |
| 11-13 02:22 | +5 | BTC | UP | 0.63 | 0.71 | 0.48 |
| 11-13 02:22 | +15 | HYPE | DOWN | 0.50 | open |  |
| 11-13 02:22 | +10 | HYPE | DOWN | 0.52 | 0.68 | 1.26 |
| 11-13 02:22 | +10 stop | HYPE | DOWN | 0.60 | 0.37 | -2.64 |
| 11-13 02:22 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.32 |
| 11-13 02:21 | +10 stop | DOGE | UP | 0.61 | 0.36 | -2.84 |
| 11-13 02:21 | +10 stop | XRP | UP | 0.66 | 0.80 | 1.12 |
| 11-13 02:21 | +15 | ZEC | UP | 0.61 | 0.84 | 2.03 |
| 11-13 02:21 | +10 stop | BTC | UP | 0.53 | 0.67 | 1.06 |
| 11-13 02:21 | +10 | BTC | UP | 0.51 | 0.61 | 0.65 |
| 11-13 02:21 | +5 | BTC | UP | 0.52 | 0.61 | 0.55 |
| 11-13 02:21 | +5 | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 11-13 02:20 | +10 stop | NEAR | UP | 0.57 | 0.67 | 0.66 |
| 11-13 02:20 | +15 | NEAR | UP | 0.58 | 0.79 | 1.80 |
| 11-13 02:20 | +10 | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 11-13 02:20 | +5 | NEAR | UP | 0.58 | 0.67 | 0.56 |
| 11-13 02:20 | +10 stop | BNB | UP | 0.61 | 0.46 | -1.85 |
| 11-13 02:20 | +20 | BNB | UP | 0.62 | 0.87 | 2.25 |
| 11-13 02:20 | +15 | BNB | UP | 0.62 | 0.87 | 2.25 |
| 11-13 02:20 | +10 | BNB | UP | 0.62 | 0.87 | 2.25 |
| 11-13 02:20 | +5 | BNB | UP | 0.62 | 0.68 | 0.27 |
| 11-13 02:20 | +5 | HYPE | UP | 0.58 | 0.68 | 0.66 |
| 11-13 02:20 | +10 stop | DOGE | UP | 0.71 | 0.56 | -1.83 |
| 11-13 02:20 | +20 | DOGE | UP | 0.71 | open |  |
| 11-13 02:20 | +15 | DOGE | UP | 0.71 | open |  |
| 11-13 02:20 | +10 | DOGE | UP | 0.71 | open |  |
| 11-13 02:20 | +5 | DOGE | UP | 0.71 | 0.76 | 0.22 |
| 11-13 02:20 | +10 stop | ZEC | UP | 0.59 | 0.73 | 1.09 |
| 11-13 02:20 | +15 | ZEC | UP | 0.51 | 0.67 | 1.26 |
| 11-13 02:20 | +5 | ZEC | UP | 0.53 | 0.64 | 0.75 |
| 11-13 02:20 | +10 stop | XRP | UP | 0.59 | 0.74 | 1.19 |
| 11-13 02:20 | +5 | HYPE | UP | 0.57 | 0.63 | 0.21 |
| 11-13 02:19 | +20 | ZEC | DOWN | 0.40 | open |  |
