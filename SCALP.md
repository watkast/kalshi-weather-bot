# Range-Scalp Bot

*Updated Tue Nov 03 21:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46354 | 40360 | 5994 (72) | 3 | $-13355.36 | -4.6% |
| **+10¢** | 34603 | 27658 | 6945 (96) | 3 | $-12217.06 | -5.6% |
| **+15¢** | 28967 | 21498 | 7469 (124) | 3 | $-11163.63 | -6.1% |
| **+20¢** | 25733 | 17905 | 7828 (164) | 3 | $-9880.79 | -6.1% |
| **+10¢ (15¢ stop)** | 56544 | 56451 | 93 (56) | 0 | $-21206.64 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 21:22 | +10 stop | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-03 21:22 | +10 stop | SOL | UP | 0.71 | 0.88 | 1.47 |
| 11-03 21:22 | +10 | SOL | UP | 0.71 | 0.88 | 1.47 |
| 11-03 21:22 | +5 | SOL | UP | 0.71 | 0.76 | 0.22 |
| 11-03 21:22 | +10 stop | BTC | DOWN | 0.55 | 0.40 | -1.85 |
| 11-03 21:20 | +10 stop | BTC | DOWN | 0.60 | 0.44 | -1.95 |
| 11-03 21:20 | +10 stop | ETH | UP | 0.63 | 0.76 | 1.00 |
| 11-03 21:20 | +10 stop | SOL | UP | 0.67 | 0.79 | 0.92 |
| 11-03 21:20 | +15 | SOL | UP | 0.67 | 0.88 | 1.86 |
| 11-03 21:20 | +10 | SOL | UP | 0.67 | 0.79 | 0.92 |
| 11-03 21:20 | +5 | SOL | UP | 0.67 | 0.75 | 0.50 |
| 11-03 21:18 | +10 stop | BTC | UP | 0.61 | 0.44 | -2.05 |
| 11-03 21:17 | +10 stop | BNB | UP | 0.70 | 0.80 | 0.73 |
| 11-03 21:17 | +20 | BNB | UP | 0.70 | 0.91 | 1.86 |
| 11-03 21:17 | +15 | BNB | UP | 0.70 | 0.86 | 1.36 |
| 11-03 21:17 | +10 | BNB | UP | 0.70 | 0.80 | 0.73 |
| 11-03 21:17 | +5 | BNB | UP | 0.70 | 0.80 | 0.73 |
| 11-03 21:16 | +10 stop | ETH | UP | 0.66 | 0.78 | 0.91 |
| 11-03 21:16 | +10 stop | HYPE | UP | 0.70 | 0.83 | 1.05 |
| 11-03 21:16 | +20 | HYPE | UP | 0.70 | 0.91 | 1.90 |
| 11-03 21:16 | +15 | HYPE | UP | 0.70 | 0.85 | 1.26 |
| 11-03 21:16 | +10 | HYPE | UP | 0.70 | 0.83 | 1.05 |
| 11-03 21:16 | +5 | HYPE | UP | 0.70 | 0.78 | 0.52 |
| 11-03 21:16 | +10 stop | SOL | UP | 0.63 | 0.76 | 1.00 |
| 11-03 21:16 | +20 | SOL | UP | 0.63 | 0.88 | 2.25 |
| 11-03 21:16 | +15 | SOL | UP | 0.63 | 0.78 | 1.20 |
| 11-03 21:16 | +10 | SOL | UP | 0.63 | 0.76 | 1.00 |
| 11-03 21:16 | +5 | SOL | UP | 0.61 | 0.70 | 0.58 |
| 11-03 21:16 | +10 stop | BTC | DOWN | 0.62 | 0.46 | -1.95 |
| 11-03 21:16 | +20 | BTC | DOWN | 0.62 | open |  |
| 11-03 21:16 | +15 | BTC | DOWN | 0.62 | open |  |
| 11-03 21:16 | +10 | BTC | DOWN | 0.62 | open |  |
| 11-03 21:16 | +5 | BTC | DOWN | 0.62 | open |  |
| 11-03 21:15 | +10 stop | ZEC | DOWN | 0.59 | 0.27 | -3.51 |
| 11-03 21:15 | +20 | ZEC | DOWN | 0.59 | open |  |
| 11-03 21:15 | +15 | ZEC | DOWN | 0.59 | open |  |
| 11-03 21:15 | +10 | ZEC | DOWN | 0.59 | open |  |
| 11-03 21:15 | +5 | ZEC | DOWN | 0.59 | open |  |
| 11-03 21:15 | +10 stop | ETH | DOWN | 0.53 | 0.36 | -2.05 |
| 11-03 21:15 | +20 | ETH | DOWN | 0.53 | open |  |
