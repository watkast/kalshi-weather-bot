# Range-Scalp Bot

*Updated Sat Oct 31 16:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42463 | 37042 | 5421 (59) | 5 | $-11918.45 | -4.5% |
| **+10¢** | 31661 | 25385 | 6276 (81) | 4 | $-10709.04 | -5.4% |
| **+15¢** | 26481 | 19714 | 6767 (109) | 5 | $-9797.29 | -5.9% |
| **+20¢** | 23519 | 16425 | 7094 (141) | 6 | $-8674.69 | -5.9% |
| **+10¢ (15¢ stop)** | 51793 | 51714 | 79 (44) | 0 | $-19596.03 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 16:28 | +5 | BTC | UP | 0.56 | 0.64 | 0.45 |
| 10-31 16:28 | +10 stop | BTC | UP | 0.58 | 0.17 | -4.38 |
| 10-31 16:28 | +10 | BTC | UP | 0.58 | 0.71 | 0.97 |
| 10-31 16:27 | +10 stop | SOL | DOWN | 0.50 | 0.68 | 1.46 |
| 10-31 16:27 | +20 | SOL | DOWN | 0.49 | open |  |
| 10-31 16:27 | +15 | SOL | DOWN | 0.49 | 0.68 | 1.56 |
| 10-31 16:27 | +10 | SOL | DOWN | 0.49 | 0.68 | 1.56 |
| 10-31 16:26 | +10 stop | BTC | UP | 0.58 | 0.23 | -3.81 |
| 10-31 16:26 | +20 | BTC | UP | 0.58 | open |  |
| 10-31 16:26 | +15 | BTC | UP | 0.58 | open |  |
| 10-31 16:26 | +5 | BTC | UP | 0.58 | 0.63 | 0.15 |
| 10-31 16:24 | +10 stop | ZEC | UP | 0.58 | 0.42 | -1.96 |
| 10-31 16:23 | +10 stop | ZEC | DOWN | 0.63 | 0.40 | -2.64 |
| 10-31 16:23 | +20 | ZEC | DOWN | 0.63 | 0.91 | 2.57 |
| 10-31 16:23 | +15 | ZEC | DOWN | 0.65 | 0.81 | 1.33 |
| 10-31 16:23 | +10 | ZEC | DOWN | 0.65 | 0.81 | 1.33 |
| 10-31 16:23 | +5 | ZEC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-31 16:23 | +10 stop | XRP | DOWN | 0.68 | 0.25 | -4.60 |
| 10-31 16:23 | +10 stop | SOL | UP | 0.64 | 0.83 | 1.63 |
| 10-31 16:22 | +10 stop | NEAR | UP | 0.56 | 0.66 | 0.66 |
| 10-31 16:21 | +10 stop | DOGE | UP | 0.51 | 0.87 | 3.34 |
| 10-31 16:21 | +20 | BTC | UP | 0.61 | 0.94 | 3.09 |
| 10-31 16:21 | +10 stop | NEAR | DOWN | 0.67 | 0.44 | -2.64 |
| 10-31 16:21 | +20 | NEAR | DOWN | 0.67 | open |  |
| 10-31 16:21 | +15 | NEAR | DOWN | 0.67 | open |  |
| 10-31 16:21 | +10 | NEAR | DOWN | 0.67 | open |  |
| 10-31 16:21 | +5 | NEAR | DOWN | 0.68 | open |  |
| 10-31 16:21 | +10 stop | BTC | UP | 0.62 | 0.72 | 0.68 |
| 10-31 16:21 | +15 | BTC | UP | 0.62 | 0.94 | 2.99 |
| 10-31 16:21 | +5 | BTC | UP | 0.62 | 0.72 | 0.68 |
| 10-31 16:20 | +10 stop | ETH | UP | 0.58 | 0.70 | 0.87 |
| 10-31 16:20 | +10 stop | HYPE | UP | 0.69 | 0.80 | 0.83 |
| 10-31 16:19 | +10 stop | SOL | DOWN | 0.54 | 0.39 | -1.89 |
| 10-31 16:19 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-31 16:18 | +5 | BTC | DOWN | 0.49 | 0.63 | 1.05 |
| 10-31 16:18 | +10 stop | HYPE | DOWN | 0.57 | 0.42 | -1.86 |
| 10-31 16:17 | +10 stop | SOL | DOWN | 0.67 | 0.52 | -1.84 |
| 10-31 16:17 | +10 stop | DOGE | DOWN | 0.62 | 0.33 | -3.23 |
| 10-31 16:17 | +20 | DOGE | DOWN | 0.62 | open |  |
| 10-31 16:17 | +15 | DOGE | DOWN | 0.62 | open |  |
