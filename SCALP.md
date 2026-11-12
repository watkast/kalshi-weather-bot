# Range-Scalp Bot

*Updated Thu Nov 12 23:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57466 | 50113 | 7353 (101) | 3 | $-15690.30 | -4.3% |
| **+10¢** | 42954 | 34369 | 8585 (133) | 4 | $-14623.76 | -5.4% |
| **+15¢** | 36012 | 26773 | 9239 (167) | 5 | $-13184.72 | -5.8% |
| **+20¢** | 32085 | 22392 | 9693 (217) | 5 | $-11531.14 | -5.7% |
| **+10¢ (15¢ stop)** | 70083 | 69955 | 128 (78) | 0 | $-25836.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 23:43 | +10 stop | SOL | UP | 0.53 | 0.79 | 2.30 |
| 11-12 23:40 | +10 stop | XRP | UP | 0.49 | 0.65 | 1.26 |
| 11-12 23:38 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 11-12 23:38 | +10 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 11-12 23:38 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 11-12 23:38 | +10 stop | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 11-12 23:37 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 11-12 23:37 | +10 stop | XRP | UP | 0.57 | 0.41 | -1.93 |
| 11-12 23:37 | +15 | XRP | UP | 0.57 | 0.76 | 1.62 |
| 11-12 23:37 | +10 | XRP | UP | 0.57 | 0.76 | 1.62 |
| 11-12 23:37 | +5 | XRP | UP | 0.56 | 0.65 | 0.57 |
| 11-12 23:37 | +10 stop | BNB | DOWN | 0.52 | 0.66 | 1.06 |
| 11-12 23:37 | +10 | BNB | DOWN | 0.53 | 0.66 | 0.96 |
| 11-12 23:37 | +5 | BNB | DOWN | 0.53 | 0.66 | 0.96 |
| 11-12 23:36 | +10 stop | SOL | DOWN | 0.71 | 0.47 | -2.73 |
| 11-12 23:36 | +10 stop | DOGE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-12 23:36 | +10 stop | BNB | UP | 0.50 | 0.63 | 0.95 |
| 11-12 23:36 | +15 | BNB | UP | 0.50 | open |  |
| 11-12 23:36 | +10 | BNB | UP | 0.50 | 0.63 | 0.95 |
| 11-12 23:36 | +5 | BNB | UP | 0.50 | 0.63 | 0.95 |
| 11-12 23:36 | +5 | DOGE | DOWN | 0.68 | 0.75 | 0.40 |
| 11-12 23:35 | +10 stop | ETH | UP | 0.54 | 0.31 | -2.63 |
| 11-12 23:35 | +5 | DOGE | UP | 0.58 | 0.66 | 0.46 |
| 11-12 23:34 | +10 stop | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-12 23:33 | +10 stop | ETH | DOWN | 0.56 | 0.40 | -1.95 |
| 11-12 23:33 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 11-12 23:33 | +10 stop | DOGE | DOWN | 0.46 | 0.61 | 1.15 |
| 11-12 23:33 | +10 stop | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 11-12 23:33 | +10 | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 11-12 23:33 | +5 | NEAR | DOWN | 0.58 | 0.66 | 0.46 |
| 11-12 23:32 | +10 stop | NEAR | DOWN | 0.55 | 0.66 | 0.76 |
| 11-12 23:32 | +20 | NEAR | DOWN | 0.55 | 0.82 | 2.41 |
| 11-12 23:32 | +15 | NEAR | DOWN | 0.55 | 0.82 | 2.41 |
| 11-12 23:32 | +10 | NEAR | DOWN | 0.55 | 0.66 | 0.76 |
| 11-12 23:32 | +5 | NEAR | DOWN | 0.55 | 0.66 | 0.76 |
| 11-12 23:31 | +5 | SOL | UP | 0.65 | 0.79 | 1.12 |
| 11-12 23:31 | +10 stop | ZEC | UP | 0.54 | 0.39 | -1.85 |
| 11-12 23:31 | +20 | ZEC | UP | 0.54 | open |  |
| 11-12 23:31 | +15 | ZEC | UP | 0.53 | open |  |
| 11-12 23:31 | +10 | ZEC | UP | 0.53 | open |  |
