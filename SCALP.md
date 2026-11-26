# Range-Scalp Bot

*Updated Thu Nov 26 03:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72322 | 63127 | 9195 (158) | 1 | $-19240.04 | -4.2% |
| **+10¢** | 53944 | 43208 | 10736 (203) | 3 | $-17816.64 | -5.3% |
| **+15¢** | 45165 | 33602 | 11563 (260) | 2 | $-15905.73 | -5.6% |
| **+20¢** | 40208 | 28028 | 12180 (326) | 2 | $-14320.16 | -5.7% |
| **+10¢ (15¢ stop)** | 88058 | 87849 | 209 (128) | 3 | $-32305.94 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 03:47 | +5 | ZEC | UP | 0.68 | open |  |
| 11-26 03:47 | +10 stop | NEAR | UP | 0.62 | open |  |
| 11-26 03:47 | +10 | NEAR | UP | 0.62 | open |  |
| 11-26 03:47 | +5 | NEAR | UP | 0.62 | 0.71 | 0.59 |
| 11-26 03:46 | +10 stop | ZEC | UP | 0.64 | open |  |
| 11-26 03:46 | +20 | ZEC | UP | 0.64 | open |  |
| 11-26 03:46 | +15 | ZEC | UP | 0.64 | open |  |
| 11-26 03:46 | +10 | ZEC | UP | 0.64 | open |  |
| 11-26 03:46 | +5 | ZEC | UP | 0.63 | 0.70 | 0.34 |
| 11-26 03:46 | +10 stop | NEAR | UP | 0.51 | 0.64 | 0.95 |
| 11-26 03:46 | +20 | NEAR | UP | 0.51 | 0.71 | 1.67 |
| 11-26 03:46 | +15 | NEAR | UP | 0.51 | 0.71 | 1.67 |
| 11-26 03:46 | +10 | NEAR | UP | 0.51 | 0.64 | 0.95 |
| 11-26 03:46 | +5 | NEAR | UP | 0.51 | 0.64 | 0.95 |
| 11-26 03:46 | +10 stop | DOGE | UP | 0.68 | open |  |
| 11-26 03:46 | +20 | DOGE | UP | 0.68 | open |  |
| 11-26 03:46 | +15 | DOGE | UP | 0.68 | open |  |
| 11-26 03:46 | +10 | DOGE | UP | 0.68 | open |  |
| 11-26 03:46 | +5 | DOGE | UP | 0.68 | 0.73 | 0.20 |
| 11-26 03:43 | +10 stop | BNB | DOWN | 0.58 | 0.86 | 2.53 |
| 11-26 03:43 | +10 stop | DOGE | UP | 0.69 | 0.81 | 0.95 |
| 11-26 03:42 | +5 | BNB | DOWN | 0.64 | 0.86 | 1.99 |
| 11-26 03:41 | +10 stop | BNB | DOWN | 0.69 | 0.54 | -1.83 |
| 11-26 03:41 | +15 | BNB | DOWN | 0.69 | 0.86 | 1.46 |
| 11-26 03:41 | +10 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 11-26 03:41 | +10 stop | XRP | DOWN | 0.54 | 0.36 | -2.15 |
| 11-26 03:41 | +15 | XRP | DOWN | 0.54 | yes | -5.58 |
| 11-26 03:41 | +10 | XRP | DOWN | 0.54 | yes | -5.58 |
| 11-26 03:41 | +5 | XRP | DOWN | 0.54 | yes | -5.58 |
| 11-26 03:40 | +10 stop | DOGE | DOWN | 0.61 | 0.46 | -1.87 |
| 11-26 03:40 | +10 | DOGE | DOWN | 0.61 | yes | -6.29 |
| 11-26 03:40 | +5 | DOGE | DOWN | 0.61 | yes | -6.29 |
| 11-26 03:39 | +10 stop | HYPE | DOWN | 0.58 | 0.77 | 1.59 |
| 11-26 03:39 | +10 stop | ETH | DOWN | 0.67 | 0.82 | 1.27 |
| 11-26 03:39 | +15 | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 11-26 03:39 | +10 | ETH | DOWN | 0.66 | 0.82 | 1.33 |
| 11-26 03:39 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 11-26 03:39 | +10 stop | BTC | DOWN | 0.62 | 0.75 | 0.99 |
| 11-26 03:39 | +5 | BTC | DOWN | 0.62 | 0.69 | 0.38 |
| 11-26 03:37 | +10 stop | HYPE | DOWN | 0.71 | 0.55 | -1.93 |
