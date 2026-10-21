# Range-Scalp Bot

*Updated Wed Oct 21 19:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27640 | 24070 | 3570 (39) | 4 | $-8043.12 | -4.6% |
| **+10¢** | 20779 | 16660 | 4119 (55) | 4 | $-7065.39 | -5.4% |
| **+15¢** | 17402 | 12968 | 4434 (78) | 4 | $-6315.10 | -5.8% |
| **+20¢** | 15405 | 10758 | 4647 (98) | 4 | $-5660.51 | -5.9% |
| **+10¢ (15¢ stop)** | 33904 | 33845 | 59 (32) | 4 | $-12601.46 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 19:39 | +10 stop | DOGE | DOWN | 0.68 | open |  |
| 10-21 19:39 | +10 stop | ZEC | UP | 0.54 | open |  |
| 10-21 19:38 | +10 stop | ETH | DOWN | 0.57 | open |  |
| 10-21 19:38 | +5 | NEAR | UP | 0.70 | open |  |
| 10-21 19:34 | +5 | DOGE | UP | 0.61 | open |  |
| 10-21 19:34 | +10 stop | NEAR | UP | 0.65 | open |  |
| 10-21 19:34 | +15 | NEAR | UP | 0.65 | open |  |
| 10-21 19:34 | +10 | NEAR | UP | 0.65 | open |  |
| 10-21 19:34 | +5 | NEAR | UP | 0.65 | 0.70 | 0.19 |
| 10-21 19:34 | +10 stop | HYPE | UP | 0.67 | 0.84 | 1.40 |
| 10-21 19:34 | +20 | HYPE | UP | 0.67 | 0.88 | 1.82 |
| 10-21 19:34 | +15 | HYPE | UP | 0.67 | 0.84 | 1.40 |
| 10-21 19:34 | +10 | HYPE | UP | 0.67 | 0.84 | 1.40 |
| 10-21 19:34 | +5 | HYPE | UP | 0.67 | 0.84 | 1.40 |
| 10-21 19:34 | +10 stop | DOGE | UP | 0.60 | 0.43 | -2.05 |
| 10-21 19:34 | +20 | DOGE | UP | 0.60 | open |  |
| 10-21 19:34 | +15 | DOGE | UP | 0.60 | open |  |
| 10-21 19:34 | +10 | DOGE | UP | 0.60 | open |  |
| 10-21 19:34 | +5 | DOGE | UP | 0.60 | 0.65 | 0.17 |
| 10-21 19:34 | +10 stop | ZEC | UP | 0.57 | 0.41 | -1.95 |
| 10-21 19:34 | +10 | ZEC | UP | 0.57 | open |  |
| 10-21 19:34 | +5 | ZEC | UP | 0.57 | open |  |
| 10-21 19:34 | +10 stop | ETH | UP | 0.56 | 0.41 | -1.85 |
| 10-21 19:34 | +10 | ETH | UP | 0.56 | open |  |
| 10-21 19:33 | +5 | ETH | UP | 0.71 | open |  |
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
