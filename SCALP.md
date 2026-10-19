# Range-Scalp Bot

*Updated Mon Oct 19 12:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23956 | 20830 | 3126 (31) | 3 | $-7138.29 | -4.7% |
| **+10¢** | 18023 | 14418 | 3605 (45) | 3 | $-6375.79 | -5.6% |
| **+15¢** | 15102 | 11220 | 3882 (68) | 3 | $-5757.58 | -6.1% |
| **+20¢** | 13368 | 9306 | 4062 (87) | 3 | $-5133.57 | -6.1% |
| **+10¢ (15¢ stop)** | 29495 | 29444 | 51 (30) | 3 | $-11195.57 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 12:00 | +10 stop | SOL | UP | 0.57 | open |  |
| 10-19 12:00 | +20 | SOL | UP | 0.57 | open |  |
| 10-19 12:00 | +15 | SOL | UP | 0.57 | open |  |
| 10-19 12:00 | +10 | SOL | UP | 0.57 | open |  |
| 10-19 12:00 | +5 | SOL | UP | 0.57 | open |  |
| 10-19 12:00 | +10 stop | BTC | UP | 0.55 | open |  |
| 10-19 12:00 | +20 | BTC | UP | 0.55 | open |  |
| 10-19 12:00 | +15 | BTC | UP | 0.55 | open |  |
| 10-19 12:00 | +10 | BTC | UP | 0.55 | open |  |
| 10-19 12:00 | +5 | BTC | UP | 0.55 | open |  |
| 10-19 12:00 | +10 stop | DOGE | UP | 0.62 | open |  |
| 10-19 12:00 | +20 | DOGE | UP | 0.62 | open |  |
| 10-19 12:00 | +15 | DOGE | UP | 0.62 | open |  |
| 10-19 12:00 | +10 | DOGE | UP | 0.62 | open |  |
| 10-19 12:00 | +5 | DOGE | UP | 0.62 | open |  |
| 10-19 11:53 | +15 | ETH | UP | 0.66 | 0.83 | 1.44 |
| 10-19 11:53 | +10 | ETH | UP | 0.66 | 0.80 | 1.12 |
| 10-19 11:53 | +10 stop | NEAR | UP | 0.67 | 0.36 | -3.40 |
| 10-19 11:52 | +10 stop | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 10-19 11:52 | +15 | ETH | UP | 0.54 | 0.70 | 1.27 |
| 10-19 11:52 | +10 | ETH | UP | 0.54 | 0.70 | 1.27 |
| 10-19 11:52 | +10 stop | NEAR | UP | 0.65 | 0.50 | -1.84 |
| 10-19 11:51 | +10 stop | ETH | UP | 0.66 | 0.80 | 1.12 |
| 10-19 11:50 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 10-19 11:50 | +10 stop | DOGE | UP | 0.63 | 0.79 | 1.31 |
| 10-19 11:49 | +10 stop | BNB | UP | 0.54 | 0.72 | 1.47 |
| 10-19 11:49 | +10 stop | SOL | DOWN | 0.68 | 0.45 | -2.64 |
| 10-19 11:49 | +20 | SOL | DOWN | 0.68 | 0.93 | 2.26 |
| 10-19 11:49 | +15 | SOL | DOWN | 0.68 | 0.93 | 2.26 |
| 10-19 11:49 | +10 | SOL | DOWN | 0.68 | 0.93 | 2.26 |
| 10-19 11:49 | +5 | SOL | DOWN | 0.68 | 0.93 | 2.26 |
| 10-19 11:49 | +5 | ETH | DOWN | 0.58 | 0.65 | 0.36 |
| 10-19 11:49 | +10 | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 10-19 11:49 | +10 stop | ETH | DOWN | 0.59 | 0.43 | -1.95 |
| 10-19 11:49 | +5 | ETH | DOWN | 0.59 | 0.65 | 0.27 |
| 10-19 11:48 | +10 stop | XRP | UP | 0.60 | 0.70 | 0.68 |
| 10-19 11:48 | +5 | XRP | UP | 0.60 | 0.69 | 0.58 |
| 10-19 11:48 | +5 | BTC | DOWN | 0.59 | yes | -6.07 |
| 10-19 11:48 | +10 stop | ZEC | DOWN | 0.55 | 0.33 | -2.54 |
| 10-19 11:48 | +5 | NEAR | DOWN | 0.67 | 0.76 | 0.61 |
