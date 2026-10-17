# Range-Scalp Bot

*Updated Sat Oct 17 04:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20334 | 17687 | 2647 (29) | 2 | $-6017.65 | -4.7% |
| **+10¢** | 15324 | 12270 | 3054 (41) | 2 | $-5359.73 | -5.6% |
| **+15¢** | 12811 | 9527 | 3284 (60) | 2 | $-4829.36 | -6.0% |
| **+20¢** | 11362 | 7922 | 3440 (79) | 2 | $-4265.03 | -6.0% |
| **+10¢ (15¢ stop)** | 25005 | 24955 | 50 (29) | 1 | $-9472.50 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 04:08 | +10 stop | NEAR | DOWN | 0.44 | 0.58 | 1.04 |
| 10-17 04:07 | +10 stop | BNB | UP | 0.57 | open |  |
| 10-17 04:06 | +10 | NEAR | UP | 0.64 | open |  |
| 10-17 04:06 | +5 | NEAR | UP | 0.64 | open |  |
| 10-17 04:06 | +10 stop | NEAR | UP | 0.71 | 0.49 | -2.53 |
| 10-17 04:05 | +10 stop | BNB | UP | 0.65 | 0.46 | -2.24 |
| 10-17 04:05 | +5 | BNB | UP | 0.65 | open |  |
| 10-17 04:05 | +10 stop | BNB | DOWN | 0.58 | 0.37 | -2.45 |
| 10-17 04:04 | +10 stop | NEAR | DOWN | 0.68 | 0.46 | -2.52 |
| 10-17 04:03 | +10 stop | BNB | UP | 0.56 | 0.39 | -2.05 |
| 10-17 04:03 | +20 | BNB | UP | 0.56 | open |  |
| 10-17 04:03 | +15 | BNB | UP | 0.56 | open |  |
| 10-17 04:03 | +10 | BNB | UP | 0.56 | open |  |
| 10-17 04:03 | +5 | BNB | UP | 0.56 | 0.61 | 0.15 |
| 10-17 04:03 | +10 stop | ETH | DOWN | 0.62 | 0.83 | 1.79 |
| 10-17 04:03 | +10 | ETH | DOWN | 0.62 | 0.83 | 1.79 |
| 10-17 04:03 | +10 stop | DOGE | DOWN | 0.54 | 0.77 | 1.99 |
| 10-17 04:03 | +20 | DOGE | DOWN | 0.54 | 0.77 | 1.99 |
| 10-17 04:03 | +15 | DOGE | DOWN | 0.54 | 0.77 | 1.99 |
| 10-17 04:03 | +10 | DOGE | DOWN | 0.54 | 0.77 | 1.99 |
| 10-17 04:03 | +5 | DOGE | DOWN | 0.54 | 0.59 | 0.15 |
| 10-17 04:03 | +10 stop | ZEC | DOWN | 0.50 | 0.69 | 1.57 |
| 10-17 04:03 | +20 | ZEC | DOWN | 0.52 | 0.73 | 1.78 |
| 10-17 04:03 | +15 | ZEC | DOWN | 0.52 | 0.69 | 1.37 |
| 10-17 04:03 | +10 | ZEC | DOWN | 0.52 | 0.69 | 1.37 |
| 10-17 04:03 | +5 | ZEC | DOWN | 0.52 | 0.69 | 1.37 |
| 10-17 04:02 | +5 | ETH | DOWN | 0.69 | 0.83 | 1.15 |
| 10-17 04:02 | +10 stop | DOGE | DOWN | 0.38 | 0.58 | 1.65 |
| 10-17 04:02 | +20 | DOGE | DOWN | 0.38 | 0.58 | 1.65 |
| 10-17 04:02 | +15 | DOGE | DOWN | 0.38 | 0.58 | 1.65 |
| 10-17 04:02 | +10 | DOGE | DOWN | 0.37 | 0.58 | 1.75 |
| 10-17 04:02 | +5 | DOGE | DOWN | 0.37 | 0.58 | 1.75 |
| 10-17 04:01 | +10 stop | BTC | DOWN | 0.65 | 0.79 | 1.12 |
| 10-17 04:01 | +20 | BTC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-17 04:01 | +15 | BTC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-17 04:01 | +10 | BTC | DOWN | 0.65 | 0.79 | 1.12 |
| 10-17 04:01 | +5 | BTC | DOWN | 0.65 | 0.73 | 0.50 |
| 10-17 04:01 | +10 stop | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 10-17 04:01 | +20 | SOL | DOWN | 0.71 | 0.92 | 1.91 |
| 10-17 04:01 | +15 | SOL | DOWN | 0.71 | 0.86 | 1.26 |
