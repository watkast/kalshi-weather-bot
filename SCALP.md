# Range-Scalp Bot

*Updated Thu Oct 15 16:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17796 | 15441 | 2355 (28) | 0 | $-5503.28 | -4.9% |
| **+10¢** | 13447 | 10720 | 2727 (40) | 0 | $-5000.41 | -5.9% |
| **+15¢** | 11281 | 8350 | 2931 (59) | 1 | $-4494.35 | -6.3% |
| **+20¢** | 10031 | 6964 | 3067 (77) | 1 | $-3923.43 | -6.2% |
| **+10¢ (15¢ stop)** | 21917 | 21867 | 50 (29) | 0 | $-8464.51 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 16:21 | +10 stop | NEAR | DOWN | 0.60 | 0.77 | 1.40 |
| 10-15 16:21 | +20 | NEAR | DOWN | 0.60 | 0.82 | 1.92 |
| 10-15 16:21 | +15 | NEAR | DOWN | 0.60 | 0.77 | 1.40 |
| 10-15 16:21 | +10 | NEAR | DOWN | 0.60 | 0.77 | 1.40 |
| 10-15 16:21 | +5 | NEAR | DOWN | 0.60 | 0.77 | 1.40 |
| 10-15 16:20 | +10 stop | ZEC | UP | 0.57 | 0.42 | -1.86 |
| 10-15 16:20 | +10 stop | HYPE | DOWN | 0.68 | 0.50 | -2.14 |
| 10-15 16:20 | +20 | HYPE | DOWN | 0.68 | 0.88 | 1.76 |
| 10-15 16:20 | +15 | HYPE | DOWN | 0.68 | 0.87 | 1.66 |
| 10-15 16:20 | +10 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-15 16:20 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-15 16:17 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-15 16:17 | +20 | XRP | DOWN | 0.71 | 0.91 | 1.79 |
| 10-15 16:17 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-15 16:17 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-15 16:17 | +5 | XRP | DOWN | 0.71 | 0.79 | 0.53 |
| 10-15 16:16 | +10 stop | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-15 16:16 | +20 | DOGE | DOWN | 0.65 | 0.85 | 1.75 |
| 10-15 16:16 | +15 | DOGE | DOWN | 0.65 | 0.81 | 1.33 |
| 10-15 16:16 | +10 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-15 16:16 | +5 | DOGE | DOWN | 0.65 | 0.71 | 0.29 |
| 10-15 16:16 | +10 stop | HYPE | DOWN | 0.57 | 0.68 | 0.72 |
| 10-15 16:16 | +20 | HYPE | DOWN | 0.57 | 0.79 | 1.86 |
| 10-15 16:16 | +15 | HYPE | DOWN | 0.57 | 0.75 | 1.44 |
| 10-15 16:16 | +10 | HYPE | DOWN | 0.57 | 0.68 | 0.72 |
| 10-15 16:16 | +5 | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 10-15 16:16 | +10 stop | ZEC | DOWN | 0.70 | 0.44 | -2.93 |
| 10-15 16:16 | +20 | ZEC | DOWN | 0.70 | open |  |
| 10-15 16:16 | +15 | ZEC | DOWN | 0.70 | open |  |
| 10-15 16:16 | +10 | ZEC | DOWN | 0.70 | 0.82 | 0.91 |
| 10-15 16:16 | +5 | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-15 16:16 | +10 stop | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-15 16:16 | +20 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 10-15 16:16 | +15 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 10-15 16:16 | +10 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 10-15 16:16 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 10-15 16:16 | +10 stop | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-15 16:16 | +20 | BNB | DOWN | 0.64 | 0.84 | 1.73 |
| 10-15 16:16 | +15 | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-15 16:16 | +10 | BNB | DOWN | 0.64 | 0.75 | 0.79 |
