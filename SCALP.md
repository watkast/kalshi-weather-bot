# Range-Scalp Bot

*Updated Fri Oct 23 04:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29765 | 25910 | 3855 (39) | 4 | $-8781.32 | -4.7% |
| **+10¢** | 22309 | 17847 | 4462 (55) | 4 | $-7904.98 | -5.6% |
| **+15¢** | 18687 | 13897 | 4790 (78) | 4 | $-7062.14 | -6.0% |
| **+20¢** | 16537 | 11517 | 5020 (101) | 7 | $-6383.60 | -6.1% |
| **+10¢ (15¢ stop)** | 36532 | 36473 | 59 (32) | 2 | $-13794.15 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 04:35 | +5 | NEAR | UP | 0.65 | open |  |
| 10-23 04:35 | +10 stop | NEAR | UP | 0.65 | open |  |
| 10-23 04:35 | +10 stop | ZEC | DOWN | 0.64 | open |  |
| 10-23 04:34 | +10 stop | DOGE | UP | 0.63 | 0.76 | 1.00 |
| 10-23 04:34 | +20 | DOGE | UP | 0.63 | open |  |
| 10-23 04:34 | +15 | DOGE | UP | 0.63 | 0.78 | 1.20 |
| 10-23 04:34 | +10 | DOGE | UP | 0.63 | 0.76 | 1.00 |
| 10-23 04:34 | +5 | DOGE | UP | 0.63 | 0.68 | 0.17 |
| 10-23 04:34 | +10 stop | ETH | DOWN | 0.70 | 0.53 | -2.03 |
| 10-23 04:34 | +10 stop | BTC | DOWN | 0.61 | 0.46 | -1.85 |
| 10-23 04:34 | +10 stop | SOL | UP | 0.61 | 0.71 | 0.68 |
| 10-23 04:34 | +20 | SOL | UP | 0.61 | open |  |
| 10-23 04:34 | +15 | SOL | UP | 0.61 | 0.76 | 1.20 |
| 10-23 04:34 | +10 | SOL | UP | 0.61 | 0.71 | 0.68 |
| 10-23 04:34 | +5 | SOL | UP | 0.61 | 0.71 | 0.68 |
| 10-23 04:34 | +5 | NEAR | UP | 0.52 | 0.57 | 0.14 |
| 10-23 04:33 | +10 stop | XRP | UP | 0.52 | 0.68 | 1.26 |
| 10-23 04:33 | +20 | XRP | UP | 0.52 | open |  |
| 10-23 04:33 | +15 | XRP | UP | 0.52 | 0.68 | 1.26 |
| 10-23 04:33 | +10 | XRP | UP | 0.52 | 0.68 | 1.26 |
| 10-23 04:33 | +5 | XRP | UP | 0.53 | 0.68 | 1.16 |
| 10-23 04:33 | +10 stop | ZEC | UP | 0.53 | 0.35 | -2.14 |
| 10-23 04:33 | +10 stop | ETH | UP | 0.64 | 0.45 | -2.25 |
| 10-23 04:33 | +20 | ETH | UP | 0.64 | open |  |
| 10-23 04:33 | +15 | ETH | UP | 0.64 | open |  |
| 10-23 04:33 | +10 | ETH | UP | 0.64 | open |  |
| 10-23 04:33 | +5 | ETH | UP | 0.63 | open |  |
| 10-23 04:32 | +10 stop | NEAR | UP | 0.71 | 0.54 | -2.03 |
| 10-23 04:32 | +20 | NEAR | UP | 0.71 | open |  |
| 10-23 04:32 | +15 | NEAR | UP | 0.71 | open |  |
| 10-23 04:32 | +10 | NEAR | UP | 0.71 | open |  |
| 10-23 04:32 | +5 | NEAR | UP | 0.71 | 0.76 | 0.22 |
| 10-23 04:31 | +10 stop | ZEC | UP | 0.71 | 0.55 | -1.93 |
| 10-23 04:31 | +20 | ZEC | UP | 0.71 | open |  |
| 10-23 04:31 | +15 | ZEC | UP | 0.70 | open |  |
| 10-23 04:31 | +10 | ZEC | UP | 0.70 | open |  |
| 10-23 04:31 | +5 | ZEC | UP | 0.70 | open |  |
| 10-23 04:31 | +10 stop | BTC | UP | 0.69 | 0.51 | -2.13 |
| 10-23 04:31 | +20 | BTC | UP | 0.69 | open |  |
| 10-23 04:31 | +15 | BTC | UP | 0.69 | open |  |
