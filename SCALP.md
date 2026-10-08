# Range-Scalp Bot

*Updated Thu Oct 08 00:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7030 | 6103 | 927 (13) | 2 | $-2089.18 | -4.7% |
| **+10¢** | 5329 | 4246 | 1083 (20) | 4 | $-1962.14 | -5.8% |
| **+15¢** | 4474 | 3332 | 1142 (28) | 4 | $-1593.37 | -5.7% |
| **+20¢** | 3996 | 2806 | 1190 (35) | 4 | $-1253.15 | -5.0% |
| **+10¢ (15¢ stop)** | 8504 | 8482 | 22 (14) | 0 | $-2986.50 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 00:28 | +5 | BTC | DOWN | 0.10 | 0.66 | 5.40 |
| 10-08 00:28 | +10 stop | BTC | DOWN | 0.65 | 0.08 | -5.94 |
| 10-08 00:28 | +20 | BTC | DOWN | 0.65 | open |  |
| 10-08 00:28 | +15 | BTC | DOWN | 0.65 | open |  |
| 10-08 00:28 | +10 | BTC | DOWN | 0.65 | open |  |
| 10-08 00:27 | +10 stop | ETH | UP | 0.66 | 0.77 | 0.81 |
| 10-08 00:27 | +20 | ETH | UP | 0.65 | 0.88 | 2.06 |
| 10-08 00:27 | +15 | ETH | UP | 0.65 | 0.88 | 2.06 |
| 10-08 00:27 | +10 | ETH | UP | 0.63 | 0.77 | 1.10 |
| 10-08 00:27 | +5 | ETH | UP | 0.63 | 0.77 | 1.10 |
| 10-08 00:27 | +10 stop | SOL | UP | 0.66 | 0.81 | 1.23 |
| 10-08 00:26 | +10 stop | NEAR | DOWN | 0.43 | 0.56 | 0.95 |
| 10-08 00:26 | +20 | NEAR | DOWN | 0.43 | 0.90 | 4.47 |
| 10-08 00:26 | +15 | NEAR | DOWN | 0.43 | 0.61 | 1.46 |
| 10-08 00:26 | +10 | NEAR | DOWN | 0.43 | 0.56 | 0.95 |
| 10-08 00:26 | +5 | NEAR | DOWN | 0.43 | 0.56 | 0.94 |
| 10-08 00:26 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-08 00:26 | +5 | XRP | UP | 0.61 | 0.92 | 2.82 |
| 10-08 00:26 | +10 stop | ETH | UP | 0.48 | 0.80 | 2.93 |
| 10-08 00:26 | +10 | ETH | UP | 0.46 | 0.80 | 3.10 |
| 10-08 00:26 | +5 | ETH | UP | 0.46 | 0.53 | 0.34 |
| 10-08 00:26 | +10 stop | SOL | DOWN | 0.65 | 0.23 | -4.49 |
| 10-08 00:26 | +20 | SOL | DOWN | 0.65 | open |  |
| 10-08 00:26 | +15 | SOL | DOWN | 0.65 | open |  |
| 10-08 00:26 | +10 | SOL | DOWN | 0.65 | open |  |
| 10-08 00:26 | +5 | SOL | DOWN | 0.65 | open |  |
| 10-08 00:26 | +10 stop | XRP | UP | 0.58 | 0.92 | 3.11 |
| 10-08 00:26 | +20 | XRP | UP | 0.58 | 0.92 | 3.11 |
| 10-08 00:26 | +15 | XRP | UP | 0.58 | 0.92 | 3.11 |
| 10-08 00:26 | +10 | XRP | UP | 0.58 | 0.92 | 3.11 |
| 10-08 00:26 | +5 | XRP | UP | 0.58 | 0.64 | 0.25 |
| 10-08 00:25 | +10 stop | ETH | UP | 0.48 | 0.58 | 0.64 |
| 10-08 00:25 | +10 | ETH | UP | 0.48 | 0.58 | 0.64 |
| 10-08 00:25 | +5 | ETH | UP | 0.49 | 0.58 | 0.54 |
| 10-08 00:25 | +10 stop | ETH | UP | 0.59 | 0.69 | 0.68 |
| 10-08 00:25 | +20 | ETH | UP | 0.59 | 0.80 | 1.81 |
| 10-08 00:25 | +15 | ETH | UP | 0.59 | 0.80 | 1.81 |
| 10-08 00:25 | +10 | ETH | UP | 0.59 | 0.69 | 0.68 |
| 10-08 00:25 | +5 | ETH | UP | 0.59 | 0.69 | 0.68 |
| 10-08 00:25 | +10 stop | BNB | UP | 0.48 | 0.59 | 0.76 |
