# Range-Scalp Bot

*Updated Sat Nov 14 16:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59589 | 51994 | 7595 (107) | 6 | $-16102.54 | -4.3% |
| **+10¢** | 44511 | 35617 | 8894 (142) | 6 | $-15147.53 | -5.4% |
| **+15¢** | 37294 | 27703 | 9591 (178) | 6 | $-13791.73 | -5.9% |
| **+20¢** | 33221 | 23155 | 10066 (230) | 7 | $-12167.79 | -5.8% |
| **+10¢ (15¢ stop)** | 72507 | 72364 | 143 (82) | 4 | $-26663.31 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 16:55 | +10 stop | BNB | UP | 0.66 | open |  |
| 11-14 16:55 | +10 stop | ETH | UP | 0.59 | open |  |
| 11-14 16:54 | +5 | DOGE | DOWN | 0.65 | open |  |
| 11-14 16:54 | +10 stop | ZEC | UP | 0.70 | open |  |
| 11-14 16:54 | +5 | SOL | UP | 0.61 | open |  |
| 11-14 16:53 | +10 stop | ETH | UP | 0.69 | 0.51 | -2.13 |
| 11-14 16:53 | +5 | SOL | DOWN | 0.45 | 0.54 | 0.50 |
| 11-14 16:53 | +10 stop | BNB | UP | 0.60 | 0.44 | -1.95 |
| 11-14 16:53 | +10 stop | ZEC | DOWN | 0.61 | 0.45 | -1.95 |
| 11-14 16:53 | +10 | ZEC | DOWN | 0.60 | open |  |
| 11-14 16:53 | +5 | ZEC | DOWN | 0.59 | open |  |
| 11-14 16:53 | +10 stop | DOGE | DOWN | 0.58 | open |  |
| 11-14 16:53 | +20 | DOGE | DOWN | 0.55 | open |  |
| 11-14 16:53 | +15 | DOGE | DOWN | 0.57 | open |  |
| 11-14 16:53 | +10 | DOGE | DOWN | 0.59 | open |  |
| 11-14 16:53 | +5 | DOGE | DOWN | 0.60 | 0.66 | 0.27 |
| 11-14 16:53 | +10 stop | SOL | DOWN | 0.56 | 0.36 | -2.35 |
| 11-14 16:53 | +10 | SOL | DOWN | 0.55 | open |  |
| 11-14 16:53 | +5 | SOL | DOWN | 0.54 | 0.59 | 0.15 |
| 11-14 16:53 | +10 stop | HYPE | UP | 0.67 | 0.78 | 0.81 |
| 11-14 16:53 | +20 | HYPE | UP | 0.67 | open |  |
| 11-14 16:53 | +15 | HYPE | UP | 0.68 | 0.84 | 1.34 |
| 11-14 16:53 | +10 | HYPE | UP | 0.68 | 0.78 | 0.75 |
| 11-14 16:53 | +5 | HYPE | UP | 0.67 | 0.75 | 0.46 |
| 11-14 16:52 | +10 stop | BNB | DOWN | 0.59 | 0.34 | -2.82 |
| 11-14 16:52 | +10 stop | ETH | DOWN | 0.62 | 0.41 | -2.44 |
| 11-14 16:52 | +10 | ETH | DOWN | 0.62 | open |  |
| 11-14 16:52 | +5 | ETH | DOWN | 0.62 | open |  |
| 11-14 16:52 | +10 stop | NEAR | UP | 0.61 | 0.72 | 0.78 |
| 11-14 16:52 | +20 | NEAR | UP | 0.61 | 0.81 | 1.72 |
| 11-14 16:52 | +15 | NEAR | UP | 0.61 | 0.81 | 1.72 |
| 11-14 16:52 | +10 stop | BTC | DOWN | 0.50 | 0.63 | 0.95 |
| 11-14 16:52 | +20 | BTC | DOWN | 0.51 | open |  |
| 11-14 16:52 | +15 | BTC | DOWN | 0.51 | open |  |
| 11-14 16:52 | +10 | BTC | DOWN | 0.51 | 0.63 | 0.85 |
| 11-14 16:52 | +5 | BTC | DOWN | 0.50 | 0.63 | 0.95 |
| 11-14 16:51 | +5 | BNB | DOWN | 0.69 | open |  |
| 11-14 16:51 | +10 stop | BNB | DOWN | 0.70 | 0.52 | -2.13 |
| 11-14 16:51 | +20 | BNB | DOWN | 0.70 | open |  |
| 11-14 16:51 | +15 | BNB | DOWN | 0.71 | open |  |
