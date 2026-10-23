# Range-Scalp Bot

*Updated Fri Oct 23 06:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29892 | 26021 | 3871 (39) | 8 | $-8817.33 | -4.7% |
| **+10¢** | 22410 | 17928 | 4482 (55) | 9 | $-7936.93 | -5.6% |
| **+15¢** | 18765 | 13948 | 4817 (78) | 9 | $-7144.68 | -6.1% |
| **+20¢** | 16609 | 11563 | 5046 (101) | 9 | $-6451.93 | -6.2% |
| **+10¢ (15¢ stop)** | 36685 | 36626 | 59 (32) | 6 | $-13816.37 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 06:35 | +10 stop | BNB | UP | 0.60 | open |  |
| 10-23 06:34 | +5 | SOL | UP | 0.55 | open |  |
| 10-23 06:34 | +10 stop | ZEC | UP | 0.63 | open |  |
| 10-23 06:34 | +20 | ZEC | UP | 0.63 | open |  |
| 10-23 06:34 | +15 | ZEC | UP | 0.63 | open |  |
| 10-23 06:34 | +10 | ZEC | UP | 0.63 | open |  |
| 10-23 06:34 | +5 | ZEC | UP | 0.63 | open |  |
| 10-23 06:33 | +10 stop | DOGE | UP | 0.69 | open |  |
| 10-23 06:33 | +20 | DOGE | UP | 0.69 | open |  |
| 10-23 06:33 | +15 | DOGE | UP | 0.69 | open |  |
| 10-23 06:33 | +10 | DOGE | UP | 0.69 | open |  |
| 10-23 06:33 | +5 | DOGE | UP | 0.69 | open |  |
| 10-23 06:33 | +10 stop | ETH | UP | 0.67 | open |  |
| 10-23 06:33 | +20 | ETH | UP | 0.67 | open |  |
| 10-23 06:33 | +5 | BNB | UP | 0.69 | open |  |
| 10-23 06:33 | +10 stop | NEAR | DOWN | 0.56 | open |  |
| 10-23 06:33 | +10 stop | XRP | UP | 0.68 | open |  |
| 10-23 06:33 | +20 | XRP | UP | 0.68 | open |  |
| 10-23 06:33 | +15 | XRP | UP | 0.69 | open |  |
| 10-23 06:33 | +10 | XRP | UP | 0.69 | open |  |
| 10-23 06:33 | +5 | XRP | UP | 0.69 | open |  |
| 10-23 06:33 | +15 | ETH | UP | 0.71 | open |  |
| 10-23 06:33 | +10 | ETH | UP | 0.69 | open |  |
| 10-23 06:33 | +5 | ETH | UP | 0.69 | open |  |
| 10-23 06:33 | +5 | SOL | UP | 0.57 | 0.62 | 0.15 |
| 10-23 06:32 | +10 stop | HYPE | UP | 0.61 | 0.45 | -1.95 |
| 10-23 06:32 | +20 | HYPE | UP | 0.61 | open |  |
| 10-23 06:32 | +15 | HYPE | UP | 0.61 | open |  |
| 10-23 06:32 | +10 | HYPE | UP | 0.61 | open |  |
| 10-23 06:32 | +5 | HYPE | UP | 0.61 | 0.67 | 0.27 |
| 10-23 06:32 | +10 stop | BTC | UP | 0.68 | 0.51 | -2.04 |
| 10-23 06:32 | +20 | BTC | UP | 0.68 | open |  |
| 10-23 06:32 | +15 | BTC | UP | 0.68 | open |  |
| 10-23 06:32 | +10 | BTC | UP | 0.68 | open |  |
| 10-23 06:32 | +5 | BTC | UP | 0.68 | open |  |
| 10-23 06:32 | +10 stop | SOL | UP | 0.65 | 0.48 | -2.03 |
| 10-23 06:32 | +20 | SOL | UP | 0.65 | open |  |
| 10-23 06:32 | +15 | SOL | UP | 0.65 | open |  |
| 10-23 06:32 | +10 | SOL | UP | 0.65 | open |  |
| 10-23 06:32 | +5 | SOL | UP | 0.64 | 0.69 | 0.18 |
