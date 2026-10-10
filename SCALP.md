# Range-Scalp Bot

*Updated Sat Oct 10 23:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11081 | 9554 | 1527 (22) | 4 | $-3761.82 | -5.4% |
| **+10¢** | 8393 | 6614 | 1779 (36) | 5 | $-3599.69 | -6.8% |
| **+15¢** | 7072 | 5190 | 1882 (52) | 7 | $-3048.00 | -6.9% |
| **+20¢** | 6294 | 4336 | 1958 (66) | 7 | $-2569.14 | -6.5% |
| **+10¢ (15¢ stop)** | 13661 | 13620 | 41 (25) | 1 | $-5483.60 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 23:40 | +10 stop | ETH | DOWN | 0.62 | open |  |
| 10-10 23:40 | +10 stop | XRP | UP | 0.53 | 0.65 | 0.86 |
| 10-10 23:40 | +20 | XRP | UP | 0.51 | open |  |
| 10-10 23:40 | +15 | XRP | UP | 0.51 | open |  |
| 10-10 23:40 | +10 | XRP | UP | 0.51 | 0.65 | 1.06 |
| 10-10 23:40 | +5 | XRP | UP | 0.51 | 0.65 | 1.06 |
| 10-10 23:40 | +10 stop | DOGE | UP | 0.47 | 0.67 | 1.66 |
| 10-10 23:40 | +20 | DOGE | UP | 0.47 | 0.67 | 1.66 |
| 10-10 23:40 | +15 | DOGE | UP | 0.47 | 0.67 | 1.66 |
| 10-10 23:40 | +10 | DOGE | UP | 0.47 | 0.67 | 1.66 |
| 10-10 23:40 | +5 | DOGE | UP | 0.37 | 0.67 | 2.67 |
| 10-10 23:39 | +10 stop | ETH | UP | 0.60 | 0.36 | -2.74 |
| 10-10 23:39 | +20 | ETH | UP | 0.60 | open |  |
| 10-10 23:39 | +10 | ETH | UP | 0.60 | open |  |
| 10-10 23:39 | +5 | ETH | UP | 0.60 | open |  |
| 10-10 23:38 | +10 stop | BNB | UP | 0.54 | 0.34 | -2.34 |
| 10-10 23:38 | +15 | BNB | UP | 0.54 | open |  |
| 10-10 23:38 | +10 | BNB | UP | 0.60 | open |  |
| 10-10 23:38 | +5 | BNB | UP | 0.60 | open |  |
| 10-10 23:37 | +10 stop | SOL | UP | 0.54 | 0.32 | -2.54 |
| 10-10 23:36 | +10 stop | ZEC | DOWN | 0.51 | 0.32 | -2.24 |
| 10-10 23:35 | +10 stop | SOL | UP | 0.57 | 0.68 | 0.76 |
| 10-10 23:35 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-10 23:35 | +15 | ETH | UP | 0.66 | open |  |
| 10-10 23:35 | +10 | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-10 23:35 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 10-10 23:35 | +10 stop | ZEC | UP | 0.56 | 0.66 | 0.66 |
| 10-10 23:33 | +10 stop | ZEC | DOWN | 0.65 | 0.44 | -2.44 |
| 10-10 23:33 | +10 | ZEC | DOWN | 0.65 | open |  |
| 10-10 23:33 | +5 | ZEC | DOWN | 0.65 | open |  |
| 10-10 23:32 | +10 stop | HYPE | DOWN | 0.56 | 0.38 | -2.19 |
| 10-10 23:32 | +20 | HYPE | DOWN | 0.56 | open |  |
| 10-10 23:32 | +15 | HYPE | DOWN | 0.56 | open |  |
| 10-10 23:32 | +10 | HYPE | DOWN | 0.56 | open |  |
| 10-10 23:32 | +5 | HYPE | DOWN | 0.57 | open |  |
| 10-10 23:31 | +10 stop | SOL | UP | 0.62 | 0.75 | 0.99 |
| 10-10 23:31 | +5 | DOGE | UP | 0.57 | 0.68 | 0.71 |
| 10-10 23:31 | +10 stop | ETH | UP | 0.62 | 0.74 | 0.89 |
| 10-10 23:31 | +10 | ETH | UP | 0.62 | 0.74 | 0.89 |
| 10-10 23:31 | +5 | ETH | UP | 0.62 | 0.74 | 0.89 |
