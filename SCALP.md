# Range-Scalp Bot

*Updated Tue Oct 27 01:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35742 | 31194 | 4548 (43) | 9 | $-9993.09 | -4.4% |
| **+10¢** | 26716 | 21454 | 5262 (65) | 9 | $-8850.92 | -5.3% |
| **+15¢** | 22363 | 16706 | 5657 (89) | 9 | $-7894.36 | -5.6% |
| **+20¢** | 19819 | 13891 | 5928 (112) | 9 | $-6963.40 | -5.6% |
| **+10¢ (15¢ stop)** | 43801 | 43738 | 63 (33) | 9 | $-16687.58 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 01:04 | +5 | ZEC | UP | 0.60 | open |  |
| 10-27 01:04 | +10 stop | XRP | DOWN | 0.57 | open |  |
| 10-27 01:04 | +20 | DOGE | UP | 0.66 | open |  |
| 10-27 01:04 | +15 | DOGE | UP | 0.66 | open |  |
| 10-27 01:04 | +5 | DOGE | UP | 0.66 | open |  |
| 10-27 01:04 | +10 stop | BTC | UP | 0.60 | open |  |
| 10-27 01:04 | +15 | BTC | UP | 0.60 | open |  |
| 10-27 01:04 | +10 | BTC | UP | 0.60 | open |  |
| 10-27 01:04 | +5 | BTC | UP | 0.60 | open |  |
| 10-27 01:04 | +10 stop | HYPE | UP | 0.62 | open |  |
| 10-27 01:04 | +15 | HYPE | UP | 0.62 | open |  |
| 10-27 01:04 | +10 | HYPE | UP | 0.62 | open |  |
| 10-27 01:04 | +5 | HYPE | UP | 0.62 | open |  |
| 10-27 01:03 | +5 | SOL | UP | 0.60 | open |  |
| 10-27 01:03 | +5 | ZEC | UP | 0.60 | 0.67 | 0.37 |
| 10-27 01:03 | +5 | ETH | UP | 0.62 | open |  |
| 10-27 01:03 | +10 stop | XRP | UP | 0.46 | 0.58 | 0.84 |
| 10-27 01:03 | +10 stop | NEAR | UP | 0.60 | open |  |
| 10-27 01:02 | +10 stop | DOGE | UP | 0.68 | open |  |
| 10-27 01:02 | +10 | DOGE | UP | 0.68 | open |  |
| 10-27 01:02 | +5 | DOGE | UP | 0.68 | 0.74 | 0.30 |
| 10-27 01:02 | +10 stop | SOL | UP | 0.63 | open |  |
| 10-27 01:02 | +20 | SOL | UP | 0.63 | open |  |
| 10-27 01:02 | +15 | SOL | UP | 0.63 | open |  |
| 10-27 01:02 | +10 | SOL | UP | 0.63 | open |  |
| 10-27 01:02 | +5 | SOL | UP | 0.63 | 0.68 | 0.17 |
| 10-27 01:02 | +10 stop | ZEC | UP | 0.61 | open |  |
| 10-27 01:02 | +15 | ZEC | UP | 0.62 | open |  |
| 10-27 01:02 | +10 | ZEC | UP | 0.61 | open |  |
| 10-27 01:02 | +5 | ZEC | UP | 0.61 | 0.66 | 0.17 |
| 10-27 01:02 | +10 stop | BNB | UP | 0.62 | open |  |
| 10-27 01:02 | +20 | BNB | UP | 0.62 | open |  |
| 10-27 01:02 | +15 | BNB | UP | 0.62 | open |  |
| 10-27 01:02 | +10 | BNB | UP | 0.62 | open |  |
| 10-27 01:02 | +5 | BNB | UP | 0.62 | open |  |
| 10-27 01:02 | +10 stop | ETH | UP | 0.61 | open |  |
| 10-27 01:02 | +20 | ETH | UP | 0.61 | open |  |
| 10-27 01:02 | +15 | ETH | UP | 0.61 | open |  |
| 10-27 01:02 | +10 | ETH | UP | 0.61 | open |  |
| 10-27 01:02 | +5 | ETH | UP | 0.61 | 0.66 | 0.17 |
