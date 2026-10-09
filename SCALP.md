# Range-Scalp Bot

*Updated Fri Oct 09 19:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9409 | 8121 | 1288 (17) | 6 | $-3182.94 | -5.4% |
| **+10¢** | 7102 | 5590 | 1512 (29) | 7 | $-3120.99 | -7.0% |
| **+15¢** | 5983 | 4393 | 1590 (42) | 7 | $-2569.23 | -6.8% |
| **+20¢** | 5326 | 3674 | 1652 (53) | 7 | $-2155.07 | -6.4% |
| **+10¢ (15¢ stop)** | 11521 | 11489 | 32 (20) | 7 | $-4438.85 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 19:46 | +10 stop | NEAR | DOWN | 0.62 | open |  |
| 10-09 19:46 | +20 | NEAR | DOWN | 0.62 | open |  |
| 10-09 19:46 | +15 | NEAR | DOWN | 0.63 | open |  |
| 10-09 19:46 | +10 | NEAR | DOWN | 0.62 | open |  |
| 10-09 19:46 | +5 | NEAR | DOWN | 0.63 | open |  |
| 10-09 19:46 | +10 stop | HYPE | DOWN | 0.61 | open |  |
| 10-09 19:46 | +20 | HYPE | DOWN | 0.61 | open |  |
| 10-09 19:46 | +15 | HYPE | DOWN | 0.61 | open |  |
| 10-09 19:46 | +10 | HYPE | DOWN | 0.61 | open |  |
| 10-09 19:46 | +5 | HYPE | DOWN | 0.61 | 0.67 | 0.23 |
| 10-09 19:46 | +10 stop | SOL | DOWN | 0.64 | open |  |
| 10-09 19:46 | +20 | SOL | DOWN | 0.64 | open |  |
| 10-09 19:46 | +15 | SOL | DOWN | 0.64 | open |  |
| 10-09 19:46 | +10 | SOL | DOWN | 0.64 | open |  |
| 10-09 19:46 | +5 | SOL | DOWN | 0.64 | open |  |
| 10-09 19:46 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 10-09 19:46 | +20 | ETH | DOWN | 0.67 | open |  |
| 10-09 19:46 | +15 | ETH | DOWN | 0.68 | open |  |
| 10-09 19:46 | +10 | ETH | DOWN | 0.67 | open |  |
| 10-09 19:46 | +5 | ETH | DOWN | 0.67 | open |  |
| 10-09 19:46 | +10 stop | BTC | DOWN | 0.61 | open |  |
| 10-09 19:46 | +20 | BTC | DOWN | 0.61 | open |  |
| 10-09 19:46 | +15 | BTC | DOWN | 0.61 | open |  |
| 10-09 19:46 | +10 | BTC | DOWN | 0.61 | open |  |
| 10-09 19:46 | +5 | BTC | DOWN | 0.61 | open |  |
| 10-09 19:46 | +10 stop | ZEC | DOWN | 0.61 | open |  |
| 10-09 19:46 | +20 | ZEC | DOWN | 0.61 | open |  |
| 10-09 19:46 | +15 | ZEC | DOWN | 0.61 | open |  |
| 10-09 19:46 | +10 | ZEC | DOWN | 0.61 | open |  |
| 10-09 19:46 | +5 | ZEC | DOWN | 0.61 | open |  |
| 10-09 19:46 | +10 stop | XRP | DOWN | 0.68 | open |  |
| 10-09 19:46 | +20 | XRP | DOWN | 0.68 | open |  |
| 10-09 19:46 | +15 | XRP | DOWN | 0.68 | open |  |
| 10-09 19:46 | +10 | XRP | DOWN | 0.68 | open |  |
| 10-09 19:46 | +5 | XRP | DOWN | 0.68 | open |  |
| 10-09 19:36 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-09 19:35 | +5 | ETH | DOWN | 0.70 | 0.79 | 0.63 |
| 10-09 19:35 | +10 | BNB | UP | 0.52 | no | -5.38 |
| 10-09 19:35 | +10 stop | XRP | DOWN | 0.61 | 0.73 | 0.89 |
| 10-09 19:35 | +10 stop | BTC | UP | 0.59 | 0.43 | -1.95 |
