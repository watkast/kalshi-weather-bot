# Range-Scalp Bot

*Updated Sat Oct 17 21:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21617 | 18847 | 2770 (29) | 1 | $-6093.21 | -4.5% |
| **+10¢** | 16257 | 13052 | 3205 (41) | 3 | $-5419.41 | -5.3% |
| **+15¢** | 13592 | 10133 | 3459 (61) | 4 | $-4926.12 | -5.8% |
| **+20¢** | 12035 | 8410 | 3625 (80) | 5 | $-4380.01 | -5.8% |
| **+10¢ (15¢ stop)** | 26531 | 26481 | 50 (29) | 0 | $-10078.21 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 21:33 | +10 stop | HYPE | DOWN | 0.59 | 0.78 | 1.60 |
| 10-17 21:33 | +15 | HYPE | DOWN | 0.59 | 0.78 | 1.60 |
| 10-17 21:33 | +10 | HYPE | DOWN | 0.59 | 0.78 | 1.60 |
| 10-17 21:33 | +5 | HYPE | DOWN | 0.59 | 0.66 | 0.37 |
| 10-17 21:33 | +10 stop | NEAR | DOWN | 0.58 | 0.79 | 1.76 |
| 10-17 21:33 | +10 | NEAR | DOWN | 0.58 | 0.79 | 1.81 |
| 10-17 21:33 | +5 | NEAR | DOWN | 0.56 | 0.79 | 2.00 |
| 10-17 21:31 | +10 stop | BNB | DOWN | 0.71 | 0.85 | 1.16 |
| 10-17 21:31 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 10-17 21:31 | +10 | BNB | DOWN | 0.71 | 0.85 | 1.16 |
| 10-17 21:31 | +10 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 10-17 21:31 | +5 | NEAR | DOWN | 0.67 | 0.82 | 1.27 |
| 10-17 21:31 | +5 | XRP | DOWN | 0.67 | 0.86 | 1.65 |
| 10-17 21:31 | +10 stop | BTC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-17 21:31 | +20 | BTC | DOWN | 0.71 | 0.92 | 1.88 |
| 10-17 21:31 | +15 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-17 21:31 | +10 | BTC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-17 21:31 | +5 | BTC | DOWN | 0.71 | 0.80 | 0.63 |
| 10-17 21:31 | +10 | ETH | DOWN | 0.69 | 0.88 | 1.67 |
| 10-17 21:31 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 10-17 21:31 | +10 stop | BNB | UP | 0.41 | 0.60 | 1.56 |
| 10-17 21:31 | +20 | BNB | UP | 0.41 | open |  |
| 10-17 21:31 | +15 | BNB | UP | 0.41 | 0.60 | 1.56 |
| 10-17 21:31 | +10 | BNB | UP | 0.41 | 0.60 | 1.56 |
| 10-17 21:31 | +5 | BNB | UP | 0.45 | 0.60 | 1.15 |
| 10-17 21:31 | +10 stop | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-17 21:31 | +20 | HYPE | DOWN | 0.65 | 0.87 | 1.96 |
| 10-17 21:31 | +15 | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-17 21:31 | +10 | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-17 21:31 | +5 | HYPE | DOWN | 0.65 | 0.71 | 0.29 |
| 10-17 21:31 | +10 stop | NEAR | UP | 0.46 | 0.17 | -3.17 |
| 10-17 21:31 | +20 | NEAR | UP | 0.46 | open |  |
| 10-17 21:31 | +15 | NEAR | UP | 0.45 | open |  |
| 10-17 21:31 | +10 | NEAR | UP | 0.45 | 0.55 | 0.64 |
| 10-17 21:31 | +5 | NEAR | UP | 0.45 | 0.55 | 0.64 |
| 10-17 21:31 | +10 stop | DOGE | UP | 0.57 | 0.37 | -2.35 |
| 10-17 21:31 | +20 | DOGE | UP | 0.57 | open |  |
| 10-17 21:31 | +15 | DOGE | UP | 0.58 | open |  |
| 10-17 21:31 | +10 | DOGE | UP | 0.58 | open |  |
| 10-17 21:31 | +5 | DOGE | UP | 0.58 | 0.63 | 0.15 |
