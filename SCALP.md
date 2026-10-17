# Range-Scalp Bot

*Updated Sat Oct 17 12:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20927 | 18209 | 2718 (29) | 3 | $-6130.70 | -4.7% |
| **+10¢** | 15750 | 12616 | 3134 (41) | 3 | $-5452.02 | -5.5% |
| **+15¢** | 13166 | 9792 | 3374 (61) | 3 | $-4937.39 | -6.0% |
| **+20¢** | 11672 | 8140 | 3532 (80) | 4 | $-4354.25 | -5.9% |
| **+10¢ (15¢ stop)** | 25713 | 25663 | 50 (29) | 1 | $-9787.83 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 12:02 | +10 stop | BNB | DOWN | 0.58 | 0.76 | 1.49 |
| 10-17 12:01 | +10 stop | ETH | UP | 0.63 | 0.41 | -2.54 |
| 10-17 12:01 | +20 | ETH | UP | 0.63 | open |  |
| 10-17 12:01 | +15 | ETH | UP | 0.63 | open |  |
| 10-17 12:01 | +10 | ETH | UP | 0.63 | open |  |
| 10-17 12:01 | +5 | ETH | UP | 0.63 | open |  |
| 10-17 12:01 | +10 stop | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-17 12:01 | +20 | HYPE | DOWN | 0.62 | open |  |
| 10-17 12:01 | +15 | HYPE | DOWN | 0.62 | 0.80 | 1.51 |
| 10-17 12:01 | +10 | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-17 12:01 | +5 | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-17 12:01 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-17 12:01 | +20 | SOL | DOWN | 0.63 | 0.83 | 1.73 |
| 10-17 12:01 | +15 | SOL | DOWN | 0.62 | 0.80 | 1.51 |
| 10-17 12:01 | +10 | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 10-17 12:01 | +5 | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 10-17 12:01 | +10 stop | BNB | UP | 0.59 | 0.40 | -2.24 |
| 10-17 12:01 | +20 | BNB | UP | 0.59 | open |  |
| 10-17 12:01 | +15 | BNB | UP | 0.59 | open |  |
| 10-17 12:01 | +10 | BNB | UP | 0.59 | open |  |
| 10-17 12:01 | +5 | BNB | UP | 0.59 | open |  |
| 10-17 12:01 | +10 stop | BTC | UP | 0.62 | open |  |
| 10-17 12:01 | +20 | BTC | UP | 0.62 | open |  |
| 10-17 12:01 | +15 | BTC | UP | 0.62 | open |  |
| 10-17 12:01 | +10 | BTC | UP | 0.62 | open |  |
| 10-17 12:01 | +5 | BTC | UP | 0.62 | open |  |
| 10-17 12:01 | +10 stop | ZEC | DOWN | 0.69 | 0.87 | 1.57 |
| 10-17 12:01 | +20 | ZEC | DOWN | 0.69 | 0.90 | 1.89 |
| 10-17 12:01 | +15 | ZEC | DOWN | 0.69 | 0.87 | 1.57 |
| 10-17 12:01 | +10 | ZEC | DOWN | 0.69 | 0.87 | 1.57 |
| 10-17 12:01 | +5 | ZEC | DOWN | 0.69 | 0.76 | 0.42 |
| 10-17 11:58 | +10 stop | BTC | DOWN | 0.67 | 0.92 | 2.19 |
| 10-17 11:58 | +5 | BTC | DOWN | 0.71 | 0.92 | 1.90 |
| 10-17 11:57 | +5 | BTC | UP | 0.38 | 0.69 | 2.78 |
| 10-17 11:57 | +10 stop | DOGE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-17 11:55 | +10 stop | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 10-17 11:55 | +5 | ZEC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-17 11:54 | +10 stop | BTC | UP | 0.62 | 0.43 | -2.25 |
| 10-17 11:54 | +20 | BTC | UP | 0.62 | no | -6.37 |
| 10-17 11:54 | +15 | BTC | UP | 0.62 | no | -6.37 |
