# Range-Scalp Bot

*Updated Thu Oct 15 16:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17810 | 15455 | 2355 (28) | 3 | $-5496.43 | -4.9% |
| **+10¢** | 13451 | 10724 | 2727 (40) | 7 | $-4996.18 | -5.9% |
| **+15¢** | 11283 | 8352 | 2931 (59) | 8 | $-4491.30 | -6.3% |
| **+20¢** | 10032 | 6965 | 3067 (77) | 9 | $-3921.29 | -6.2% |
| **+10¢ (15¢ stop)** | 21931 | 21881 | 50 (29) | 1 | $-8489.46 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 16:34 | +10 stop | HYPE | UP | 0.70 | open |  |
| 10-15 16:34 | +5 | ETH | DOWN | 0.47 | 0.57 | 0.64 |
| 10-15 16:34 | +5 | BTC | DOWN | 0.52 | 0.60 | 0.45 |
| 10-15 16:33 | +10 stop | SOL | DOWN | 0.71 | 0.54 | -2.03 |
| 10-15 16:33 | +10 | SOL | DOWN | 0.71 | open |  |
| 10-15 16:33 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 10-15 16:33 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-15 16:33 | +10 stop | NEAR | DOWN | 0.66 | 0.49 | -2.04 |
| 10-15 16:33 | +10 | NEAR | DOWN | 0.66 | open |  |
| 10-15 16:33 | +5 | NEAR | DOWN | 0.66 | open |  |
| 10-15 16:33 | +5 | ETH | DOWN | 0.58 | 0.70 | 0.87 |
| 10-15 16:33 | +10 stop | ZEC | DOWN | 0.56 | 0.32 | -2.73 |
| 10-15 16:33 | +10 stop | DOGE | DOWN | 0.50 | 0.30 | -2.35 |
| 10-15 16:32 | +5 | ZEC | DOWN | 0.70 | open |  |
| 10-15 16:32 | +10 stop | BNB | DOWN | 0.63 | 0.48 | -1.88 |
| 10-15 16:32 | +10 stop | ETH | DOWN | 0.67 | 0.47 | -2.34 |
| 10-15 16:32 | +20 | ETH | DOWN | 0.67 | open |  |
| 10-15 16:32 | +15 | ETH | DOWN | 0.67 | open |  |
| 10-15 16:32 | +10 | ETH | DOWN | 0.66 | open |  |
| 10-15 16:32 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 10-15 16:32 | +10 stop | BTC | DOWN | 0.68 | 0.50 | -2.14 |
| 10-15 16:32 | +20 | BTC | DOWN | 0.68 | open |  |
| 10-15 16:32 | +15 | BTC | DOWN | 0.67 | open |  |
| 10-15 16:32 | +10 | BTC | DOWN | 0.67 | open |  |
| 10-15 16:32 | +5 | BTC | DOWN | 0.66 | 0.74 | 0.50 |
| 10-15 16:32 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-15 16:32 | +20 | SOL | DOWN | 0.64 | open |  |
| 10-15 16:32 | +15 | SOL | DOWN | 0.63 | open |  |
| 10-15 16:32 | +10 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-15 16:32 | +5 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-15 16:32 | +10 stop | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 10-15 16:32 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-15 16:32 | +15 | NEAR | DOWN | 0.66 | open |  |
| 10-15 16:32 | +10 | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 10-15 16:32 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 10-15 16:32 | +5 | HYPE | UP | 0.60 | 0.69 | 0.58 |
| 10-15 16:31 | +10 stop | ZEC | UP | 0.52 | 0.34 | -2.12 |
| 10-15 16:31 | +20 | ZEC | UP | 0.52 | open |  |
| 10-15 16:31 | +15 | ZEC | UP | 0.52 | open |  |
| 10-15 16:31 | +10 | ZEC | UP | 0.51 | 0.66 | 1.16 |
