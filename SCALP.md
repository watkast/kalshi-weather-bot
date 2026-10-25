# Range-Scalp Bot

*Updated Sun Oct 25 23:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33919 | 29614 | 4305 (43) | 2 | $-9375.70 | -4.4% |
| **+10¢** | 25392 | 20415 | 4977 (65) | 2 | $-8200.86 | -5.1% |
| **+15¢** | 21242 | 15885 | 5357 (89) | 2 | $-7317.09 | -5.5% |
| **+20¢** | 18823 | 13214 | 5609 (111) | 2 | $-6392.12 | -5.4% |
| **+10¢ (15¢ stop)** | 41544 | 41482 | 62 (33) | 2 | $-15792.83 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 23:52 | +10 stop | XRP | DOWN | 0.62 | open |  |
| 10-25 23:52 | +20 | XRP | DOWN | 0.62 | open |  |
| 10-25 23:52 | +15 | XRP | DOWN | 0.62 | open |  |
| 10-25 23:52 | +10 | XRP | DOWN | 0.63 | open |  |
| 10-25 23:52 | +5 | XRP | DOWN | 0.63 | open |  |
| 10-25 23:52 | +10 stop | NEAR | DOWN | 0.64 | open |  |
| 10-25 23:52 | +15 | NEAR | DOWN | 0.64 | open |  |
| 10-25 23:52 | +10 | NEAR | DOWN | 0.64 | open |  |
| 10-25 23:52 | +5 | NEAR | DOWN | 0.64 | open |  |
| 10-25 23:50 | +10 stop | NEAR | DOWN | 0.60 | 0.75 | 1.19 |
| 10-25 23:50 | +20 | NEAR | DOWN | 0.60 | open |  |
| 10-25 23:50 | +15 | NEAR | DOWN | 0.60 | 0.75 | 1.19 |
| 10-25 23:50 | +10 | NEAR | DOWN | 0.59 | 0.75 | 1.29 |
| 10-25 23:50 | +5 | NEAR | DOWN | 0.58 | 0.75 | 1.38 |
| 10-25 23:46 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-25 23:46 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-25 23:46 | +15 | BTC | DOWN | 0.69 | 0.88 | 1.67 |
| 10-25 23:46 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-25 23:46 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-25 23:42 | +10 stop | SOL | UP | 0.69 | 0.52 | -2.03 |
| 10-25 23:34 | +10 stop | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 10-25 23:34 | +20 | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 10-25 23:34 | +15 | NEAR | UP | 0.68 | 0.83 | 1.24 |
| 10-25 23:34 | +10 | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 10-25 23:34 | +5 | NEAR | UP | 0.68 | 0.77 | 0.61 |
| 10-25 23:34 | +10 stop | BTC | UP | 0.70 | 0.85 | 1.26 |
| 10-25 23:33 | +10 stop | DOGE | DOWN | 0.59 | 0.41 | -2.14 |
| 10-25 23:33 | +20 | DOGE | DOWN | 0.59 | 0.98 | 3.71 |
| 10-25 23:33 | +15 | DOGE | DOWN | 0.59 | 0.98 | 3.71 |
| 10-25 23:33 | +10 | DOGE | DOWN | 0.59 | 0.98 | 3.71 |
| 10-25 23:33 | +5 | DOGE | DOWN | 0.59 | 0.98 | 3.71 |
| 10-25 23:33 | +10 stop | BNB | DOWN | 0.57 | 0.34 | -2.64 |
| 10-25 23:33 | +20 | BNB | DOWN | 0.57 | yes | -5.88 |
| 10-25 23:33 | +15 | BNB | DOWN | 0.59 | yes | -6.07 |
| 10-25 23:33 | +10 | BNB | DOWN | 0.59 | yes | -6.07 |
| 10-25 23:33 | +5 | BNB | DOWN | 0.59 | yes | -6.07 |
| 10-25 23:33 | +10 stop | ETH | DOWN | 0.63 | 0.43 | -2.35 |
| 10-25 23:33 | +20 | ETH | DOWN | 0.63 | 1.00 | 3.49 |
| 10-25 23:33 | +15 | ETH | DOWN | 0.63 | 0.80 | 1.41 |
| 10-25 23:33 | +10 | ETH | DOWN | 0.63 | 0.80 | 1.41 |
