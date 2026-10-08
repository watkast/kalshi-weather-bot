# Range-Scalp Bot

*Updated Thu Oct 08 22:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8112 | 7018 | 1094 (13) | 9 | $-2639.28 | -5.2% |
| **+10¢** | 6142 | 4848 | 1294 (25) | 8 | $-2604.62 | -6.7% |
| **+15¢** | 5170 | 3809 | 1361 (37) | 9 | $-2119.88 | -6.5% |
| **+20¢** | 4616 | 3205 | 1411 (45) | 9 | $-1697.76 | -5.9% |
| **+10¢ (15¢ stop)** | 9853 | 9823 | 30 (19) | 4 | $-3632.86 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 22:49 | +10 stop | ETH | DOWN | 0.57 | open |  |
| 10-08 22:49 | +5 | XRP | DOWN | 0.56 | open |  |
| 10-08 22:49 | +10 stop | DOGE | UP | 0.51 | 0.63 | 0.85 |
| 10-08 22:48 | +10 stop | NEAR | UP | 0.68 | open |  |
| 10-08 22:48 | +10 stop | XRP | UP | 0.51 | open |  |
| 10-08 22:48 | +20 | XRP | UP | 0.50 | open |  |
| 10-08 22:48 | +15 | XRP | UP | 0.50 | open |  |
| 10-08 22:48 | +10 | XRP | UP | 0.50 | 0.60 | 0.65 |
| 10-08 22:48 | +5 | XRP | UP | 0.50 | 0.55 | 0.14 |
| 10-08 22:48 | +10 stop | SOL | DOWN | 0.57 | 0.78 | 1.79 |
| 10-08 22:48 | +5 | BNB | UP | 0.68 | open |  |
| 10-08 22:47 | +10 stop | ZEC | DOWN | 0.60 | 0.44 | -1.95 |
| 10-08 22:47 | +20 | ZEC | DOWN | 0.60 | open |  |
| 10-08 22:47 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-08 22:47 | +10 | ZEC | DOWN | 0.60 | open |  |
| 10-08 22:47 | +5 | ZEC | DOWN | 0.60 | open |  |
| 10-08 22:46 | +10 stop | BNB | UP | 0.68 | open |  |
| 10-08 22:46 | +20 | BNB | UP | 0.68 | open |  |
| 10-08 22:46 | +15 | BNB | UP | 0.68 | open |  |
| 10-08 22:46 | +10 | BNB | UP | 0.68 | open |  |
| 10-08 22:46 | +5 | BNB | UP | 0.68 | 0.73 | 0.20 |
| 10-08 22:46 | +10 stop | NEAR | UP | 0.71 | 0.56 | -1.83 |
| 10-08 22:46 | +20 | NEAR | UP | 0.71 | open |  |
| 10-08 22:46 | +15 | NEAR | UP | 0.71 | open |  |
| 10-08 22:46 | +10 | NEAR | UP | 0.71 | open |  |
| 10-08 22:46 | +5 | NEAR | UP | 0.71 | open |  |
| 10-08 22:46 | +10 stop | SOL | UP | 0.62 | 0.40 | -2.52 |
| 10-08 22:46 | +20 | SOL | UP | 0.62 | open |  |
| 10-08 22:46 | +15 | SOL | UP | 0.62 | open |  |
| 10-08 22:46 | +10 | SOL | UP | 0.62 | open |  |
| 10-08 22:46 | +5 | SOL | UP | 0.62 | open |  |
| 10-08 22:46 | +10 stop | ETH | UP | 0.62 | 0.43 | -2.25 |
| 10-08 22:46 | +20 | ETH | UP | 0.62 | open |  |
| 10-08 22:46 | +15 | ETH | UP | 0.62 | open |  |
| 10-08 22:46 | +10 | ETH | UP | 0.62 | open |  |
| 10-08 22:46 | +5 | ETH | UP | 0.63 | open |  |
| 10-08 22:46 | +10 stop | BTC | UP | 0.62 | 0.43 | -2.25 |
| 10-08 22:46 | +20 | BTC | UP | 0.62 | open |  |
| 10-08 22:46 | +15 | BTC | UP | 0.62 | open |  |
| 10-08 22:46 | +10 | BTC | UP | 0.62 | open |  |
