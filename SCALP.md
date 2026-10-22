# Range-Scalp Bot

*Updated Thu Oct 22 20:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29246 | 25461 | 3785 (39) | 3 | $-8591.65 | -4.7% |
| **+10¢** | 21935 | 17555 | 4380 (55) | 4 | $-7717.07 | -5.6% |
| **+15¢** | 18365 | 13660 | 4705 (78) | 4 | $-6902.83 | -6.0% |
| **+20¢** | 16256 | 11323 | 4933 (100) | 4 | $-6242.31 | -6.1% |
| **+10¢ (15¢ stop)** | 35894 | 35835 | 59 (32) | 0 | $-13529.67 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 20:35 | +10 stop | ZEC | DOWN | 0.68 | 0.81 | 1.07 |
| 10-22 20:35 | +5 | ZEC | DOWN | 0.68 | 0.76 | 0.55 |
| 10-22 20:33 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-22 20:33 | +5 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-22 20:33 | +10 stop | HYPE | DOWN | 0.68 | 0.79 | 0.82 |
| 10-22 20:33 | +10 stop | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-22 20:32 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-22 20:32 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.93 |
| 10-22 20:32 | +15 | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 10-22 20:32 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-22 20:32 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 10-22 20:32 | +10 stop | NEAR | DOWN | 0.56 | 0.71 | 1.17 |
| 10-22 20:32 | +20 | NEAR | DOWN | 0.56 | 0.77 | 1.79 |
| 10-22 20:32 | +15 | NEAR | DOWN | 0.57 | 0.77 | 1.69 |
| 10-22 20:32 | +10 | NEAR | DOWN | 0.56 | 0.71 | 1.17 |
| 10-22 20:32 | +5 | NEAR | DOWN | 0.56 | 0.71 | 1.17 |
| 10-22 20:32 | +10 stop | HYPE | UP | 0.62 | 0.41 | -2.44 |
| 10-22 20:32 | +20 | HYPE | UP | 0.62 | open |  |
| 10-22 20:32 | +15 | HYPE | UP | 0.62 | open |  |
| 10-22 20:32 | +10 | HYPE | UP | 0.64 | open |  |
| 10-22 20:32 | +5 | HYPE | UP | 0.64 | open |  |
| 10-22 20:31 | +10 stop | BTC | DOWN | 0.55 | 0.69 | 1.07 |
| 10-22 20:31 | +20 | BTC | DOWN | 0.55 | 0.77 | 1.89 |
| 10-22 20:31 | +15 | BTC | DOWN | 0.55 | 0.77 | 1.89 |
| 10-22 20:31 | +10 | BTC | DOWN | 0.55 | 0.69 | 1.07 |
| 10-22 20:31 | +5 | BTC | DOWN | 0.55 | 0.69 | 1.07 |
| 10-22 20:31 | +10 stop | SOL | UP | 0.59 | 0.41 | -2.14 |
| 10-22 20:31 | +20 | SOL | UP | 0.59 | open |  |
| 10-22 20:31 | +15 | SOL | UP | 0.59 | open |  |
| 10-22 20:31 | +10 | SOL | UP | 0.59 | open |  |
| 10-22 20:31 | +5 | SOL | UP | 0.59 | open |  |
| 10-22 20:31 | +10 stop | DOGE | UP | 0.58 | 0.39 | -2.25 |
| 10-22 20:31 | +20 | DOGE | UP | 0.58 | open |  |
| 10-22 20:31 | +15 | DOGE | UP | 0.58 | open |  |
| 10-22 20:31 | +10 | DOGE | UP | 0.58 | open |  |
| 10-22 20:31 | +5 | DOGE | UP | 0.58 | open |  |
| 10-22 20:30 | +10 stop | ETH | DOWN | 0.57 | 0.73 | 1.28 |
| 10-22 20:30 | +20 | ETH | DOWN | 0.57 | 0.79 | 1.90 |
| 10-22 20:30 | +15 | ETH | DOWN | 0.57 | 0.73 | 1.28 |
| 10-22 20:30 | +10 | ETH | DOWN | 0.57 | 0.73 | 1.28 |
