# Range-Scalp Bot

*Updated Sat Oct 03 12:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 771 | 669 | 102 (1) | 6 | $-235.08 | -4.8% |
| **+10¢** | 588 | 477 | 111 (2) | 7 | $-154.90 | -4.2% |
| **+15¢** | 500 | 381 | 119 (3) | 7 | $-134.16 | -4.3% |
| **+20¢** | 437 | 312 | 125 (3) | 7 | $-129.05 | -4.7% |
| **+10¢ (15¢ stop)** | 991 | 990 | 1 (1) | 5 | $-523.60 | -8.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 12:47 | +10 stop | DOGE | DOWN | 0.46 | 0.56 | 0.64 |
| 10-03 12:47 | +5 | DOGE | DOWN | 0.52 | open |  |
| 10-03 12:47 | +10 stop | NEAR | UP | 0.63 | open |  |
| 10-03 12:47 | +20 | NEAR | UP | 0.63 | open |  |
| 10-03 12:47 | +15 | NEAR | UP | 0.63 | open |  |
| 10-03 12:47 | +10 | NEAR | UP | 0.63 | open |  |
| 10-03 12:47 | +5 | NEAR | UP | 0.63 | 0.69 | 0.28 |
| 10-03 12:46 | +10 stop | BTC | UP | 0.58 | open |  |
| 10-03 12:46 | +20 | BTC | UP | 0.58 | open |  |
| 10-03 12:46 | +15 | BTC | UP | 0.58 | open |  |
| 10-03 12:46 | +10 | BTC | UP | 0.59 | open |  |
| 10-03 12:46 | +5 | BTC | UP | 0.59 | open |  |
| 10-03 12:46 | +10 stop | DOGE | UP | 0.55 | 0.38 | -2.05 |
| 10-03 12:46 | +20 | DOGE | UP | 0.53 | open |  |
| 10-03 12:46 | +15 | DOGE | UP | 0.53 | open |  |
| 10-03 12:46 | +10 | DOGE | UP | 0.53 | open |  |
| 10-03 12:46 | +5 | DOGE | UP | 0.53 | 0.59 | 0.25 |
| 10-03 12:46 | +10 stop | ZEC | UP | 0.58 | 0.37 | -2.48 |
| 10-03 12:46 | +20 | ZEC | UP | 0.58 | open |  |
| 10-03 12:46 | +15 | ZEC | UP | 0.58 | open |  |
| 10-03 12:46 | +10 | ZEC | UP | 0.58 | open |  |
| 10-03 12:46 | +5 | ZEC | UP | 0.57 | open |  |
| 10-03 12:46 | +10 stop | ETH | UP | 0.61 | open |  |
| 10-03 12:46 | +20 | ETH | UP | 0.61 | open |  |
| 10-03 12:46 | +15 | ETH | UP | 0.61 | open |  |
| 10-03 12:46 | +10 | ETH | UP | 0.61 | open |  |
| 10-03 12:46 | +5 | ETH | UP | 0.61 | open |  |
| 10-03 12:45 | +10 stop | HYPE | UP | 0.70 | open |  |
| 10-03 12:45 | +20 | HYPE | UP | 0.70 | open |  |
| 10-03 12:45 | +15 | HYPE | UP | 0.70 | open |  |
| 10-03 12:45 | +10 | HYPE | UP | 0.70 | open |  |
| 10-03 12:45 | +5 | HYPE | UP | 0.70 | open |  |
| 10-03 12:45 | +10 stop | SOL | UP | 0.68 | open |  |
| 10-03 12:45 | +20 | SOL | UP | 0.68 | open |  |
| 10-03 12:45 | +15 | SOL | UP | 0.68 | open |  |
| 10-03 12:45 | +10 | SOL | UP | 0.68 | open |  |
| 10-03 12:45 | +5 | SOL | UP | 0.68 | open |  |
| 10-03 12:43 | +10 stop | BNB | UP | 0.71 | 0.81 | 0.75 |
| 10-03 12:42 | +10 stop | NEAR | UP | 0.38 | 0.59 | 1.77 |
| 10-03 12:42 | +20 | NEAR | UP | 0.38 | 0.59 | 1.77 |
