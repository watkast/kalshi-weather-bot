# Range-Scalp Bot

*Updated Wed Oct 21 19:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27637 | 24067 | 3570 (39) | 0 | $-8044.88 | -4.6% |
| **+10¢** | 20777 | 16658 | 4119 (55) | 1 | $-7067.77 | -5.4% |
| **+15¢** | 17401 | 12967 | 4434 (78) | 2 | $-6316.50 | -5.8% |
| **+20¢** | 15403 | 10756 | 4647 (98) | 4 | $-5664.22 | -5.9% |
| **+10¢ (15¢ stop)** | 33899 | 33840 | 59 (32) | 1 | $-12597.99 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 19:32 | +10 stop | ZEC | UP | 0.67 | 0.79 | 0.92 |
| 10-21 19:32 | +20 | ZEC | UP | 0.67 | open |  |
| 10-21 19:32 | +15 | ZEC | UP | 0.67 | open |  |
| 10-21 19:32 | +10 | ZEC | UP | 0.67 | 0.79 | 0.92 |
| 10-21 19:32 | +5 | ZEC | UP | 0.67 | 0.79 | 0.92 |
| 10-21 19:32 | +5 | NEAR | UP | 0.71 | 0.80 | 0.63 |
| 10-21 19:32 | +5 | DOGE | UP | 0.65 | 0.72 | 0.39 |
| 10-21 19:31 | +10 stop | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-21 19:31 | +20 | SOL | UP | 0.62 | 0.83 | 1.83 |
| 10-21 19:31 | +15 | SOL | UP | 0.62 | 0.83 | 1.83 |
| 10-21 19:31 | +10 | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-21 19:31 | +5 | SOL | UP | 0.62 | 0.67 | 0.17 |
| 10-21 19:31 | +10 stop | NEAR | UP | 0.61 | 0.73 | 0.89 |
| 10-21 19:31 | +20 | NEAR | UP | 0.61 | open |  |
| 10-21 19:31 | +15 | NEAR | UP | 0.61 | 0.80 | 1.61 |
| 10-21 19:31 | +10 | NEAR | UP | 0.61 | 0.73 | 0.89 |
| 10-21 19:31 | +5 | NEAR | UP | 0.61 | 0.68 | 0.37 |
| 10-21 19:31 | +10 stop | XRP | UP | 0.64 | 0.75 | 0.79 |
| 10-21 19:31 | +20 | XRP | UP | 0.64 | 0.88 | 2.15 |
| 10-21 19:31 | +15 | XRP | UP | 0.64 | 0.79 | 1.21 |
| 10-21 19:31 | +10 | XRP | UP | 0.64 | 0.75 | 0.79 |
| 10-21 19:31 | +5 | XRP | UP | 0.64 | 0.75 | 0.79 |
| 10-21 19:31 | +10 stop | DOGE | UP | 0.54 | 0.66 | 0.86 |
| 10-21 19:31 | +20 | DOGE | UP | 0.54 | open |  |
| 10-21 19:31 | +15 | DOGE | UP | 0.54 | 0.72 | 1.47 |
| 10-21 19:31 | +10 | DOGE | UP | 0.54 | 0.66 | 0.86 |
| 10-21 19:31 | +5 | DOGE | UP | 0.55 | 0.61 | 0.25 |
| 10-21 19:31 | +10 stop | ETH | UP | 0.59 | open |  |
| 10-21 19:31 | +20 | ETH | UP | 0.59 | open |  |
| 10-21 19:31 | +15 | ETH | UP | 0.59 | open |  |
| 10-21 19:31 | +10 | ETH | UP | 0.59 | open |  |
| 10-21 19:31 | +5 | ETH | UP | 0.59 | 0.67 | 0.47 |
| 10-21 19:24 | +10 stop | BTC | UP | 0.65 | 0.79 | 1.12 |
| 10-21 19:22 | +10 stop | XRP | DOWN | 0.61 | 0.43 | -2.14 |
| 10-21 19:22 | +5 | XRP | DOWN | 0.60 | yes | -6.17 |
| 10-21 19:22 | +5 | BNB | UP | 0.42 | 0.57 | 1.14 |
| 10-21 19:21 | +10 stop | BTC | UP | 0.70 | 0.52 | -2.13 |
| 10-21 19:21 | +10 stop | BNB | DOWN | 0.51 | 0.36 | -1.85 |
| 10-21 19:21 | +20 | BNB | DOWN | 0.51 | yes | -5.28 |
| 10-21 19:21 | +15 | BNB | DOWN | 0.51 | yes | -5.28 |
