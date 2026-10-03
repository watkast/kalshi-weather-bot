# Range-Scalp Bot

*Updated Sat Oct 03 13:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 807 | 704 | 103 (1) | 5 | $-220.86 | -4.3% |
| **+10¢** | 616 | 504 | 112 (2) | 5 | $-129.10 | -3.3% |
| **+15¢** | 522 | 402 | 120 (3) | 5 | $-107.13 | -3.3% |
| **+20¢** | 453 | 327 | 126 (3) | 9 | $-101.37 | -3.5% |
| **+10¢ (15¢ stop)** | 1030 | 1029 | 1 (1) | 5 | $-523.95 | -8.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 13:17 | +5 | BTC | DOWN | 0.71 | open |  |
| 10-03 13:17 | +5 | DOGE | DOWN | 0.68 | open |  |
| 10-03 13:17 | +5 | NEAR | DOWN | 0.59 | open |  |
| 10-03 13:17 | +10 stop | SOL | DOWN | 0.70 | open |  |
| 10-03 13:17 | +10 | SOL | DOWN | 0.70 | open |  |
| 10-03 13:17 | +5 | SOL | DOWN | 0.70 | open |  |
| 10-03 13:17 | +10 stop | NEAR | UP | 0.48 | open |  |
| 10-03 13:17 | +20 | NEAR | UP | 0.48 | open |  |
| 10-03 13:17 | +15 | NEAR | UP | 0.48 | open |  |
| 10-03 13:17 | +10 | NEAR | UP | 0.48 | open |  |
| 10-03 13:17 | +5 | NEAR | UP | 0.48 | 0.53 | 0.14 |
| 10-03 13:17 | +10 stop | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 10-03 13:17 | +20 | ETH | DOWN | 0.59 | open |  |
| 10-03 13:17 | +15 | ETH | DOWN | 0.59 | 0.74 | 1.19 |
| 10-03 13:17 | +10 | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 10-03 13:17 | +5 | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 10-03 13:16 | +10 stop | BTC | DOWN | 0.64 | open |  |
| 10-03 13:16 | +20 | BTC | DOWN | 0.64 | open |  |
| 10-03 13:16 | +15 | BTC | DOWN | 0.64 | open |  |
| 10-03 13:16 | +10 | BTC | DOWN | 0.64 | open |  |
| 10-03 13:16 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 10-03 13:16 | +5 | HYPE | UP | 0.57 | open |  |
| 10-03 13:15 | +10 stop | DOGE | DOWN | 0.59 | open |  |
| 10-03 13:15 | +20 | DOGE | DOWN | 0.59 | open |  |
| 10-03 13:15 | +15 | DOGE | DOWN | 0.59 | open |  |
| 10-03 13:15 | +10 | DOGE | DOWN | 0.59 | open |  |
| 10-03 13:15 | +5 | DOGE | DOWN | 0.59 | 0.65 | 0.27 |
| 10-03 13:15 | +10 stop | XRP | DOWN | 0.60 | 0.74 | 1.09 |
| 10-03 13:15 | +20 | XRP | DOWN | 0.60 | open |  |
| 10-03 13:15 | +15 | XRP | DOWN | 0.60 | open |  |
| 10-03 13:15 | +10 | XRP | DOWN | 0.60 | 0.74 | 1.09 |
| 10-03 13:15 | +5 | XRP | DOWN | 0.60 | 0.74 | 1.09 |
| 10-03 13:15 | +10 stop | SOL | DOWN | 0.52 | 0.64 | 0.85 |
| 10-03 13:15 | +20 | SOL | DOWN | 0.52 | open |  |
| 10-03 13:15 | +15 | SOL | DOWN | 0.52 | 0.67 | 1.16 |
| 10-03 13:15 | +10 | SOL | DOWN | 0.52 | 0.64 | 0.85 |
| 10-03 13:15 | +5 | SOL | DOWN | 0.52 | 0.64 | 0.85 |
| 10-03 13:15 | +10 stop | ZEC | DOWN | 0.56 | open |  |
| 10-03 13:15 | +20 | ZEC | DOWN | 0.56 | open |  |
| 10-03 13:15 | +15 | ZEC | DOWN | 0.56 | open |  |
