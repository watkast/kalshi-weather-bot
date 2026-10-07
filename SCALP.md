# Range-Scalp Bot

*Updated Wed Oct 07 22:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6902 | 5996 | 906 (10) | 6 | $-2063.10 | -4.7% |
| **+10¢** | 5233 | 4171 | 1062 (17) | 6 | $-1943.77 | -5.9% |
| **+15¢** | 4388 | 3272 | 1116 (21) | 6 | $-1595.25 | -5.8% |
| **+20¢** | 3921 | 2758 | 1163 (28) | 6 | $-1255.37 | -5.1% |
| **+10¢ (15¢ stop)** | 8359 | 8342 | 17 (10) | 0 | $-2952.28 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 22:24 | +10 stop | ETH | UP | 0.71 | 0.81 | 0.74 |
| 10-07 22:23 | +10 stop | ETH | DOWN | 0.42 | 0.58 | 1.24 |
| 10-07 22:23 | +10 stop | NEAR | UP | 0.64 | 0.83 | 1.63 |
| 10-07 22:23 | +10 | NEAR | UP | 0.64 | 0.83 | 1.63 |
| 10-07 22:23 | +5 | NEAR | UP | 0.64 | 0.83 | 1.63 |
| 10-07 22:22 | +10 stop | ETH | DOWN | 0.49 | 0.59 | 0.65 |
| 10-07 22:22 | +10 stop | NEAR | UP | 0.56 | 0.66 | 0.67 |
| 10-07 22:22 | +20 | NEAR | UP | 0.56 | 0.83 | 2.43 |
| 10-07 22:22 | +15 | NEAR | UP | 0.56 | 0.83 | 2.43 |
| 10-07 22:22 | +10 | NEAR | UP | 0.56 | 0.66 | 0.67 |
| 10-07 22:22 | +5 | NEAR | UP | 0.56 | 0.66 | 0.67 |
| 10-07 22:21 | +10 stop | SOL | UP | 0.66 | 0.89 | 2.07 |
| 10-07 22:21 | +5 | ETH | DOWN | 0.55 | open |  |
| 10-07 22:21 | +10 stop | DOGE | UP | 0.64 | 0.74 | 0.69 |
| 10-07 22:21 | +10 stop | HYPE | UP | 0.70 | 0.86 | 1.32 |
| 10-07 22:21 | +15 | HYPE | UP | 0.70 | 0.86 | 1.36 |
| 10-07 22:21 | +10 | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-07 22:21 | +5 | HYPE | UP | 0.69 | 0.78 | 0.58 |
| 10-07 22:21 | +10 stop | BTC | UP | 0.56 | 0.68 | 0.86 |
| 10-07 22:20 | +5 | ZEC | DOWN | 0.65 | open |  |
| 10-07 22:19 | +10 stop | BNB | UP | 0.69 | 0.80 | 0.83 |
| 10-07 22:19 | +5 | SOL | DOWN | 0.60 | open |  |
| 10-07 22:19 | +10 stop | DOGE | DOWN | 0.66 | 0.50 | -1.89 |
| 10-07 22:19 | +20 | DOGE | DOWN | 0.66 | open |  |
| 10-07 22:19 | +15 | DOGE | DOWN | 0.66 | open |  |
| 10-07 22:19 | +10 | DOGE | DOWN | 0.66 | open |  |
| 10-07 22:19 | +5 | DOGE | DOWN | 0.66 | open |  |
| 10-07 22:18 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.22 |
| 10-07 22:18 | +5 | ZEC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-07 22:16 | +10 stop | HYPE | UP | 0.57 | 0.74 | 1.38 |
| 10-07 22:16 | +20 | HYPE | UP | 0.57 | 0.78 | 1.79 |
| 10-07 22:16 | +15 | HYPE | UP | 0.58 | 0.74 | 1.28 |
| 10-07 22:16 | +10 | HYPE | UP | 0.58 | 0.74 | 1.28 |
| 10-07 22:16 | +5 | HYPE | UP | 0.58 | 0.63 | 0.15 |
| 10-07 22:16 | +10 stop | BNB | DOWN | 0.58 | 0.34 | -2.74 |
| 10-07 22:16 | +20 | BNB | DOWN | 0.58 | open |  |
| 10-07 22:16 | +15 | BNB | DOWN | 0.58 | open |  |
| 10-07 22:16 | +10 | BNB | DOWN | 0.58 | open |  |
| 10-07 22:16 | +5 | BNB | DOWN | 0.58 | open |  |
| 10-07 22:16 | +10 stop | SOL | DOWN | 0.65 | 0.46 | -2.24 |
