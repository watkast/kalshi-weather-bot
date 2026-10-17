# Range-Scalp Bot

*Updated Sat Oct 17 03:49 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20316 | 17669 | 2647 (29) | 4 | $-6027.74 | -4.7% |
| **+10¢** | 15309 | 12255 | 3054 (41) | 5 | $-5377.51 | -5.6% |
| **+15¢** | 12798 | 9514 | 3284 (60) | 6 | $-4850.01 | -6.0% |
| **+20¢** | 11349 | 7909 | 3440 (79) | 6 | $-4290.33 | -6.0% |
| **+10¢ (15¢ stop)** | 24982 | 24932 | 50 (29) | 5 | $-9469.72 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 03:48 | +10 stop | ZEC | DOWN | 0.57 | open |  |
| 10-17 03:46 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 10-17 03:46 | +20 | BNB | DOWN | 0.65 | open |  |
| 10-17 03:46 | +15 | BNB | DOWN | 0.65 | open |  |
| 10-17 03:46 | +10 | BNB | DOWN | 0.64 | open |  |
| 10-17 03:46 | +5 | BNB | DOWN | 0.64 | open |  |
| 10-17 03:46 | +10 stop | BTC | DOWN | 0.64 | open |  |
| 10-17 03:46 | +20 | BTC | DOWN | 0.64 | open |  |
| 10-17 03:46 | +15 | BTC | DOWN | 0.64 | open |  |
| 10-17 03:46 | +10 | BTC | DOWN | 0.64 | open |  |
| 10-17 03:46 | +5 | BTC | DOWN | 0.64 | open |  |
| 10-17 03:46 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-17 03:46 | +20 | SOL | DOWN | 0.67 | open |  |
| 10-17 03:46 | +15 | SOL | DOWN | 0.67 | open |  |
| 10-17 03:46 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-17 03:46 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 10-17 03:46 | +10 stop | ETH | DOWN | 0.70 | open |  |
| 10-17 03:46 | +20 | ETH | DOWN | 0.70 | open |  |
| 10-17 03:46 | +15 | ETH | DOWN | 0.70 | open |  |
| 10-17 03:46 | +10 | ETH | DOWN | 0.70 | open |  |
| 10-17 03:46 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 10-17 03:46 | +10 stop | ZEC | DOWN | 0.66 | 0.47 | -2.24 |
| 10-17 03:46 | +20 | ZEC | DOWN | 0.66 | open |  |
| 10-17 03:46 | +15 | ZEC | DOWN | 0.64 | open |  |
| 10-17 03:46 | +10 | ZEC | DOWN | 0.64 | open |  |
| 10-17 03:46 | +5 | ZEC | DOWN | 0.64 | open |  |
| 10-17 03:46 | +10 stop | HYPE | DOWN | 0.56 | open |  |
| 10-17 03:46 | +20 | HYPE | DOWN | 0.56 | open |  |
| 10-17 03:46 | +15 | HYPE | DOWN | 0.56 | open |  |
| 10-17 03:46 | +10 | HYPE | DOWN | 0.56 | open |  |
| 10-17 03:46 | +5 | HYPE | DOWN | 0.56 | open |  |
| 10-17 03:41 | +10 stop | BTC | UP | 0.69 | 0.79 | 0.73 |
| 10-17 03:40 | +10 stop | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-17 03:40 | +10 stop | HYPE | UP | 0.68 | 0.52 | -1.94 |
| 10-17 03:39 | +10 stop | ETH | UP | 0.60 | 0.83 | 2.03 |
| 10-17 03:38 | +5 | ETH | DOWN | 0.68 | yes | -6.96 |
| 10-17 03:38 | +10 stop | ETH | DOWN | 0.64 | 0.49 | -1.85 |
| 10-17 03:37 | +20 | SOL | UP | 0.60 | 0.80 | 1.71 |
| 10-17 03:37 | +15 | SOL | UP | 0.60 | 0.76 | 1.30 |
| 10-17 03:37 | +5 | SOL | UP | 0.60 | 0.69 | 0.58 |
