# Range-Scalp Bot

*Updated Fri Oct 09 22:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9547 | 8242 | 1305 (18) | 1 | $-3210.42 | -5.3% |
| **+10¢** | 7206 | 5675 | 1531 (30) | 1 | $-3140.32 | -6.9% |
| **+15¢** | 6077 | 4465 | 1612 (43) | 1 | $-2593.33 | -6.8% |
| **+20¢** | 5410 | 3736 | 1674 (55) | 2 | $-2151.28 | -6.3% |
| **+10¢ (15¢ stop)** | 11678 | 11643 | 35 (22) | 1 | $-4477.88 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 22:07 | +10 stop | HYPE | DOWN | 0.56 | open |  |
| 10-09 22:07 | +20 | HYPE | DOWN | 0.56 | open |  |
| 10-09 22:07 | +15 | HYPE | DOWN | 0.56 | open |  |
| 10-09 22:07 | +10 | HYPE | DOWN | 0.56 | open |  |
| 10-09 22:07 | +5 | HYPE | DOWN | 0.58 | open |  |
| 10-09 22:01 | +10 stop | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 10-09 22:01 | +20 | BTC | DOWN | 0.70 | open |  |
| 10-09 22:01 | +15 | BTC | DOWN | 0.70 | 0.86 | 1.36 |
| 10-09 22:01 | +10 | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 10-09 22:01 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-09 22:01 | +10 stop | ETH | DOWN | 0.68 | 0.81 | 1.03 |
| 10-09 22:01 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 10-09 22:01 | +15 | ETH | DOWN | 0.67 | 0.84 | 1.44 |
| 10-09 22:01 | +10 | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 10-09 22:01 | +5 | ETH | DOWN | 0.67 | 0.76 | 0.61 |
| 10-09 22:01 | +10 stop | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-09 22:01 | +20 | BNB | DOWN | 0.60 | 0.81 | 1.82 |
| 10-09 22:01 | +15 | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-09 22:01 | +10 | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-09 22:01 | +5 | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-09 21:57 | +10 stop | ETH | UP | 0.68 | 0.86 | 1.55 |
| 10-09 21:57 | +10 stop | XRP | DOWN | 0.70 | 0.34 | -3.93 |
| 10-09 21:57 | +20 | XRP | DOWN | 0.70 | yes | -7.17 |
| 10-09 21:57 | +15 | XRP | DOWN | 0.70 | yes | -7.17 |
| 10-09 21:57 | +10 | XRP | DOWN | 0.70 | yes | -7.17 |
| 10-09 21:57 | +5 | XRP | DOWN | 0.70 | yes | -7.17 |
| 10-09 21:57 | +10 stop | BNB | DOWN | 0.48 | 0.69 | 1.77 |
| 10-09 21:57 | +20 | BNB | DOWN | 0.50 | 0.79 | 2.60 |
| 10-09 21:57 | +15 | BNB | DOWN | 0.50 | 0.69 | 1.57 |
| 10-09 21:57 | +10 | BNB | DOWN | 0.51 | 0.69 | 1.47 |
| 10-09 21:57 | +5 | BNB | DOWN | 0.50 | 0.69 | 1.57 |
| 10-09 21:56 | +10 stop | NEAR | UP | 0.65 | 0.92 | 2.45 |
| 10-09 21:54 | +10 stop | DOGE | UP | 0.62 | 0.77 | 1.15 |
| 10-09 21:53 | +10 stop | ETH | DOWN | 0.61 | 0.33 | -3.11 |
| 10-09 21:52 | +10 stop | DOGE | UP | 0.67 | 0.39 | -3.13 |
| 10-09 21:52 | +15 | DOGE | UP | 0.66 | 0.81 | 1.28 |
| 10-09 21:52 | +10 | DOGE | UP | 0.66 | 0.77 | 0.81 |
| 10-09 21:52 | +5 | DOGE | UP | 0.66 | 0.77 | 0.86 |
| 10-09 21:52 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-09 21:52 | +20 | XRP | DOWN | 0.66 | 0.86 | 1.75 |
