# Range-Scalp Bot

*Updated Thu Oct 15 00:49 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16821 | 14590 | 2231 (28) | 6 | $-5223.16 | -4.9% |
| **+10¢** | 12715 | 10128 | 2587 (40) | 6 | $-4773.73 | -6.0% |
| **+15¢** | 10679 | 7900 | 2779 (59) | 6 | $-4283.48 | -6.4% |
| **+20¢** | 9486 | 6575 | 2911 (76) | 8 | $-3783.41 | -6.4% |
| **+10¢ (15¢ stop)** | 20713 | 20663 | 50 (29) | 1 | $-8004.59 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 00:48 | +10 stop | NEAR | DOWN | 0.58 | open |  |
| 10-15 00:47 | +10 stop | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 10-15 00:47 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-15 00:47 | +10 stop | ETH | DOWN | 0.63 | 0.74 | 0.80 |
| 10-15 00:47 | +10 stop | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 10-15 00:47 | +20 | XRP | DOWN | 0.56 | 0.76 | 1.69 |
| 10-15 00:47 | +15 | XRP | DOWN | 0.56 | 0.76 | 1.69 |
| 10-15 00:47 | +10 | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 10-15 00:47 | +5 | XRP | DOWN | 0.56 | 0.65 | 0.56 |
| 10-15 00:46 | +10 stop | SOL | DOWN | 0.59 | 0.70 | 0.78 |
| 10-15 00:46 | +10 stop | BNB | DOWN | 0.66 | 0.81 | 1.24 |
| 10-15 00:46 | +20 | BNB | DOWN | 0.65 | open |  |
| 10-15 00:46 | +15 | BNB | DOWN | 0.65 | 0.81 | 1.33 |
| 10-15 00:46 | +10 | BNB | DOWN | 0.65 | 0.81 | 1.33 |
| 10-15 00:46 | +5 | BNB | DOWN | 0.65 | 0.72 | 0.39 |
| 10-15 00:46 | +10 stop | ZEC | UP | 0.55 | 0.38 | -2.05 |
| 10-15 00:46 | +20 | ZEC | UP | 0.55 | open |  |
| 10-15 00:46 | +15 | ZEC | UP | 0.56 | open |  |
| 10-15 00:46 | +10 | ZEC | UP | 0.56 | open |  |
| 10-15 00:46 | +5 | ZEC | UP | 0.56 | open |  |
| 10-15 00:46 | +10 stop | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-15 00:46 | +20 | BTC | DOWN | 0.59 | open |  |
| 10-15 00:46 | +15 | BTC | DOWN | 0.59 | 0.75 | 1.29 |
| 10-15 00:46 | +10 | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-15 00:46 | +5 | BTC | DOWN | 0.59 | 0.64 | 0.16 |
| 10-15 00:46 | +10 stop | NEAR | UP | 0.70 | 0.53 | -2.03 |
| 10-15 00:46 | +20 | NEAR | UP | 0.70 | open |  |
| 10-15 00:46 | +15 | NEAR | UP | 0.70 | open |  |
| 10-15 00:46 | +10 | NEAR | UP | 0.70 | open |  |
| 10-15 00:46 | +5 | NEAR | UP | 0.70 | open |  |
| 10-15 00:46 | +10 stop | DOGE | UP | 0.64 | 0.47 | -2.05 |
| 10-15 00:46 | +20 | DOGE | UP | 0.64 | open |  |
| 10-15 00:46 | +15 | DOGE | UP | 0.64 | open |  |
| 10-15 00:46 | +10 | DOGE | UP | 0.64 | open |  |
| 10-15 00:46 | +5 | DOGE | UP | 0.64 | open |  |
| 10-15 00:46 | +10 stop | ETH | UP | 0.60 | 0.40 | -2.34 |
| 10-15 00:46 | +20 | ETH | UP | 0.60 | open |  |
| 10-15 00:46 | +15 | ETH | UP | 0.61 | open |  |
| 10-15 00:46 | +10 | ETH | UP | 0.61 | open |  |
| 10-15 00:46 | +5 | ETH | UP | 0.61 | open |  |
