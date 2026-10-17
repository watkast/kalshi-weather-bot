# Range-Scalp Bot

*Updated Sat Oct 17 22:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21644 | 18871 | 2773 (29) | 3 | $-6098.58 | -4.5% |
| **+10¢** | 16277 | 13068 | 3209 (41) | 4 | $-5425.79 | -5.3% |
| **+15¢** | 13609 | 10144 | 3465 (61) | 4 | $-4938.82 | -5.8% |
| **+20¢** | 12052 | 8420 | 3632 (80) | 4 | $-4394.94 | -5.8% |
| **+10¢ (15¢ stop)** | 26565 | 26515 | 50 (29) | 3 | $-10101.47 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 22:06 | +5 | NEAR | DOWN | 0.60 | open |  |
| 10-17 22:06 | +10 stop | ZEC | DOWN | 0.60 | open |  |
| 10-17 22:06 | +10 | ZEC | DOWN | 0.60 | open |  |
| 10-17 22:06 | +5 | ZEC | DOWN | 0.60 | open |  |
| 10-17 22:06 | +20 | XRP | UP | 0.67 | open |  |
| 10-17 22:06 | +15 | XRP | UP | 0.68 | open |  |
| 10-17 22:05 | +5 | NEAR | DOWN | 0.56 | 0.64 | 0.45 |
| 10-17 22:05 | +10 | XRP | UP | 0.71 | open |  |
| 10-17 22:05 | +5 | XRP | UP | 0.71 | open |  |
| 10-17 22:05 | +10 stop | XRP | UP | 0.71 | open |  |
| 10-17 22:05 | +10 stop | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 10-17 22:05 | +10 stop | NEAR | DOWN | 0.60 | open |  |
| 10-17 22:05 | +20 | NEAR | DOWN | 0.60 | open |  |
| 10-17 22:05 | +15 | NEAR | DOWN | 0.60 | open |  |
| 10-17 22:05 | +10 | NEAR | DOWN | 0.60 | open |  |
| 10-17 22:05 | +5 | NEAR | DOWN | 0.60 | 0.67 | 0.38 |
| 10-17 22:05 | +5 | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-17 22:04 | +10 stop | ZEC | UP | 0.51 | 0.62 | 0.75 |
| 10-17 22:04 | +20 | ZEC | UP | 0.51 | open |  |
| 10-17 22:04 | +15 | ZEC | UP | 0.50 | open |  |
| 10-17 22:04 | +10 | ZEC | UP | 0.50 | 0.62 | 0.85 |
| 10-17 22:04 | +5 | ZEC | UP | 0.51 | 0.62 | 0.75 |
| 10-17 22:04 | +10 stop | HYPE | UP | 0.53 | 0.37 | -1.95 |
| 10-17 22:04 | +10 | HYPE | UP | 0.53 | open |  |
| 10-17 22:04 | +5 | HYPE | UP | 0.53 | 0.58 | 0.14 |
| 10-17 22:02 | +10 stop | HYPE | UP | 0.63 | 0.73 | 0.69 |
| 10-17 22:02 | +20 | HYPE | UP | 0.62 | open |  |
| 10-17 22:02 | +15 | HYPE | UP | 0.62 | open |  |
| 10-17 22:02 | +10 | HYPE | UP | 0.62 | 0.73 | 0.75 |
| 10-17 22:02 | +5 | HYPE | UP | 0.62 | 0.69 | 0.34 |
| 10-17 21:57 | +10 stop | NEAR | UP | 0.57 | 0.74 | 1.38 |
| 10-17 21:57 | +10 | NEAR | UP | 0.57 | 0.74 | 1.38 |
| 10-17 21:57 | +5 | NEAR | UP | 0.57 | 0.64 | 0.35 |
| 10-17 21:56 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-17 21:56 | +10 stop | NEAR | UP | 0.52 | 0.66 | 1.11 |
| 10-17 21:56 | +20 | NEAR | UP | 0.51 | 0.74 | 1.96 |
| 10-17 21:56 | +15 | NEAR | UP | 0.51 | 0.74 | 1.96 |
| 10-17 21:56 | +10 | NEAR | UP | 0.52 | 0.66 | 1.11 |
| 10-17 21:56 | +5 | NEAR | UP | 0.52 | 0.66 | 1.11 |
| 10-17 21:56 | +10 stop | SOL | DOWN | 0.69 | 0.38 | -3.42 |
