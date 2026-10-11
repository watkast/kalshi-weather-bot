# Range-Scalp Bot

*Updated Sun Oct 11 05:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11451 | 9877 | 1574 (24) | 8 | $-3854.72 | -5.3% |
| **+10¢** | 8673 | 6841 | 1832 (37) | 9 | $-3684.15 | -6.7% |
| **+15¢** | 7309 | 5371 | 1938 (53) | 9 | $-3114.24 | -6.8% |
| **+20¢** | 6514 | 4498 | 2016 (67) | 8 | $-2594.56 | -6.3% |
| **+10¢ (15¢ stop)** | 14119 | 14078 | 41 (25) | 5 | $-5664.04 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 05:51 | +10 stop | NEAR | DOWN | 0.58 | open |  |
| 10-11 05:51 | +10 stop | XRP | UP | 0.66 | open |  |
| 10-11 05:50 | +10 stop | HYPE | UP | 0.53 | 0.38 | -1.85 |
| 10-11 05:50 | +10 stop | SOL | UP | 0.67 | 0.48 | -2.24 |
| 10-11 05:50 | +10 | HYPE | UP | 0.62 | open |  |
| 10-11 05:49 | +10 stop | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 10-11 05:49 | +10 stop | BNB | UP | 0.59 | open |  |
| 10-11 05:49 | +10 stop | NEAR | UP | 0.68 | 0.46 | -2.54 |
| 10-11 05:49 | +10 | NEAR | UP | 0.68 | open |  |
| 10-11 05:49 | +5 | NEAR | UP | 0.68 | open |  |
| 10-11 05:49 | +10 stop | XRP | UP | 0.69 | 0.54 | -1.83 |
| 10-11 05:49 | +15 | BTC | DOWN | 0.69 | open |  |
| 10-11 05:49 | +10 stop | HYPE | UP | 0.71 | 0.55 | -1.93 |
| 10-11 05:49 | +5 | HYPE | UP | 0.71 | open |  |
| 10-11 05:48 | +10 stop | DOGE | UP | 0.57 | 0.70 | 0.97 |
| 10-11 05:48 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 10-11 05:48 | +10 | BTC | DOWN | 0.70 | open |  |
| 10-11 05:48 | +10 stop | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 10-11 05:48 | +5 | BTC | DOWN | 0.70 | 0.77 | 0.42 |
| 10-11 05:48 | +10 stop | HYPE | DOWN | 0.54 | 0.36 | -2.15 |
| 10-11 05:47 | +10 stop | BNB | DOWN | 0.55 | 0.37 | -2.15 |
| 10-11 05:47 | +15 | DOGE | DOWN | 0.58 | open |  |
| 10-11 05:47 | +5 | ZEC | DOWN | 0.67 | open |  |
| 10-11 05:47 | +10 stop | DOGE | DOWN | 0.61 | 0.43 | -2.15 |
| 10-11 05:47 | +10 | DOGE | DOWN | 0.61 | open |  |
| 10-11 05:47 | +5 | DOGE | DOWN | 0.61 | open |  |
| 10-11 05:47 | +10 stop | NEAR | UP | 0.55 | 0.68 | 0.97 |
| 10-11 05:47 | +20 | NEAR | UP | 0.55 | open |  |
| 10-11 05:47 | +15 | NEAR | UP | 0.55 | open |  |
| 10-11 05:47 | +10 | NEAR | UP | 0.55 | 0.68 | 0.97 |
| 10-11 05:47 | +5 | NEAR | UP | 0.55 | 0.68 | 0.97 |
| 10-11 05:46 | +10 stop | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-11 05:46 | +10 stop | HYPE | UP | 0.57 | 0.39 | -2.15 |
| 10-11 05:46 | +20 | HYPE | UP | 0.57 | open |  |
| 10-11 05:46 | +15 | HYPE | UP | 0.57 | open |  |
| 10-11 05:46 | +10 | HYPE | UP | 0.57 | 0.69 | 0.87 |
| 10-11 05:46 | +5 | HYPE | UP | 0.57 | 0.63 | 0.25 |
| 10-11 05:46 | +10 stop | ETH | UP | 0.56 | 0.37 | -2.25 |
| 10-11 05:46 | +20 | ETH | UP | 0.56 | open |  |
| 10-11 05:46 | +15 | ETH | UP | 0.56 | open |  |
