# Range-Scalp Bot

*Updated Sun Oct 25 03:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32508 | 28344 | 4164 (42) | 5 | $-9269.37 | -4.5% |
| **+10¢** | 24330 | 19508 | 4822 (60) | 5 | $-8308.32 | -5.4% |
| **+15¢** | 20369 | 15181 | 5188 (83) | 7 | $-7463.79 | -5.8% |
| **+20¢** | 18043 | 12615 | 5428 (105) | 7 | $-6602.03 | -5.8% |
| **+10¢ (15¢ stop)** | 39937 | 39877 | 60 (32) | 3 | $-15270.95 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 03:34 | +5 | HYPE | DOWN | 0.61 | open |  |
| 10-25 03:33 | +5 | BTC | DOWN | 0.68 | open |  |
| 10-25 03:32 | +10 stop | XRP | DOWN | 0.65 | open |  |
| 10-25 03:32 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-25 03:32 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-25 03:32 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-25 03:32 | +10 stop | BNB | DOWN | 0.61 | 0.74 | 0.99 |
| 10-25 03:32 | +20 | BNB | DOWN | 0.61 | open |  |
| 10-25 03:32 | +15 | BNB | DOWN | 0.62 | open |  |
| 10-25 03:32 | +10 | BNB | DOWN | 0.61 | 0.74 | 0.95 |
| 10-25 03:32 | +5 | BNB | DOWN | 0.61 | 0.74 | 0.95 |
| 10-25 03:32 | +10 stop | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-25 03:32 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 10-25 03:32 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-25 03:32 | +20 | SOL | DOWN | 0.64 | open |  |
| 10-25 03:32 | +15 | SOL | DOWN | 0.65 | open |  |
| 10-25 03:32 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-25 03:32 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.29 |
| 10-25 03:32 | +10 stop | HYPE | DOWN | 0.59 | open |  |
| 10-25 03:32 | +20 | HYPE | DOWN | 0.59 | open |  |
| 10-25 03:32 | +15 | HYPE | DOWN | 0.59 | open |  |
| 10-25 03:32 | +10 | HYPE | DOWN | 0.59 | open |  |
| 10-25 03:32 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.27 |
| 10-25 03:31 | +10 stop | BTC | DOWN | 0.60 | open |  |
| 10-25 03:31 | +20 | BTC | DOWN | 0.60 | open |  |
| 10-25 03:31 | +15 | BTC | DOWN | 0.60 | open |  |
| 10-25 03:31 | +10 | BTC | DOWN | 0.60 | open |  |
| 10-25 03:31 | +5 | BTC | DOWN | 0.60 | 0.65 | 0.17 |
| 10-25 03:31 | +10 stop | XRP | UP | 0.62 | 0.40 | -2.57 |
| 10-25 03:31 | +20 | XRP | UP | 0.63 | open |  |
| 10-25 03:31 | +15 | XRP | UP | 0.63 | open |  |
| 10-25 03:31 | +10 | XRP | UP | 0.63 | open |  |
| 10-25 03:31 | +5 | XRP | UP | 0.63 | open |  |
| 10-25 03:30 | +10 stop | ZEC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-25 03:30 | +20 | ZEC | DOWN | 0.59 | 0.79 | 1.71 |
| 10-25 03:30 | +15 | ZEC | DOWN | 0.59 | 0.74 | 1.19 |
| 10-25 03:30 | +10 | ZEC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-25 03:30 | +5 | ZEC | DOWN | 0.59 | 0.64 | 0.16 |
| 10-25 03:30 | +10 stop | DOGE | UP | 0.60 | 0.39 | -2.44 |
| 10-25 03:30 | +20 | DOGE | UP | 0.60 | open |  |
