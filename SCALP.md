# Range-Scalp Bot

*Updated Thu Oct 22 04:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28266 | 24632 | 3634 (39) | 0 | $-8107.27 | -4.6% |
| **+10¢** | 21224 | 17022 | 4202 (55) | 0 | $-7182.45 | -5.4% |
| **+15¢** | 17777 | 13254 | 4523 (78) | 0 | $-6425.78 | -5.8% |
| **+20¢** | 15726 | 10983 | 4743 (98) | 0 | $-5806.31 | -5.9% |
| **+10¢ (15¢ stop)** | 34689 | 34630 | 59 (32) | 0 | $-12986.18 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 04:12 | +5 | BNB | UP | 0.70 | 0.80 | 0.73 |
| 10-22 04:12 | +10 stop | BNB | DOWN | 0.44 | 0.24 | -2.35 |
| 10-22 04:12 | +5 | BNB | DOWN | 0.44 | 0.53 | 0.50 |
| 10-22 04:11 | +10 stop | BNB | DOWN | 0.50 | 0.62 | 0.85 |
| 10-22 04:11 | +10 stop | DOGE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-22 04:11 | +5 | BNB | DOWN | 0.50 | 0.62 | 0.85 |
| 10-22 04:10 | +10 stop | SOL | UP | 0.40 | 0.60 | 1.66 |
| 10-22 04:10 | +5 | SOL | UP | 0.40 | 0.60 | 1.66 |
| 10-22 04:10 | +5 | BNB | UP | 0.50 | 0.58 | 0.40 |
| 10-22 04:09 | +10 stop | DOGE | UP | 0.67 | 0.41 | -2.93 |
| 10-22 04:09 | +15 | DOGE | UP | 0.67 | no | -6.86 |
| 10-22 04:09 | +10 | DOGE | UP | 0.66 | no | -6.76 |
| 10-22 04:09 | +5 | DOGE | UP | 0.66 | no | -6.76 |
| 10-22 04:09 | +5 | BNB | UP | 0.59 | 0.64 | 0.16 |
| 10-22 04:09 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-22 04:09 | +10 stop | SOL | UP | 0.52 | 0.76 | 2.09 |
| 10-22 04:09 | +5 | SOL | UP | 0.52 | 0.61 | 0.55 |
| 10-22 04:09 | +10 stop | ETH | DOWN | 0.60 | 0.73 | 0.99 |
| 10-22 04:09 | +10 stop | ZEC | UP | 0.52 | 0.32 | -2.34 |
| 10-22 04:09 | +10 stop | ETH | UP | 0.44 | 0.57 | 0.94 |
| 10-22 04:08 | +10 stop | NEAR | UP | 0.57 | 0.27 | -3.32 |
| 10-22 04:08 | +10 stop | BNB | UP | 0.70 | 0.43 | -3.03 |
| 10-22 04:07 | +10 stop | NEAR | DOWN | 0.66 | 0.49 | -2.04 |
| 10-22 04:07 | +10 stop | ZEC | DOWN | 0.56 | 0.33 | -2.64 |
| 10-22 04:07 | +10 stop | SOL | DOWN | 0.58 | 0.29 | -3.23 |
| 10-22 04:07 | +10 stop | XRP | UP | 0.71 | 0.85 | 1.16 |
| 10-22 04:07 | +15 | XRP | UP | 0.71 | 0.87 | 1.37 |
| 10-22 04:07 | +10 | XRP | UP | 0.71 | 0.85 | 1.16 |
| 10-22 04:07 | +5 | XRP | UP | 0.71 | 0.85 | 1.16 |
| 10-22 04:06 | +10 stop | HYPE | UP | 0.54 | 0.78 | 2.09 |
| 10-22 04:06 | +5 | HYPE | UP | 0.54 | 0.63 | 0.55 |
| 10-22 04:05 | +10 stop | BTC | DOWN | 0.61 | 0.87 | 2.35 |
| 10-22 04:05 | +10 stop | NEAR | UP | 0.69 | 0.54 | -1.83 |
| 10-22 04:05 | +10 | NEAR | UP | 0.69 | no | -7.05 |
| 10-22 04:05 | +5 | NEAR | UP | 0.69 | no | -7.05 |
| 10-22 04:05 | +10 stop | SOL | UP | 0.70 | 0.53 | -2.03 |
| 10-22 04:05 | +20 | SOL | UP | 0.70 | no | -7.15 |
| 10-22 04:05 | +15 | SOL | UP | 0.70 | no | -7.15 |
| 10-22 04:05 | +10 | SOL | UP | 0.70 | no | -7.15 |
| 10-22 04:05 | +5 | SOL | UP | 0.70 | 0.78 | 0.52 |
