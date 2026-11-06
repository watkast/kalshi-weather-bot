# Range-Scalp Bot

*Updated Fri Nov 06 16:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49702 | 43323 | 6379 (76) | 6 | $-13968.86 | -4.5% |
| **+10¢** | 37098 | 29678 | 7420 (101) | 8 | $-12864.22 | -5.5% |
| **+15¢** | 31071 | 23077 | 7994 (130) | 9 | $-11761.64 | -6.0% |
| **+20¢** | 27620 | 19238 | 8382 (171) | 9 | $-10415.79 | -6.0% |
| **+10¢ (15¢ stop)** | 60558 | 60461 | 97 (57) | 7 | $-22409.01 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 16:04 | +5 | ZEC | UP | 0.58 | open |  |
| 11-06 16:04 | +10 stop | DOGE | DOWN | 0.51 | open |  |
| 11-06 16:04 | +5 | DOGE | DOWN | 0.51 | 0.56 | 0.14 |
| 11-06 16:04 | +10 stop | BNB | DOWN | 0.61 | open |  |
| 11-06 16:04 | +10 stop | BTC | DOWN | 0.66 | open |  |
| 11-06 16:04 | +10 stop | SOL | DOWN | 0.65 | open |  |
| 11-06 16:03 | +10 stop | ZEC | UP | 0.55 | open |  |
| 11-06 16:03 | +10 | ZEC | UP | 0.55 | open |  |
| 11-06 16:03 | +5 | ZEC | UP | 0.55 | 0.63 | 0.45 |
| 11-06 16:03 | +5 | XRP | UP | 0.67 | 0.73 | 0.30 |
| 11-06 16:03 | +10 stop | DOGE | UP | 0.57 | 0.37 | -2.35 |
| 11-06 16:03 | +10 stop | ETH | UP | 0.59 | open |  |
| 11-06 16:02 | +10 stop | NEAR | UP | 0.60 | 0.43 | -2.05 |
| 11-06 16:02 | +5 | DOGE | DOWN | 0.57 | 0.62 | 0.15 |
| 11-06 16:02 | +10 stop | XRP | UP | 0.66 | open |  |
| 11-06 16:02 | +20 | XRP | UP | 0.67 | open |  |
| 11-06 16:02 | +15 | XRP | UP | 0.67 | open |  |
| 11-06 16:02 | +10 | XRP | UP | 0.67 | open |  |
| 11-06 16:02 | +5 | XRP | UP | 0.67 | 0.72 | 0.19 |
| 11-06 16:01 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-06 16:01 | +20 | HYPE | DOWN | 0.69 | open |  |
| 11-06 16:01 | +15 | HYPE | DOWN | 0.69 | open |  |
| 11-06 16:01 | +10 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-06 16:01 | +5 | HYPE | DOWN | 0.69 | 0.77 | 0.52 |
| 11-06 16:01 | +10 stop | DOGE | DOWN | 0.56 | 0.41 | -1.85 |
| 11-06 16:01 | +20 | DOGE | DOWN | 0.56 | open |  |
| 11-06 16:01 | +15 | DOGE | DOWN | 0.56 | open |  |
| 11-06 16:01 | +10 | DOGE | DOWN | 0.56 | open |  |
| 11-06 16:01 | +5 | DOGE | DOWN | 0.56 | 0.62 | 0.25 |
| 11-06 16:01 | +5 | SOL | DOWN | 0.65 | open |  |
| 11-06 16:01 | +10 stop | ZEC | UP | 0.64 | 0.75 | 0.79 |
| 11-06 16:01 | +20 | ZEC | UP | 0.64 | open |  |
| 11-06 16:01 | +15 | ZEC | UP | 0.64 | open |  |
| 11-06 16:01 | +10 | ZEC | UP | 0.65 | 0.75 | 0.70 |
| 11-06 16:01 | +5 | ZEC | UP | 0.65 | 0.75 | 0.70 |
| 11-06 16:01 | +10 stop | ETH | DOWN | 0.61 | 0.46 | -1.85 |
| 11-06 16:01 | +20 | ETH | DOWN | 0.61 | open |  |
| 11-06 16:01 | +15 | ETH | DOWN | 0.61 | open |  |
| 11-06 16:01 | +10 | ETH | DOWN | 0.61 | open |  |
| 11-06 16:01 | +5 | ETH | DOWN | 0.61 | open |  |
