# Range-Scalp Bot

*Updated Sat Oct 10 18:49 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10749 | 9264 | 1485 (22) | 4 | $-3685.11 | -5.4% |
| **+10¢** | 8139 | 6409 | 1730 (36) | 4 | $-3524.38 | -6.9% |
| **+15¢** | 6864 | 5034 | 1830 (52) | 6 | $-2977.89 | -6.9% |
| **+20¢** | 6103 | 4196 | 1907 (66) | 8 | $-2544.16 | -6.6% |
| **+10¢ (15¢ stop)** | 13214 | 13173 | 41 (25) | 2 | $-5264.27 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 18:47 | +10 stop | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-10 18:47 | +10 stop | BTC | UP | 0.64 | open |  |
| 10-10 18:47 | +10 stop | BNB | UP | 0.64 | open |  |
| 10-10 18:46 | +10 stop | SOL | UP | 0.67 | 0.79 | 0.92 |
| 10-10 18:46 | +20 | SOL | UP | 0.67 | open |  |
| 10-10 18:46 | +15 | SOL | UP | 0.67 | 0.82 | 1.23 |
| 10-10 18:46 | +10 | SOL | UP | 0.67 | 0.79 | 0.92 |
| 10-10 18:46 | +5 | SOL | UP | 0.67 | 0.79 | 0.92 |
| 10-10 18:46 | +5 | BTC | UP | 0.64 | open |  |
| 10-10 18:46 | +10 stop | DOGE | UP | 0.67 | 0.78 | 0.81 |
| 10-10 18:46 | +20 | DOGE | UP | 0.67 | open |  |
| 10-10 18:46 | +15 | DOGE | UP | 0.67 | open |  |
| 10-10 18:46 | +10 | DOGE | UP | 0.67 | 0.78 | 0.81 |
| 10-10 18:46 | +5 | DOGE | UP | 0.67 | 0.75 | 0.50 |
| 10-10 18:46 | +10 stop | XRP | UP | 0.64 | 0.80 | 1.26 |
| 10-10 18:46 | +20 | XRP | UP | 0.64 | open |  |
| 10-10 18:46 | +15 | XRP | UP | 0.64 | 0.80 | 1.26 |
| 10-10 18:46 | +10 | XRP | UP | 0.64 | 0.80 | 1.26 |
| 10-10 18:46 | +5 | XRP | UP | 0.64 | 0.74 | 0.64 |
| 10-10 18:46 | +10 stop | ZEC | UP | 0.70 | 0.55 | -1.83 |
| 10-10 18:46 | +20 | ZEC | UP | 0.70 | open |  |
| 10-10 18:46 | +15 | ZEC | UP | 0.70 | open |  |
| 10-10 18:46 | +10 | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 10-10 18:46 | +5 | ZEC | UP | 0.70 | 0.77 | 0.42 |
| 10-10 18:45 | +10 stop | HYPE | DOWN | 0.55 | 0.34 | -2.44 |
| 10-10 18:45 | +20 | HYPE | DOWN | 0.55 | open |  |
| 10-10 18:45 | +15 | HYPE | DOWN | 0.55 | open |  |
| 10-10 18:45 | +10 | HYPE | DOWN | 0.55 | open |  |
| 10-10 18:45 | +5 | HYPE | DOWN | 0.55 | open |  |
| 10-10 18:45 | +10 stop | BNB | DOWN | 0.60 | 0.44 | -1.95 |
| 10-10 18:45 | +20 | BNB | DOWN | 0.60 | open |  |
| 10-10 18:45 | +15 | BNB | DOWN | 0.60 | open |  |
| 10-10 18:45 | +10 | BNB | DOWN | 0.60 | open |  |
| 10-10 18:45 | +5 | BNB | DOWN | 0.61 | open |  |
| 10-10 18:45 | +10 stop | BTC | DOWN | 0.49 | 0.34 | -1.84 |
| 10-10 18:45 | +20 | BTC | DOWN | 0.49 | open |  |
| 10-10 18:45 | +15 | BTC | DOWN | 0.49 | open |  |
| 10-10 18:45 | +10 | BTC | DOWN | 0.49 | open |  |
| 10-10 18:45 | +5 | BTC | DOWN | 0.49 | 0.54 | 0.14 |
| 10-10 18:45 | +10 stop | NEAR | DOWN | 0.54 | 0.38 | -1.95 |
