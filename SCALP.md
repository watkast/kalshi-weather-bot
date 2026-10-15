# Range-Scalp Bot

*Updated Thu Oct 15 22:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18221 | 15816 | 2405 (28) | 3 | $-5603.75 | -4.9% |
| **+10¢** | 13758 | 10975 | 2783 (40) | 3 | $-5058.79 | -5.8% |
| **+15¢** | 11537 | 8543 | 2994 (59) | 4 | $-4581.13 | -6.3% |
| **+20¢** | 10250 | 7121 | 3129 (78) | 4 | $-3972.72 | -6.2% |
| **+10¢ (15¢ stop)** | 22423 | 22373 | 50 (29) | 2 | $-8691.83 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 22:06 | +10 stop | NEAR | DOWN | 0.65 | open |  |
| 10-15 22:06 | +10 stop | ZEC | DOWN | 0.64 | open |  |
| 10-15 22:04 | +10 stop | NEAR | UP | 0.65 | 0.46 | -2.24 |
| 10-15 22:04 | +20 | NEAR | UP | 0.65 | open |  |
| 10-15 22:04 | +15 | NEAR | UP | 0.65 | open |  |
| 10-15 22:04 | +10 | NEAR | UP | 0.65 | open |  |
| 10-15 22:04 | +5 | NEAR | UP | 0.65 | open |  |
| 10-15 22:04 | +5 | BNB | UP | 0.67 | open |  |
| 10-15 22:03 | +5 | ZEC | UP | 0.69 | open |  |
| 10-15 22:03 | +10 stop | BNB | UP | 0.71 | 0.55 | -1.93 |
| 10-15 22:03 | +10 stop | ZEC | UP | 0.61 | 0.45 | -1.95 |
| 10-15 22:03 | +20 | ZEC | UP | 0.61 | open |  |
| 10-15 22:03 | +15 | ZEC | UP | 0.61 | open |  |
| 10-15 22:03 | +10 | ZEC | UP | 0.61 | open |  |
| 10-15 22:03 | +5 | ZEC | UP | 0.61 | 0.67 | 0.27 |
| 10-15 22:02 | +5 | BNB | UP | 0.57 | 0.64 | 0.35 |
| 10-15 22:01 | +10 stop | BNB | UP | 0.69 | 0.54 | -1.83 |
| 10-15 22:01 | +20 | BNB | UP | 0.68 | open |  |
| 10-15 22:01 | +15 | BNB | UP | 0.68 | open |  |
| 10-15 22:01 | +10 | BNB | UP | 0.68 | open |  |
| 10-15 22:01 | +5 | BNB | UP | 0.68 | 0.73 | 0.20 |
| 10-15 22:01 | +10 stop | SOL | UP | 0.71 | 0.83 | 0.95 |
| 10-15 22:01 | +20 | SOL | UP | 0.71 | open |  |
| 10-15 22:01 | +15 | SOL | UP | 0.71 | open |  |
| 10-15 22:01 | +10 | SOL | UP | 0.71 | 0.83 | 0.95 |
| 10-15 22:01 | +5 | SOL | UP | 0.71 | 0.77 | 0.32 |
| 10-15 21:58 | +10 stop | NEAR | DOWN | 0.63 | 0.85 | 1.94 |
| 10-15 21:58 | +10 stop | ETH | UP | 0.62 | 0.21 | -4.39 |
| 10-15 21:58 | +20 | ETH | UP | 0.62 | 0.97 | 3.35 |
| 10-15 21:58 | +15 | ETH | UP | 0.62 | 0.97 | 3.35 |
| 10-15 21:58 | +10 | ETH | UP | 0.62 | 0.97 | 3.35 |
| 10-15 21:58 | +5 | ETH | UP | 0.62 | 0.97 | 3.35 |
| 10-15 21:58 | +10 stop | BNB | UP | 0.54 | 0.27 | -3.02 |
| 10-15 21:58 | +20 | BNB | UP | 0.61 | 0.99 | 3.60 |
| 10-15 21:58 | +15 | BNB | UP | 0.59 | 0.99 | 3.81 |
| 10-15 21:58 | +10 | BNB | UP | 0.57 | 0.99 | 4.01 |
| 10-15 21:58 | +5 | BNB | UP | 0.57 | 0.99 | 4.01 |
| 10-15 21:58 | +10 stop | XRP | UP | 0.70 | 0.12 | -6.03 |
| 10-15 21:58 | +10 | XRP | UP | 0.70 | no | -7.15 |
| 10-15 21:58 | +5 | XRP | UP | 0.70 | no | -7.15 |
