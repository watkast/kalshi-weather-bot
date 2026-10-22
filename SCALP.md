# Range-Scalp Bot

*Updated Thu Oct 22 19:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29151 | 25392 | 3759 (39) | 5 | $-8463.41 | -4.6% |
| **+10¢** | 21864 | 17512 | 4352 (55) | 5 | $-7584.99 | -5.5% |
| **+15¢** | 18303 | 13626 | 4677 (78) | 5 | $-6779.04 | -5.9% |
| **+20¢** | 16201 | 11298 | 4903 (100) | 5 | $-6110.94 | -6.0% |
| **+10¢ (15¢ stop)** | 35765 | 35706 | 59 (32) | 5 | $-13469.19 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 19:01 | +10 stop | ETH | UP | 0.60 | open |  |
| 10-22 19:01 | +20 | ETH | UP | 0.60 | open |  |
| 10-22 19:01 | +15 | ETH | UP | 0.60 | open |  |
| 10-22 19:01 | +10 | ETH | UP | 0.60 | open |  |
| 10-22 19:01 | +5 | ETH | UP | 0.60 | open |  |
| 10-22 19:01 | +10 stop | BTC | UP | 0.63 | open |  |
| 10-22 19:01 | +20 | BTC | UP | 0.62 | open |  |
| 10-22 19:01 | +15 | BTC | UP | 0.61 | open |  |
| 10-22 19:01 | +10 | BTC | UP | 0.61 | open |  |
| 10-22 19:01 | +5 | BTC | UP | 0.61 | open |  |
| 10-22 19:01 | +10 stop | XRP | UP | 0.58 | open |  |
| 10-22 19:01 | +20 | XRP | UP | 0.58 | open |  |
| 10-22 19:01 | +15 | XRP | UP | 0.58 | open |  |
| 10-22 19:01 | +10 | XRP | UP | 0.58 | open |  |
| 10-22 19:01 | +5 | XRP | UP | 0.58 | open |  |
| 10-22 19:01 | +10 stop | NEAR | UP | 0.55 | open |  |
| 10-22 19:01 | +20 | NEAR | UP | 0.55 | open |  |
| 10-22 19:01 | +15 | NEAR | UP | 0.56 | open |  |
| 10-22 19:01 | +10 | NEAR | UP | 0.58 | open |  |
| 10-22 19:01 | +5 | NEAR | UP | 0.58 | open |  |
| 10-22 19:01 | +10 stop | DOGE | UP | 0.58 | open |  |
| 10-22 19:01 | +20 | DOGE | UP | 0.58 | open |  |
| 10-22 19:01 | +15 | DOGE | UP | 0.58 | open |  |
| 10-22 19:01 | +10 | DOGE | UP | 0.58 | open |  |
| 10-22 19:01 | +5 | DOGE | UP | 0.58 | open |  |
| 10-22 18:55 | +10 stop | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 10-22 18:55 | +5 | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 10-22 18:55 | +10 stop | DOGE | UP | 0.66 | 0.77 | 0.81 |
| 10-22 18:53 | +15 | DOGE | UP | 0.71 | 0.89 | 1.58 |
| 10-22 18:53 | +10 | SOL | UP | 0.56 | no | -5.78 |
| 10-22 18:53 | +5 | SOL | UP | 0.56 | 0.65 | 0.56 |
| 10-22 18:51 | +10 stop | DOGE | UP | 0.70 | 0.52 | -2.13 |
| 10-22 18:50 | +10 stop | SOL | UP | 0.70 | 0.49 | -2.43 |
| 10-22 18:50 | +5 | SOL | UP | 0.70 | 0.77 | 0.42 |
| 10-22 18:49 | +5 | DOGE | DOWN | 0.64 | yes | -6.57 |
| 10-22 18:49 | +10 stop | XRP | DOWN | 0.58 | 0.40 | -2.15 |
| 10-22 18:49 | +5 | SOL | UP | 0.50 | 0.55 | 0.14 |
| 10-22 18:48 | +10 stop | DOGE | DOWN | 0.57 | 0.37 | -2.35 |
| 10-22 18:48 | +10 | DOGE | DOWN | 0.57 | yes | -5.88 |
| 10-22 18:48 | +5 | DOGE | DOWN | 0.57 | 0.64 | 0.35 |
