# Range-Scalp Bot

*Updated Sat Oct 17 04:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20349 | 17702 | 2647 (29) | 0 | $-6007.51 | -4.7% |
| **+10¢** | 15337 | 12283 | 3054 (41) | 0 | $-5344.68 | -5.5% |
| **+15¢** | 12820 | 9536 | 3284 (60) | 4 | $-4813.53 | -6.0% |
| **+20¢** | 11368 | 7928 | 3440 (79) | 7 | $-4250.62 | -6.0% |
| **+10¢ (15¢ stop)** | 25018 | 24968 | 50 (29) | 0 | $-9463.99 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 04:18 | +5 | BTC | DOWN | 0.62 | 0.70 | 0.48 |
| 10-17 04:18 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 10-17 04:16 | +10 stop | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-17 04:16 | +20 | BNB | DOWN | 0.63 | open |  |
| 10-17 04:16 | +15 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 10-17 04:16 | +10 | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-17 04:16 | +5 | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-17 04:16 | +10 stop | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-17 04:16 | +20 | BTC | DOWN | 0.59 | open |  |
| 10-17 04:16 | +15 | BTC | DOWN | 0.59 | open |  |
| 10-17 04:16 | +10 | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-17 04:16 | +5 | BTC | DOWN | 0.59 | 0.64 | 0.16 |
| 10-17 04:16 | +10 stop | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 10-17 04:16 | +20 | SOL | DOWN | 0.66 | open |  |
| 10-17 04:16 | +15 | SOL | DOWN | 0.66 | open |  |
| 10-17 04:16 | +10 | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 10-17 04:16 | +5 | SOL | DOWN | 0.66 | 0.75 | 0.60 |
| 10-17 04:16 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-17 04:16 | +20 | DOGE | DOWN | 0.66 | open |  |
| 10-17 04:16 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-17 04:16 | +10 | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-17 04:16 | +5 | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-17 04:16 | +10 stop | NEAR | DOWN | 0.62 | 0.77 | 1.20 |
| 10-17 04:16 | +20 | NEAR | DOWN | 0.62 | 0.82 | 1.72 |
| 10-17 04:16 | +15 | NEAR | DOWN | 0.62 | 0.77 | 1.20 |
| 10-17 04:16 | +10 | NEAR | DOWN | 0.62 | 0.77 | 1.20 |
| 10-17 04:16 | +5 | NEAR | DOWN | 0.62 | 0.68 | 0.27 |
| 10-17 04:16 | +10 stop | ETH | DOWN | 0.58 | 0.72 | 1.07 |
| 10-17 04:16 | +20 | ETH | DOWN | 0.58 | open |  |
| 10-17 04:16 | +15 | ETH | DOWN | 0.58 | open |  |
| 10-17 04:16 | +10 | ETH | DOWN | 0.58 | 0.72 | 1.03 |
| 10-17 04:16 | +5 | ETH | DOWN | 0.59 | 0.67 | 0.47 |
| 10-17 04:16 | +10 stop | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 10-17 04:16 | +20 | XRP | DOWN | 0.59 | open |  |
| 10-17 04:16 | +15 | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 10-17 04:16 | +10 | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 10-17 04:16 | +5 | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 10-17 04:16 | +10 stop | ZEC | DOWN | 0.66 | 0.78 | 0.91 |
| 10-17 04:16 | +20 | ZEC | DOWN | 0.68 | open |  |
| 10-17 04:16 | +15 | ZEC | DOWN | 0.68 | open |  |
