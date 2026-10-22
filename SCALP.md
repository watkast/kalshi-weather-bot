# Range-Scalp Bot

*Updated Thu Oct 22 09:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28544 | 24875 | 3669 (39) | 3 | $-8198.29 | -4.6% |
| **+10¢** | 21416 | 17169 | 4247 (55) | 6 | $-7308.89 | -5.4% |
| **+15¢** | 17928 | 13358 | 4570 (78) | 5 | $-6548.30 | -5.8% |
| **+20¢** | 15860 | 11066 | 4794 (100) | 7 | $-5923.28 | -5.9% |
| **+10¢ (15¢ stop)** | 35015 | 34956 | 59 (32) | 3 | $-13154.70 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 09:48 | +10 stop | NEAR | UP | 0.70 | open |  |
| 10-22 09:48 | +10 | NEAR | UP | 0.70 | open |  |
| 10-22 09:48 | +5 | NEAR | UP | 0.70 | 0.79 | 0.63 |
| 10-22 09:48 | +10 stop | SOL | UP | 0.71 | open |  |
| 10-22 09:48 | +20 | SOL | UP | 0.71 | open |  |
| 10-22 09:48 | +15 | SOL | UP | 0.71 | open |  |
| 10-22 09:48 | +10 | SOL | UP | 0.71 | open |  |
| 10-22 09:48 | +5 | SOL | UP | 0.71 | 0.78 | 0.42 |
| 10-22 09:47 | +10 stop | HYPE | UP | 0.61 | 0.72 | 0.78 |
| 10-22 09:47 | +5 | BTC | UP | 0.60 | 0.65 | 0.17 |
| 10-22 09:47 | +10 stop | BNB | UP | 0.61 | 0.72 | 0.78 |
| 10-22 09:47 | +20 | BNB | UP | 0.61 | open |  |
| 10-22 09:47 | +15 | BNB | UP | 0.61 | 0.80 | 1.61 |
| 10-22 09:47 | +10 | BNB | UP | 0.61 | 0.72 | 0.78 |
| 10-22 09:47 | +5 | BNB | UP | 0.61 | 0.69 | 0.48 |
| 10-22 09:47 | +10 stop | NEAR | UP | 0.51 | 0.63 | 0.85 |
| 10-22 09:47 | +20 | NEAR | UP | 0.51 | 0.71 | 1.67 |
| 10-22 09:47 | +15 | NEAR | UP | 0.51 | 0.67 | 1.26 |
| 10-22 09:47 | +10 | NEAR | UP | 0.51 | 0.63 | 0.85 |
| 10-22 09:47 | +5 | NEAR | UP | 0.51 | 0.63 | 0.85 |
| 10-22 09:47 | +10 stop | DOGE | UP | 0.61 | open |  |
| 10-22 09:47 | +20 | DOGE | UP | 0.61 | open |  |
| 10-22 09:47 | +15 | DOGE | UP | 0.61 | open |  |
| 10-22 09:47 | +10 | DOGE | UP | 0.61 | open |  |
| 10-22 09:47 | +5 | DOGE | UP | 0.61 | 0.67 | 0.27 |
| 10-22 09:47 | +10 stop | ETH | UP | 0.61 | 0.73 | 0.89 |
| 10-22 09:47 | +20 | ETH | UP | 0.61 | open |  |
| 10-22 09:47 | +15 | ETH | UP | 0.62 | 0.78 | 1.30 |
| 10-22 09:47 | +10 | ETH | UP | 0.62 | 0.73 | 0.79 |
| 10-22 09:47 | +5 | ETH | UP | 0.62 | 0.73 | 0.79 |
| 10-22 09:46 | +10 stop | XRP | DOWN | 0.58 | 0.41 | -2.05 |
| 10-22 09:46 | +20 | XRP | DOWN | 0.58 | open |  |
| 10-22 09:46 | +15 | XRP | DOWN | 0.58 | open |  |
| 10-22 09:46 | +10 | XRP | DOWN | 0.58 | open |  |
| 10-22 09:46 | +5 | XRP | DOWN | 0.58 | open |  |
| 10-22 09:46 | +10 stop | ZEC | DOWN | 0.67 | 0.49 | -2.14 |
| 10-22 09:46 | +20 | ZEC | DOWN | 0.67 | open |  |
| 10-22 09:46 | +15 | ZEC | DOWN | 0.67 | open |  |
| 10-22 09:46 | +10 | ZEC | DOWN | 0.67 | open |  |
| 10-22 09:46 | +5 | ZEC | DOWN | 0.67 | open |  |
