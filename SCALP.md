# Range-Scalp Bot

*Updated Sun Oct 11 04:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11368 | 9802 | 1566 (23) | 2 | $-3862.08 | -5.4% |
| **+10¢** | 8608 | 6787 | 1821 (36) | 3 | $-3681.83 | -6.8% |
| **+15¢** | 7256 | 5330 | 1926 (52) | 3 | $-3110.79 | -6.8% |
| **+20¢** | 6464 | 4460 | 2004 (66) | 3 | $-2607.50 | -6.4% |
| **+10¢ (15¢ stop)** | 13997 | 13956 | 41 (25) | 0 | $-5626.88 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 04:32 | +10 stop | NEAR | UP | 0.64 | 0.80 | 1.31 |
| 10-11 04:32 | +10 stop | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 10-11 04:32 | +10 stop | XRP | UP | 0.69 | 0.83 | 1.12 |
| 10-11 04:32 | +20 | XRP | UP | 0.66 | 0.90 | 2.19 |
| 10-11 04:32 | +15 | XRP | UP | 0.66 | 0.83 | 1.44 |
| 10-11 04:32 | +10 | XRP | UP | 0.66 | 0.79 | 1.02 |
| 10-11 04:32 | +5 | XRP | UP | 0.66 | 0.73 | 0.40 |
| 10-11 04:32 | +5 | SOL | UP | 0.60 | 0.72 | 0.88 |
| 10-11 04:31 | +10 stop | ZEC | UP | 0.62 | 0.73 | 0.74 |
| 10-11 04:31 | +20 | ZEC | UP | 0.62 | 0.90 | 2.55 |
| 10-11 04:31 | +15 | ZEC | UP | 0.62 | 0.78 | 1.25 |
| 10-11 04:31 | +10 | ZEC | UP | 0.62 | 0.73 | 0.74 |
| 10-11 04:31 | +5 | ZEC | UP | 0.62 | 0.68 | 0.22 |
| 10-11 04:31 | +10 stop | DOGE | DOWN | 0.56 | 0.37 | -2.27 |
| 10-11 04:31 | +20 | DOGE | DOWN | 0.56 | open |  |
| 10-11 04:31 | +15 | DOGE | DOWN | 0.56 | open |  |
| 10-11 04:31 | +10 | DOGE | DOWN | 0.56 | open |  |
| 10-11 04:31 | +5 | DOGE | DOWN | 0.56 | open |  |
| 10-11 04:31 | +10 stop | SOL | DOWN | 0.50 | 0.27 | -2.62 |
| 10-11 04:31 | +20 | SOL | DOWN | 0.50 | open |  |
| 10-11 04:31 | +15 | SOL | DOWN | 0.50 | open |  |
| 10-11 04:31 | +10 | SOL | DOWN | 0.50 | open |  |
| 10-11 04:31 | +5 | SOL | DOWN | 0.50 | 0.56 | 0.24 |
| 10-11 04:31 | +10 stop | HYPE | UP | 0.62 | 0.74 | 0.85 |
| 10-11 04:31 | +20 | HYPE | UP | 0.62 | 0.88 | 2.31 |
| 10-11 04:31 | +15 | HYPE | UP | 0.62 | 0.80 | 1.47 |
| 10-11 04:31 | +10 | HYPE | UP | 0.63 | 0.74 | 0.75 |
| 10-11 04:31 | +5 | HYPE | UP | 0.62 | 0.74 | 0.85 |
| 10-11 04:31 | +10 stop | NEAR | DOWN | 0.69 | 0.40 | -3.22 |
| 10-11 04:31 | +20 | NEAR | DOWN | 0.69 | open |  |
| 10-11 04:31 | +15 | NEAR | DOWN | 0.69 | open |  |
| 10-11 04:31 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-11 04:31 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-11 04:24 | +5 | HYPE | UP | 0.69 | 0.74 | 0.21 |
| 10-11 04:23 | +10 stop | ZEC | DOWN | 0.66 | 0.50 | -1.94 |
| 10-11 04:23 | +10 | ZEC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-11 04:23 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.19 |
| 10-11 04:23 | +15 | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 10-11 04:23 | +10 stop | SOL | UP | 0.60 | 0.78 | 1.50 |
| 10-11 04:23 | +10 | SOL | UP | 0.60 | 0.78 | 1.50 |
