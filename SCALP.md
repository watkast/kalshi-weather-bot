# Range-Scalp Bot

*Updated Tue Nov 03 00:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45333 | 39471 | 5862 (67) | 8 | $-13112.96 | -4.6% |
| **+10¢** | 33834 | 27042 | 6792 (89) | 9 | $-11986.95 | -5.6% |
| **+15¢** | 28302 | 20993 | 7309 (116) | 9 | $-11041.61 | -6.2% |
| **+20¢** | 25133 | 17478 | 7655 (151) | 9 | $-9813.90 | -6.2% |
| **+10¢ (15¢ stop)** | 55311 | 55224 | 87 (51) | 7 | $-20891.47 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 00:05 | +5 | NEAR | DOWN | 0.56 | open |  |
| 11-03 00:04 | +10 stop | SOL | UP | 0.62 | open |  |
| 11-03 00:04 | +15 | SOL | UP | 0.62 | open |  |
| 11-03 00:04 | +10 | SOL | UP | 0.62 | open |  |
| 11-03 00:04 | +5 | SOL | UP | 0.62 | open |  |
| 11-03 00:04 | +10 stop | BNB | UP | 0.59 | open |  |
| 11-03 00:04 | +10 | BNB | UP | 0.59 | open |  |
| 11-03 00:04 | +10 stop | DOGE | DOWN | 0.62 | open |  |
| 11-03 00:04 | +15 | DOGE | DOWN | 0.62 | open |  |
| 11-03 00:04 | +10 | DOGE | DOWN | 0.62 | open |  |
| 11-03 00:04 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-03 00:04 | +5 | ZEC | DOWN | 0.64 | open |  |
| 11-03 00:04 | +5 | BNB | UP | 0.60 | open |  |
| 11-03 00:03 | +10 stop | NEAR | DOWN | 0.60 | open |  |
| 11-03 00:03 | +10 | NEAR | DOWN | 0.60 | open |  |
| 11-03 00:03 | +5 | NEAR | DOWN | 0.60 | 0.65 | 0.17 |
| 11-03 00:03 | +10 stop | HYPE | UP | 0.63 | 0.76 | 0.99 |
| 11-03 00:03 | +5 | SOL | UP | 0.63 | 0.72 | 0.58 |
| 11-03 00:03 | +10 stop | ETH | DOWN | 0.67 | open |  |
| 11-03 00:03 | +10 stop | NEAR | DOWN | 0.54 | 0.66 | 0.86 |
| 11-03 00:03 | +20 | NEAR | DOWN | 0.54 | open |  |
| 11-03 00:03 | +15 | NEAR | DOWN | 0.54 | open |  |
| 11-03 00:03 | +10 | NEAR | DOWN | 0.54 | 0.66 | 0.86 |
| 11-03 00:03 | +5 | NEAR | DOWN | 0.54 | 0.66 | 0.86 |
| 11-03 00:02 | +10 stop | SOL | UP | 0.53 | 0.64 | 0.75 |
| 11-03 00:02 | +20 | SOL | UP | 0.53 | open |  |
| 11-03 00:02 | +15 | SOL | UP | 0.53 | 0.72 | 1.57 |
| 11-03 00:02 | +10 | SOL | UP | 0.53 | 0.64 | 0.75 |
| 11-03 00:02 | +5 | SOL | UP | 0.53 | 0.58 | 0.14 |
| 11-03 00:02 | +10 stop | BNB | UP | 0.48 | 0.60 | 0.85 |
| 11-03 00:02 | +20 | BNB | UP | 0.48 | open |  |
| 11-03 00:02 | +15 | BNB | UP | 0.48 | open |  |
| 11-03 00:02 | +10 | BNB | UP | 0.48 | 0.60 | 0.85 |
| 11-03 00:02 | +5 | BNB | UP | 0.48 | 0.54 | 0.24 |
| 11-03 00:02 | +10 stop | BTC | DOWN | 0.53 | 0.64 | 0.75 |
| 11-03 00:02 | +10 stop | ETH | DOWN | 0.57 | 0.70 | 0.97 |
| 11-03 00:02 | +10 stop | ZEC | DOWN | 0.62 | open |  |
| 11-03 00:02 | +20 | ZEC | DOWN | 0.62 | open |  |
| 11-03 00:02 | +15 | ZEC | DOWN | 0.63 | open |  |
| 11-03 00:02 | +10 | ZEC | DOWN | 0.63 | open |  |
