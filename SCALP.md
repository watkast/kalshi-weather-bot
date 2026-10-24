# Range-Scalp Bot

*Updated Sat Oct 24 02:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31291 | 27265 | 4026 (40) | 7 | $-9063.06 | -4.6% |
| **+10¢** | 23417 | 18767 | 4650 (58) | 8 | $-8054.70 | -5.5% |
| **+15¢** | 19596 | 14599 | 4997 (81) | 8 | $-7197.76 | -5.8% |
| **+20¢** | 17361 | 12127 | 5234 (103) | 8 | $-6432.44 | -5.9% |
| **+10¢ (15¢ stop)** | 38393 | 38334 | 59 (32) | 6 | $-14605.76 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 02:33 | +10 stop | NEAR | UP | 0.58 | open |  |
| 10-24 02:33 | +10 stop | BNB | UP | 0.56 | open |  |
| 10-24 02:33 | +20 | BNB | UP | 0.56 | open |  |
| 10-24 02:33 | +15 | BNB | UP | 0.56 | open |  |
| 10-24 02:33 | +10 | BNB | UP | 0.56 | open |  |
| 10-24 02:33 | +5 | BNB | UP | 0.56 | 0.64 | 0.45 |
| 10-24 02:33 | +10 stop | ETH | DOWN | 0.54 | open |  |
| 10-24 02:33 | +5 | ZEC | DOWN | 0.63 | open |  |
| 10-24 02:33 | +10 stop | SOL | DOWN | 0.71 | open |  |
| 10-24 02:33 | +20 | SOL | DOWN | 0.71 | open |  |
| 10-24 02:33 | +15 | SOL | DOWN | 0.71 | open |  |
| 10-24 02:33 | +10 | SOL | DOWN | 0.71 | open |  |
| 10-24 02:33 | +5 | SOL | DOWN | 0.71 | open |  |
| 10-24 02:31 | +10 stop | BTC | DOWN | 0.59 | open |  |
| 10-24 02:31 | +20 | BTC | DOWN | 0.59 | open |  |
| 10-24 02:31 | +15 | BTC | DOWN | 0.59 | open |  |
| 10-24 02:31 | +10 | BTC | DOWN | 0.59 | open |  |
| 10-24 02:31 | +5 | BTC | DOWN | 0.59 | open |  |
| 10-24 02:31 | +10 stop | XRP | DOWN | 0.64 | 0.46 | -2.15 |
| 10-24 02:31 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-24 02:31 | +15 | XRP | DOWN | 0.65 | open |  |
| 10-24 02:31 | +10 | XRP | DOWN | 0.65 | open |  |
| 10-24 02:31 | +5 | XRP | DOWN | 0.65 | open |  |
| 10-24 02:31 | +10 stop | HYPE | DOWN | 0.60 | 0.45 | -1.89 |
| 10-24 02:31 | +20 | HYPE | DOWN | 0.60 | open |  |
| 10-24 02:31 | +15 | HYPE | DOWN | 0.60 | open |  |
| 10-24 02:31 | +10 | HYPE | DOWN | 0.59 | open |  |
| 10-24 02:31 | +5 | HYPE | DOWN | 0.60 | open |  |
| 10-24 02:31 | +10 stop | ZEC | DOWN | 0.67 | open |  |
| 10-24 02:31 | +20 | ZEC | DOWN | 0.67 | open |  |
| 10-24 02:31 | +15 | ZEC | DOWN | 0.67 | open |  |
| 10-24 02:31 | +10 | ZEC | DOWN | 0.67 | open |  |
| 10-24 02:31 | +5 | ZEC | DOWN | 0.67 | 0.74 | 0.41 |
| 10-24 02:31 | +10 stop | NEAR | DOWN | 0.59 | 0.44 | -1.85 |
| 10-24 02:31 | +20 | NEAR | DOWN | 0.59 | open |  |
| 10-24 02:31 | +15 | NEAR | DOWN | 0.59 | open |  |
| 10-24 02:31 | +10 | NEAR | DOWN | 0.59 | open |  |
| 10-24 02:31 | +5 | NEAR | DOWN | 0.59 | open |  |
| 10-24 02:31 | +10 stop | ETH | DOWN | 0.62 | 0.44 | -2.15 |
| 10-24 02:31 | +20 | ETH | DOWN | 0.62 | open |  |
