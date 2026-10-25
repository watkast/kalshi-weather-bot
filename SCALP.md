# Range-Scalp Bot

*Updated Sun Oct 25 14:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33257 | 29019 | 4238 (42) | 7 | $-9322.26 | -4.4% |
| **+10¢** | 24890 | 19985 | 4905 (60) | 7 | $-8286.49 | -5.3% |
| **+15¢** | 20823 | 15540 | 5283 (83) | 7 | $-7480.25 | -5.7% |
| **+20¢** | 18447 | 12915 | 5532 (105) | 9 | $-6604.04 | -5.7% |
| **+10¢ (15¢ stop)** | 40787 | 40727 | 60 (32) | 4 | $-15592.20 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 14:08 | +10 stop | ZEC | DOWN | 0.63 | open |  |
| 10-25 14:08 | +20 | ZEC | DOWN | 0.64 | open |  |
| 10-25 14:08 | +15 | ZEC | DOWN | 0.64 | open |  |
| 10-25 14:08 | +10 | ZEC | DOWN | 0.64 | open |  |
| 10-25 14:08 | +5 | ZEC | DOWN | 0.64 | open |  |
| 10-25 14:08 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 10-25 14:08 | +10 | BTC | DOWN | 0.70 | open |  |
| 10-25 14:08 | +5 | BTC | DOWN | 0.70 | open |  |
| 10-25 14:07 | +5 | ETH | DOWN | 0.71 | open |  |
| 10-25 14:07 | +5 | DOGE | DOWN | 0.71 | open |  |
| 10-25 14:06 | +10 stop | SOL | DOWN | 0.65 | 0.48 | -2.04 |
| 10-25 14:06 | +10 | SOL | DOWN | 0.65 | open |  |
| 10-25 14:06 | +5 | SOL | DOWN | 0.65 | open |  |
| 10-25 14:06 | +10 | ETH | DOWN | 0.64 | open |  |
| 10-25 14:06 | +5 | ETH | DOWN | 0.63 | 0.69 | 0.28 |
| 10-25 14:06 | +5 | DOGE | DOWN | 0.58 | 0.64 | 0.25 |
| 10-25 14:04 | +5 | SOL | DOWN | 0.69 | 0.77 | 0.52 |
| 10-25 14:04 | +10 stop | ETH | DOWN | 0.70 | open |  |
| 10-25 14:04 | +5 | ETH | DOWN | 0.70 | 0.77 | 0.42 |
| 10-25 14:04 | +10 stop | DOGE | DOWN | 0.65 | open |  |
| 10-25 14:04 | +15 | DOGE | DOWN | 0.65 | open |  |
| 10-25 14:04 | +10 | DOGE | DOWN | 0.65 | open |  |
| 10-25 14:04 | +5 | DOGE | DOWN | 0.65 | 0.73 | 0.50 |
| 10-25 14:04 | +10 stop | NEAR | DOWN | 0.61 | 0.43 | -2.15 |
| 10-25 14:04 | +10 stop | BNB | DOWN | 0.51 | 0.29 | -2.53 |
| 10-25 14:03 | +10 stop | XRP | DOWN | 0.65 | 0.78 | 1.01 |
| 10-25 14:02 | +10 stop | NEAR | UP | 0.56 | 0.30 | -2.93 |
| 10-25 14:02 | +5 | NEAR | UP | 0.56 | open |  |
| 10-25 14:02 | +10 stop | BNB | UP | 0.65 | 0.47 | -2.18 |
| 10-25 14:02 | +15 | XRP | DOWN | 0.56 | 0.72 | 1.27 |
| 10-25 14:02 | +10 | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 10-25 14:02 | +5 | XRP | DOWN | 0.59 | 0.67 | 0.47 |
| 10-25 14:02 | +5 | BTC | DOWN | 0.57 | 0.78 | 1.79 |
| 10-25 14:02 | +10 stop | DOGE | DOWN | 0.53 | 0.64 | 0.75 |
| 10-25 14:02 | +15 | DOGE | DOWN | 0.53 | 0.77 | 2.09 |
| 10-25 14:02 | +10 | DOGE | DOWN | 0.53 | 0.64 | 0.75 |
| 10-25 14:02 | +5 | DOGE | DOWN | 0.53 | 0.59 | 0.25 |
| 10-25 14:02 | +5 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-25 14:02 | +10 stop | HYPE | DOWN | 0.62 | 0.80 | 1.51 |
| 10-25 14:02 | +15 | HYPE | DOWN | 0.61 | 0.80 | 1.61 |
