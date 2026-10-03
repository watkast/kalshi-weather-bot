# Range-Scalp Bot

*Updated Sat Oct 03 11:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 666 | 573 | 93 (1) | 8 | $-241.84 | -5.7% |
| **+10¢** | 506 | 402 | 104 (2) | 9 | $-200.58 | -6.3% |
| **+15¢** | 431 | 320 | 111 (3) | 9 | $-182.41 | -6.7% |
| **+20¢** | 374 | 260 | 114 (3) | 9 | $-169.05 | -7.2% |
| **+10¢ (15¢ stop)** | 863 | 862 | 1 (1) | 7 | $-479.76 | -8.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 11:18 | +5 | HYPE | UP | 0.61 | open |  |
| 10-03 11:18 | +10 stop | SOL | UP | 0.57 | open |  |
| 10-03 11:18 | +5 | BNB | DOWN | 0.61 | open |  |
| 10-03 11:17 | +10 | HYPE | UP | 0.57 | open |  |
| 10-03 11:17 | +5 | HYPE | UP | 0.56 | 0.63 | 0.35 |
| 10-03 11:17 | +10 stop | ZEC | UP | 0.60 | open |  |
| 10-03 11:17 | +15 | ZEC | UP | 0.61 | open |  |
| 10-03 11:17 | +10 | ZEC | UP | 0.62 | open |  |
| 10-03 11:17 | +5 | ZEC | UP | 0.63 | open |  |
| 10-03 11:17 | +10 stop | ETH | UP | 0.54 | open |  |
| 10-03 11:17 | +20 | ETH | UP | 0.54 | open |  |
| 10-03 11:17 | +15 | ETH | UP | 0.54 | open |  |
| 10-03 11:17 | +10 | ETH | UP | 0.54 | open |  |
| 10-03 11:17 | +5 | ETH | UP | 0.54 | open |  |
| 10-03 11:17 | +10 stop | HYPE | UP | 0.55 | open |  |
| 10-03 11:17 | +20 | HYPE | UP | 0.53 | open |  |
| 10-03 11:17 | +15 | HYPE | UP | 0.53 | open |  |
| 10-03 11:17 | +10 | HYPE | UP | 0.53 | 0.63 | 0.65 |
| 10-03 11:17 | +5 | HYPE | UP | 0.53 | 0.62 | 0.55 |
| 10-03 11:16 | +10 stop | DOGE | DOWN | 0.53 | 0.37 | -1.95 |
| 10-03 11:16 | +20 | DOGE | DOWN | 0.53 | open |  |
| 10-03 11:16 | +15 | DOGE | DOWN | 0.53 | open |  |
| 10-03 11:16 | +10 | DOGE | DOWN | 0.53 | open |  |
| 10-03 11:16 | +5 | DOGE | DOWN | 0.53 | 0.59 | 0.25 |
| 10-03 11:16 | +10 stop | BTC | UP | 0.58 | open |  |
| 10-03 11:16 | +20 | BTC | UP | 0.58 | open |  |
| 10-03 11:16 | +15 | BTC | UP | 0.58 | open |  |
| 10-03 11:16 | +10 | BTC | UP | 0.58 | open |  |
| 10-03 11:16 | +5 | BTC | UP | 0.58 | open |  |
| 10-03 11:16 | +10 stop | NEAR | DOWN | 0.53 | open |  |
| 10-03 11:16 | +20 | NEAR | DOWN | 0.53 | open |  |
| 10-03 11:16 | +15 | NEAR | DOWN | 0.53 | open |  |
| 10-03 11:16 | +10 | NEAR | DOWN | 0.53 | open |  |
| 10-03 11:16 | +5 | NEAR | DOWN | 0.53 | open |  |
| 10-03 11:15 | +10 stop | SOL | DOWN | 0.61 | 0.36 | -2.84 |
| 10-03 11:15 | +20 | SOL | DOWN | 0.61 | open |  |
| 10-03 11:15 | +15 | SOL | DOWN | 0.61 | open |  |
| 10-03 11:15 | +10 | SOL | DOWN | 0.61 | open |  |
| 10-03 11:15 | +5 | SOL | DOWN | 0.61 | open |  |
| 10-03 11:15 | +10 stop | XRP | DOWN | 0.61 | 0.37 | -2.74 |
