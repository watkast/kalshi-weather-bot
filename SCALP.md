# Range-Scalp Bot

*Updated Thu Nov 12 22:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57369 | 50027 | 7342 (101) | 3 | $-15676.23 | -4.3% |
| **+10¢** | 42874 | 34306 | 8568 (133) | 5 | $-14589.44 | -5.4% |
| **+15¢** | 35946 | 26723 | 9223 (167) | 5 | $-13171.28 | -5.8% |
| **+20¢** | 32029 | 22352 | 9677 (217) | 4 | $-11519.90 | -5.7% |
| **+10¢ (15¢ stop)** | 69962 | 69834 | 128 (78) | 0 | $-25810.73 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 22:12 | +10 stop | NEAR | UP | 0.53 | 0.38 | -1.85 |
| 11-12 22:12 | +10 stop | HYPE | DOWN | 0.52 | 0.84 | 2.92 |
| 11-12 22:11 | +10 stop | NEAR | UP | 0.64 | 0.42 | -2.55 |
| 11-12 22:10 | +10 stop | HYPE | UP | 0.65 | 0.37 | -3.13 |
| 11-12 22:10 | +10 stop | SOL | UP | 0.71 | 0.86 | 1.26 |
| 11-12 22:09 | +10 stop | HYPE | DOWN | 0.70 | 0.40 | -3.32 |
| 11-12 22:09 | +15 | HYPE | DOWN | 0.71 | open |  |
| 11-12 22:09 | +5 | HYPE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-12 22:07 | +10 stop | BNB | DOWN | 0.69 | 0.82 | 1.04 |
| 11-12 22:07 | +10 | BNB | DOWN | 0.69 | 0.82 | 1.04 |
| 11-12 22:07 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-12 22:07 | +10 stop | ZEC | UP | 0.70 | 0.82 | 0.94 |
| 11-12 22:07 | +10 | ZEC | UP | 0.70 | 0.82 | 0.94 |
| 11-12 22:07 | +10 stop | DOGE | UP | 0.64 | 0.79 | 1.21 |
| 11-12 22:07 | +5 | HYPE | UP | 0.62 | 0.67 | 0.17 |
| 11-12 22:06 | +10 stop | NEAR | UP | 0.67 | 0.49 | -2.19 |
| 11-12 22:06 | +10 stop | SOL | UP | 0.70 | 0.51 | -2.23 |
| 11-12 22:06 | +5 | DOGE | UP | 0.68 | 0.79 | 0.82 |
| 11-12 22:06 | +10 stop | XRP | UP | 0.62 | 0.46 | -1.92 |
| 11-12 22:06 | +5 | ETH | DOWN | 0.58 | 0.73 | 1.18 |
| 11-12 22:06 | +10 stop | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-12 22:06 | +20 | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 11-12 22:06 | +15 | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 11-12 22:06 | +10 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-12 22:06 | +5 | BNB | DOWN | 0.62 | 0.68 | 0.27 |
| 11-12 22:06 | +5 | ZEC | UP | 0.71 | 0.77 | 0.32 |
| 11-12 22:05 | +10 stop | DOGE | UP | 0.60 | 0.70 | 0.68 |
| 11-12 22:05 | +5 | DOGE | UP | 0.60 | 0.68 | 0.47 |
| 11-12 22:05 | +10 stop | HYPE | UP | 0.67 | 0.52 | -1.84 |
| 11-12 22:05 | +10 | HYPE | UP | 0.67 | open |  |
| 11-12 22:05 | +5 | ZEC | UP | 0.56 | 0.61 | 0.15 |
| 11-12 22:04 | +10 stop | NEAR | UP | 0.55 | 0.68 | 0.96 |
| 11-12 22:04 | +10 stop | SOL | DOWN | 0.51 | 0.36 | -1.85 |
| 11-12 22:03 | +5 | HYPE | UP | 0.67 | 0.73 | 0.29 |
| 11-12 22:03 | +5 | DOGE | UP | 0.57 | 0.70 | 0.97 |
| 11-12 22:03 | +10 stop | BNB | DOWN | 0.61 | 0.74 | 1.00 |
| 11-12 22:03 | +10 | BNB | DOWN | 0.61 | 0.74 | 1.00 |
| 11-12 22:03 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.20 |
| 11-12 22:03 | +10 stop | XRP | DOWN | 0.63 | 0.40 | -2.64 |
| 11-12 22:03 | +20 | XRP | DOWN | 0.63 | open |  |
